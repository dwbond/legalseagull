from django.shortcuts import render, get_object_or_404
from courts.models import Base, Tags, Justice, Opinion, Case
from django.contrib.auth.decorators import login_required
import time

@login_required
def index(request):
    cases = Case.objects.all()# .order_by('-decisionDate')
    # tags = Tags.objects.all()
    return render(request, 'courts.html', {
    'cases' : cases,
    },
    )

@login_required
def justice(request, slug):
    justice = get_object_or_404(Justice, slug=slug)
    return render(request, 'justice.html', {
    },
    )

@login_required
def tags(request, slug):
    tags = get_object_or_404(Tags, slug=slug)
    return render(request,'tags.html', {
    },
    )

@login_required
def opinion(request, slug):
    opinion = get_object_or_404(Opinion, slug=slug) 
    return render(request, 'opinion.html', {
    },
    )

@login_required
def case(request, slug):
    case = get_object_or_404(Case, slug=slug)
    return render(request, 'case.html', {
    },
    )
