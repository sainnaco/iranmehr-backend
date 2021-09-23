from django.contrib import admin
from .models import *
from .actions import *


admin.site.site_header = 'پنل مدیریت وب سایت مدرسه ایران مهر'
admin.site.site_title = 'ایران مهر'
admin.site.index_title = 'مدیریت سایت'
    

class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'grade', 'emergensi_phone_number','j_time','choose_to_send_email', 'social_id','sex'
                    ]

    list_display_links = ['first_name', 'last_name', 'social_id']

    search_fields = ['first_name', 'last_name', 'social_id',
                     'birth_place', 'address']
    list_filter = ['grade','sex','register_time', 'birth_month','birth_day','parent_divorced', 'parent_death', 'is_fallen_familly', 'is_veteran_familly', 'is_azadeh',
                   'is_janbaz', 'religion', 'gilder', ]
    change_list_template ='admin/studentinfo/studentinfo_change_list.html' 
    change_list_search_template = 'admin/studentinfo/studentinfo_change_list_search.html'             
    list_per_page = 50               

    #filter_horizontal = ('familly_member',)

    actions = [choose_people_to_send_sms,unchoose_people_to_send_sms]


class FamilyAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'workphone','choose_to_send_sms','choose_to_send_email','s_id']

    list_display_links = ['name', 'phone_number']

    search_fields = ['name', 'social_id', 'job','s_id']
    list_filter = ['relativ']
    change_list_template ='admin/studentinfo/studentinfo_family_change_list.html' 
    list_per_page = 50               


    #filter_horizontal = ('s',)

    actions = [choose_people_to_send_email,unchoose_people_to_send_email]


class RelationsAdmin(admin.ModelAdmin):

    list_display = ['student', 'family_to_str']
    # filter_horizontal = ('s',)
    filter_horizontal = ('f',)

    def family_to_str(self, obj):
        return " ,".join([family.name for family in obj.f.all()])
    family_to_str.short_description = 'لیست اعضای خوانواده'



admin.site.register(Student, StudentAdmin)
admin.site.register(Family, FamilyAdmin)
# admin.site.register(Relations, RelationsAdmin)
