# import Http Response from django
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from .models import *
from .forms import *
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def landing_page_view(request):
    """
    Renders Landing Page 
    """

    return render(request, "landingPage.html")


def home_view(request):
    """
    Renders Home Page 
    """    

    return render(request, "home.html")


def about_view(request):
    """
    Renders About Page 
    """    

    return render(request, "about/about.html")


def category_view(request):
    """
    Renders Categories Page 
    """   

    return render(request, "categories/categories.html")


def event_view(request):
    """
    Renders Event Page 
    """   
    events = Event.objects.all()

    return render(request, "events/events.html", {"events": events})


def display_event_view(request, pk):
    """
    Renders Single Event Display Page
    ---
    Parameters
    pk -> primary key of the event
    ---
    """       

    try:
        event = Event.objects.get(pk=pk)

        return render(request, "events/displayEvent.html", {"event": event})

    except Event.DoesNotExist:

        return render(request, "home.html")    

    return None 


def project_view(request):
    """
    Renders Project Page 
    """       

    projects = Project.objects.all()

    return render(request, "projects/projects.html", {"projects": projects})


def display_project_view(request, pk):
    """
    Renders Single Project Display Page
    ---
    Parameters
    pk -> primary key of the event
    ---
    """        

    try:
        project = Project.objects.get(pk=pk)

        return render(request, "projects/displayProject.html", {"project": project})

    except Project.DoesNotExist:

        return render(request, "home.html")    

    return None 


def add_subscriber_view(request):
    """
    Add a subscriber in the database
    ---
    Parameters
    POST METHOD -> Receives subscriber's email address
    ---
    """            

    if request.method == 'POST':
        email_address = request.POST.get('email', None)
        if email_address is not None:
            _  , __isCreated = Subscriber.objects.get_or_create(email_address=email_address)
            if not __isCreated:
                return render(request, "home.html", {"warning": "You are already a subscriber, Thanks :)"})
            else:
                return render(request, "home.html", {"success": "You are now a subscriber, Thanks :)"})
    return redirect(home_view)



# -------------------------------ADMIN VIEWS----------------------------------------



def login_view(request):
    """
    Renders Admin Login Page
    """         

    return render(request, "emag_admin/login.html")


def authenticate_view(request):
    """
    Authenticate Admin
    ---
    Paramaters
    POST METHOD -> Receives email address and password
    ---
    """      

    if request.method == 'POST':
        email    = request.POST.get('email')
        password = request.POST.get('password')

        user     = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect(event_form_view)
        else:
            return render(request, "emag_admin/login.html", {"error": "Invalid Credentials"})    

    return render(request, "emag_admin/login.html")


@login_required(login_url='/emag/admin/')
def event_form_view(request):
    """
    Renders Admin Add Event Page
    """         

    return render(request, "emag_admin/addEvent.html")


@login_required(login_url='/emag/admin/')
def add_event_view(request):
    """
    Add Event in the database
    ---
    Paramaters
    POST METHOD -> Receives event data
    ---
    """        

    if request.method == 'POST':

        title           =   request.POST.get('title')
        description     =   request.POST.get('editor')
        category        =   request.POST.get('category')
        tags            =   request.POST.get('tag')
        banner          =   request.FILES.get('banner')
        data            =   request.FILES.get('data', None)
        organised_by    =   request.POST.get('organised_by', None)
        sponsored_by    =   request.POST.get('sponsored_by', None)
        event_date      =   request.POST.get('event_date', None)

        Event.objects.create(user_id=request.user, event_title=title, event_description=description, event_category=category, event_tags=tags, event_banner=banner, event_data=data, organised_by=organised_by, sponsored_by=sponsored_by, event_date=event_date)
        
        return redirect(event_view)


def logout_view(request):
    """
    Log out Admin
    """        
    logout(request)
    return redirect(login_view)