import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.http import HttpResponseRedirect

cloudinary.config(
    cloud_name="deaqqpgjy",
    api_key="826548937239154",
    api_secret="i7o81JXgLMxGMG_xzkOpGgxRER0",
    secure=True
)

def login_required(function):
    def wrapper(request, *args, **kw):
        print(request.session.get("email"))
        if not request.session.get("email"):
            return HttpResponseRedirect('/auth/')
        else:
            return function(request, *args, **kw)
    return wrapper