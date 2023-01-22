from django.contrib import admin
from .models import UserSubmit

class SubmitAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated']

admin.site.register(UserSubmit, SubmitAdmin)