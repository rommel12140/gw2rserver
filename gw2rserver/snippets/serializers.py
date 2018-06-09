from rest_framework import serializers
from django.contrib.auth.models import User
from snippets.models import Snippet, CheckVoucher


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'created', 'owner',
                  'code', 'project', 'materials', 'CR', 'DR')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.code = validated_data.get('code', instance.code)
        instance.project = validated_data.get('project', instance.project)
        instance.materials = validated_data.get('materials', instance.materials)
        instance.CR = validated_data.get('CR', instance.CR)
        instance.DR = validated_data.get('DR', instance.DR)
        instance.save()
        return instance

class CheckVoucherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CheckVoucher
        fields = ('particulars','amount','owner', 'supplier', 'date', 'cvno')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return CheckVoucher.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.particulars = validated_data.get('particulars', instance.particulars)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.supplier = validated_data.get('supplier', instance.supplier)
        instance.cvno = validated_data.get('cvno', instance.cvno)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.save()
        return instance

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')