from app.utils.common.mixins.mixin import MyCreateModeMixin
from app_user import models
from app_user.views.api.data.update_timeline.updata_timeline_serializer import UpdateTimeLineSerializer


class UpdateTimeLineViewSet(MyCreateModeMixin):
    """更新时光轴"""

    # authentication_classes = () # 验证
    # permission_classes = () # 权限
    msg_detail = "更新时光轴" # 提示信息
    serializer_class = UpdateTimeLineSerializer # 序列化类
    queryset = models.UserData.objects.all() # models


