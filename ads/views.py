import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import AdSerializer
from .utils import r, store_increment_in_redis

AD_URL = 'https://6u3td6zfza.execute-api.us-east-2.amazonaws.com/prod/ad/vast'


class GetAd(APIView):
    serializer_class = AdSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        sdk_version = serializer.data.get("sdk_version")
        user_name = serializer.data.get("user_name")

        for field in [sdk_version, user_name]:
            if field:
                store_increment_in_redis(field, "ad_count", 1)

        xml = requests.get(AD_URL)
        return Response(xml)


class Impressions(APIView):
    serializer_class = AdSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        sdk_version = serializer.data.get("sdk_version")
        user_name = serializer.data.get("user_name")

        for field in [sdk_version, user_name]:
            if field:
                store_increment_in_redis(field, "impressions_count", 1)

        return Response(status=status.HTTP_200_OK)


class GetStats(APIView):

    def get(self, request):
        filter_key = request.query_params.get("filter_key")
        if not filter_key:
            return Response(data="Please provide filter type", status=status.HTTP_400_BAD_REQUEST)

        data = r.hgetall(filter_key)
        if not data:
            return Response(data=f"No data for key - {filter_key} yet", status=status.HTTP_400_BAD_REQUEST)

        ad_count = int(data.get("ad_count", 0))
        impressions_count = int(data.get("impressions_count", 0))

        stats = {
            "ad_requests": ad_count,
            "impressions": impressions_count,
            "fill_rate": impressions_count / ad_count if ad_count else 0
        }

        return Response(stats)
