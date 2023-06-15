from django.contrib import admin

# Register your models here.
from .models import Issue, Agent, Mechanic

admin.site.register(Issue)
admin.site.register(Agent)
admin.site.register(Mechanic)