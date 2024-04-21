from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name='index'),
    path("contact/",views.contact,name="contact"),
    path("about/<int:myid>",views.about,name="about"),
    path("services/<int:myid>",views.services,name="services"),
    path("login/",views.loginUser,name="login"),
    path("logout/",views.logoutuser,name="logout"),
    path("sign_in/",views.sign,name="sign"),
    path('guide/',views.guide,name="guide"),
    path('services/HISTORY/',views.customer,name="customer"),

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
