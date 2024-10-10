from django import forms
from .models import Room, Comment, Booking, SpecialOffer, Menu, Food, SpaService, SpaPricing, Therapist, Activity, ActivityImage, Blog, BlogComment


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            'price',
            'room_type',
            'subtitle',
            'included_options',
            'included_options1',
            'included_options2',
            'description',
            'additional_description',
            'more_facilities',
            'more_facilities1',
            'more_facilities2',
            'more_facilities3',
            
        ]

class CommentForm(forms.ModelForm):
    RATE_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    sender_rate = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select())

    class Meta:
        model = Comment
        fields = [
            'sender_rate',
            'sender_message'
        ]        




class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'arrival',
            'departure',
            'guest',
            'rooms',

        ]

        


class SpecialOfferForm(forms.ModelForm):
    class Meta:
        model = SpecialOffer   
        fields = [
            'title',
            'description',
            'image'
        ]     


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = [
            'types',
            'description',
            'image'
        ]


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = [
            'name',
            'description',
            'price',
            'menu'
        ]


class SpaServiceForm(forms.ModelForm):
    class Meta:
        model = SpaService
        fields = [
            'image',
            'price',
            'name',
            'description',
            'inclusions_1',
            'inclusions_2',
            'inclusions_3'
        ] 

class SpaPricingForm(forms.ModelForm):
    class Meta:

        model = SpaPricing
        fields = [
            'image',
            'status',
            'price',
            'inclusions_1',
            'inclusions_2',
            'inclusions_3'
        ]  


class TherapistForm(forms.ModelForm):
    class Meta:
        model = Therapist
        fields = [
            'name',
            'job',
            'image',
            'description'
        ]             


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = [
            'name',
            'info_1',
            'info_2',
            'inclusions_1',
            'inclusions_2',
            'inclusions_3',
            'inclusions_4',
        ]     



class ActivityImageForm(forms.ModelForm):
    class Meta:
        model = ActivityImage
        fields = [
            'activity',
            'image'
        ]          




class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'name',
            'blog_info',
            'video',
            'description',
            'blog_comment'
        ]       