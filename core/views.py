from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from .forms import SignupForm, OTPVerificationForm
import africastalking
import random

# Initialize Africa's Talking
# africastalking.initialize(
#     # username=settings.AFRICASTALKING_USERNAME,
#     # api_key=settings.AFRICASTALKING_API_KEY
# )
sms = africastalking.SMS

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp(phone_number, otp):
    try:
        response = sms.send(f"Your OTP is: {otp}", [phone_number])
        return response
    except Exception as e:
        print(f"Error sending OTP: {e}")
        return None

def send_welcome_message(phone_number, username):
    message = f"Hello {username}, thank you for creating an account with us. To explore our marketplace please visit www.craftyangu.com."
    try:
        response = sms.send(message, [phone_number])
        return response
    except Exception as e:
        print(f"Error sending welcome message: {e}")
        return None

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # User won't be able to log in until OTP is verified
            user.save()
            
            # Generate and send OTP
            otp = generate_otp()
            user.profile.otp = otp  # Assuming you have a Profile model with an OTP field
            user.profile.save()
            
            send_otp(user.profile.phone_number, otp)
            
            # Redirect to OTP verification page
            return redirect('verify_otp', user_id=user.id)
    else:
        form = SignupForm()
    
    return render(request, 'core/signup.html', {'form': form})

def verify_otp(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except ObjectDoesNotExist:
        return redirect('signup')

    if request.method == 'POST':
        form = OTPVerificationForm(request.POST)
        if form.is_valid():
            otp = form.cleaned_data['otp']
            if otp == user.profile.otp:
                user.is_active = True
                user.save()
                login(request, user)
                
                # Send welcome message
                send_welcome_message(user.profile.phone_number, user.username)
                
                return redirect('index')
            else:
                form.add_error('otp', 'Invalid OTP')
    else:
        form = OTPVerificationForm()
    
    return render(request, 'core/verify_otp.html', {'form': form})

def index(request):
    # items = Item.objects.filter(is_sold=False)[0:6]
    # categories = Category.objects.all()

    return render(request, 'core/index.html', {
        # 'categories': categories,
        # 'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')