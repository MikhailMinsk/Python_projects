from django.contrib import admin
from .models import Questions, Choice


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('date information', {'fields': ['date_public'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'date_public', 'was_published')
    list_filter = ['date_public']
    search_fields = ['question_text']


# fields = ['date_public', 'question_text']

admin.site.register(Choice)
admin.site.register(Questions, QuestionsAdmin)
