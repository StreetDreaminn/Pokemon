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

    def test_fairy_pokemon_GET(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('fairy'))
        self.assertEqual(response.status_code, 200)

    @patch('pokemon.models.Pokemon.objects.all')
    def test_add_pokemon_GET(self, mock_object):
        mock_object.return_value = None
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('add_pokemon'))
        self.assertEqual(response.status_code, 200)

    def test_legendary_pokemon_GET(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('legendary_pokemon'))
        self.assertEqual(response.status_code, 200)

    def test_fast_pokemon_GET(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('fast_pokemon'))
        self.assertEqual(response.status_code, 200)

    def test_weak_pokemon_GET(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('weak_pokemon'))
        self.assertEqual(response.status_code, 200)

    def test_attack_pokemon_GET(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('strong_pokemon'))
        self.assertEqual(response.status_code, 200)

    def test_gen_3_pokemon_GET(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('gen_3_pokemon'))
        self.assertEqual(response.status_code, 200)

    def test_mega_pokemon_GET(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('mega_pokemon'))
        self.assertEqual(response.status_code, 200)

    def test_o_pokemon_GET(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('o_pokemon'))
        self.assertEqual(response.status_code, 200)