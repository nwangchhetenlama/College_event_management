# 🎉 College Event Management System

A full‑stack **Django web application** designed for managing college events. Admins can create and manage events, while students can browse events, register, and view their registration history from their profile.

---

## 🚀 Features

### 👨‍💼 Admin

* Create, update, and delete events
* Upload event banner images
* Set registration deadline & participant limit
* View registered participants per event (Admin panel)

### 🎓 Students

* User authentication (Register / Login / Logout)
* View upcoming events
* Register for events (with email confirmation)
* Prevent duplicate registrations
* View registration history in Profile

### 📅 Extras


* Role‑based access control
* Responsive UI using Bootstrap

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, Bootstrap 5
* **Database:** SQLite (default)
* **Authentication:** Django Auth System
* **Email:** SMTP / Console backend

---

## 📂 Project Structure

```
college_event_management/
│
├── accounts/            # Authentication & profile
├── events/              # Event logic
├── templates/           # HTML templates
│   ├── accounts/
│   └── events/
├── media/               # Uploaded event banners
├── static/              # Static files
├── db.sqlite3
└── manage.py
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <repository-url>
cd college_event_management
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install django pillow
```

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```


### 6️⃣ Run Server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 📧 Email Configuration (Optional)

For testing (recommended):

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

For production (Gmail SMTP):

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'app_password'
```

---

## 🖼️ Media Configuration

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

```python
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 🔐 User Roles

| Role    | Permissions                       |
| ------- | --------------------------------- |
| Admin   | Manage events & view participants |
| Student | Register & view profile history   |

---



## ✅ Future Enhancements

* Event cancellation by students
* PDF export of registration history
* Event reminder emails

---

## 👨‍💻 Author

**Nwang Chheten Lama**
College Event Management System 

---

⭐ If you like this project, feel free to improve or extend it!
