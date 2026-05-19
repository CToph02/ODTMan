from django.contrib.auth import authenticate, get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, permissions, status
from .serializers import UserSerializer

User = get_user_model()

class user_register(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        refresh_token = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh_token),
            'access': str(refresh_token.access_token),
            'Message': 'Login successful.'
        }, status=status.HTTP_200_OK)
    return Response({'Error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def user_logout(request):
    try:
        refresh_token = request.data.get('refresh')
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({'Message': 'Logout successful.'}, status=status.HTTP_205_RESET_CONTENT)
    except Exception:
        return Response({'Error': 'The token is invalid or expired.'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def user_pwd_change(request):
    user = request.user
    old_pwd = request.data.get('old_pwd')
    new_pwd = request.data.get('new_pwd')
    new_pwd_confirm = request.data.get('new_pwd_confirm')

    if not user.check_password(old_pwd):
        return Response({'Error': 'The actual password is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)
    
    if new_pwd != new_pwd_confirm:
        return Response({'Error': "Passwords don't match."}, status=status.HTTP_400_BAD_REQUEST)
    
    user.set_password(new_pwd_confirm)
    user.save()
    return Response({'Message': 'Updated password'})