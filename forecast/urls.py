from django.urls import include, path
from forecast import views


urlpatterns = [
    path('', views.get_all)
]
