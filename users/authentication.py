from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
import json
import redis
from django_redis import get_redis_connection


class RedisJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        validated_data = super().authenticate(request)
        if validated_data is None:
            return None
        
        user, token = validated_data
        redis_client = get_redis_connection("default")
        # Check Redis for the stored token
        redis_key = f"user:{user.id}:tokens"
        token_json = redis_client.get(redis_key)

        if not token_json:
            raise AuthenticationFailed("Token not found in Redis. It may have been revoked.")

        token_data = json.loads(token_json)
        if str(token) != token_data.get("access"):
            raise AuthenticationFailed("Token mismatch or revoked.")

        return user, token
         