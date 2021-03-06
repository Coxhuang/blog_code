from app.utils.common.mixins.mixin import MyRetrieveModelMixin
from app_user import models
from rest_framework.response import Response
from rest_framework import status
from app_user.views_blog.api.detail_data.detail_data_serializer import DetailDataSerializerBlog


class DetailDataViewSetBlog(MyRetrieveModelMixin):
    """查看data详细信息"""

    authentication_classes = () # 验证
    permission_classes = () # 权限
    msg_detail = "查看用户个人中心" # 提示信息
    serializer_class = DetailDataSerializerBlog # 序列化类
    queryset = models.UserData.objects.all() # models
    lookup_field = "user__username"  # 主键


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        ret_data = serializer.data # 获取序列化后的数据, 直接操作serializer不可行

        value = eval(ret_data["timeline"]) # 将字符串转成字典
        value.sort(key=lambda k: (int(k.get('id'))), reverse=True) # 列表按id排序
        ret_data["timeline"] = value # 前端更新, 后端将下面一行代码也更新
        # ret_data["timeline"] = str(value).replace("'","\"") # 前端框架不能解锁单引号

        return Response({
            "success": True,
            "msg": self.msg_detail,
            "results": [ret_data] # 以列表的格式给
        }, status=status.HTTP_200_OK)



