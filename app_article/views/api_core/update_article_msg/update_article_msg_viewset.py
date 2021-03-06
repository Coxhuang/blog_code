from app.utils.common.mixins.mixin import MyUpdateModelMixin
from app_article import models
from app_article.views.api_core.update_article_msg.update_article_msg_serializer import UpdateArticleMsgSerializer


class UpdateArticleMsgViewSet(MyUpdateModelMixin):
    """更新文章弹框信息"""

    # authentication_classes = ()  # 验证
    # permission_classes = ()  # 权限
    msg_update = "保存成功" # 提示信息
    queryset = models.Article.objects.all()
    results_display = True  # 是否显示序列化信息, 默认显示
    serializer_class = UpdateArticleMsgSerializer # 序列化类
