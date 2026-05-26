from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .forms import (
    ContactMessageForm,
    EmailAuthenticationForm,
    UserRegistrationForm,
    VolunteerApplicationForm,
)
from .models import DonationTier, Event, Service, SiteConfiguration, Statistic, Testimonial


class SiteLoginView(LoginView):
    authentication_form = EmailAuthenticationForm
    template_name = "registration/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(common_context())
        return context


def get_site_config():
    return SiteConfiguration.objects.first() or SiteConfiguration()


def common_context():
    return {"site_config": get_site_config()}


def home(request):
    context = {
        **common_context(),
        "statistics": Statistic.objects.filter(is_active=True),
        "services": Service.objects.filter(is_active=True),
        "featured_events": Event.objects.filter(is_active=True, is_featured=True)[:3],
        "featured_testimonials": Testimonial.objects.filter(
            is_active=True,
            is_featured=True,
        )[:3],
        "donation_tiers": DonationTier.objects.filter(is_active=True),
        "contact_form": ContactMessageForm(),
    }
    return render(request, "core/home.html", context)


def events_page(request):
    context = {
        **common_context(),
        "events": Event.objects.filter(is_active=True),
    }
    return render(request, "core/events.html", context)


def testimonials_page(request):
    context = {
        **common_context(),
        "testimonials": Testimonial.objects.filter(is_active=True),
    }
    return render(request, "core/testimonials.html", context)


def volunteer_page(request):
    if request.method == "POST":
        form = VolunteerApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Inscricao enviada com sucesso.")
            return redirect("volunteer")
    else:
        form = VolunteerApplicationForm()

    context = {
        **common_context(),
        "form": form,
    }
    return render(request, "core/volunteer.html", context)


def contact_submit(request):
    if request.method != "POST":
        return redirect("home")

    form = ContactMessageForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Mensagem enviada com sucesso.")
    else:
        messages.error(request, "Nao foi possivel enviar a mensagem. Verifique os campos.")
    return redirect("home")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Cadastro realizado com sucesso.")
            return redirect("home")
    else:
        form = UserRegistrationForm()

    context = {
        **common_context(),
        "form": form,
    }
    return render(request, "registration/register.html", context)


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Sessao encerrada com sucesso.")
    return redirect("home")
