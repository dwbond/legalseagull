from django.shortcuts import render, get_object_or_404
from courts.models import Base, Tags, Justice, Opinion, Case
from django.db.models import Count
import time
import wikipedia

def popular_tags():
    return Tags.objects.annotate(num_cases=Count('case')).order_by('num_cases')[:4]

# this should probably be written to the database instead of generated
# on the fly on the page
def wikipedia(justiceName):
    try:
        summary = wikipedia.summary(justiceName)
	return summary

    except DisambiguationError, e:
        return ""

def index(request):
    # should this be pulled out? it's used by all of them
    cases = Case.objects.all().order_by('-decisionDate')
    # tags = Tags.objects.all()
    return render(request, 'courts.html', {
    'cases' : cases,
    'toptags' : popular_tags(),
    },
    )

def justice(request, slug):
    justice = get_object_or_404(Justice, slug=slug)
    all_opinions = Opinion.objects.all()
    opinions = []
    for opinion in all_opinions:
        authors = opinion.writtenBy.all()
        if justice in authors:
            opinions.append( opinion )
    all_cases = Case.objects.all()
    cases = []
    for case in all_cases:
        case_opinions = case.opinion_set.all()
        for opinion in opinions:
            if opinion in case_opinions:
                cases.append( case )
    summary = wikipedia(justice.name)
    return render(request, 'justice.html', {
        'justice' : justice,
        'opinions' : opinions,
        'cases' : cases,
        'toptags' : popular_tags(),
	'summary' : summary,
    },
    )

def tags(request, slug):
    tag = get_object_or_404(Tags, slug=slug)
    cases = Case.objects.filter(tags=tag)#.order_by('-decisionDate')
    return render(request,'tags.html', {
        'tag' : tag,
        'cases' : cases,
        'toptags' : popular_tags(),
    },
    )

def opinion(request, slug):
    opinion = get_object_or_404(Opinion, slug=slug) 
    return render(request, 'opinion.html', {
        'opinion' : opinion,
        'toptags' : popular_tags(),
    },
    )

def case(request, slug):
    case = get_object_or_404(Case, slug=slug)
    opinions = Opinion.objects.filter(case=case)
    return render(request, 'case.html', {
        'case' : case,
        'opinions' : opinions,
        'toptags' : popular_tags(),
    },
    )
