from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import HttpResponse
from django.utils.http import is_safe_url
from .forms import LoginForm, RegisterForm, RegisterFormFirma, RegisterFormOpiekun
from django.views.generic.edit import CreateView, FormView

User = get_user_model()


class OpiekunRegisterView(CreateView):
    form_class = RegisterFormOpiekun
    template_name = 'registration/signup_opiekun.html'
    success_url = '/'

    def form_invalid(self, form):
        return HttpResponse("Podaj wszystkie wymagane dane do rejestracji")


class UserRegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/signup.html'
    success_url = '/'

    def form_invalid(self, form):
        return HttpResponse("Podaj wszystkie wymagane dane do rejestracji")


class FirmaRegisterView(CreateView):
    form_class = RegisterFormFirma
    template_name = 'registration/signup_firm.html'
    success_url = '/'

    def form_invalid(self, form):
        return HttpResponse("Podaj wszystkie wymagane dane do rejestracji")


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'registration/login.html'
    success_url = 'profile.html'

    def form_valid(self, form):
        request = self.request
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        return super(LoginView, self).form_invalid(form)


def logout_view(request):
    logout(request)
    return render(request, 'index.html')
