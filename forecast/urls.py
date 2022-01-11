from django.urls import path
from forecast import views


urlpatterns = [
    path('', views.get_all)
]
