from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.core.signing import BadSignature
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from .forms import ChangeUserInfoForm, RegisterUserForm, SearchForm, AdsForm, ImagesFormSet
from .models import AdvUser, SubRubric, Ads
from .utilities import signer


def index(request):
    ads = Ads.objects.filter(is_active=True)[:10]
    context = {'ads': ads}
    return render(request, 'main/index.html', context)


def other_page(request, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))


@login_required
def profile(request):
    ads = Ads.objects.filter(author=request.user.pk, is_active=True)
    context = {'ads': ads}
    return render(request, 'main/profile.html', context)


class ShopLoginView(LoginView):
    template_name = 'main/login.html'


class ShopLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'main/logout.html'


class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = AdvUser
    template_name = 'main/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('main:profile')
    success_message = 'Data is changed'

    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class ChangeUserPasswordView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'main/password_change.html'
    success_url = reverse_lazy('main:profile')
    success_message = 'Password is changed'


class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'main/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')


class RegisterDoneView(TemplateView):
    template_name = 'main/register_done.html'


# TODO: setting config SMTP-server for message
# TODO: активация через вк
# TODO: сброс пароля

def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'main/bad_signature.html')
    user = get_object_or_404(AdvUser, username=username)
    if user.is_activated:
        template = 'main/user_is_activate.html'
    else:
        template = 'main/activation_done.html'
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)


class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = AdvUser
    template_name = 'main/delete_user.html'
    success_url = reverse_lazy('main:index')

    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'User delete')
        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


def by_rubric(request, pk):
    rubric = get_object_or_404(SubRubric, pk=pk)
    ads = Ads.objects.filter(is_active=True, rubric=pk)
    # search
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        q = Q(title__icontains=keyword) | Q(content__icontains=keyword)
        ads = ads.filter(q)
    else:
        keyword = ''
    form = SearchForm(initial={'keyword': keyword})
    paginator = Paginator(ads, 2)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'rubric': rubric, 'page': page, 'ads': page.object_list, 'form': form}
    return render(request, 'main/by_rubric.html', context)


def detail(request, rubric_pk, pk):
    ad = get_object_or_404(Ads, pk=pk)
    images = ad.additionalimage_set.all()
    context = {'ad': ad, 'images': images}
    return render(request, 'main/detail.html', context)


@login_required
def profile_ad_detail(request, pk):
    ad = get_object_or_404(Ads, pk=pk)
    images = ad.additionalimage_set.all()
    context = {'ad': ad, 'images': images}
    return render(request, 'main/detail_user_ad.html', context)


@login_required
def profile_ad_add(request):
    if request.method == 'POST':
        form = AdsForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save()
            formset = ImagesFormSet(request.POST, request.FILES, instance=ad)
            if formset.is_valid():
                formset.save()
                messages.add_message(request, messages.SUCCESS, 'Ad add :)')
                return redirect('main:profile')
    else:
        form = AdsForm(initial={'author': request.user.pk})
        formset = ImagesFormSet()
    context = {'form': form, 'formset': formset}
    return render(request, 'main/profile_ad_add.html', context)


@login_required
def profile_ad_change(request, pk):
    ad = get_object_or_404(Ads, pk=pk)
    if request.method == 'POST':
        form = AdsForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            ad = ad.save()
            formset = ImagesFormSet(request.POST, request.FILES, instance=ad)
            if formset.is_valid():
                formset.save()
                messages.add_message(request, messages.SUCCESS, 'Ad is changed')
                return redirect('main:profile')
    else:
        form = AdsForm(instance=ad)
        formset = ImagesFormSet(instance=ad)
    context = {'form': form, 'formset': formset, 'ad': ad}
    return render(request, 'main/profile_ad_change.html', context)


@login_required
def profile_ad_delete(request, pk):
    ad = get_object_or_404(Ads, pk=pk)
    if request.method == 'POST':
        ad.delete()
        messages.add_message(request, messages.SUCCESS, 'Ad is deleted')
        return redirect('main:profile')
    else:
        context = {'ad': ad}
        return render(request, 'main/profile_ad_delete.html', context)
