from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import *
from .serializers import XmSerializer

class GetGoodView(APIView):
    def get(self,request):
        return_data = []
        nav_list = Category_nav.objects.all()
        for nav in nav_list:
            category_dict = {}
            category_dict["nav_id"] = nav.nav_id
            category_dict["nav_name"] = nav.nav_name
            r_pic = Recommend_pic.objects.filter(category_id_id=nav.nav_id)
            if r_pic.count() != 0:
                r_pic = Recommend_pic.objects.filter(category_id_id=nav.nav_id)[0]
                category_dict["img_url"] = r_pic.img_url
                category_dict["rpic_id"] = r_pic.rpic_id
            else:
                category_dict["img_url"] = ""
                category_dict["rpic_id"] = ""
            category_list = []
            deep_categorys = deep_Category.objects.filter(nav_id_id=nav.nav_id)
            for deep_category in deep_categorys:
                c_dict = {}
                category_name = eval(deep_category.category_name)['name']
                c_dict['name'] = category_name
                c_dict['items'] = []

                goods = Category_goods.objects.filter(good_category_name=category_name)
                for good in goods:
                    c_g_dict = {
                        "good_name": good.good_name,
                        "good_img": good.good_img,
                        "good_category": good.good_category,
                        "good_id": good.good_id,
                        "good_type_id": good.good_category_id_id,
                        "isNew": good.isNew,
                        "pic_id": good.pic_id
                    }
                    c_dict['items'].append(c_g_dict)
                category_list.append(c_dict)
                category_dict["category"] = category_list
            return_data.append(category_dict)

        data = {
            "code": 0,
            "data": return_data
        }
        return JsonResponse(data)

class GoodView(APIView):
    def get(self,request):
        get = request.GET
        pid = get.get('pid')
        data = {}
        buyoptions = Detail_buyoptions.objects.filter(product_id=pid)

        b_v_list = []
        b_c_list = []
        for buyoption in buyoptions:
            data['default_id'] = buyoption.default_good_id
            if buyoption.class_name == "版本":
                options_dict = {
                    "price": buyoption.price,
                    "ver_name": buyoption.version_name,
                    "value_id": buyoption.value_id
                }
                b_v_list.append(options_dict)
                # list = bv_list
            else:
                options_dict = {
                    "price": buyoption.price,
                    "ver_name": buyoption.version_name,
                    "value_id": buyoption.value_id
                }
                b_c_list.append(options_dict)
        buy_options_list = []
        b_v_dict = {
            'list': b_v_list,
            "name": "版本"
        }
        buy_options_list.append(b_v_dict)
        b_c_dict = {
            'list': b_c_list,
            "name": "颜色"
        }
        # buy_options
        buy_options_list.append(b_c_dict)
        goods_infos = Goods_info.objects.filter(product_id=pid)
        good_info_list = []
        for goods_info in goods_infos:
            good_name = goods_info.good_name
            button_title = goods_info.button_title
            good_market_price = goods_info.good_market_price
            goods_price = goods_info.good_price
            good_id = goods_info.goods_id
            img_url = goods_info.img_url
            img_share_url = goods_info.image_share_url
            classparameters = ClassParameters.objects.filter(good_id=good_id)
            c_p_list = []
            for classparameter in classparameters:
                c_p_dict = {}
                c_p_dict['top_title'] = classparameter.top_title
                c_p_dict['bottom_title'] = classparameter.bottom_title
                c_p_dict['param_img'] = classparameter.parameter_icon
                c_p_dict['parameter_name'] = classparameter.parameter_name
                c_p_dict['parameter_value'] = classparameter.parameter_value
                c_p_list.append(c_p_dict)
            goods_info_dict = {
                "classparameters": c_p_list,
                "id": pid,
                "good_name": good_name,
                "market_price": good_market_price,
                "price": goods_price,
                "button_title": button_title,
                "img_url": img_url,
                "image_share_url": img_share_url
            }
            # data['goods_info']
            good_info_list.append(goods_info_dict)

        comments = Comment.objects.filter(product_id=pid)
        # data[goods_share_datas][comments]
        comment_list = []
        for comment in comments:
            comment_pic = eval(comment.com_image)
            comment_dict = {
                "add_time": comment.add_time,
                "add_timestamp": comment.add_timestamp,
                "content": comment.content,
                "pic": comment_pic,
                'reply_time': comment.reply_day,
                "reply": comment.reply,
                'user_name': comment.user_name,
                'user_icon': comment.user_icon
            }
            comment_list.append(comment_dict)
        galleries = Gallery.objects.filter(product_id=pid)
        # data[goods_share_datas][gallery]
        galleries_list = []
        for gallery in galleries:
            galleries_dict = {
                "img_url": gallery.img_url,
                "sort_id": gallery.sort_id
            }
            galleries_list.append(galleries_dict)
        product_infos = Product_infos.objects.filter(product_id=pid)
        product_info_list = []
        for product_info in product_infos:
            product_info_dict = {
                'product_name': product_info.product_name,
                'product_desc': product_info.product_desc,
                'product_gallery_icon': product_info.product_gallery_icon,
                "product_total_comment": product_info.product_comment_total
            }
            product_info_list.append(product_info_dict)
        data = {
            "code": 0,
            "data": {
                "buy_options": buy_options_list,
                "goods_info": good_info_list,
                "goods_share_datas": {
                    "comments": comment_list,
                    "gallery": galleries_list
                },
                "product_info": product_info_list
            }
        }

        return JsonResponse(data)
