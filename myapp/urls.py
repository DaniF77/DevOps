# myapp/urls.py
from django.urls import path
from . import views  # Импортируем наши представления из views.py
urlpatterns = [
    path('', views.note_list, name='note_list'),  # Основная страница с заметками
]
