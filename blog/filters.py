import django_filters
from .models import Post, TestCase


class PostFilter(django_filters.rest_framework.FilterSet):
    '''
    商品过滤的类
    '''
    #两个参数，name是要过滤的字段，lookup是执行的行为，‘小与等于本店价格’
    #price_min = django_filters.NumberFilter(name="id", lookup_expr='gte')
    #price_max = django_filters.NumberFilter(name="id", lookup_expr='lte')
    dtime = django_filters.DateFromToRangeFilter(field_name="created_time")

    class Meta:
        model = Post
        fields = ['dtime']

class TestCaseFilter(django_filters.rest_framework.FilterSet):
    dtime = django_filters.DateTimeFromToRangeFilter(field_name="created_time")
    testcase_name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")
    testcase_tag = django_filters.Filter(field_name="tags")
    class Meta:
        model = TestCase
        fields = ['dtime', 'testcase_name', 'testcase_tag']