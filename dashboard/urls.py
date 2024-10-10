from django.urls import path
from dashboard import views


urlpatterns = [
    path('profile/', views.about, name='about'),
    
    path('element/', views.element, name='element'),
    path('gallery/', views.gallery, name='gallery'),
    path('room_detail/', views.room_detail, name='room_detail'),
    path('rooms2/', views.rooms2, name='rooms2'),
    path('rooms3/', views.rooms3, name='rooms3'),
    path('single-post/', views.single_post, name='single_post'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('contact/', views.contact, name='contact')
]
