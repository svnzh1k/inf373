from django.contrib import admin
from .models import Subject, Lecture, Practice

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('code', 'subject_name')
    search_fields = ('code', 'subject_name')

@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('subject', 'lecturer', 'day', 'time', 'duration')
    list_filter = ('day', 'lecturer')
    search_fields = ('lecturer',)

@admin.register(Practice)
class PracticeAdmin(admin.ModelAdmin):
    list_display = ('lecture', 'practice_teacher', 'day', 'time', 'duration')
    list_filter = ('day', 'practice_teacher')
    search_fields = ('practice_teacher',)
