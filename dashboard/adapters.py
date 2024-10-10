from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.models import EmailAddress

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = sociallogin.user
        # Check if the login is from a social provider (like Google)
        if sociallogin.account.provider:
            # Fetch the email and mark it as verified automatically
            email_address = user.email
            # Ensure the email address exists in the database and is marked verified
            email_address_obj, created = EmailAddress.objects.get_or_create(user=user, email=email_address)
            if not email_address_obj.verified:
                email_address_obj.verified = True
                email_address_obj.save()
        return super().save_user(request, sociallogin, form)
