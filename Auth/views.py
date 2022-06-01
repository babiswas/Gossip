from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from .forms import RegisterForm


class AppLogin(LoginView):
    template_name = 'Auth/loginview_form.html'


class RegisterView(FormView):
    template_name = 'Auth/register.html'
    form_class = RegisterForm
    success_url = '/auth/login/'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)
