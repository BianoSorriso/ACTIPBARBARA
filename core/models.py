from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class OrderedContent(models.Model):
    order = models.PositiveIntegerField(default=0, verbose_name="Ordem")
    is_active = models.BooleanField(default=True, verbose_name="Ativo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ("order", "id")


class SiteConfiguration(models.Model):
    organization_name = models.CharField(max_length=120, default="ACITP")
    hero_badge = models.CharField(
        max_length=180,
        default="ONG ACITP - A CASA DO IDOSO PARA TODOS OS POVOS",
    )
    hero_title = models.CharField(
        max_length=180,
        default="Cuidando de quem sempre cuidou de nos",
    )
    hero_description = models.TextField(
        default=(
            "Ha 15 anos levando dignidade, amor e qualidade de vida para idosos "
            "em situacao de vulnerabilidade."
        )
    )
    history_title = models.CharField(
        max_length=180,
        default="Uma decada de amor e dedicacao",
    )
    history_description = models.TextField(
        default=(
            "Fundada em 2010, a ACITP nasceu para acolher idosos em "
            "vulnerabilidade com dignidade, cuidado e presenca diaria."
        )
    )
    history_highlight = models.CharField(max_length=140, default="Nossa Historia")
    director_role = models.CharField(max_length=120, default="Diretor e Fundador")
    director_name = models.CharField(max_length=120, default="Pastor Marcio Vieira")
    services_title = models.CharField(max_length=140, default="Nossos Servicos")
    services_description = models.TextField(
        default="Oferecemos um cuidado integral, atendendo as necessidades fisicas, emocionais e sociais dos nossos idosos."
    )
    donation_title = models.CharField(max_length=140, default="Apoie Nossa Causa")
    donation_description = models.TextField(
        default="Sua contribuicao ajuda na alimentacao, nos medicamentos, nos eventos e na manutencao da instituicao."
    )
    pix_key = models.CharField(max_length=180, default="acitp2010@gmail.com")
    volunteer_title = models.CharField(max_length=140, default="Seja Voluntario")
    volunteer_intro = models.TextField(
        default="Doe seu tempo e suas habilidades. Precisamos de pessoas dispostas a fazer companhia, apoiar e cuidar."
    )
    volunteer_benefits = models.TextField(
        default=(
            "Atividades recreativas e culturais\n"
            "Acompanhamento em consultas medicas\n"
            "Apoio administrativo e logistico\n"
            "Oficinas de artesanato e musica"
        )
    )
    contact_phone = models.CharField(max_length=40, default="(+55) 21 96441-4945")
    contact_email = models.EmailField(default="acitp2010@gmail.com")
    contact_address = models.TextField(
        default="Estrada do Babi, 14455, Vila Magalhaes em Belford Roxo"
    )
    footer_text = models.TextField(
        default="Transformando vidas com amor e dignidade desde 2010. Cada idoso merece ser cuidado com carinho."
    )
    hero_image = models.FileField(upload_to="site/", blank=True, null=True)
    events_banner = models.FileField(upload_to="site/", blank=True, null=True)

    class Meta:
        verbose_name = "Configuracao do site"
        verbose_name_plural = "Configuracao do site"

    def __str__(self):
        return f"Configuracao - {self.organization_name}"

    @property
    def volunteer_benefits_list(self):
        return [item.strip() for item in self.volunteer_benefits.splitlines() if item.strip()]


class Statistic(OrderedContent):
    label = models.CharField(max_length=120)
    value = models.CharField(max_length=60)
    icon = models.CharField(max_length=50, default="fa-solid fa-plus")

    class Meta(OrderedContent.Meta):
        verbose_name = "Estatistica"
        verbose_name_plural = "Estatisticas"

    def __str__(self):
        return f"{self.value} - {self.label}"


class Service(OrderedContent):
    title = models.CharField(max_length=120)
    description = models.TextField()
    icon = models.CharField(max_length=50, default="fa-solid fa-plus")

    class Meta(OrderedContent.Meta):
        verbose_name = "Servico"
        verbose_name_plural = "Servicos"

    def __str__(self):
        return self.title


class Event(OrderedContent):
    title = models.CharField(max_length=140)
    description = models.TextField()
    location = models.CharField(max_length=140)
    starts_at = models.DateTimeField(default=timezone.now)
    ends_at = models.DateTimeField(blank=True, null=True)
    image = models.FileField(upload_to="events/", blank=True, null=True)
    is_featured = models.BooleanField(default=True, verbose_name="Destacar na home")

    class Meta(OrderedContent.Meta):
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ("starts_at", "order", "id")

    def __str__(self):
        return self.title


class Testimonial(OrderedContent):
    author_name = models.CharField(max_length=120)
    author_role = models.CharField(max_length=120, blank=True)
    content = models.TextField()
    is_featured = models.BooleanField(default=True, verbose_name="Destacar na home")

    class Meta(OrderedContent.Meta):
        verbose_name = "Depoimento"
        verbose_name_plural = "Depoimentos"

    def __str__(self):
        return self.author_name


class DonationTier(OrderedContent):
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    title = models.CharField(max_length=80, blank=True)
    description = models.TextField()

    class Meta(OrderedContent.Meta):
        verbose_name = "Faixa de doacao"
        verbose_name_plural = "Faixas de doacao"

    def __str__(self):
        return self.display_value

    @property
    def display_value(self):
        if self.title:
            return self.title
        return f"R$ {self.amount:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


class VolunteerApplication(models.Model):
    STATUS_CHOICES = [
        ("novo", "Novo"),
        ("em_analise", "Em analise"),
        ("contatado", "Contatado"),
        ("aprovado", "Aprovado"),
        ("arquivado", "Arquivado"),
    ]

    PROFESSION_CHOICES = [
        ("Enfermeiro / Técnico de Enfermagem", "Enfermeiro / Técnico de Enfermagem"),
        ("Fisioterapeuta", "Fisioterapeuta"),
        ("Psicólogo", "Psicólogo"),
        ("Nutricionista", "Nutricionista"),
        ("Assistente Social", "Assistente Social"),
        ("Artesão / Professor de Artes", "Artesão / Professor de Artes"),
        ("Comunicador / Social Media", "Comunicador / Social Media"),
        ("Voluntário Geral", "Voluntário Geral"),
    ]

    full_name = models.CharField(max_length=140)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    profession = models.CharField(
        max_length=120, choices=PROFESSION_CHOICES, default="Voluntário Geral"
    )
    motivation = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="novo")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Inscricao de voluntario"
        verbose_name_plural = "Inscricoes de voluntarios"
        ordering = ("-created_at",)

    def __str__(self):
        return self.full_name


class ContactMessage(models.Model):
    STATUS_CHOICES = [
        ("novo", "Novo"),
        ("respondido", "Respondido"),
        ("arquivado", "Arquivado"),
    ]

    full_name = models.CharField(max_length=140)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    subject = models.CharField(max_length=160)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="novo")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Mensagem de contato"
        verbose_name_plural = "Mensagens de contato"
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.full_name} - {self.subject}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=140)
    phone = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name = "Perfil de usuario"
        verbose_name_plural = "Perfis de usuarios"

    def __str__(self):
        return self.full_name
