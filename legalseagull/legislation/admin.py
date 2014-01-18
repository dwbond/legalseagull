from django.contrib import admin
from legislation.models import Title, Chapter, Section

# Register your models here.
admin.site.register( Title )
admin.site.register( Chapter )
admin.site.register( Section )
