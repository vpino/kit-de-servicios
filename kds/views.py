from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage


class IndexView(TemplateView):
    template_name = 'index.html'

    redis_publisher = RedisPublisher(facility='foobar', broadcast=True)
    message = RedisMessage('Hello World')
    #and somewhere else
    redis_publisher.publish_message(message)

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)
