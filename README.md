# CraftYangu: Empowering Artisans, Crafting Futures

![CraftYangu Logo](path/to/logo.png)

## 🚀 About CraftYangu

CraftYangu is a revolutionary marketplace that connects skilled artisans with a history of incarceration to buyers seeking quality handcrafted products. Our platform empowers individuals to rebuild their lives through their craftsmanship, while providing customers with unique, high-quality goods.

### 🌟 Key Features

- **Artisan Profiles**: Showcase skills, products, and stories
- **Secure Marketplace**: Browse, buy, and sell handcrafted items
- **USSD Service**: Access core features via basic mobile phones
- **OTP Authentication**: Ensure secure access with Africa's Talking API
![Marketplace Screenshot](path/to/marketplace_screenshot.png)

## 🛠 Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: PostgreSQL
- **API**: Africa's Talking (for OTP and USSD)

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Django 3.2+
- PostgreSQL
- Africa's Talking API key

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/reforgedskills.git
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```
   cp .env.example .env
   # Edit .env with your database and API credentials
   ```

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

Visit `http://localhost:8000` to see the application in action!

## 📱 USSD Service

Our USSD service allows users to access core features via basic mobile phones. Here's a quick guide:

1. Dial `*384*303#` (example code)
2. Follow the prompts to:
   - View products
   - Check order status
   - Update profile

![USSD Flow](path/to/ussd_flow_diagram.png)

## 🤝 Contributing

We welcome contributions! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to get started.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 🙏 Acknowledgements

- [Africa's Talking](https://africastalking.com/) for their robust API
- All the amazing artisans who make this platform possible
- [Hackathon Name] for the inspiration and opportunity

---

Built with ❤️ by [Kelvin Wepo] for social impact and economic empowerment.