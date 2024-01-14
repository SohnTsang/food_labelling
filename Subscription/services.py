from django.utils import timezone
from .models import UserSubscription


def renew_subscription(user_subscription):
    # Check if auto-renew is enabled
    if user_subscription.auto_renew:
        # Extend the subscription
        user_subscription.end_date += timezone.timedelta(days=30)  # Assuming monthly subscription
        user_subscription.save()


def cancel_subscription(user_subscription):
    user_subscription.status = 'cancelled'
    user_subscription.is_active = False
    user_subscription.save()


def upgrade_subscription(user_subscription, new_subscription_type):
    user_subscription.subscription_type = new_subscription_type
    user_subscription.save()
