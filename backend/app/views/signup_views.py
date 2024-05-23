from django.contrib.auth.models import User
# from app.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response



@csrf_exempt
@api_view(["GET", "POST"])
def signup(request):
    if request.method == 'POST':
        firstName = request.data['firstName']
        lastName = request.data['lastName']
        email = request.data['email']
        password = request.data['password']
        try:
            user = User.objects.create_user(username=email, email=email, password=password, first_name=firstName, last_name=lastName)
            user.save()
            return Response({'message': '회원가입 성공'}, status=201)
        except Exception as e:
            return Response({'message': str(e)}, status=400)
    elif request.method == 'GET':
        users = User.objects.all()
        return Response({'users': list(users.values())}, status=200)