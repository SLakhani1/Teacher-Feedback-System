from django.contrib import admin
from . import models

admin.site.register(models.Student)
admin.site.register(models.Teacher)
admin.site.register(models.Feedback)
admin.site.register(models.Course)