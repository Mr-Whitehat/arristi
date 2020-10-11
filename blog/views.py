from django.shortcuts import render, HttpResponse, redirect
from .models import Blogpost, PostComment
from django.contrib import messages
from blog.templatetags import extra

def index(request):
    return render(request, 'blog/bloghome.html')

def ai(request):
    aiposts = Blogpost.objects.filter(category='ai')
    count = 0;
    for i in aiposts:
        count += 1;
    return render(request, 'blog/ai.html',{'aiposts':aiposts, 'nPosts': count})

def ethical(request):
    csposts = Blogpost.objects.filter(category='cs')
    count = 0;
    for i in csposts:
        count += 1;
    return render(request, 'blog/ethical.html',{'csposts':csposts, 'nPosts': count})

def blogslug(request,postslug):
    slugpost = Blogpost.objects.filter(slug=postslug)[0]
    asidepost = Blogpost.objects.all()
    ''' slugpost = Blogpost.objects.filter(slug=postslug) will give a Query set, check by (print(slugpost));
        but we require its first Object, so here we can use 
        "slugpost = Blogpost.objects.filter(slug=postslug)[0]" or 
        "slugpost = Blogpost.objects.filter(slug=postslug).first()" 
    '''
    comments = PostComment.objects.filter(post=slugpost, parent=None)
    replies = PostComment.objects.filter(post=slugpost).exclude(parent=None)

    replydic = {}
    for relpy in replies:
        if relpy.parent.sno not in replydic.keys():
            replydic[relpy.parent.sno] = [relpy]
        else:
            replydic[relpy.parent.sno].append(relpy)

    if slugpost.category == 'cs':
        link = 'ethical'
        bCrumb = 'EH'
    elif slugpost.category == 'ai':
        link = 'ai'
        bCrumb = 'AI'
    print(asidepost)
    dic = {'post': slugpost,'bCrumb': bCrumb, 'link': link, 'comments': comments, 'user': request.user, 'replydic':replydic,'asidepost':asidepost}
    return render(request, 'blog/blogpost.html', dic)

# def blogpost(request,id):
#     post = Blogpost.objects.filter(post_id=id)[0]

def postcomment(request):
    if request.method == "POST":
        user = request.user
        postid = request.POST['postid']
        comment = request.POST['comment']
        post = Blogpost.objects.get(post_id=postid)
        parentsno = request.POST['parentsno']
        if parentsno == "" :
            comment = PostComment(user=user, post=post, comment=comment)
            comment.save()
            messages.success(request, "Your comment has been posted successfully!")
        else:
            parent = PostComment.objects.get(sno=parentsno)
            comment = PostComment(user=user, post=post, comment=comment, parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully!")

    return redirect(f"/blog/blogpost/{post.slug}")