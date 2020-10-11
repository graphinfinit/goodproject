from django.shortcuts import render, redirect

from .models import Herb_article, Comment
from time import timezone

from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms  import Herb_articleForm

from django.contrib.auth.decorators import login_required

# Create your views here.

# All articles

def herbs_app_main(request):
    '''Пагинатор.Все статьи '''
    articles_list = Herb_article.objects.order_by('-date_updatese')
    paginator = Paginator(articles_list, 10)

    page = request.GET.get('page')
    try:
        herb_list = paginator.page(page)
    except PageNotAnInteger:
        herb_list = paginator.page(1)
    except EmptyPage:
        herb_list = paginator.page(paginator.num_pages)
        
        
    data = {"herb_list": herb_list}

    
    return render(request,'herb_articles/herbs_app_main.html',context = data)
    
    
    
# Новинки
def new_items(request):
    '''Выкидывает x последних статей '''
    x = 3
    latest_articles_list = Herb_article.objects.order_by('-date_updatese')[:x]
    data = {"latest_articles_list": latest_articles_list}
    return render(request,'herb_articles/title.html', context = data)
    
    

def herb_id_info(request,herb_id):
    '''По id статьи выдает из базы данных статью и все комментарии к ней'''
    article_id = Herb_article.objects.get(id = herb_id)

    comments = Comment.objects.all().filter(article = article_id.id)
    
    data = {'article_id': article_id, 'comments': comments}
    return render(request,'herb_articles/herb_id_info.html', context = data)

@login_required
def leave_aricle(request):

    herb_articleform = Herb_articleForm()
    articles = Herb_article.objects.all()

    if request.method == 'POST':

        herb_articleform = Herb_articleForm(data=request.POST)
        if herb_articleform.is_valid():
            article = herb_articleform.save(commit=False)

            article.author = request.user

            article.save()

        return redirect('new_items')

    else:
        return render(request, 'herb_articles/leave_article.html', {'herb_articleform': herb_articleform})



def leave_comment(request, herb_id):
    '''Оставляет комментарий к статье по ее id'''
    print(request.POST)
    if 'user_named' in request.POST:
        userd = request.POST['user_named']
    else:
        userd = False
    if 'comment' in request.POST:
        comment_text = request.POST['comment']
    else:
        comment_text = False

    article = Herb_article.objects.get(id=herb_id)
    article.comment_set.create(comment_text=comment_text, author_name=userd)

    article_id = Herb_article.objects.get(id=herb_id)
    comments = Comment.objects.all().filter(article=article_id.id)

    data = {'article_id': article_id, 'comments': comments}

    return render(request, 'herb_articles/herb_id_info.html', context=data)




def all_info(request):
    '''Раздел о нас'''
    data = {'':0}
    return render(request,'herb_articles/all_info.html', context = data)
    
    
    

    


   
