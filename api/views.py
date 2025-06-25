from .serializers import CommentSerializer
from .models import Comment
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .utils import check_toxicity


class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({'error': 'User already exists'}, status=400)

        user = User.objects.create_user(username=username, password=password)
        return Response({'message': 'User created'}, status=201)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        from django.contrib.auth import authenticate

        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid credentials'}, status=401)


class CommentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        content = request.data.get("content", "")
        user = request.user

        flagged, categories = check_toxicity(content)
        reason = ", ".join(categories.keys()) if flagged else ""

        comment = Comment.objects.create(
            user=user,
            content=content,
            flagged=flagged,
            flag_reason=reason
        )

        serializer = CommentSerializer(comment)
        message = "Comment posted"
        if flagged:
            message += " (flagged for moderation)"

        return Response({
            "message": message,
            "comment": serializer.data
        })
