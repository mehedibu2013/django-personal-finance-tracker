# Django Personal Finance Tracker

A simple web-based personal finance tracker built with **Django**.  
Keep track of income, expenses, categories, and budgets — all from one dashboard.

---

## 🎯 Features

- User authentication (login/logout)
- Add/edit/delete transactions
- Manage income vs expenses
- Categorize spending
- Dashboard with recent transactions
- Password reset via email
- Admin panel for data management

---

## 🧾 URLs Available

| Feature | URL |
|--------|-----|
| Login | http://127.0.0.1:8000/accounts/login/ |
| Logout | http://127.0.0.1:8000/accounts/logout/ |
| Dashboard | http://127.0.0.1:8000/ |
| All Transactions | http://127.0.0.1:8000/transactions/ |
| Add Transaction | http://127.0.0.1:8000/transactions/add/ |
| Edit Transaction | http://127.0.0.1:8000/transactions/<id>/edit/ |
| Delete Transaction | http://127.0.0.1:8000/transactions/<id>/delete/ |
| All Categories | http://127.0.0.1:8000/categories/ |
| Add Category | http://127.0.0.1:8000/categories/add/ |
| Edit Category | http://127.0.0.1:8000/categories/<id>/edit/ |
| Delete Category | http://127.0.0.1:8000/categories/<id>/delete/ |
| Password Reset | http://127.0.0.1:8000/accounts/password_reset/ |
| Admin Panel | http://127.0.0.1:8000/admin/ |

---

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/mehedibu2013/django-personal-finance-tracker.git
cd django-personal-finance-tracker
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate    # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create superuser (for admin access)

```bash
python manage.py createsuperuser
```

### 6. Run development server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## 📦 Requirements

Your project should include a `requirements.txt` file with:

```
Django>=5.0,<6.0
python-decouple
```

---

## 📨 Email Configuration (Optional)

To enable password reset emails, configure your `.env` file like this:

```env
EMAIL_HOST_USER=your-gmail@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

> ⚠️ Use an [App Password](https://myaccount.google.com/apppasswords) if using Gmail.

---

## 🧪 Testing

You can manually test each feature by visiting the URLs listed above.  
For unit testing, run:

```bash
python manage.py test
```

---

## 🚀 Deployment (Optional)

You can deploy this app on cloud platforms.
Update `settings.py` with `ALLOWED_HOSTS`, `DATABASES`, and static files settings before deployment.

---

## 🤝 Contributing

Feel free to fork this repo, raise issues, or submit pull requests!

---

## ✅ What to Include in Your Repo

Make sure your repo includes these files:

```
django-personal-finance-tracker/
├── finance_app/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
├── users/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── finance_tracker_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 📦 Optional: Generate Requirements File

If you don’t already have a `requirements.txt`, generate it with:

```bash
pip freeze > requirements.txt
```