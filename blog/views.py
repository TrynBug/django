from django.shortcuts import render, get_object_or_404
from .models import Post, PyTest
from django.utils import timezone
from .forms import PostForm, PyForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'blog/post_list.html', {'posts':posts, 'form':form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form})


def py_test(request):

    pytest = get_object_or_404(PyTest, pk=1)
    if request.method == "POST":
        #form = PyForm(request.POST, instance=pytest)
        form = PyForm()
    else:
        form = PyForm()

    input_text = request.POST.get('input_text')
    if input_text is None:
        input_text = ""

    split_text = input_text.split()

    print(request.POST.getlist('words'))
    if 'submit_split' in request.POST:
        print('submit_split')
    elif 'submit_save' in request.POST:
        print('submit_save')

    return render(request, 'blog/important_words.html', {'pytest':pytest, 'form':form, 'input_text':input_text, 'split_text':split_text})