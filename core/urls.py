from django.urls import path
from .views import home
from .views import login
from .views import singin
from .views import cat
from .views import dog
from .views import bird
from .views import exotic


urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('singin/', singin, name="singin"),
    path('cat/', cat, name="cat"),
    path('dog/', dog, name="dog"),
    path('bird/', bird, name="bird"),
    path('exotic/', exotic, name="exotic"),

]