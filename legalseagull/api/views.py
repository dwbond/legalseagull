from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings
import json
from evernote.api.client import EvernoteClient
from evernote.edam.type.ttypes import Note, Notebook

def get_note_store():
    client = EvernoteClient( token = settings.EVERNOTE_DEVELOPER_TOKEN )
    return client.get_note_store()

# Create your views here.
def index(request):
    return render(request, 'api.html', {
    },
    )

def evernote_create_note(request):
    if request.method != 'POST':
        return redirect('/api')

    title = request.POST.get('title')
    content = request.POST.get('content')

    note_store = get_note_store()
    response_data = {}

    nBody = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
    nBody += "<!DOCTYPE en-note SYSTEM \"http://xml.evernote.com/pub/enml2.dtd\">"
    nBody += "<en-note>%s</en-note>"
    
    newNote = Note()
    newNote.title = title
    newNote.content = nBody % content

    note = None
    try:
        note = note_store.createNote( newNote )
        response_data['result'] = "success"
    except:
        response_data['result'] = "error"

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )

def evernote_create_notebook(request):
    if request.method != 'POST':
        return redirect('/api')

    name = request.POST.get('notebook')

    note_store = get_note_store()
    response_data = {}

    newNotebook = Notebook()
    newNotebook.name = name

    notebook = None
    try:
        notebook = note_store.createNotebook( newNotebook )
        response_data['result'] = "success"
    except:
        response_data['result'] = "error"

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )
