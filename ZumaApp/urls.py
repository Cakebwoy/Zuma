from django.urls import path
from . import views

urlpatterns= [
    path("", views.signin)
    path("index", views.index)
    path("buysel", views.buysel)

]
