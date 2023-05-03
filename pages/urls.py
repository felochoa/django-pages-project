from django.urls import path
from .views import HomePageView, AboutPageView

#when using Class-Based Views, you always add as_view() 
#at the end of the view name.
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
]
