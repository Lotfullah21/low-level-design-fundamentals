from rest_framework.views import APIView
from rest_framework.response import Response
from .services import UserService

class RegisterView(APIView):
    def post(self, request):
        # Use service in view 
        service = UserService()  
        
        user = service.register_user(
            user_name=request.data.get('username'),
            email=request.data.get('email'),
            password=request.data.get('password')
        )
        
        return Response({
            'id': user.id,
            'username': user.user_name,
            'email': user.email
        }, status=201)