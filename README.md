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

    $ git clone http://github.com/dwbond/legalseagull
    $ cd legalseagull
    $ virtualenv .virtualenv
    $ source .virtualenv/bin/activate
    $ pip install -r requirements.txt

Do some magic voodoo chanting to get the database working. Then:

    $ cd legalseagull
    $ python manage.py runserver

