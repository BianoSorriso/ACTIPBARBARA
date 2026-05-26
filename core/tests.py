from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import ContactMessage, UserProfile, VolunteerApplication


class PublicPagesTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cuidando de quem")

    def test_contact_form_creates_message(self):
        response = self.client.post(
            reverse("contact_submit"),
            {
                "full_name": "Maria Silva",
                "email": "maria@example.com",
                "phone": "21999990000",
                "subject": "Ajuda",
                "message": "Gostaria de saber como ajudar.",
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 1)

    def test_volunteer_form_creates_application(self):
        response = self.client.post(
            reverse("volunteer"),
            {
                "full_name": "Carlos Souza",
                "email": "carlos@example.com",
                "phone": "21999991111",
                "profession": "Voluntario Geral",
                "motivation": "Quero apoiar a rotina do abrigo.",
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(VolunteerApplication.objects.count(), 1)


class AuthenticationFlowTests(TestCase):
    def test_register_creates_user_and_profile(self):
        response = self.client.post(
            reverse("register"),
            {
                "full_name": "Ana Rocha",
                "phone": "21988887777",
                "email": "ana@example.com",
                "password1": "SenhaSegura123",
                "password2": "SenhaSegura123",
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username="ana@example.com").exists())
        self.assertTrue(UserProfile.objects.filter(user__username="ana@example.com").exists())
