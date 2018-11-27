from django.db import models


# category页面
class Category_nav(models.Model):
    nav_id = models.IntegerField(unique=True)
    nav_name = models.CharField(max_length=20)

    class Meta:
        db_table = 'xm_category_nav'

class Recommend_pic(models.Model):
    img_url = models.CharField(max_length=1000)
    category_id = models.ForeignKey(Category_nav,to_field='nav_id')
    category_name = models.CharField(max_length=50)
    rpic_id = models.IntegerField()

    class Meta:
        db_table = 'xm_category_recommend_pic'

class deep_Category(models.Model):
    nav_id = models.ForeignKey(Category_nav,to_field='nav_id')
    category_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'xm_category_deep_category'


class Category_goods(models.Model):
    good_name = models.CharField(max_length=100)
    good_img = models.CharField(max_length=2000)
    good_category = models.CharField(max_length=100)
    good_category_name = models.CharField(max_length=100)
    good_id = models.CharField(max_length=200)
    good_category_id = models.ForeignKey(Category_nav,to_field='nav_id')
    pic_id = models.IntegerField()
    isNew = models.BooleanField(default=False)
    isDelete = models.BooleanField(default=False)



    class Meta:
        db_table = 'xm_category_goods'



#商品详情页
class Detail_buyoptions(models.Model):
    product_id = models.BigIntegerField()
    class_name = models.CharField(max_length=100,default="0")
    version_name = models.CharField(max_length=100)
    buy_img = models.CharField(max_length=1000,null=True,blank=True)
    price = models.CharField(max_length=100,null=True,blank=True)
    value_id = models.IntegerField()
    default_good_id = models.CharField(max_length=50)

    class Meta:
        db_table = 'xm_goods_buyoption'

class Goods_info(models.Model):
    product_id = models.BigIntegerField()
    goods_id = models.BigIntegerField()
    good_name = models.CharField(max_length=100)
    good_price = models.CharField(max_length=20)
    good_market_price = models.CharField(max_length=20)
    image_share_url = models.CharField(max_length=1000)
    img_url = models.CharField(max_length=1000)
    button_title = models.CharField(max_length=50)

    class Meta:
        db_table = 'xm_goods_info'

class ClassParameters(models.Model):
    product_id = models.IntegerField()
    good_id = models.BigIntegerField()
    class_parameters_name = models.CharField(max_length=50)
    top_title = models.CharField(max_length=50)
    bottom_title = models.CharField(max_length=50)
    parameter_icon = models.CharField(max_length=500)
    parameter_name = models.CharField(max_length=50)
    parameter_value = models.CharField(max_length=50)

    class Meta:
        db_table = 'xm_ClassParameters'

class Comment(models.Model):
    product_id =models.BigIntegerField()
    add_time = models.CharField(max_length=100)
    add_timestamp = models.IntegerField()
    content = models.CharField(max_length=5000)
    com_image = models.CharField(max_length=5000)
    reply = models.CharField(max_length=5000)
    reply_day = models.CharField(max_length=100)
    user_icon = models.CharField(max_length=1000)
    user_name = models.CharField(max_length=500)


    class Meta:
        db_table = 'xm_comment'

class Gallery(models.Model):
    img_url = models.CharField(max_length=1000)
    product_id = models.BigIntegerField()
    sort_id = models.IntegerField()


    class Meta:
        db_table = 'xm_gallery'



class Product_infos(models.Model):
    product_id = models.BigIntegerField()
    product_name = models.CharField(max_length=50)
    product_desc = models.CharField(max_length=5000)
    product_gallery_icon = models.CharField(max_length=500,null=True,blank=True)
    product_comment_total = models.IntegerField()

    class Meta:
        db_table = 'xm_product_infos'
