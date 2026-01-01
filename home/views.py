from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm
from .models import Testimonial


def home_view(request):
    from portfolio.models import Project
    from services.models import Service
    from blog.models import Post

    featured_projects = Project.objects.filter(is_featured=True)[:3]
    latest_posts = Post.objects.filter(is_published=True).order_by('-created_at')[:3]
    services = Service.objects.all()
    testimonials = Testimonial.objects.filter(is_active=True)

    context = {
        'featured_projects': featured_projects,
        'latest_posts': latest_posts,
        'services': services,
        'testimonials': testimonials,
    }
    return render(request, 'core/home.html', context)


def about_view(request):
    return render(request, 'core/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully.")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})