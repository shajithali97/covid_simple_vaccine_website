from . models import District
def district_links(request):
    links=District.objects.all()
    return dict(links=links)
    