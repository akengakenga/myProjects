from django.middleware.common import CommonMiddleware
from django.utils.deprecation import MiddlewareMixin


class CROSMiddleware(MiddlewareMixin):
    #自定义中间件
    def process_response(self,request,response):
        # 允许你的域名来获取我的数据
        response['Access-Control-Allow-Origin'] = "*"
        # 允许你携带Content-Type请求头,这里不能写*
        response['Access-Control-Allow-Headers'] = 'Content-Type'
        # 允许你发送GET/POST/DELETE/PUT
        response['Access-Control-Allow-Methods'] = "GET, POST"
        return response
