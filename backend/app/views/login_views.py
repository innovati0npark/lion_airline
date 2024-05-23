from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework_jwt.settings import api_settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

@csrf_exempt
@api_view(["POST"])
def login(request):
    if request.method == 'POST':
        email = request.data['email']
        password = request.data['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            try:
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                return Response({'message': '로그인 성공', 'token': token, 'user': user.first_name}, status=200)
            except Exception as e:
                raise e
        else:
            return Response({'message': '비밀번호가 일치하지 않습니다.'}, status=401)
    else:
        return Response({'message': '사용자를 찾을 수 없습니다.'}, status=401)