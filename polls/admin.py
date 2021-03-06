from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    list_display = ('question_text', 'pub_date')
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
