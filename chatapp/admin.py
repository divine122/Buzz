from django.contrib import admin
from . models import UserProfile,Friend
# Register your models here.

admin.site.register([UserProfile,Friend])
