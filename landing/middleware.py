from social_django.middleware import SocialAuthExceptionMiddleware


class CustomSocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def get_message(self, request, exception):
        return "Bro, please login using IIITV's email address"
