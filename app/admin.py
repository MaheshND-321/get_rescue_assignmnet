from django.contrib import admin

# Register your models here.
from .models import Issue, Agent1,Agent2,Agent3,Agent4,Agent5, Mechanic

admin.site.register(Issue)
admin.site.register(Agent1)
admin.site.register(Agent2)
admin.site.register(Agent3)
admin.site.register(Agent4)
admin.site.register(Agent5)
admin.site.register(Mechanic)