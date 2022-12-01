from django.contrib import admin
from . models import  beach
from . models import forest
from . models import hillstation
from . models import founder
from . models import manager
from . models import travel
from . models import consultant 

# Register your models here.
admin.site.register(beach)
admin.site.register(forest)
admin.site.register(hillstation)
admin.site.register(founder)
admin.site.register(manager)
admin.site.register(travel)
admin.site.register(consultant)
