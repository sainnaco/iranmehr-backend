from django.urls import path , include

urlpatterns = [
    path('blog/',include('blog.blog_api.blog_api_urls')),
    path('users/',include('accounts.urls')),

]