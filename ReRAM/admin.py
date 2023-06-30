from django.contrib import admin
from. models import Question, Category

from mptt.admin import DraggableMPTTAdmin


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Category, DraggableMPTTAdmin)


# Register your models here.
