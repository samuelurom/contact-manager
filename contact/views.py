from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm


# Create your views here.
def home(request):
    contacts = Contact.objects.all()
    context = {"contacts": contacts}
    return render(request, "index.html", context)


def profile(request, id):
    contact = get_object_or_404(Contact, id=id)
    context = {"contact": contact}
    return render(request, "profile.html", context)


def add_contact(request):
    # If post request, process the form

    if request.method == "POST":
        # Populate new form instance with data from the request
        form = ContactForm(request.POST)

        # Check if form is valid, save data, and redirect to home
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ContactForm()

    context = {"form": form}
    return render(request, "add-contact.html", context)


def update_contact(request, id):
    # Get the contact instance
    contact = get_object_or_404(Contact, id=id)

    if request.method == "POST":
        # New form instance with data from request and contact instance
        form = ContactForm(request.POST, instance=contact)

        # Check if form is valid, save data, and redirect to edited record
        if form.is_valid():
            form.save()
            return redirect("contact", id)
    else:
        form = ContactForm(instance=contact)

    context = {"form": form, "contact": contact}
    return render(request, "update-contact.html", context)


def delete_contact(request, id):
    # Get the contact instace
    contact = get_object_or_404(Contact, id=id)
    contact.delete()
    return redirect("home")
