from rest_framework import serializers
from xm.models import *


class XmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category_goods
        fields = ('id', 'good_name', 'good_img', 'good_category', 'good_category_name', 'good_id'
                  , 'good_category_id', 'pic_id', 'isNew', 'isDelete')