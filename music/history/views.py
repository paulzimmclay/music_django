from django.http import HttpResponse


def artist_list(request):
    return HttpResponse("Page for listing artists.")

def artist_details(request):
    return HttpResponse("Page for artist details.")