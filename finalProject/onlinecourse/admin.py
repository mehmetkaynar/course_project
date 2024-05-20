from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Enrollment, Question, Choice, Submission

# Register your models here.

# QuestionInline ve ChoiceInline sınıflarını burada kaydedin
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]  # Course admin panelinde Lesson ve Question inlines olacak
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]  # Question admin panelinde Choice inlines olacak
    list_display = ['content']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('content', 'question', 'is_correct')
    search_fields = ['content', 'question__content']

# Modelleri admin paneline kaydedin
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Enrollment)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Submission)
