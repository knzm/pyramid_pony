import base64
import zlib

from pyramid.response import Response
from pyramid.decorator import reify

from .pony import PONY, UNICORN, TEMPLATE


class Pony(object):
    def __init__(self, request):
        self.request = request

    data = PONY
    link = "add horn!"

    @reify
    def animal(self):
        data = self.data
        data = base64.b64decode(data)
        return zlib.decompress(data).decode('ascii')

    @reify
    def url(self):
        return self.request.path + "?horn=1"

    @reify
    def home(self):
        return self.request.script_name or "/"


class Unicorn(Pony):
    data = UNICORN
    link = "remove horn!"

    @reify
    def url(self):
        return self.request.path


def pony_response_adapter(pony):
    html = TEMPLATE.format(
        animal=pony.animal,
        url=pony.url,
        link=pony.link,
        home=pony.home)
    return Response(html)


def view(request):
    if request.params.get("horn"):
        return Unicorn(request)
    else:
        return Pony(request)


def includeme(config):
    config.add_route("pony", "/pony")
    config.add_response_adapter(pony_response_adapter, Pony)
    config.add_view(view, route_name="pony")
