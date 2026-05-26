from django.urls import path

from .views import (
    SiteLoginView,
    contact_submit,
    events_page,
    home,
    logout_view,
    register_view,
    testimonials_page,
    volunteer_page,
)

urlpatterns = [
    path("", home, name="home"),
    path("eventos/", events_page, name="events"),
    path("depoimentos/", testimonials_page, name="testimonials"),
    path("voluntariado/", volunteer_page, name="volunteer"),
    path("contato/", contact_submit, name="contact_submit"),
    path("entrar/", SiteLoginView.as_view(), name="login"),
    path("cadastro/", register_view, name="register"),
    path("sair/", logout_view, name="logout"),
]
