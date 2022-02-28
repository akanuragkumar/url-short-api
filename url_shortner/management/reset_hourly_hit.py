from url_shortner.models import Url


def reset_hourly_hit():
    url_objs = Url.objects.all()
    for url_obj in url_objs:
        url_obj.hourly_hit = 0
        url_obj.save()
