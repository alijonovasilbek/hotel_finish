from django.shortcuts import render

def profile(request):
    return render(request, 'profile.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')

def element(request):
    return render(request, 'element.html')

def gallery(request):
    return render(request, 'gallery.html')


def room_detail(request):
    return render(request, 'room-detail.html')

def rooms2(request):
    return render(request, 'rooms2.html')

def rooms3(request):
    return render(request, 'rooms3.html')

def single_post(request):
    return render(request, 'single-post.html')

def testimonial(request):
    return render(request, 'testimonial.html')


def contact(request):
    return render(request, 'contact.html')

