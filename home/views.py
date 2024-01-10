from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Contact, Newsletter
from .forms import ContactForm, NewsletterForm
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def about_us(request):
    """ A view to return the about us page """

    return render(request, 'about_us.html')


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)

    contact_form = ContactForm(data=request.POST)
    if contact_form.is_valid():
            contact_form.instance.email = request.user.email
            contact_form.instance.name = request.user.username
            contact = contact_form.save(commit=False)
            contact.article = article
            contact.save()
    else:
            contact_form = ContactForm()

    return render(
            {
                "contact_form": contact_form
            },
        )

def success(request):
    if request.method == "POST":
        # success = request.POST['success']
        print("if block")
        return render(request, 'success.html')

    else:
        print("else block")
        return render(request, 'success.html', {})


def newsletter(request):
    form = NewsletterForm()
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_newsletter')
    context = {
        'form': form
    }
    return render(request, 'newsletter.html', context)


def success_newsletter(request):
    if request.method == "POST":
        # success = request.POST['success_newsletter']
        print("if block")
        return render(request, 'success_newsletter.html')

    else:
        print("else block")
        return render(request, 'success_newsletter.html', {})
