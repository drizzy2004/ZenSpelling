from django.contrib import admin

from .models import Answer, Question, Course, Tile


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Other information", {"fields": ["course"], "classes": ["collapse"]}),
    ]
    inlines = [AnswerInline]
    list_display = ["question_text", "percent_correct"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Course)
admin.site.register(Tile)

