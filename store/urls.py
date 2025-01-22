from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_list, name='store_list'),
    path('chat/<int:store_id>/', views.chat_with_store, name='chat_with_store'),
    path('api/send_message/', views.send_message, name='send_message'),
]