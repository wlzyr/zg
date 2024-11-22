import hashlib
import time

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from login.models import User, Token


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

        is_exist = User.objects.filter(user=user).exists()
        if is_exist:
            return Response({
                "code": status.HTTP_403_FORBIDDEN,
                "data": {},
                "msg": "账号已注册。"
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

        user_obj = User.objects.filter(user=user, password=pass_sha)
        if user_obj.exists():

            # 生成的token
            token = hashlib.sha256(str(time.time()).encode("utf-8")).hexdigest()
            Token.objects.update_or_create(user=user_obj.first(), defaults={
                "token": token
            })

            return Response({
                "code": status.HTTP_200_OK,
                "data": {
                    "token": token,
                },
                "msg": "操作成功。"
            })

        else:
            return Response({
                "code": status.HTTP_403_FORBIDDEN,
                "data": {},
                "msg": "登录失败。"
            })
