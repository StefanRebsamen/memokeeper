from django.contrib import admin
from .models import Memo, Label, Attachement

for cls in [Memo, Label, Attachement]:
    admin.site.register(cls)
