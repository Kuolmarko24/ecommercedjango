from django.urls import path, include
from product import views
#from .views import LatestProductsList

urlpatterns = [
    path('latest-products/',views.LatestproductsList.as_view()),
]
