from django.contrib import admin
from affiliate_mvp.models import *

models = [PreRegisterUser, User, Platform, UserPlatform, Keyword, UserKeyword]

for model in models:
    admin.site.register(model)
