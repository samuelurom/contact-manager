from django.urls import path
from . import views

# URLconf
urlpatterns = [
    path("", views.home, name="home"),
    path("contact/<int:id>", views.profile, name="contact"),
    path("contact/add", views.add_contact, name="add"),
    path("contact/edit/<int:id>", views.update_contact, name="update"),
    path("contact/delete/<int:id>", views.delete_contact, name="delete"),
]
