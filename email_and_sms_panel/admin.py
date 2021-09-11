from django.contrib import admin
from .actions import *
from .models import *
# from .utils import send_sms



class SmsAdmin(admin.ModelAdmin):
    list_display = ['title','choose_to_send']
    search_fields = ['title',]
    actions = [choose_sms_to_send,unchoose_sms_to_send]
    list_per_page = 50 

class EmailAdmin(admin.ModelAdmin):
    list_display = ['title','choose_to_send']
    search_fields = ['title',]
    actions = [choose_email_to_send,unchoose_email_to_send]
    list_per_page = 50     

admin.site.register(SmsPanel,SmsAdmin)
admin.site.register(SmsPanel,SmsAdmin)

