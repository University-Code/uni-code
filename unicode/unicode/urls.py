from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from users import views as user_views
from problems.views import index



admin.autodiscover()

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls,),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', user_views.register, name='register'), 
    path('problems/', include("problems.urls")),
    path('editor/', include('problems.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=( staticfiles_urlpatterns())
