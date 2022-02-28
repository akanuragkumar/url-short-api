from django.shortcuts import redirect
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from url_shortner.handlers.url_shortner import UrlModifier


class UrlShortnerView(APIView):
    """Short-ner url."""

    def post(self, request):
        """Short-ner url."""
        link = request.data.get('link')
        resp = UrlModifier.url_shortner(link)
        return Response(status=status.HTTP_202_ACCEPTED, data=resp)


class ReDirectUrl(APIView):
    """Redirect to original url."""

    def post(self, request):
        """Redirect to original url."""
        link = request.data.get('link')
        original_link = UrlModifier.get_original_url(link)
        return redirect(original_link)


class SearchKeyword(APIView):
    """Search to original url."""

    def post(self, request):
        """Search to original url."""
        keyword = request.data.get('keyword')
        resp = UrlModifier.search_similar_url(keyword)
        return Response(status=status.HTTP_202_ACCEPTED, data=resp)


class KeyMetaData(APIView):
    """GetMetaData of keys."""

    def post(self, request):
        """GetMetaData of keys."""
        keyword = request.data.get('keyword')
        resp = UrlModifier.search_similar_url(keyword)
        return Response(status=status.HTTP_202_ACCEPTED, data=resp)
