from django.contrib import admin
from courts.models import Tags, Justice, Opinion, Case

# Register your models here.
admin.site.register( Tags )
admin.site.register( Justice )
admin.site.register( Opinion )
admin.site.register( Case )
