from django.contrib import admin
from ads.models import Category, Ad, Location, User

admin.site.register(Location)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Ad)
