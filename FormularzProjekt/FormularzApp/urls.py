from django.urls import path
from . import views

urlpatterns = [
    path('dodaj_przyjecia/', views.dodaj_przyjecia, name='dodaj_przyjecia'),
    # ... inne ścieżki ...

-- to jest