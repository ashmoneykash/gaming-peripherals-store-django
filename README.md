# 🕹️ NexGen — Gaming Peripherals E-Commerce Platform

A full-stack e-commerce web application built with **Django**, **MySQL**, and **Tailwind CSS**, featuring secure authentication, robust backend logic, and a modern premium UI.

This project demonstrates real-world full-stack development concepts including user authentication, relational database design, order management, and production-safe debugging practices.

![Django](https://img.shields.io/badge/Django-5.2-092E20?style=flat&logo=django&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=flat&logo=mysql&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.0-38B2AC?style=flat&logo=tailwind-css&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Authentication Fix](#-authentication-fix-resolved)
- [Learning Outcomes](#-learning-outcomes)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

## ✨ Features

### 🔐 **Authentication System**
- User registration with validation
- Secure login/logout functionality
- Password hashing using Django's `pbkdf2_sha256`
- Session-based authentication
- Protected routes with `@login_required` decorator
- User profile management

### 🛒 **E-Commerce Functionality**
- Product catalog with detailed listings
- Real-time stock tracking
- Buy-now order flow
- Order history and tracking
- Automatic stock decrement on purchase

### 📦 **Admin Dashboard**
- Full-featured Django Admin panel
- Product CRUD operations
- Order management and tracking
- User management
- Inventory control

### 🎨 **Frontend Design**
- Modern, premium dark theme
- Responsive design (mobile-first)
- Tailwind CSS utility classes
- Consistent UI/UX across all pages
- Clean, intuitive navigation

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Django 5.2 |
| **Database** | MySQL 8.0+ |
| **Frontend** | HTML5, Tailwind CSS (CDN) |
| **Authentication** | Django Authentication System |
| **ORM** | Django ORM |
| **Server** | Django Development Server |

---

## 📁 Project Structure

```
shop/
├── adminapp/           # Product and Order management
│   ├── models.py       # Product, Order models
│   ├── views.py        # Admin views
│   └── urls.py         # Admin URL routing
├── main/               # Landing pages
│   ├── views.py        # Home, Contact views
│   └── urls.py         # Main URL routing
├── users/              # Authentication & User management
│   ├── views.py        # Login, Register, Profile views
│   ├── models.py       # User profile extensions
│   └── urls.py         # User URL routing
├── templates/          # HTML templates
│   ├── base.html       # Base template
│   ├── home.html       # Landing page
│   ├── login.html      # Login page
│   ├── register.html   # Registration page
│   └── orders.html     # Order history
├── static/             # Static files
│   ├── css/            # Custom CSS
│   └── images/         # Product images
├── shop/               # Project configuration
│   ├── settings.py     # Django settings
│   ├── urls.py         # Root URL configuration
│   └── wsgi.py         # WSGI config
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies
```

---

## 🚀 Installation

### Prerequisites

- Python 3.11 or higher
- MySQL 8.0 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/nexgen-gaming-store.git
cd nexgen-gaming-store
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Manual installation (if requirements.txt is not available):**
```bash
pip install django mysqlclient
```

### Step 4: Configure MySQL Database

1. Create a MySQL database:
```sql
CREATE DATABASE shopdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

2. Update `shop/settings.py` with your MySQL credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shopdb',
        'USER': 'root',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',  # Default MySQL port
    }
}
```

### Step 5: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### Step 7: Start Development Server

```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000** in your browser.

---

## 💻 Usage

### User Flow

1. **Register**: Create a new account at `/register`
2. **Login**: Access your account at `/login`
3. **Browse Products**: View available gaming peripherals
4. **Place Order**: Click "Buy Now" on any product
5. **View Orders**: Check order history at `/orders`
6. **Logout**: Securely end your session

### Admin Panel

Access the admin panel at **http://127.0.0.1:8000/admin**

- Manage products (add/edit/delete)
- View and process orders
- Manage user accounts
- Monitor inventory

---

## 🔧 Authentication Fix (Resolved)

### ❌ **The Issue**

The registration form initially used two password fields (`password1` and `password2`) for confirmation, but the backend was not correctly mapping the submitted password to Django's `create_user()` method.

**Problems:**
- Password parameter was not passed correctly
- Invalid password hashes were stored in the database
- Login authentication consistently failed
- Users couldn't authenticate even with correct credentials

### ✅ **The Solution**

Correctly mapped `password1` from the form data and passed it to Django's `create_user()` method:

```python
# users/views.py (Fixed)
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Validation
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')
        
        # Correct user creation with password hashing
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1  # ✅ Now correctly passed
        )
        user.save()
        messages.success(request, "Registration successful!")
        return redirect('login')
```

### 🎯 **Results**

- ✅ Passwords are now securely hashed using Django's default hasher
- ✅ Authentication works reliably
- ✅ No database resets required
- ✅ Production-safe implementation

## 🧠 Learning Outcomes

This project helped develop understanding of:

- ✅ Django authentication system internals
- ✅ Secure password handling and hashing mechanisms
- ✅ MySQL relational database design and integrity
- ✅ ORM-based database operations and queries
- ✅ Form validation and data sanitization
- ✅ Session management and middleware
- ✅ Debugging full-stack form-to-backend workflows
- ✅ Building production-safe Django applications
- ✅ RESTful URL routing and views
- ✅ Template inheritance and context management

---

## 🚧 Future Enhancements

- [ ] Implement shopping cart functionality
- [ ] Add payment gateway integration (Stripe/PayPal)
- [ ] Product search and filtering
- [ ] Product reviews and ratings
- [ ] Wishlist feature
- [ ] Email notifications for orders
- [ ] Password reset functionality
- [ ] Social media authentication (OAuth)
- [ ] Advanced admin analytics dashboard
- [ ] RESTful API with Django REST Framework
- [ ] Deploy to production (AWS/Heroku/DigitalOcean)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Ayush**  
*Full-Stack Django Developer*

- GitHub: [@ashmoneykash](https://github.com/ashmoneykash)
- LinkedIn: [ashmoneykash](https://linkedin.com/in/ashmoneykash)
- Email: ayushsalaria321@gmail.com

---

## 🙏 Acknowledgments

- Django Documentation
- Tailwind CSS Team
- MySQL Community
- Stack Overflow Community

---

## 📝 Notes

- **Payments**: Not implemented (demo/academic project)
- **Focus**: Backend correctness, security, and UI polish
- **Purpose**: Portfolio demonstration and academic submission

---

<div align="center">
Made with ♥ by Ayush | 2026
</div>
