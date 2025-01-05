pip install -r /home/franklin/Pokemon/requirements.txt
python manage.py migrate

echo "
from django.contrib.auth.models import User
user=User.objects.create_user('admin', password='abc123')
user.is_superuser=True
user.is_staff=True
user.save()
" | python manage.py shell

python manage.py runserver 0.0.0.0:8000