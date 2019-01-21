from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import UserRegisterView, FirmaRegisterView, LoginView, logout_view, OpiekunRegisterView
from SRP.views import lista_praktyk, lista_praktyk_firma, stworz_Praktyke, edytuj_praktyke, usun_praktyke, main_page, \
    user_profile, dolaczdopraktyk, listafirm, activefirm

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', main_page, name='main'),
                  path('main/', main_page, name='main_page'),
                  path('login/', LoginView.as_view(), name='login'),
                  path('logout/', logout_view, name='logout'),
                  path('signup_opiekun/', OpiekunRegisterView.as_view(), name='signup_opiekun'),
                  path('signup_firm/', FirmaRegisterView.as_view(), name='signup_firm'),
                  path('signup/', UserRegisterView.as_view(), name='signup'),
                  path('user_settings/', user_profile, name='user_settings'),
                  path('listafirm/', listafirm, name='listafirm'),
                  path('listafirm/activefirm/<int:id>', activefirm, name='activefirm'),
                  path('praktyki/', lista_praktyk, name='praktyki'),
                  path('praktyki_firma/', lista_praktyk_firma, name='praktyki_firma'),
                  path('str_pr/', stworz_Praktyke, name='create_practice'),
                  path('praktyki/edytuj_praktyke/<int:id_Praktyki>', edytuj_praktyke, name="edytuj_praktyke"),
                  path('praktyki/usun_praktyke/<int:id_Praktyki>', usun_praktyke, name="usun_praktyke"),
                  path('praktyki_firma/edytuj_praktyke/<int:id_Praktyki>', edytuj_praktyke, name="edytuj_praktyke"),
                  path('praktyki_firma/usun_praktyke/<int:id_Praktyki>', usun_praktyke, name="usun_praktyke"),
                  path('praktyki/dolacz/<int:id_Praktyki>', dolaczdopraktyk, name='dolacz'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
