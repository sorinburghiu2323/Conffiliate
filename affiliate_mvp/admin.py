from django.contrib import admin
from affiliate_mvp.models import *

models = [PreRegisterUser]

for model in models:
    admin.site.register(model)
