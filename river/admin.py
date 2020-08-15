from django.contrib import admin
from .models import DeluxRooms, FamilyRooms, SpecialRooms
# Register your models here.
admin.site.register(DeluxRooms)
admin.site.register(FamilyRooms)
admin.site.register(SpecialRooms)