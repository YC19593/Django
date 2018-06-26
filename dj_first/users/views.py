from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo

# Create your views here.


# heh
# def index(request):
#     """index视图函数"""
#     return HttpResponse("hello the world!")

def index(request):
    """index视图
    ：param request: 包含请求信息的请求对象
    ：return: 响应对象
    """
    # 在模板中显示
    data = {
        "message": "hello world"
    }
    return render(request, "index.html", context=data)
