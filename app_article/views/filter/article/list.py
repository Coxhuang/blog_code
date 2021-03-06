import django_filters
from app_article import models




"""
查看博文列表
"""
class GetArticleListFilter(django_filters.rest_framework.FilterSet):

    # gamename = django_filters.CharFilter(
    #     field_name='state',
    #     label="文章状态"
    # )
    # gamestatus = django_filters.CharFilter(field_name='gameid__GameStatus',
    #                                        label="比赛状态")
    # username = django_filters.CharFilter(field_name='userid__displayname',
    #                                        label="玩家用户名")
    # odernumber = django_filters.CharFilter(field_name='OderNumber',
    #                                        label="比赛状态")
    createdate = django_filters.DateFromToRangeFilter(
        field_name='createdate',
        lookup_expr='gte',
        label='创建时间'
    )
    updatedate = django_filters.DateFromToRangeFilter(
        field_name='updatedate',
        lookup_expr='gte',
        label='更新时间'
    )

    class Meta:
        model = models.Article
        fields = [
            "state", # 文章状态
            "createdate", # 创建时间
            "updatedate", # 更新时间
        ]