import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

# -----------------------------
# SECURITY SETTINGS
# -----------------------------
SECRET_KEY = os.getenv("SECRET_KEY", "unsafe-secret-key")  # Default for local dev
DEBUG = os.getenv("DEBUG", "False") == "True"

# Allowed hosts (comma-separated in .env or Render environment variables)
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost").split(",")

# -----------------------------
# APPLICATION DEFINITION
# -----------------------------
INSTALLED_APPS = [
    # default Django apps...
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    # your apps
    "app1",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "new.urls"  # replace 'new' with your project folder

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "new.wsgi.application"  # replace 'new' with your project folder

# -----------------------------
# DATABASE (example using MySQL)
# -----------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DATABASE_NAME"),
        "USER": os.getenv("DATABASE_USER"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": os.getenv("DATABASE_HOST", "localhost"),
        "PORT": os.getenv("DATABASE_PORT", "3306"),
    }
}

# -----------------------------
# STATIC FILES
# -----------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"  # collected static files for production

# -----------------------------
# MEDIA FILES (if needed)
# -----------------------------
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
