from app_article import models
from utils.common.serializers.serializer import MySerializerBase
from rest_framework import serializers
from utils.common.exceptions import exception


class UpdateImageSerializer(MySerializerBase):
    """更新图片-序列化"""

    class Meta:
        model = models.Article
        fields = []

    def create(self, validated_data):

        blogid = validated_data.get("blogid",-1) # 获取文章id
        if blogid <= 0: # id 异常, 报错
            raise exception.myException401({
                "success": False,
                "msg": "保存失败,文章不存在",
                "results": "",
            })
        else: # id 正常
            article_list = models.Article.objects.filter(id=blogid) # 获取id对应的文章列表
            if not article_list.exists(): # 在数据库中能找不到这个id对应的文章
                raise exception.myException401({
                    "success": False,
                    "msg": "保存失败,文章不存在",
                    "results": "",
                })
            else: # 数据库中存在着篇文章
                file = validated_data.get("file", None) # 获取前端传过来的图片数据流
                if not file: # 图片为空
                    raise exception.myException401({
                        "success": False,
                        "msg": "保存失败,后端没拿到图片",
                        "results": "",
                    })
                else: # 图片不为空
                    article_obj = article_list.first() # 获取文章对象
                    article_obj.image = file # 更新图片
                    article_obj.save() # 保存实例

        return article_obj # 返回实例




