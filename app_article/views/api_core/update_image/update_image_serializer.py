from rest_framework import serializers
from app.utils.common.files.file import FileBase
from app.utils.common.serializers.serializer import MySerializerBase

from app.utils.common.exceptions import exception
from app_article import models


class UpdateImageSerializer(MySerializerBase):
    """更新图片-序列化"""

    image = serializers.SerializerMethodField(
        label="图片路径",
        required=False,
        allow_null=True,
    )
    class Meta:
        model = models.Article
        fields = ["image",]

    def get_image(self,obj):

        return 'data:image/jpeg;base64,%s' % obj.image

    def create(self, validated_data):
        data = self.context["request"].data
        blogid = eval(data.get("blogid",["-1"])[0]) # 获取文章id
        if blogid <= 0: # id 异常, 报错
            raise exception.myException400({
                "success": False,
                "msg": "保存失败,文章不存在",
                "results": "",
            })
        else: # id 正常
            article_list = models.Article.objects.filter(id=blogid) # 获取id对应的文章列表
            if not article_list.exists(): # 在数据库中能找不到这个id对应的文章
                raise exception.myException400({
                    "success": False,
                    "msg": "保存失败,文章不存在",
                    "results": "",
                })
            else: # 数据库中存在着篇文章
                file = data.get("file", None) # 获取前端传过来的图片数据流
                if not file: # 图片为空
                    raise exception.myException400({
                        "success": False,
                        "msg": "保存失败,后端没拿到图片",
                        "results": "",
                    })
                else: # 图片不为空
                    base64_data = FileBase.image_to_base64(file)
                    article_obj = article_list.first() # 获取文章对象
                    article_obj.image = base64_data # 更新图片
                    article_obj.save() # 保存实例

        return article_obj # 返回实例




