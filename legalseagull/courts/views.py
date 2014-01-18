from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'courts.html', {
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
