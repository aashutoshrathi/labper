from landing.models import Profile


def get_profile(backend, user, response, details, *args, **kwargs):
    url = None
    small_url = None
    profile = Profile.objects.get_or_create(user=user)[0]
    if backend.name == "google-oauth2":
        if response['picture']:
            small_url = response['picture']
            url = small_url
    profile.avatar_small = small_url
    profile.avatar = url
    profile.save()
