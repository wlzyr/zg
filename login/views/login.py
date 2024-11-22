import hashlib

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from login.models import User


class CreateUser(APIView):
    @staticmethod
    def post(request):
        data = request.data
        user = data.get("user")
        if not user:
            return Response({
                "code": status.HTTP_403_FORBIDDEN,
                "data": {},
                "msg": "用户为空。"
            })

        password = data.get("password")
        if not password:
            return Response({
                "code": status.HTTP_403_FORBIDDEN,
                "data": {},
                "msg": "密码为空。"
            })

        pass_sha = hashlib.sha256(password.encode("utf-8")).hexdigest()
        User.objects.create(user=user, password=pass_sha)

        return Response({
            "code": status.HTTP_200_OK,
            "data": {},
            "msg": "操作成功。"
        })


class Login(APIView):
    @staticmethod
    def post(request):
        data = request.data
        user = data.get("user")
        if not user:
            return Response({
                "code": status.HTTP_403_FORBIDDEN,
                "data": {},
                "msg": "用户为空。"
            })

        password = data.get("password")
        if not password:
            return Response({
                "code": status.HTTP_403_FORBIDDEN,
                "data": {},
                "msg": "密码为空。"
            })

        pass_sha = hashlib.sha256(password.encode("utf-8")).hexdigest()

        is_exist = User.objects.filter(user=user, password=pass_sha).exists()
        if is_exist:
            return Response({
                "code": status.HTTP_200_OK,
                "data": {},
                "msg": "操作成功。"
            })

        else:
            return Response({
                "code": status.HTTP_403_FORBIDDEN,
                "data": {},
                "msg": "登录失败。"
            })
