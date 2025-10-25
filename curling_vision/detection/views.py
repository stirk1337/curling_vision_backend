import requests
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings

from detection.serializers import TrackSerializer, DetectSerializer, RotationSerializer, SummarySerializer

INFERENCER_URL = settings.INFERENCER_URL  # теперь берём из настроек


class DetectAPIView(APIView):
    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(request_body=DetectSerializer)
    def post(self, request):
        serializer = DetectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file_obj = serializer.validated_data["file"]
        files = {"file": (file_obj.name, file_obj.read(), file_obj.content_type)}

        resp = requests.post(f"{INFERENCER_URL}/detect", files=files)
        return Response(resp.json(), status=resp.status_code)



class RotationAPIView(APIView):
    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(request_body=RotationSerializer)
    def post(self, request):
        serializer = RotationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file_obj = serializer.validated_data["file"]

        data = {
            "session_id": serializer.validated_data.get("session_id"),
            "reset": serializer.validated_data.get("reset", False),
            "min_conf": serializer.validated_data.get("min_conf", 0.0),
        }
        files = {"file": (file_obj.name, file_obj.read(), file_obj.content_type)}

        resp = requests.post(f"{INFERENCER_URL}/rotation", files=files, data=data)
        return Response(resp.json(), status=resp.status_code)


class TrackAPIView(APIView):
    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(request_body=TrackSerializer)
    def post(self, request):
        serializer = TrackSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file_obj = serializer.validated_data["file"]
        params = serializer.validated_data
        files = {"file": (file_obj.name, file_obj.read(), file_obj.content_type)}
        del params["file"]
        resp = requests.post(f"{INFERENCER_URL}/track", files=files, data=params)
        return Response(resp.json(), status=resp.status_code)


class SummaryAPIView(APIView):
    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(request_body=SummarySerializer)
    def post(self, request):
        serializer = SummarySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file_obj = serializer.validated_data["file"]

        params = serializer.validated_data.copy()
        del params["file"]
        files = {"file": (file_obj.name, file_obj.read(), file_obj.content_type)}

        resp = requests.post(f"{INFERENCER_URL}/summary", files=files, data=params)
        return Response(resp.json(), status=resp.status_code)
