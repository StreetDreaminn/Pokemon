from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pokemon.views import pokemon, get_fairy_pokemon, add_pokemon, get_legendary_pokemon, \
get_top_ten_fastest_pokemon, get_top_five_weakest_pokemon, get_top_three_physical_attacking_pokemon, \
get_generation_three_pokemon, get_all_mega_pokemon, get_all_pokemon_that_start_with_o

class TestUrls(SimpleTestCase):

    def test_pokemon_url_is_resolved(self):
        url = reverse('pokemon')
        self.assertEqual(resolve(url).func, pokemon)
    
    def test_fairy_url_is_resolved(self):
        url = reverse('fairy')
        self.assertEqual(resolve(url).func, get_fairy_pokemon)
    
    def test_add_pokemon_url_is_resolved(self):
        url = reverse('add_pokemon')
        self.assertEqual(resolve(url).func, add_pokemon)
    
    def test_legendary_pokemon_url_is_resolved(self):
        url = reverse('legendary_pokemon')
        self.assertEqual(resolve(url).func, get_legendary_pokemon)
    
    def test_fast_pokemon_url_is_resolved(self):
        url = reverse('fast_pokemon')
        self.assertEqual(resolve(url).func, get_top_ten_fastest_pokemon)
    
    def test_weak_pokemon_url_is_resolved(self):
        url = reverse('weak_pokemon')
        self.assertEqual(resolve(url).func, get_top_five_weakest_pokemon)
    
    def test_strong_pokemon_url_is_resolved(self):
        url = reverse('strong_pokemon')
        self.assertEqual(resolve(url).func, get_top_three_physical_attacking_pokemon)
    
    def test_gen_3_pokemon_url_is_resolved(self):
        url = reverse('gen_3_pokemon')
        self.assertEqual(resolve(url).func, get_generation_three_pokemon)
    
    def test_mega_pokemon_url_is_resolved(self):
        url = reverse('mega_pokemon')
        self.assertEqual(resolve(url).func, get_all_mega_pokemon)
    
    def test_o_pokemon_url_is_resolved(self):
        url = reverse('o_pokemon')
        self.assertEqual(resolve(url).func, get_all_pokemon_that_start_with_o)