from django.contrib import admin

from .models import (
    ContactMessage,
    DonationTier,
    Event,
    Service,
    SiteConfiguration,
    Statistic,
    Testimonial,
    UserProfile,
    VolunteerApplication,
)


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Identidade", {"fields": ("organization_name", "footer_text")}),
        (
            "Hero",
            {"fields": ("hero_badge", "hero_title", "hero_description", "hero_image")},
        ),
        (
            "Historia e direcao",
            {
                "fields": (
                    "history_title",
                    "history_description",
                    "history_highlight",
                    "director_role",
                    "director_name",
                )
            },
        ),
        (
            "Servicos e doacoes",
            {
                "fields": (
                    "services_title",
                    "services_description",
                    "donation_title",
                    "donation_description",
                    "pix_key",
                    "events_banner",
                )
            },
        ),
        (
            "Voluntariado e contato",
            {
                "fields": (
                    "volunteer_title",
                    "volunteer_intro",
                    "volunteer_benefits",
                    "contact_phone",
                    "contact_email",
                    "contact_address",
                )
            },
        ),
    )


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ("value", "label", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("label", "value")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("title", "description")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "starts_at", "is_featured", "is_active")
    list_filter = ("is_featured", "is_active", "starts_at")
    search_fields = ("title", "location", "description")
    ordering = ("starts_at",)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("author_name", "author_role", "is_featured", "is_active")
    list_filter = ("is_featured", "is_active")
    search_fields = ("author_name", "author_role", "content")


@admin.register(DonationTier)
class DonationTierAdmin(admin.ModelAdmin):
    list_display = ("display_value", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("title", "description")


@admin.register(VolunteerApplication)
class VolunteerApplicationAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "profession", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("full_name", "email", "phone", "profession")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "subject", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("full_name", "email", "subject", "message")


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "user", "phone")
    search_fields = ("full_name", "user__username", "phone")
