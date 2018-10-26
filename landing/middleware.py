from social_django.middleware import SocialAuthExceptionMiddleware

class CustomSocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def get_message(self, request, exception):
       default_msg = super(CustomSocialAuthExceptionMiddleware).get_message(request, exception)
       return "Bhag BC"