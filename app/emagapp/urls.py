from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', landing_page_view),
    path('welcome/', home_view),
    path('about/', about_view),
    path('add/subscriber', add_subscriber_view),
    path('categories/', category_view),
    path('categories/events/', event_view),
    path('categories/projects/', project_view),
    path('event/', display_event_view),
    path('project/<int:pk>', display_project_view),
    path('event/<int:pk>', display_event_view),
    path('emag/admin/', login_view),
    path('success/', authenticate_view),
    path('add-event/', event_form_view),
    path('event/add', add_event_view),
    path('logout/', logout_view)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)