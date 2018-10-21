from landing.models import Profile


def get_profile(backend, user, response, details, *args, **kwargs):
    url = None
    small_url = None
    profile = Profile.objects.get_or_create(user=user)[0]
    if backend.name == "google-oauth2":
        if response['image'].get('url'):
            small_url = response['image'].get('url')
            url = small_url.replace("sz=50", "sz=160")
    profile.avatar_small = small_url
    profile.avatar = url
    profile.save()