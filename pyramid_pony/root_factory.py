import base64
import zlib

from pyramid.response import Response
from pyramid.decorator import reify

from .pony import PONY, UNICORN, TEMPLATE


class RootContext(object):
    def __init__(self, request):
        self.request = request
        if request.params.get("horn"):
            self.data = UNICORN
            self.link = "remove horn!"
            self.url = request.path
        else:
            self.data = PONY
            self.link = "add horn!"
            self.url = request.path + "?horn=1"

    @reify
    def home(self):
        self.request.script_name or "/"

    def decode(self, data):
        data = base64.b64decode(data)
        return zlib.decompress(data).decode('ascii')


def view(request):
    context = request.context
    data = context.data
    html = TEMPLATE.format(
        animal=context.decode(data),
        url=context.url,
        link=context.link,
        home=context.home)
    return Response(html)


def includeme(config):
    config.add_route("pony", "/pony", factory=RootContext)
    config.add_view(view, route_name='pony')
