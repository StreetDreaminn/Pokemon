from django.urls import path
from pokemon import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/pokemon", views.pokemon),
    path("api/fairy", views.get_fairy_pokemon),
    path("api/add_pokemon", views.add_pokemon),
    path("api/legendary", views.get_legendary_pokemon),
    path("api/fast_pokemon", views.get_top_ten_fastest_pokemon),
    path("api/weak_pokemon", views.get_top_five_weakest_pokemon),
    path("api/strong_pokemon", views.get_top_three_physical_attacking_pokemon),
    path("api/generation_three", views.get_generation_three_pokemon),
    path("api/mega_pokemon", views.get_all_mega_pokemon),
    path("api/o_pokemon", views.get_all_pokemon_that_start_with_o),
]