from . import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include  # <-- add include
from users import views as userviews
from myapp import views as myviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myviews.home, name='home'),
    path('about/', myviews.about, name='about'),
    path('cars/', myviews.car_list, name='all_cars'),
    path('cars_details/<str:id>', myviews.car_details, name='car_details'),
    path('upload/', myviews.upload_car, name='upload_car'),
    path('update/<str:id>', myviews.update_car, name='update_car'),
    path('delete/<str:id>', myviews.delete_car, name='delete'),
    path('login/', userviews.login_view, name='login'),
    path('signup/', userviews.register_view, name='signup'),
    path('welcome/', userviews.welcome_view, name='welcome'),
    path('users/', include('users.urls')),
    path('help/', myviews.help, name='help'),
    path('purchase/<int:car_id>/', myviews.purchase_car, name='purchase_car'),
    path('contact/', myviews.contact, name='contact'),
   
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

