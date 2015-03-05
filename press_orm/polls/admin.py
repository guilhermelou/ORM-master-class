from django.contrib import admin

from polls.models import Choice, Poll
# Register your models here.

admin.site.register(Choice)
admin.site.register(Poll)
