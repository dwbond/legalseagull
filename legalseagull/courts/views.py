from django.shortcuts import render
from courts.models import Base, Tags, Justice, Opinion, Case
from datetime import datetime, timedelta

def index(request):
    cases = Case.objects.all()# .order_by('-decisionDate')
    # tags = Tags.objects.all()
    return render(request, 'courts.html', {
    'cases' : cases,
    },
    )

def justice(request, slug):
    justice = get_object_or_404(Justice, slug=slug)
    return render(request, 'justice.html', {
    },
    )

def tags(request, slug):
    tags = get_object_or_404(Tags, slug=slug)
    return render(request,'tags.html', {
    },
    )

def opinion(request, slug):
    opinion = get_object_or_404(Opinion, slug=slug) 
    return render(request, 'opinion.html', {
    },
    )

def case(request, slug):
    case = get_object_or_404(Case, slug=slug)
    return render(request, 'case.html', {
    },
    )
