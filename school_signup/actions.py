

def choose_people_to_send_sms(modeladmin,request, queryset):
    queryset.update(choose_to_send=True)
choose_people_to_send_sms.short_description = 'انتخاب برای ارسال پیامک'

def unchoose_people_to_send_sms(modeladmin,request, queryset):
    queryset.update(choose_to_send=False)
unchoose_people_to_send_sms.short_description = 'لغو انتخاب برای ارسال پیامک'

def choose_people_to_send_email(modeladmin,request, queryset):
    queryset.update(choose_to_send=True)
choose_people_to_send_email.short_description = 'انتخاب برای ارسال ایمیل'

def unchoose_people_to_send_email(modeladmin,request, queryset):
    queryset.update(choose_to_send=False)
unchoose_people_to_send_email.short_description = 'لغو انتخاب برای ارسال ایمیل'