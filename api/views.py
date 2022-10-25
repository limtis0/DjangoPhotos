from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/list/',
        'Create': '/create/',
        'Update': '/update/',
        'Delete': '/delete/<str:pk>/'
    }
    return Response(api_urls)
