from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

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
