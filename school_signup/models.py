from django.db import models
from django.conf import settings
from extensions.utils import jalali_converter
from .choices import *
from django.contrib.auth import get_user_model
User = get_user_model()

class Student(models.Model):
    signer = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='کاربرثبت نام کننده')
    first_name = models.CharField(
        verbose_name='نام', max_length=50, blank=True)
    last_name = models.CharField(
        verbose_name='نام خوانوادگی', max_length=100, blank=True, null=True)
    sex = models.CharField(
        verbose_name='جنسیت', choices=SEX_CHOICES, max_length=50, null=True, blank=True)
    social_id = models.CharField(
        verbose_name='شماره ملی', max_length=10, null=True, blank=True)
    phone_number = models.CharField(max_length=11,
                                    verbose_name='شماره تلفن', null=True, blank=True)
    birth_day = models.CharField(
        verbose_name='روز تولد', max_length=50, choices=DAY_CHOICES, null=True, blank=True)
    birth_month = models.CharField(
        choices=MONTH_CHOICES, verbose_name='ماه تولد', null=True, max_length=50, blank=True)
    birth_year = models.IntegerField(
        verbose_name='سال تولد', null=True, blank=True)
    birth_place = models.CharField(
        verbose_name='محل صدور', max_length=100, null=True, blank=True)
    register_time = models.DateTimeField(
        auto_now_add=True, verbose_name='زمان ثبت نام', null=True, blank=True)

    religion = models.CharField(
        verbose_name='دین', choices=RELIGION_CHOICES, max_length=50, null=True, blank=True)

    gilder = models.CharField(
        verbose_name='مذهب', choices=GILDER_CHOICES, max_length=50, null=True, blank=True)

    grade = models.CharField(
        verbose_name='مقطع', choices=GRADE_CHOICES, max_length=50, null=True, blank=True)
    branch = models.CharField(
        verbose_name='شعبه', max_length=50, null=True, blank=True)
    last_edu_year = models.IntegerField(
        verbose_name='سال تحصیلی قبل', null=True, blank=True)
    previos_institutions = models.CharField(
        verbose_name='نام آموزشگاه قبلی', max_length=100, null=True, blank=True)
    city = models.CharField(
        verbose_name='شهرستان', max_length=100, null=True, blank=True)
    urban_section = models.CharField(
        verbose_name='ناحیه', max_length=100, null=True, blank=True)
    # familly_member = models.ManyToManyField(
    #    'Familly',blank=True,null=True, verbose_name='اطلاعات اعضای خوانواده(در صورت وجود اطلاعات خانواده ازقسمت چپ جستجو کرده و با دوبار کلیک به سمت راست اضافه کنید در غیر این صورت علامت به علاوه را زده و سپس اطلاعات عضو خانواده را وارد کنید..توجه داشته باشید در صفحه باز شده گزینه اضافه کردن دانش اموز را نزنید)')
    parent_divorced = models.BooleanField(
        verbose_name='آیاوالدین جدا شده اند؟', default=False, null=True, blank=True)
    divorce_date = models.IntegerField(
        verbose_name='تاریخ جدایی والدین', null=True, blank=True)
    parent_death = models.BooleanField(
        verbose_name='آیاوالدین یا یکی از انها فوت کرده اند؟', default=False, blank=True, null=True)
    death_date = models.IntegerField(
        verbose_name='سال فوت', null=True, blank=True)
    is_fallen_familly = models.BooleanField(
        verbose_name='خانواده شهید', default=False, blank=True, null=True)
    is_veteran_familly = models.BooleanField(
        verbose_name='مفقود الاثر', default=False, blank=True, null=True)
    is_azadeh = models.BooleanField(
        verbose_name='آزاده', default=False, blank=True, null=True)

    is_janbaz = models.BooleanField(
        verbose_name='جانباز', default=False, blank=True, null=True)

    darsad = models.IntegerField(
        default=0, verbose_name='درصد', null=True, blank=True)

    address = models.TextField(verbose_name='آدرس منزل', null=True, blank=True)
    zip_code = models.CharField(
        verbose_name='کد پستی', max_length=10, null=True, blank=True)

    home_phone_number = models.CharField(
        max_length=11, verbose_name='شماره تلفن منزل', null=True, blank=True)
    emergensi_phone_number = models.CharField(
        max_length=11, verbose_name='شماره تلفن ضروری', null=True, blank=True)
    choose_to_send_sms = models.BooleanField(
        default=False, verbose_name='انتخاب برای ارسال پیامک')
    choose_to_send_email = models.BooleanField(
        default=False, verbose_name='انتخاب برای ارسال ایمیل')  

    class Meta:
        verbose_name = 'اطلاعات فردی دانش آموزان'
        verbose_name_plural = 'اطلاعات فردی دانش آموزان'

    if last_name == '':
        def __str__(self):

            return f"{self.first_name }"

    def __str__(self):

        return f"{self.first_name +''+ self.last_name }"

    def j_time(self):
        return jalali_converter(self.register_time)
    j_time.short_description = 'تاریخ ثبت نام'


class Family(models.Model):
    signer = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='کاربر ثبت نام کننده')

    name = models.CharField(
        verbose_name='نام و نام خوانوادگی', max_length=200, null=True, blank=True)
    relativ = models.CharField(
        choices=RELATIV_CHOICES, verbose_name='نسبت', max_length=150, null=True, blank=True)

    #s = models.ManyToManyField(Student, verbose_name='دانش آموز', blank=True)
    phone_number = models.CharField(max_length=11,
                                    verbose_name='شماره تلفن', null=True, blank=True)
    social_id = models.CharField(
        verbose_name='شماره ملی عضو خانواده', max_length=10, null=True, blank=True)
    s_id = models.CharField(
        verbose_name='شماره ملی دانش آموز', max_length=10, null=True, blank=True)
    age = models.IntegerField(
        verbose_name='سن', null=True, blank=True)
    education = models.CharField(
        verbose_name='تحصیلات', max_length=150, null=True, blank=True)
    job = models.CharField(
        verbose_name='شغل', max_length=200, null=True, blank=True)
    workplace = models.TextField(
        verbose_name='محل کار', max_length=250, null=True, blank=True)
    workphone = models.CharField(max_length=11,
                                 verbose_name='شماره تلفن محل کار', null=True, blank=True)

    choose_to_send_sms = models.BooleanField(
        default=False, verbose_name='انتخاب برای ارسال پیامک')
    choose_to_send_email = models.BooleanField(
        default=False, verbose_name='انتخاب برای ارسال ایمیل')
    class Meta:
        verbose_name = 'اطلاعات خوانوادگی دانش آموزان'
        verbose_name_plural = 'اطلاعات خوانوادگی دانش آموزان'

    def __str__(self):
        return f"{self.name }"


class Relations(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, null=True, blank=True, verbose_name='دانش آموز')
    #s = models.ManyToManyField(Student,blank=True ,verbose_name="دانش آموزان")
    f = models.ManyToManyField(
        Family, blank=True, verbose_name="اعضای خوانواده")

    class Meta:
        verbose_name = 'جدول اعضای خانوادگی'
        verbose_name_plural = 'جدول اعضای خانوادگی'

