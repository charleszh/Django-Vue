from rest_framework import serializers
from .models import Post, Category, TestCase, ExecuteStatus, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ExecteStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecuteStatus
        fields = "__all__"
class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Post
        fields = "__all__"

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        # 'created' will be True if no existing category matches
        tagRecords = validated_data.pop('tags')
        category, created = Category.objects.get_or_create(**category_data)
        post = Post.objects.create(category=category, **validated_data)
        for tag in tagRecords:
            post.tags.add(tag)
        return post

class TestCaseSerializer(serializers.ModelSerializer):
    execute_status = ExecteStatusSerializer()
    # print(TestCase.objects.filter(name='6').explain(verbose=True))
    class Meta:
        model = TestCase
        fields = "__all__"

    def create(self, validated_data):
        executeStatusData = validated_data.pop('execute_status')
        # 'created' will be True if no existing category matches
        tagRecords = validated_data.pop('tags')
        execute_status, created = ExecuteStatus.objects.get_or_create(**executeStatusData)
        testCase = TestCase.objects.create(execute_status=execute_status, **validated_data)
        for tag in tagRecords:
            testCase.tags.add(tag)
        return testCase

    def update(self, instance, validated_data):
        executeStatusData = validated_data.pop('execute_status')
        tagRecords = validated_data.pop('tags')
        execute_status, created = ExecuteStatus.objects.get_or_create(**executeStatusData)
        instance.execute_status = execute_status
        instance.tags.set(tagRecords)
        instance = super().update(instance, validated_data)
        instance.save()
        return instance

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"



