from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import ContactMessage, UserProfile, VolunteerApplication


class StyledFormMixin:
    def apply_styles(self):
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "form-control")
            field.widget.attrs.setdefault("placeholder", field.label)


class VolunteerApplicationForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = VolunteerApplication
        fields = ["full_name", "email", "phone", "profession", "motivation"]
        labels = {
            "full_name": "Nome completo",
            "email": "E-mail",
            "phone": "Telefone",
            "profession": "Profissao atual",
            "motivation": "Como deseja ajudar?",
        }
        widgets = {
            "motivation": forms.Textarea(attrs={"rows": 4}),
            "profession": forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styles()


class ContactMessageForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["full_name", "email", "phone", "subject", "message"]
        labels = {
            "full_name": "Nome",
            "email": "E-mail",
            "phone": "Telefone",
            "subject": "Assunto",
            "message": "Mensagem",
        }
        widgets = {
            "message": forms.Textarea(attrs={"rows": 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styles()


class UserRegistrationForm(StyledFormMixin, forms.Form):
    full_name = forms.CharField(label="Nome completo", max_length=140)
    phone = forms.CharField(label="Telefone", max_length=30, required=False)
    email = forms.EmailField(label="E-mail")
    password1 = forms.CharField(label="Senha", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar senha", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styles()

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        if User.objects.filter(username=email).exists():
            raise forms.ValidationError("Ja existe um cadastro com este e-mail.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        if (
            cleaned_data.get("password1")
            and cleaned_data.get("password2")
            and cleaned_data["password1"] != cleaned_data["password2"]
        ):
            raise forms.ValidationError("As senhas informadas nao coincidem.")
        return cleaned_data

    def save(self):
        email = self.cleaned_data["email"].lower()
        user = User.objects.create_user(
            username=email,
            email=email,
            password=self.cleaned_data["password1"],
        )
        UserProfile.objects.create(
            user=user,
            full_name=self.cleaned_data["full_name"],
            phone=self.cleaned_data.get("phone", ""),
        )
        return user


class EmailAuthenticationForm(StyledFormMixin, AuthenticationForm):
    username = forms.EmailField(label="E-mail")
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styles()

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            self.user_cache = authenticate(
                self.request,
                username=username.lower(),
                password=password,
            )
            if self.user_cache is None:
                raise forms.ValidationError(
                    "Nao foi possivel entrar com os dados informados.",
                    code="invalid_login",
                )
            self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data
