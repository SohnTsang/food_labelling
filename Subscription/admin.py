from django.contrib import admin
from .models import SubscriptionType, UserSubscription
from .services import renew_subscription, cancel_subscription  # Import your functions

class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'subscription_type', 'is_active', 'auto_renew', 'status')
    actions = ['admin_renew_subscription', 'admin_cancel_subscription']

    def admin_renew_subscription(self, request, queryset):
        for subscription in queryset:
            renew_subscription(subscription)
    admin_renew_subscription.short_description = "Renew selected subscriptions"

    def admin_cancel_subscription(self, request, queryset):
        for subscription in queryset:
            cancel_subscription(subscription)
    admin_cancel_subscription.short_description = "Cancel selected subscriptions"

admin.site.register(SubscriptionType)
admin.site.register(UserSubscription, UserSubscriptionAdmin)