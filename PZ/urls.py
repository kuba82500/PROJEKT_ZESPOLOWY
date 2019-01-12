from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import UserRegisterView, FirmaRegisterView, LoginView, logout_view
from SRP.views import lista_praktyk, stworz_Praktyke, edytuj_praktyke, usun_praktyke, CRUD, main_page, user_profile


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='main'),
    path('main/', main_page, name='main_page'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup_firm/', FirmaRegisterView.as_view(), name='signup_firm'),
    path('signup/', UserRegisterView.as_view(), name='signup'),
    path('user_settings/', user_profile, name='user_settings'),
    path('praktyki/', lista_praktyk, name='praktyki'),
    path('str_pr/', stworz_Praktyke, name='create_practice'),
    path('edytuj_praktyke/<int:id_Praktyki>/', edytuj_praktyke, name="edytuj_praktyke"),
    path('usun_praktyke/<int:id_Praktyki>/', usun_praktyke, name="usun_praktyke"),
    path('CRUD/', CRUD, name="CRUD"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
