from django.urls import path , include

urlpatterns = [
    path('blog/',include('blog.api.urls')),
    path('users/',include('accounts.urls')),
    path('categories/',include('categories.urls')),
    path('gallery/',include('gallery.urls')),
    path('school-signup/',include('school_signup.urls')),
    path('email-panel/',include('email_and_sms_panel.urls')),

]