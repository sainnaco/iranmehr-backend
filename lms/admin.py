from django.contrib import admin
from .models import Certificate,GradeLessons,AddLessons,ClassDays,PriodicExam

class CertificateAdmin(admin.ModelAdmin):
    pass
class GradeLessonsAdmin(admin.ModelAdmin):
    filter_horizontal = ('lessons',)


class AddLessonsAdmin(admin.ModelAdmin):
    filter_horizontal = ['class_day_times','priodic_exam']  


class ClassDaysAdmin(admin.ModelAdmin):
    pass

class PriodicExamAdmin(admin.ModelAdmin):
    pass


admin.site.register(Certificate)
admin.site.register(GradeLessons,GradeLessonsAdmin)
admin.site.register(AddLessons,AddLessonsAdmin)
admin.site.register(ClassDays)
admin.site.register(PriodicExam)