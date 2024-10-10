from django.db import models
from django.contrib.auth import get_user_model

# Get the user model to avoid conflicts
User = get_user_model()

# Rooms Model
class Room(models.Model):
    SINGLE_ROOM = 'single-room'
    DOUBLE_ROOM = 'double-room'
    PREMIUM_ROOM = 'premium-room'
    DELUXE_ROOM = 'deluxe-room'

    ROOM_TYPE_CHOICES = [
        (SINGLE_ROOM, 'Single Room'),
        (DOUBLE_ROOM, 'Double Room'),
        (PREMIUM_ROOM, 'Premium Room'),
        (DELUXE_ROOM, 'Deluxe Room'),
    ]

    price = models.DecimalField(max_digits=10, decimal_places=2)
    room_type = models.CharField(max_length=100, choices=ROOM_TYPE_CHOICES)  # Updated
    subtitle = models.CharField(max_length=255)
    included_options = models.TextField()
    included_options1 = models.TextField()
    included_options2 = models.TextField()
    description = models.TextField()
    additional_description = models.TextField(blank=True, null=True)
    more_facilities = models.TextField(blank=True, null=True)
    more_facilities1 = models.TextField(blank=True, null=True)
    more_facilities2 = models.TextField(blank=True, null=True)
    more_facilities3 = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.room_type


# Comments Model
class Comment(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sender_name = models.CharField(max_length=100)
    sender_rate = models.IntegerField()
    sender_message = models.TextField()

    def __str__(self):
        return f"Comment by {self.sender_name}"
    



# Room Services Model
class RoomService(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=100)
    service_description = models.TextField()

    def __str__(self):
        return self.service_name

# Restaurant Special Offers Model
class SpecialOffer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='restaurant/offers/')

    def __str__(self):
        return self.title

# Restaurant Menu Model
class Menu(models.Model):
    types = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='restaurant/menu/')

    def __str__(self):
        return self.types

# Restaurant Foods Model
class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Restaurant Gallery Section Model
class GalleryImage(models.Model):
    image = models.ImageField(upload_to='restaurant/gallery/')

    def __str__(self):
        return f"Image {self.id}"

# SPA Services Model
class SpaService(models.Model):
    image = models.ImageField(upload_to='spa/services/')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    name = models.CharField(max_length=100)
    description = models.TextField()
    inclusions_1 = models.CharField(max_length=255)
    inclusions_2 = models.CharField(max_length=255)
    inclusions_3 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

# SPA Pricing Model
class SpaPricing(models.Model):
    image = models.ImageField(upload_to='spa/pricing/') 
    status = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    inclusions_1 = models.CharField(max_length=255)
    inclusions_2 = models.CharField(max_length=255)
    inclusions_3 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.status

# SPA Therapists Model
class Therapist(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    image = models.ImageField(upload_to='spa/therapists/')
    description = models.TextField()

    def __str__(self):
        return self.name

# Activities Model
from django.db import models

class Activity(models.Model):
    CATEGORY_CHOICES = (
        ('family_fun', 'Family Fun'),
        ('kids_playground', 'Kids Playground'),
        # Add more categories if necessary
    )
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='family_fun')  # New field for categories
    info_1 = models.TextField()
    info_2 = models.TextField()
    inclusions_1 = models.CharField(max_length=255)
    inclusions_2 = models.CharField(max_length=255)
    inclusions_3 = models.CharField(max_length=255, blank=True, null=True)
    inclusions_4 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


# Activity Images Model
class ActivityImage(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='activities/')

    def __str__(self):
        return f"Image for {self.activity.name}"



    
# Blogs Mode    l
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=255)
    blog_info = models.TextField()
    video = models.FileField(upload_to='blogs/videos/', blank=True, null=True)
    description = models.TextField()
    blog_comment = models.TextField()
    

    def __str__(self):
        return self.name
    

class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.first_name}"    

# Blog Tags Connection Model
class BlogTagConnection(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)

    def __str__(self):
        return f"Tag for {self.blog.name}"

# Tags Model
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    arrival = models.DateField()
    departure = models.DateField()
    guest = models.IntegerField()
    rooms = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)    


    def __str__(self):
        return self.email