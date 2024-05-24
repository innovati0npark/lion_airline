from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def Delete_User(request, uid):
    if request.method == 'DELETE':
        user = get_object_or_404(User, pk=uid)
        user.delete()
        return JsonResponse({'message': 'User deleted successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=400)