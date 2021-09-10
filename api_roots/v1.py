from django.urls import path , include

urlpatterns = [
    path('blog/',include('blog.api.urls')),
    path('users/',include('accounts.urls')),
    path('categories/',include('categories.urls')),
    path('gallery/',include('gallery.urls')),

]