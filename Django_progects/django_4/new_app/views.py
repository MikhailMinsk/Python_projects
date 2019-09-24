from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Blog
from .forms import ContactForm, BlogForm, BlogModelForm


def contact(request):
    """
    only for test forms
    """
    print(request.POST)
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form = ContactForm()  # cleaning form
    return render(request, 'new_app/form.html', {'title': 'Contact us',
                                                 'form': form,
                                                 })


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'new_app/detail.html', {'blog': blog})


def blog_list(request):
    # blogs = Blog.objects.all()[:3] -only 3 blogs on main page. Its pagination
    qs = Blog.objects.all().published()
    if request.user.is_authenticated:
        my_qs = Blog.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    return render(request, 'new_app/list.html', {'blogs': qs})


# @login_required  # LOGIN_URL = '/login' in settings.py
@staff_member_required  # gives the user administrator access . staff in panel admin at the user
def blog_create(request):
    form = BlogModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        form = BlogModelForm()
        return redirect('detail', slug=post.slug)
    # form = BlogForm(request.POST or None)
    # if form.is_valid():
    #     # django method 1
    #     # title = form.cleaned_data['title']
    #     # blog = Blog.objects.create(title=title)
    #     blog = Blog.objects.create(**form.cleaned_data)  # django method create 2
    #     form = BlogForm()
    #     # obj = Blog()         #  standard
    #     # obj.title = title    #  method
    #     # obj.save()           #
    return render(request, 'new_app/create.html', {'title': 'Create',
                                                   'form': form,
                                                   })


@staff_member_required
def blog_update(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    form = BlogModelForm(request.POST or None, request.FILES or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('detail', slug=blog.slug)
    return render(request, 'new_app/form.html', {'title': f'Update {blog.title}',
                                                 'form': form,
                                                 })


@staff_member_required
def blog_delete(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.method == 'POST':
        blog.delete()
        return redirect('home')
    return render(request, 'new_app/form.html', {'title': f'Delete {blog.title}'})
