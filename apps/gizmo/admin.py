from django.apps import apps
from django.contrib import admin

from qux.admin import QuxModelAdmin

excluded_models = []

app = apps.get_app_config("gizmo")
app_models = [x for x in app.get_models() if x not in excluded_models]

for model in app_models:
    admin.site.register(model, QuxModelAdmin)
