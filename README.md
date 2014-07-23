README
==

LegalSeagull-- analyze and visualize legal information.

Setup
---

To get started, you'll need to have the following installed:
* [Git](http://http://git-scm.com/book/en/Getting-Started-Installing-Git)

Open a terminal window and type in the following commands. (If you're on Windows,
use [Cygwin](http://cygwin.com/). This will create a local, workable copy of the
project.

    bash
    git clone git@git.gmu.edu:dbond2/legalseagull.git
    cd legalseagull
    mkdir ~/.virtualenvs
    virtualenv ~/.virtualenvs/legalseagull
    source ~/.virtualenvs/legalseagull/bin/activate
    pip install -r requirements.txt

database

    cd legalseagull
    python manage.py runserver

