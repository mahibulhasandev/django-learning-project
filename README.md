# My First Django Project

This is my first Django project, created while learning the fundamentals of Django and web development.

The project contains a basic Django structure with HTML, CSS, JavaScript, and Tailwind CSS integration. It serves as a foundation for learning and experimenting with Django features.

## Technologies Used

- Python
- Django
- HTML5
- CSS3
- JavaScript
- Tailwind CSS
- DaisyUI

## Project Structure

```text
mysite/
├── firstApp/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── theme/
│   └── static_src/
├── templates/
├── manage.py
└── README.md
```

## Getting Started

Clone the repository:

```bash
git clone https://github.com/mahibulhasandev/my-first-django-project.git
cd my-first-django-project
```

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install Django:

```bash
pip install django
```

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Purpose

- Learn Django project structure and fundamentals.
- Understand Django apps, views, URLs, and templates.
- Practice HTML, CSS, and JavaScript.
- Integrate Tailwind CSS into Django.
- Build a foundation for future Django projects.

## Author

**Mahibul Hasan**

GitHub: [@mahibulhasandev](https://github.com/mahibulhasandev)

---

*My first step into Django and web development.*
