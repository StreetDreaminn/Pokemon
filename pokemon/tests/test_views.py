from django.test import TestCase
from rest_framework.test import force_authenticate, APIClient
from django.urls import reverse
from unittest.mock import patch
from django.contrib.auth.models import User

# Patch BEFORE importing views
with patch('pokemon.decorators.has_permission') as mock_permission:
    def mock_decorator(perm_name):
        print(f"Mocking has_permission with: {perm_name}")
        def decorator(view_func):
            def wrapped_view(request, *args, **kwargs):
                return view_func(request, *args, **kwargs)
            return wrapped_view
        return decorator

    mock_permission.side_effect = mock_decorator

    from pokemon import views

class TestViews(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="admin", password="abc123")

    def test_pokemon_GET(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('pokemon'))
        self.assertEqual(response.status_code, 200)