from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='shopeHome'),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="ContactUs"),
    path("products/<int:myid>", views.productView, name="ProductView"),

]