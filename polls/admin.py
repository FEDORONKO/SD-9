from django.contrib import admin
from .models import Question

# Реєструємо модель Question в адмінці
admin.site.register(Question)
