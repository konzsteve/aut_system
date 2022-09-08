from django.contrib import admin
from .models import *

admin.site.register(Candidate)
admin.site.register(Votes)
admin.site.register(Position)
admin.site.register(Voter)
# Register your models here.
