from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
User = get_user_model()

DAY_CHOICES = (
    ('0','شنبه'),
    ('1','یکشنبه'),
    ('2','دوشنبه'),
    ('3','سه شنبه'),
    ('4','چهارشنبه'),
    ('5','پنج شنبه'),
    ('6','جمعه')
)
GRADE_CHOICES =(
    ('10','دهم'),
    ('11','یازدهم'),
    ('12','دوازدهم')
)

class Certificate(models.Model):
    pass

class GradeLessons(models.Model):
    class_name = models.CharField(max_length=255,blank=True,null=True,verbose_name='نام کلاس(یا شعبه)')
    grade = models.CharField(choices=GRADE_CHOICES,max_length=2, blank=True, null=True,verbose_name='مقطع')
    lessons = models.ManyToManyField('AddLessons', blank=True,verbose_name='دروس')


class AddLessons(models.Model):
    lesson = models.CharField(max_length=255, blank=True, null=True,verbose_name='نام درس')
    teacher = models.ForeignKey(User,max_length=255,on_delete=models.CASCADE, blank=True, null=True,verbose_name='استاد درس')
    class_day_times = models.ManyToManyField('ClassDays', verbose_name='روز یا روزهای کلاس')
    class_time_from = models.IntegerField(blank=True, null=True,verbose_name='ساعت شروع کلاس')
    class_time_to = models.IntegerField(blank=True, null=True,verbose_name='ساعت اتمام کلاس')
    priodic_exam = models.ManyToManyField('PriodicExam',verbose_name='امتحانات دوره ای(مستمر)')
    final_exam_day = models.DateField(blank=True, null=True,verbose_name='تاریخ امتحان پایانی')
    final_exam_time = models.TimeField(blank=True, null=True,verbose_name='ساعت امتحان پایانی')

class ClassDays(models.Model):
    class_day = models.CharField(choices=DAY_CHOICES,max_length=2, blank=True, null=True,verbose_name='اضافه کردن روز یا روز های کلاس')


class PriodicExam(models.Model):
    priodic_exam_time = models.DateTimeField(blank=True, null=True,verbose_name='تاریخ امتحان دوره ای')
    class_time_from = models.IntegerField(blank=True, null=True,verbose_name='ساعت شروع امتحان')
    description = models.TextField(blank=True, null=True,verbose_name='توضیحات امتحان')