from django.shortcuts import render, get_object_or_404
from legislation.models import Title

# Create your views here.
def index(request):
    return render(request, 'legislation.html', {
    },
    )

def view_title(request, number):
    title = get_object_or_404(Title, number=number)

    return render(request, 'title.html', {
        'title' : title,
    },
    )
