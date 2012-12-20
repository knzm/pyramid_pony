import base64
import zlib

from pyramid.events import subscriber
from pyramid.events import BeforeRender

from .pony import PONY, UNICORN


def add_global(event):
    req = event['request']
    event["home"] = req.script_name or "/"
    url = req.path
    if req.params.get("horn"):
        data = UNICORN
        event["link"] = "remove horn!"
        event["url"] = req.path
    else:
        data = PONY
        event["link"] = "add horn!"
        event["url"] = req.path + "?horn=1"
    data = base64.b64decode(data)
    animal = zlib.decompress(data).decode('ascii')
    event["animal"] = animal


def view(request):
    return {}


def includeme(config):
    config.add_route("pony", "/pony")
    config.add_subscriber(add_global, BeforeRender)
    config.add_view(view, route_name="pony", renderer='pyramid_pony:pony.mako')
