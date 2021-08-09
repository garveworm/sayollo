import redis

from django.conf import settings

r = redis.Redis(settings.REDIS_HOST, settings.REDIS_PORT, decode_responses=True)


def store_increment_in_redis(hash, key, increment):
    """
    Function used for keeping count of impressions and SDK requests
    """
    r.hincrby(hash, key, increment)
