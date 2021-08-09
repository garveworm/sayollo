from rest_framework import serializers


class AdSerializer(serializers.Serializer):
    sdk_version = serializers.IntegerField()
    session_id = serializers.CharField(required=False)
    platform = serializers.CharField(required=False)
    user_name = serializers.CharField()
    country_code = serializers.CharField(required=False)

    class Meta:
        fields = ("sdk_version", "session_id", "platform", "user_name", "country_code")
