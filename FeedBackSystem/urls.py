"""FeedBackSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from SabKuch import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.HomePage),
<<<<<<< HEAD
    url(r'^login_student/$', views.student_login,name='login_student'),
    url(r'^login_teacher/$', views.teacher_login,name='login_teacher'),
    url(r'^create/feedback/$',views.create_feedback,name = "create_feedback"),
=======
<<<<<<< HEAD
    url(r'^create/feedback/$',views.create_feedback, name="create_feedback"),
=======
<<<<<<< HEAD
    url(r'^login_student/$', views.student_login,name='login_student'),
    url(r'^login_teacher/$', views.teacher_login,name='login_teacher')
=======
    url(r'^create/feedback/$',views.create_feedback),
>>>>>>> 5193875c7e365ef7333f6836246882e5b31f0a85
>>>>>>> 5b5260392cda4bbaa57de0f771d1d7de9bb2da84
>>>>>>> 10ca43950ab89106963dfd84537f6739e70aef2e
]
