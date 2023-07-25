from django.urls import path
from . import views
urlpatterns = [
    path('http://pyang22.pythonanywhere.com', views.post_list, name='post_list'),
]