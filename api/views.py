from .serializers import CommentSerializer, SignupSerializer
from .models import Comment, User, FlaggedComment
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import check_toxicity
from .tasks import send_flag_notification
from django.contrib.auth import authenticate

class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created'}, status=201)
        return Response(serializer.errors, status=400)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
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

        if flagged:
            # Save to separate flagged table
            FlaggedComment.objects.create(
                comment=comment,
                user=user,
                content=content,
                reason=reason
            )
            # Notify user asynchronously
            send_flag_notification.delay(user.email, content)

        serializer = CommentSerializer(comment)
        message = "Comment posted"
        if flagged:
            message += " (flagged for moderation)"

        return Response({"message": message, "comment": serializer.data})