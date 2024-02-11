
from . models import Profile


def menu_link(request):
    link = Profile.objects.all()
    return dict(links=link)
