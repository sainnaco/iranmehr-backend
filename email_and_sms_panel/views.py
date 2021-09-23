from django.shortcuts import get_object_or_404, render
from rest_framework.viewsets import ModelViewSet
from .serializers import EmailSerializer
from permissions.permissions import IsStaffOrReadOnly,IsAuthorOrReadOnly
from .models import EmailPanel ,SmsPanel
from school_signup.models import Student , Family
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class EmailViewSet(ModelViewSet):
    queryset = EmailPanel.objects.all()
    serializer_class = EmailSerializer
    filterset_fields = ['category']
    search_fields = ['title','email_text']
    ordering_fields = ['choose_to_send']

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]


#هندل کردن ارسال ایمیل از پنل مدیریت خود جنگو
@login_required
def send_email_task(request, *args, **kwargs):

    user = request.user
    email_addresses = []

    if user.is_superuser or user.is_supervisor:
        try:
            email = EmailPanel.objects.get(choose_to_send=True)
            students = Student.objects.email_address()
            family = Family.objects.email_address()
            print(students)
            print(family)
                # students = [Student.objects.get(choose_to_send_email=True)]
                # family = [Family.objects.get(choose_to_send_email=True)]
            if(students):
                for i in students:
                    email_addresses.append(i.email)
            if (family):
                for i in family:
                    email_addresses.append(i.email)
            if email_addresses is None:
                messages.warning(request,'لطفا مخاطبانی را برای ارسال ایمیل انتخاب کنید')    
        
            messages.success(request,"ok")
            #call sms func
        except:
            messages.warning(request,'لطفا ایمیلی را بسازید یا انتخاب کنید')    

    else:
        messages.warning(request,'فقط مدیر سایت و مدیر مدرسه اجازه ارسال ایمیل را دارند')    


#این یکی با ای پی آی ویو هست برای پنل مدیریت با ری اکت

# @api_view(('GET',))
# def send_email_task(request):
#     email_addresses = []
#     user = request.user
#     if user.is_superuser or user.is_supervisor:
#         try:
#             email = EmailPanel.objects.get(choose_to_send=True)
#             students = Student.objects.email_address()
#             family = Family.objects.email_address()
#             print(students)
#             print(family)
#                 # students = [Student.objects.get(choose_to_send_email=True)]
#                 # family = [Family.objects.get(choose_to_send_email=True)]
#             if(students):
#                 for i in students:
#                     email_addresses.append(i.email)
#             if (family):
#                 for i in family:
#                     email_addresses.append(i.email)
#             return Response(email_addresses)
#         except:
#             return Response({'message':'لطفا ایمیلی را بسازید یا انتخاب کنید'})
#     else:
#         return Response({'message':'فقط مدیر سایت و مدیر مدرسه اجازه ارسال ایمیل را دارند'})
