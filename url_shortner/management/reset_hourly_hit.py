from url_shortner.models import Url


def reset_hourly_hit():
    Url.objects.all().update(hourly_hit=0)
