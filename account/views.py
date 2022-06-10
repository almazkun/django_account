from django.urls import reverse_lazy
from django.views.generic import CreateView

from account.forms import CustomUserCreationForm


# Create your views here.
class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("signin")