from django.db import models
from categories.models import Category

class SmsPanel(models.Model):
    title = models.CharField(max_length=150, blank=True,
                             null=True, verbose_name='عنوان پیامک')

    sms_text = models.TextField(max_length=200, blank=True,
                           null=True, verbose_name="متن پیامک")
    category = models.ForeignKey(Category, blank=True , null=True , on_delete=models.SET_NULL)
    choose_to_send = models.BooleanField(
        default=False, verbose_name='انتخاب برای ارسال')

    class Meta:
        verbose_name = ' پیامک'
        verbose_name_plural = 'پنل پیامک ها'

    def __str__(self):
        return f"{self.title }"


class EmailPanel(models.Model):
    title = models.CharField(max_length=150, blank=True,
                             null=True, verbose_name='عنوان پیامک')
    email_text = models.TextField(max_length=200, blank=True,
                           null=True, verbose_name="متن پیامک")
    category = models.ForeignKey(Category, blank=True , null=True , on_delete=models.SET_NULL)

    choose_to_send = models.BooleanField(
        default=False, verbose_name='انتخاب برای ارسال')

    class Meta:
        verbose_name = ' ایمیل'
        verbose_name_plural = 'پنل ایمیل ها'

    def __str__(self):
        return f"{self.title }"        
