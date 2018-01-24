from django.shortcuts import render
from django.http import HttpResponse
from blog import models
# Create your views here.
#博客主页面
def index(request):
    # return HttpResponse("hello world")
    # return render(request,'blog/index.html',{'hello':"hello world"})
    # article=models.Article.objects.get(pk=1)

    #第一步：获取所有的文章对象列表
    articles = models.Article.objects.all()
    #第二步：将对象列表传递到前端
    return render(request, 'blog/index.html', {'articles':articles})

#博客文章内容页面
def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'article':article})

#博客撰写页面
# def edit_page(request):
#     return render(request,'blog/edit_page.html')
#博客撰写和修改页面
def edit_page(request,article_id):
    if str(article_id)=='0':
        return render(request,'blog/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})

#表单响应
def edit_action(request):
    title=request.POST.get('title','Title')
    content = request.POST.get('content', 'Content')
    id=request.POST.get('article_id', '0')
    #创建文章对象
    if id=='0':
        models.Article.objects.create(title=title,content=content)
        articles = models.Article.objects.all()
        #返回主页面
        return render(request, 'blog/index.html', {'articles': articles})
    else:
        article = models.Article.objects.get(pk=id)
        article.title=title
        article.content=content
        article.save()
        # 返回主页面
        return render(request, 'blog/article_page.html', {'article': article})

