from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage

def redisPublishMessage(msj):

    redis_publisher = RedisPublisher(facility='foobar', broadcast=True)

    message = RedisMessage(msj)

    redis_publisher.publish_message(message)