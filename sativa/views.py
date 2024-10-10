from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import RoomForm, CommentForm, BookingForm, SpecialOfferForm, MenuForm, FoodForm, SpaServiceForm, SpaPricingForm, TherapistForm, ActivityForm, ActivityImageForm, BlogForm
from project import settings
# Create your views here.
from .models import Room, Comment, Booking, SpecialOffer, Menu, Food, SpaService, SpaPricing, Therapist, Activity, ActivityImage, Blog, BlogComment
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse


# Superuserligini tekshiruvchi funksiya
def superuser_required(user):
    return user.is_superuser


@user_passes_test(superuser_required)
def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Room has been added successfully')
            return redirect('rooms1')
    else:
        form = RoomForm()


    return render(request, 'add_room.html', {'form': form})        


from .models import Room
from django.shortcuts import get_object_or_404
import logging

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Room, Booking
from .forms import BookingForm
import logging

logger = logging.getLogger(__name__)

def rooms1(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            logger.info("Form is valid. Saving booking...")
            booking = form.save(commit=False)
            booking.user = request.user
            booking.email = request.user.email
            booking.save()

            # Send confirmation email
            send_mail(
                subject=f'Booking from {request.user.first_name}',
                message=f'Message: {booking}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[request.user.email],
                fail_silently=False
            )
            return redirect('homepage')
        else:
            logger.warning("Form is invalid: %s", form.errors)  # Log errors
    else:
        form = BookingForm()

    rooms = Room.objects.all()  # Fetch all room data from the database

    return render(request, 'rooms1.html', {'rooms': rooms, 'form': form})




def homepage(request):
    rooms = Room.objects.all()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.email = request.user.email
            booking.save()

            send_mail(
                subject=f'Booking from {request.user.first_name}',
                message=f'Message: {booking}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[request.user.email],
                fail_silently=False
                )    
            return redirect('homepage') 

    else:
        form = BookingForm() 

    return render(request, 'index.html', {'form': form, 'rooms': rooms})





def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    comments = Comment.objects.filter(room=room)
    
    form = None 

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.room = room
                comment.user = request.user
                comment.sender_name = request.user.first_name
                comment.save()
                return redirect('room_detail', pk=pk)

    else:
        # Initialize an empty form for GET requests
        form = CommentForm()   



    return render(request, 'room-detail.html', {'room' : room, 'form' : form, 'comments': comments})




def restaurant(request):
    offers = SpecialOffer.objects.all()
    menu_all = Menu.objects.all()
    foods = Food.objects.all()
    return render(request, 'restaurant.html', {'offers': offers,'menu_all': menu_all, 'foods': foods})

# Superuserligini tekshiruvchi funksiya
def superuser_required(user):
    return user.is_superuser


@user_passes_test(superuser_required)
def add_offer(request):
    if request.method == 'POST':
        form = SpecialOfferForm(request.POST, request.FILES )
        form_menu = MenuForm(request.POST, request.FILES)
        form_food = FoodForm(request.POST)
        if 'offer_submit' in request.POST:

            if form.is_valid():
                form.save()
                return redirect('add-offer')
        elif 'menu_submit' in request.POST:
            if form_menu.is_valid():
                form_menu.save()
                return redirect('add-offer')
        elif 'food_submit' in request.POST:
            if form_food.is_valid():
                form_food.save()
                return redirect('add-offer')
                

        
        
    else:
        form = SpecialOfferForm()
        form_menu = MenuForm()
        form_food = FoodForm()
            
    return render(request, 'add_offer.html', {'form': form, 'form_menu': form_menu, 'form_food': form_food})  



def spa(request):
    spa_service = SpaService.objects.all()
    spa_pricing = SpaPricing.objects.all()
    therapist = Therapist.objects.all()
    return render(request, 'spa.html', {'spa_service': spa_service, 'spa_pricing': spa_pricing, 'therapist': therapist})

# Superuserligini tekshiruvchi funksiya
def superuser_required(user):
    return user.is_superuser


@user_passes_test(superuser_required)
def add_spa_service(request):
    if request.method == 'POST':
        spa_service_form = SpaServiceForm(request.POST, request.FILES )
        spa_pricing_form = SpaPricingForm(request.POST, request.FILES)
        therapist_form = TherapistForm(request.POST, request.FILES)
        if 'spa_service_submit' in request.POST:
            if spa_service_form.is_valid():
                spa_service_form.save()
                return redirect('add-spa')
        if 'spa_pricing_submit' in request.POST:
            if spa_pricing_form.is_valid():
                spa_pricing_form.save()
                return redirect('add-spa')
        if 'therapist_submit' in request.POST:   
            if therapist_form.is_valid():
                therapist_form.save()
                return redirect('add-spa')

    else:
        spa_pricing_form = SpaPricingForm()
        spa_service_form = SpaServiceForm()         
        therapist_form = TherapistForm()

    return render(request, 'add_spa.html', {'spa_service_form': spa_service_form, 'spa_pricing_form': spa_pricing_form, 'therapist_form': therapist_form})   




def activities(request):
    family_fun_activities = Activity.objects.filter(category='family_fun')
    kids_playground_activities = Activity.objects.filter(category='kids_playground')
    outdoor_activities = Activity.objects.filter(category='outdoor')
    gym_activities = Activity.objects.filter(category='gym')

    activity_image = ActivityImage.objects.all()
    family_fun_images = ActivityImage.objects.filter(activity__category='family_fun')
    kids_playground_images = ActivityImage.objects.filter(activity__category='kids_playground')


    return render(request, 'activities.html', {
        'family_fun_activities': family_fun_activities,
        'kids_playground_activities': kids_playground_activities,
        'outdoor_activities': outdoor_activities,
        'gym_activities': gym_activities,
        'activity_image': activity_image,
    })


# Superuserligini tekshiruvchi funksiya
def superuser_required(user):
    return user.is_superuser


@user_passes_test(superuser_required)
def add_activity(request):
    if request.method == 'POST':
        activity_form = ActivityForm(request.POST)
        activity_image = ActivityImageForm(request.POST, request.FILES)

    if 'activity_submit' in request.POST:
        if activity_form.is_valid():
            activity_form.save()
            return redirect('add-activity')
    if 'activity_image_submit'in request.POST:
        if activity_image.is_valid():
            activity_image.save()
            return redirect('add-activity')
        
    else:
        activity_image = ActivityImageForm()
        activity_form = ActivityForm()

    return render(request, 'add-activity.html', {'activity_form': activity_form, 'activity_image': activity_image})        



def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html', {'blog': blog})



def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id = blog_id)
    comments = blog.comments.all()
    if request.method == 'POST':
        content = request.POST.get('content')
        BlogComment.objects.create(blog=blog, user=request.user, message=content)
        return redirect('blog_detail', blog_id=blog_id)
    return render(request, 'single-post.html', {'comments': comments, 'blog': blog})


# Superuserligini tekshiruvchi funksiya
def superuser_required(user):
    return user.is_superuser


@user_passes_test(superuser_required)
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('add-blog')
    
    else:
        form = BlogForm()


    return render(request, 'add_blog.html', {'form': form})    



# Superuserligini tekshiruvchi funksiya
def superuser_required(user):
    return user.is_superuser


@user_passes_test(superuser_required)
def admin(request):
    return render(request, 'admin_page.html')