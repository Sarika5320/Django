from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Replay)