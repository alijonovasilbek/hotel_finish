from django.urls import path
from . import views



urlpatterns = [
    path('add-room/', views.add_room, name='add_room'),
    path('rooms1/', views.rooms1, name='rooms1'),
    path('room-detail/<int:pk>/', views.room_detail, name='room_detail'),
    path('', views.homepage, name='homepage'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('add-offer/', views.add_offer, name='add-offer'),
    path('spa/', views.spa, name='spa'),
    path('add-spa/', views.add_spa_service, name='add-spa'),
    path('activities/', views.activities, name='activities'),
    path('add-activity/', views.add_activity, name='add-activity'),
    path('blog/', views.blog,name='blog'),
    path('add-blog/', views.add_blog, name='add-blog'),
    path('blogs/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('admin-page/', views.admin, name='admin-page')
]