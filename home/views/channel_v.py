from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from home.models import Channel
from login.models import Token


class ChannelList(APIView):
    @staticmethod
    def post(request):
        data = request.data
        token = data.get('token')

        token_obj = Token.objects.filter(token=token).first()
        if not token_obj or token_obj.is_expired:
            return Response({
                "code": status.HTTP_400_BAD_REQUEST,
                "data": {},
                "msg": "无效token。"
            })

        res = []
        channel_list = token_obj.user.user_channel.all()
        for channel in channel_list:
            res.append({
                "id": channel.channel_id,
                "name": channel.channel_name,
            })

        return Response({
            "code": status.HTTP_200_OK,
            "data": res,
            "msg": "操作成功。"
        })


class CreateChannel(APIView):
    @staticmethod
    def post(request):
        data = request.data
        token = data.get('token')

        token_obj = Token.objects.filter(token=token).first()
        if not token_obj or token_obj.is_expired:
            return Response({
                "code": status.HTTP_400_BAD_REQUEST,
                "data": {},
                "msg": "无效token。"
            })

        return Response({
            "code": status.HTTP_200_OK,
            "data": [],
            "msg": "操作成功。"
        })


class ADDChannel(APIView):
    @staticmethod
    def post(request):
        data = request.data
        token = data.get('token')

        token_obj = Token.objects.filter(token=token).first()
        if not token_obj or token_obj.is_expired:
            return Response({
                "code": status.HTTP_400_BAD_REQUEST,
                "data": {},
                "msg": "无效token。"
            })

        channel_id = data.get("channel_id")
        if not channel_id:
            return Response({
                "code": status.HTTP_403_FORBIDDEN,
                "data": {},
                "msg": "频道id为空。"
            })

        channel_obj = Channel.objects.filter(channel_id=channel_id)
        if not channel_obj.exists():
            return Response({
                "code": status.HTTP_403_FORBIDDEN,
                "data": {},
                "msg": "无效频道id。"
            })

        token_obj.user.user_channel.add(channel_obj.first())

        return Response({
            "code": status.HTTP_200_OK,
            "data": [],
            "msg": "操作成功。"
        })


class DeleteChannel(APIView):
    @staticmethod
    def post(request):
        data = request.data
        token = data.get('token')

        token_obj = Token.objects.filter(token=token).first()
        if not token_obj or token_obj.is_expired:
            return Response({
                "code": status.HTTP_400_BAD_REQUEST,
                "data": {},
                "msg": "无效token。"
            })

        channel_id = data.get("channel_id")
        if not channel_id:
            return Response({
                "code": status.HTTP_403_FORBIDDEN,
                "data": {},
                "msg": "频道id为空。"
            })

        channel_obj = Channel.objects.filter(channel_id=channel_id)
        if not channel_obj.exists():
            return Response({
                "code": status.HTTP_403_FORBIDDEN,
                "data": {},
                "msg": "无效频道id。"
            })

        token_obj.user.user_channel.remove(channel_obj.first())

        return Response({
            "code": status.HTTP_200_OK,
            "data": [],
            "msg": "操作成功。"
        })


class UpdateChannel(APIView):
    @staticmethod
    def post(request):
        data = request.data
        token = data.get('token')

        token_obj = Token.objects.filter(token=token).first()
        if not token_obj or token_obj.is_expired:
            return Response({
                "code": status.HTTP_400_BAD_REQUEST,
                "data": {},
                "msg": "无效token。"
            })

        channel_id = data.get("channel_id")
        if not channel_id:
            return Response({
                "code": status.HTTP_403_FORBIDDEN,
                "data": {},
                "msg": "频道id为空。"
            })

        channel_obj = Channel.objects.filter(channel_id=channel_id)
        if not channel_obj.exists():
            return Response({
                "code": status.HTTP_403_FORBIDDEN,
                "data": {},
                "msg": "无效频道id。"
            })

        channel_name = data.get("channel_name")
        if not channel_name:
            return Response({
                "code": status.HTTP_403_FORBIDDEN,
                "data": {},
                "msg": "频道名称为空。"
            })

        Channel.objects.filter(channel_id=channel_id).update(channel_name=channel_name)

        return Response({
            "code": status.HTTP_200_OK,
            "data": [],
            "msg": "操作成功。"
        })
