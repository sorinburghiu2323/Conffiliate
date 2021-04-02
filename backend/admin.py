from django.contrib import admin

from backend.models import *

models = [User, Platform, UserPlatform, Keyword, UserKeyword]

for model in models:
    admin.site.register(model)
