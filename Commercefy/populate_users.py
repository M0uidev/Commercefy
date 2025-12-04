import os
import django
import sys

# Add the project directory to the sys.path
sys.path.append(os.getcwd())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Commercefy.settings')
django.setup()

from django.contrib.auth.models import User, Group

def populate_users():
    print("Creating users...")

    # Admin
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("User 'admin' created (Superuser).")
    else:
        print("User 'admin' already exists.")

    # Trabajador
    if not User.objects.filter(username='trabajador').exists():
        user = User.objects.create_user('trabajador', 'trabajador@example.com', 'trabajador123')
        user.is_staff = True
        user.save()
        print("User 'trabajador' created (Staff).")
    else:
        print("User 'trabajador' already exists.")

    # Cliente
    if not User.objects.filter(username='cliente').exists():
        User.objects.create_user('cliente', 'cliente@example.com', 'cliente123')
        print("User 'cliente' created.")
    else:
        print("User 'cliente' already exists.")

if __name__ == '__main__':
    populate_users()
