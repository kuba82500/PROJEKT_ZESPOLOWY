from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from SRP.views import signup_view, lista_praktyk, stworz_Praktyke, edytuj_praktyke, usun_praktyke, CRUD
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('SRP/', include('SRP.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup_view, name='signup'),
    path('praktyki/', lista_praktyk, name='praktyki'),
    path('str_pr/', stworz_Praktyke, name='str_pr'),
    path('edytuj_praktyke/<int:id_Praktyki>/', edytuj_praktyke, name="edytuj_praktyke"),
    path('usun_praktyke/<int:id_Praktyki>/', usun_praktyke, name="usun_praktyke"),
    path('CRUD/', CRUD, name="CRUD"),
    path(r'^__debug__', include(debug_toolbar.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
