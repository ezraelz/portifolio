from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PageView
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['POST'])
def track_view(request):
    page = request.data.get('page')

    if not request.session.get(f"viewed_{page}"):
        PageView.objects.create(
            page=page,
            ip_address=request.META.get('REMOTE_ADDR'),
            user_agent=request.META.get('HTTP_USER_AGENT')
        )
        request.session[f"viewed_{page}"] = True

    return Response({"status": "view recorded"})

@api_view(['GET'])
def total_views(request):
    count = PageView.objects.count()
    return Response({"total_views": count})

