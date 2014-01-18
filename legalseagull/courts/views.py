from django.shortcuts import render, get_object_or_404
from courts.models import Base, Tags, Justice, Opinion, Case
import time

def index(request):
    # should this be pulled out? it's used by all of them
    cases = Case.objects.all()# .order_by('-decisionDate')
    # tags = Tags.objects.all()
    return render(request, 'courts.html', {
    'cases' : cases,
    },
    )

def justice(request, slug):
    justice = get_object_or_404(Justice, slug=slug)
    cases = Case.objects.all()#.orderby('-decisionDate')
    return render(request, 'justice.html', {
        'justice' = justice,

    },
    )

def tags(request, slug):
    tag = get_object_or_404(Tags, slug=slug)
    cases = Case.objects.all()#.order_by('-decisionDate')
    return render(request,'tags.html', {
        'tag' : tag,
        'cases' : cases,
    },
    )

def opinion(request, slug):
    opinion = get_object_or_404(Opinion, slug=slug) 
    return render(request, 'opinion.html', {
        'opinion' : opinion,
    },
    )

def case(request, slug):
    opinions = get_object_or_404(Case, slug=slug)
    return render(request, 'case.html', {
        'opinions' : opinions,
    },
    )
