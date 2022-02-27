from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from shortner.models import Url
import uuid


class UrlShortnerView(APIView):
    """Short-ner url."""

    def post(self, request):
        """Short-ner url."""
        link = request.data.get('link')
        if ("http://" not in link) and ("https://" not in link):
            link = "http://" + link
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return Response(status=status.HTTP_202_ACCEPTED, data={"shortened_url": uid})


# def final(request, pk):
#     url_details = Url.objects.get(uuid=pk)
#     return redirect(url_details.link)
