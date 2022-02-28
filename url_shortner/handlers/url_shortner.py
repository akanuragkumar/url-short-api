import uuid

from url_shortner.models import Url


class UrlModifier:

    @staticmethod
    def url_shortner(link):
        if ("http://" not in link) and ("https://" not in link):
            link = "http://" + link
        uid = str(uuid.uuid4())[:5]
        try:
            url_details = Url.objects.get(link=link)
            key = url_details.uuid
            new_url = 'https://url-shortner-anurag.herokuapp.com/' + key
            return {"shortened_url": new_url}
        except Url.DoesNotExist:
            Url.objects.create(link=link, uuid=uid)
            new_url = 'https://url-shortner-anurag.herokuapp.com/' + uid
            return {"shortened_url": new_url}

    @staticmethod
    def get_original_url(link):
        uuid = link[-5:]
        try:
            url_details = Url.objects.get(uuid=uuid)
            total_hit = url_details.total_hit
            total_hourly_hit = url_details.hourly_hit
            url_details.total_hit = total_hit + 1
            url_details.hourly_hit = total_hourly_hit + 1
            url_details.save()
            return url_details.link
        except Url.DoesNotExist:
            return {'error': 'This url does not exist.'}

    @staticmethod
    def search_similar_url(key):
        try:
            results = Url.objects.filter(link__icontains=key).values_list('link', flat=True)
            return {'link_list': results}
        except Url.DoesNotExist:
            return {'error': 'This keyword does not exist.'}
