from django.shortcuts import render,redirect
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from .models import *
from .forms import *
from utils.PageHelper import PageHelper
import json
import re
import os
# Create your views here.
#自动登录
def autologin(request):
    if request.COOKIES.get('uname'):
        uname = request.get_signed_cookie('uname',salt="abc159")
        request.session['uid'] = User.objects.filter(user_name=uname)
        return render(request,'login.html')
    else:
        return redirect('/login/')
#登录
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        user1 = User.objects.filter(user_name = uname,user_password=pwd).first()
        if not user1:
            return render(request, 'login.html', {"msg": "用户名或密码错误！"})
        else:
            resp = redirect('/index/')
            #uname存入cookie
            resp.set_signed_cookie('uname', json.dumps(uname), salt="abc159")
            #id存入session
            request.session['uid'] = user1.user_id
            print(request.session.get('uid'))
            return resp
#跳转首页
def index(request):
    if request.method == 'GET':
        uname = request.get_signed_cookie("uname",salt='abc159')
        uname = json.loads(uname)
        user = User.objects.filter(user_name=uname).first()
        uinf = UserDetail.objects.filter(uinf_id=user.user_id).first()
        return render(request,'login.html',{'user':user,'uinf':uinf})
def regist(request):
    if request.method == 'GET':
        return render(request,'reg.html')
    else:
        uname = request.POST.get("uname")
        email = request.POST.get("email")
        url = request.POST.get("url")
        mobile = request.POST.get("mobile")
        pwd = request.POST.get("pwd")
        repwd = request.POST.get("repwd")
        user1 = User.objects.filter(user_name=uname)
        if user1:
            return render(request,'reg.html',{"uname":uname,"email":email,"url":url,"msg":'用户名已存在，请重新输入'})
        else:
            pattern = '^\d{11}$'
            if re.match(pattern,mobile) == None:
                return render(request, 'reg.html', {"uname": uname, "email": email, "url": url, "msg": '手机格式错误，请重新输入'})
            else:
                pattern = '^[a-zA-Z0-9]{6,16}$'
                if re.match(pattern,pwd) == None:
                    return render(request, 'reg.html', {"uname": uname, "email": email, "url": url, "msg": '密码格式错误，请重新输入'})
                else:
                    if pwd != repwd:
                        return render(request, 'reg.html',{"uname": uname, "email": email, "url": url,"msg": '两次密码不一致，请重新试'})
                    else:
                        userDetail = UserDetail.objects.create(uinf_email=email,uinf_url=url,uinf_mobile=mobile)
                        userDetail.save()
                        user1 = User.objects.create(user_name=uname,user_password=pwd,userDetail=userDetail)
                        return render(request,'login.html',{"msg":"注册成功，请登录"})

def inf(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        user = User.objects.filter(user_id=uid).first()
        uinf = UserDetail.objects.filter(uinf_id=user.userDetail_id).first()
        avatar=os.path.join('blog',uinf.uinf_avatar.name)
        print(avatar)
        return render(request,'inf.html',{'user':user,'uinf':uinf,'avatar':avatar})
def updateinf(request):
    if request.method == 'GET':
        userid = request.GET.get('userid')
        user = User.objects.filter(user_id=userid).first()
        uinf = UserDetail.objects.filter(uinf_id=user.userDetail_id).first()
        avatar = uinf.uinf_avatar.name
        avatar = os.path.join('blog', uinf.uinf_avatar.name)
        print(avatar)
        return render(request,'updateinf.html',{'user':user,'uinf':uinf,'avatar':avatar})
    else:
        id = request.POST.get("id")
        uname = request.POST.get("uname")
        # if request.FILES.get("avatar",'') != '':
        #     f
        email = request.POST.get("email")
        url = request.POST.get("url")
        mobile = request.POST.get("mobile")
        sign = request.POST.get("sign")
        user = User.objects.filter(user_id=id).first()
        uinf = UserDetail.objects.filter(uinf_id=user.userDetail_id).first()
        ul = User.objects.filter(user_name=user.user_name)
        if len(ul)>1:
            return render(request, 'reg.html',
                          {"uname": uname, "email": email, "url": url, "msg": '用户名已存在，请重新输入'})
        else:
            pattern = '^\d{11}$'
            if re.match(pattern, mobile) == None:
                return render(request, 'reg.html',
                              {"uname": uname, "email": email, "url": url, "msg": '手机格式错误，请重新输入'})
            else:
                user.user_name = uname
                uinf.uinf_email = email
                uinf.uinf_mobile = mobile
                uinf.uinf_url = url
                uinf.uinf_sign = sign
                if request.FILES.get("avatar", '') != '':
                    avatar = request.FILES.get("avatar")
                    uinf.uinf_avatar = avatar
                    user.save()
                    uinf.save()
                    avatar = os.path.join("blog",uinf.uinf_avatar.name)
                    print(avatar)
                    return render(request, 'inf.html', {"msg": "修改成功",'user':user,'uinf':uinf,'avatar':avatar})
                else:
                    user.save()
                    uinf.save()
                    avatar = os.path.join("blog",uinf.uinf_avatar.name)
                    return render(request, 'inf.html', {"msg": "修改成功", 'user': user, 'uinf': uinf,'avatar':avatar})
#django自带分页
def getpage(request,articles):
    paginator = Paginator(articles,4)
    try:
        page = int(request.GET.get('page', 1))
        articles = paginator.page(page)
    except(EmptyPage, InvalidPage, PageNotAnInteger):
        articles = paginator.page(1)
    return articles
def article(request):
    uid = request.GET.get('uid')
    uid = request.session.get('uid')
    pageno = request.GET.get('pageno',1)
    print('pageno',pageno)
    articles = Article.objects.all()
    # articles = getpage(request,articles)
    pageHelper = PageHelper('/article/',articles,pageno,9,8)
    articles = pageHelper.getQueryList
    pages = pageHelper.getPage
    print('uiduid',uid)
    return render(request,"article.html",{"articles":articles,"pages":pages,"uid":uid})
def addarticle(request):
    if request.method =='GET':
        uid = request.GET.get('uid')
        uid = request.session.get('uid')
        user = User.objects.filter(user_id=uid).first()
        form = ArticltForm()
    else:
        uid = request.POST.get('uid')
        new_article = ArticltForm(request.POST)
        print('*'*50,uid)
        if new_article.is_valid():
            new_article.instance.user_id =uid
            new_article.instance.art_time = timezone.now()
            new_article.save()
            return redirect("/addarticle/?uid=%s" % (uid))
        else:
            print('再来一次')
            return render(request,'addarticle.html',{"uid": uid,"form":new_article})
    return render(request, "addarticle.html", {"uid":uid,"user": user,"form":form})
def articledetail(request):
    form = ArticltForm
    uid = request.GET.get('uid')
    artid = request.GET.get('artid')
    article = Article.objects.filter(art_id=artid).first()
    return render(request,'articledetail.html',{'uid':uid,'article':article})
def updatearticle(request):
    if request.method =='GET':
        uid = request.GET.get('uid')
        articleid = request.GET.get('artid')
        article = Article.objects.filter(art_id = articleid).first()
        if int(uid) == article.art_id:
            form = ArticltForm(instance=article)
            return render(request,'updatearticle.html',{'form':form,"article":article,'uid':uid})
        else:
            uid = request.GET.get('uid')
            articles = Article.objects.all()
            return render(request, "article.html", {"articles": articles, "uid": uid,"msg":"对不起，不是您的文章，您无此权限"})
    else:
        uid = request.POST.get('uid')
        articleid = request.POST.get('artid')
        article = Article.objects.filter(art_id=articleid).first()
        form = ArticltForm(request.POST, instance=article)
        if form.is_valid():
            form.instance.art_time = timezone.now()
            form.save()
            return redirect("/article/?uid=%s" % uid)
        else:
            return render(request,'updatearticle.html',{'form':article,'uid':uid})
def delarticle(request):
    uid = request.session.get('uid')
    if request.method=='GET':
        articleid = request.GET.get('artid')
        article = Article.objects.filter(art_id = articleid).first()
        print(uid)
        print(articleid)
        if int(uid) == article.user_id:
            Article.objects.filter(art_id=articleid).delete()
            return redirect('/article/')
        else:
            articles = Article.objects.all()
            return render(request, "article.html", {"articles": articles,"msg":"对不起，不是您的文章，您无此权限"})
