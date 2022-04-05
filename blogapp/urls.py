from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main_index', views.index, name='main_index'),

    path('register', views.register, name='register'),
    path('signin', views.signin, name='signin'),
    path('home', views.home, name='home'),
    path('member', views.member, name='member'),
    path('signout', views.signout, name='signout'),
    
    path('member-list', views.member_details, name='member-list'),
    path('newcomer-list', views.newcomer_details, name='newcomer-list'),

    path('<int:ref_id>', views.activity_stream, name="activity_stream"),
    # path('activity_stream/<int:ref_id>', activity_stream_details, name="activity_stream_details"),
    # path('activity_stream/', views.signout, name='signout'),


]



