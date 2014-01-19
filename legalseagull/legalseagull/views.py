from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html', {
    },
    )

def about(request):
    return render(request, 'about.html', {
    },
    )

def pricing(request):
    return render(request, 'pricing.html', {
    },
    )

def contact(request):
    return render(request, 'contact.html', {
    },
    )

def terms(request):
    return render(request, 'terms.html', {
    },
    )

def privacy(request):
    return render(request, 'privacy.html', {
    },
    )
