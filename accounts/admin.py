from django.contrib import admin
from accounts.models import UserProfiles, Audio, Messages

# Register your models here.

admin.site.register(UserProfiles)
admin.site.register(Audio)
admin.site.register(Messages)
