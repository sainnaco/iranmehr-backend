

def choose_sms_to_send(modeladmin,request, queryset):
    queryset.update(choose_to_send=True)
choose_sms_to_send.short_description = 'انتخاب پیامک برای ارسال'

def unchoose_sms_to_send(modeladmin,request, queryset):
    queryset.update(choose_to_send=False)
unchoose_sms_to_send.short_description = 'لغو انتخاب پیامک برای ارسال'

def choose_email_to_send(modeladmin,request, queryset):
    queryset.update(choose_to_send=True)
choose_sms_to_send.short_description = 'انتخاب ایمیل برای ارسال'

def unchoose_email_to_send(modeladmin,request, queryset):
    queryset.update(choose_to_send=False)
unchoose_sms_to_send.short_description = 'لغو انتخاب ایمیل برای ارسال'