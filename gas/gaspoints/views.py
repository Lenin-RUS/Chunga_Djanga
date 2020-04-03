from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from .models import Point, Sinonim, pars
from .forms import SendMail, Add_sinonim
from django.core.mail import send_mail as Core_Send_Mail
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def main_view(request):
    points = Point.objects.all()
    return render(request, 'gaspoints/index.html', context={'points': points})


# def point(request, id):
#     point = get_object_or_404(Point, id=id)
#     sinonim = Sinonim.objects.filter(root_point=id)
#     if request.method == 'POST':
#         form = Sinonim_form(request.POST)
#         if form.is_valid():
#             new_sinonim = form.cleaned_data['point_sinonim']
#             try:
#                 Sinonim.objects.create(name=new_sinonim, root_point=Point.objects.filter(id=id).first())
#             except:
#                 pass
#             return render(request, 'gaspoints/point.html', context={'point': point, 'sinonims': sinonim, 'form': form})
#         else:
#             return render(request, 'gaspoints/point.html', context={'point': point, 'sinonims': sinonim, 'form': form})
#     else:
#         form = Sinonim_form
#         return render(request, 'gaspoints/point.html', context={'point': point, 'sinonims': sinonim, 'form': form})


def send_mail(request):
    if request.method == 'POST':
        mail_form = SendMail(request.POST)
        if mail_form.is_valid():
            Core_Send_Mail('Сообщение с сайта', mail_form.cleaned_data['message'], 'LaninSN@yandex.ru',
                           [mail_form.cleaned_data['email']], fail_silently=False)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'gaspoints/send_mail.html', context={'mail_form': mail_form})
        pass
    else:
        mail_form = SendMail
        return render(request, 'gaspoints/send_mail.html', context={'mail_form': mail_form})


# def add_point(request):
#     if request.method == 'GET':
#         form = Add_point()
#         return render(request, 'gaspoints/add_point.html', context={'form': form})
#     else:
#         form = Add_point(request.POST)
#         if form.is_valid():
#             form.instance.user = request.user
#             form.save()
#             return HttpResponseRedirect('/')
#         else:
#             return render(request, 'gaspoints/add_point.html', context={'form': form})


class PointListView(ListView):
    model = Point
    tamplate_name = 'gaspoints/point_list.html'
    paginate_by = 20


class PointDetailView(LoginRequiredMixin, DetailView):
    model = Point
    tamplate_name = 'gaspoints/point_detail.html'

    def get_context_data(self, **kwards):
        context = super(PointDetailView, self).get_context_data(**kwards)
        context['point_sinonims'] = Sinonim.objects.filter(root_point=self.object)
        context['form_sinonims'] = Add_sinonim()
        return context

class PointCreateView(UserPassesTestMixin, CreateView):
    fields = ('pointKey', 'pointLabel', 'commercialType', 'pointType', 'point_id', )
    model = Point
    success_url = reverse_lazy('gas:point_list')
    tamplate_name = 'gaspoints/new_point.html'
    login_url = 'users:login'

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect(self.login_url)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PointUpdateView(UpdateView):
    fields = ('pointKey', 'pointLabel', 'commercialType', 'pointType', 'point_id', )
    model = Point
    success_url = reverse_lazy('gas:point_list')
    tamplate_name = 'gaspoints/point_detail.html'


class PointDeleteView(DeleteView):
    tamplate_name = 'gaspoints/point_confirm_delete.html'
    model = Point
    success_url = reverse_lazy('gas:point_list')

@user_passes_test(lambda u: u.is_superuser)
def pars_new_points_view(request):
    new_points = pars()
    return render(request, 'gaspoints/parser.html', context={'new_points': new_points})


class SinonimCreateView(CreateView):
    tamplate_name = 'gaspoints/point_detail.html'
    form_class=Add_sinonim
    model = Sinonim
    # success_url = reverse_lazy('gas:sinonim_form')

    def post(self, request, *args, **kwargs):
        self.point_pk = kwargs['pk']
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.root_point = get_object_or_404(Point, pk=self.point_pk)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('gas:point_detail', kwargs={'pk':self.point_pk})