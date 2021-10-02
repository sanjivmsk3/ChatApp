from django.urls import path
from app.views import *
from  django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',UserRegistration.as_view(),name='home'),
    path('login',Home.as_view(), name='login'),
    path('logout',LogOut.as_view(),name='logout'),
    path('user-details',UserDetails.as_view(),name='user-details'),
    path('add-post',AddPost.as_view(),name='add-post'),
    path('update-post/<int:pk>',UpdatePost.as_view(),name='update-post'),
    path('search',Search.as_view(),name='search'),
    path('chat',Chat.as_view(),name='chat')

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)