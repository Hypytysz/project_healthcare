# Project Django

## Przygotowanie
- otwieramy git basha
- towrzymy folder projektu w tym przypadku django_projects (wchodząc do lokalizacji w której chcemy utworzyć projekt komendami 
"cd ścieżka" oraz "cd..") następnie używając komendy "mkdir django_projects"
- wchodzimy do utworzonego folderu komendą "cd django_projects"
- w nim tworzymy folder konkretnego projektu w tym przypadku project_healthcare uzywając komendy powyżej "mkdir project_healthcare"
- ponownie wchodzimy do utworzonego projektu komendą "cd project_healthcare"
- kolejnym krokiem jest utworzenie srodowiska komenda "python -m venv venv"
## Aktywacja środowiska
- w folderze project_healthcare mozemy aktywowac środowisko,
w przypadku maca i linuxa komendą "source venv/bin/activate"
w przypadku windowsa "source venv/Scripts/activate"
- teraz używając komendy "vim README.md" tworzymy plik README, w którym zawieramy instrukcję.
- zapisujemy klikając ESC i wpisując ":wq"
## Instalacja Django w wirtualnym środowisku
- używamy komendy "pip install django"
## Tworzenie projektu
- projekt tworzymy komendą "django-admin startproject healthcare"
- dodajemy aplikację komendą "django-admin startapp bloodpressure"
- tworzymy model
- w urls do importów obok path dodajemy include oraz 
  path("", include('bloodpressure.urls')),
- tworzymy urls w bloodpressure, gdzie importujemy
  from . import views
  oraz tworzymy ścieżki
- dodajemy funkcję do views, które będą obsługiwały naszą aplikację
- dodajemy templates, a w nich szablony
- tworzymy plik forms
- przygotowujemy migrację "python manage.py makemigration"
- wykonujemy migrację "python manage.py migration"