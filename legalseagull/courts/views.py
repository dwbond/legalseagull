from django.shortcuts import render
from courts.models import Base, Tags, Justice, Opinion, Case
from datetime import datetime, timedelta

def index(request):
    cases = Case.objects.all()# .order_by('-decisionDate')
    return render(request, 'courts.html', {
    'cases' : cases,
    },
    )

def justice(request, slug):
    return render(request, 'justice.html', {
    },
    )

def tags(request, slug):
    return render(request,'tags.html', {
    },
    )

def opinion(request, slug):
    return render(request, 'opinion.html', {
    },
    )

def case(request, slug):
    return render(request, 'case.html', {
    },
    )
