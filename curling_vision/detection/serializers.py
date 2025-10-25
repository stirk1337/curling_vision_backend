from rest_framework import serializers


class DetectSerializer(serializers.Serializer):
    file = serializers.FileField()


class RotationSerializer(serializers.Serializer):
    file = serializers.FileField()
    session_id = serializers.CharField(required=False, allow_blank=True)
    reset = serializers.BooleanField(default=False)
    min_conf = serializers.FloatField(default=0.0)


class SummarySerializer(serializers.Serializer):
    file = serializers.FileField()
    sample_every_n = serializers.IntegerField(default=5)
    max_match_dist = serializers.FloatField(default=80.0)
    rotation_window_n = serializers.IntegerField(default=10)
    min_conf = serializers.FloatField(default=0.0)
    min_track_len = serializers.IntegerField(default=5)

class TrackSerializer(serializers.Serializer):
    file = serializers.FileField()
    sample_every_n = serializers.IntegerField(default=5)
    max_match_dist = serializers.FloatField(default=80.0)
    rotation_window_n = serializers.IntegerField(default=10)
    min_conf = serializers.FloatField(default=0.0)
