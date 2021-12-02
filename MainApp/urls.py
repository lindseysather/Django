from django.urls import path

from . import views

app_name = 'MainApp'

urlpatterns = [
    path('',views.index, name='index'),

    #makes url 127.0.0.1:8000/topics
    path('topics',views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'), 
    path('new_topic/',views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'), 
]