from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date']
    fieldsets = [
        (None,                  {"fields":['question_text']}),
        ('date information',    {'fields':['pub_date']}),
    ]
    inlines = [ChoiceInline]

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question','choice_text','votes']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)