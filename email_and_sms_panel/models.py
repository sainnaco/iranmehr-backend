from django.db import models

class SmsPanel(models.Model):
    title = models.CharField(max_length=150, blank=True,
                             null=True, verbose_name='عنوان پیامک')
    sms = models.TextField(max_length=200, blank=True,
                           null=True, verbose_name="متن پیامک")
    choose_to_send = models.BooleanField(
        default=False, verbose_name='انتخاب برای ارسال')

    class Meta:
        verbose_name = ' پیامکی'
        verbose_name_plural = 'پنل پیامکی'

    def __str__(self):
        return f"{self.title }"


class EmailPanel(models.Model):
    title = models.CharField(max_length=150, blank=True,
                             null=True, verbose_name='عنوان پیامک')
    sms = models.TextField(max_length=200, blank=True,
                           null=True, verbose_name="متن پیامک")
    choose_to_send = models.BooleanField(
        default=False, verbose_name='انتخاب برای ارسال')

    class Meta:
        verbose_name = ' پیامکی'
        verbose_name_plural = 'پنل پیامکی'

    def __str__(self):
        return f"{self.title }"        
