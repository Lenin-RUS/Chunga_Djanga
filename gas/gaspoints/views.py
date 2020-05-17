from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from .models import Point, Sinonim, pars, CommercialType, PointType, ExportCountry
from .forms import SendMail, Add_sinonim
from django.core.mail import send_mail as Core_Send_Mail
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
def main_view(request):
    return render(request, 'gaspoints/index.html')

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

class PointListView(ListView):
    queryset = Point.objects.select_related('point_export_from')
    # model = Point
    template_name = 'gaspoints/point_list.html'
    paginate_by = 20


class PointTypeView(ListView):
    queryset = Point.objects.select_related('point_export_from')
    # model = Point
    template_name = 'gaspoints/list_point_type.html'
    paginate_by = 20

    def get_queryset(self):
        my_cat=self.request.GET.get('type_pk')
        return Point.objects.filter(pointType=PointType.objects.get(pk=my_cat)).select_related('point_export_from')

    def get_context_data(self, **kwards):
        my_type=self.request.GET.get('type_pk')
        context = super(PointTypeView, self).get_context_data(**kwards)
        context['point_type'] = PointType.objects.get(pk=my_type)
        context['type_pk'] = my_type
        return context

class PointCategoryView(ListView):
    queryset = Point.objects.select_related('point_export_from')
    # model = Point
    template_name = 'gaspoints/list_category_type.html'
    paginate_by = 20

    def get_queryset(self):
        my_cat=self.request.GET.get('cat_pk')
        return Point.objects.filter(commercialType=CommercialType.objects.get(pk=my_cat)).select_related('point_export_from')

    def get_context_data(self, **kwards):
        my_cat=self.request.GET.get('cat_pk')
        print('-------------------------------', my_cat)
        context = super(PointCategoryView, self).get_context_data(**kwards)
        context['commercial_type'] = CommercialType.objects.get(pk=my_cat)
        context['cat_pk'] = my_cat
        return context

class PointListView_export(ListView):
    queryset = Point.objects.select_related('point_export_from')
    # model = Point
    template_name = 'gaspoints/list_export.html'
    # paginate_by = 200

    def get_queryset(self):
        my_cat=self.request.GET.get('export_pk')
        return Point.objects.filter(point_export_from=ExportCountry.objects.get(pk=my_cat)).select_related('point_export_from')

    def get_context_data(self, **kwards):
        my_country=self.request.GET.get('export_pk')
        context = super(PointListView_export, self).get_context_data(**kwards)
        context['export_country'] = ExportCountry.objects.get(pk=my_country)
        context['export_pk'] = my_country
        return context

class PointDetailView(LoginRequiredMixin, DetailView):
    # queryset = Point.objects.select_related('user')
    model = Point
    template_name = 'gaspoints/point_detail.html'

    def get_context_data(self, **kwards):
        context = super(PointDetailView, self).get_context_data(**kwards)
        context['point_sinonims'] = Sinonim.objects.filter(root_point=self.object)
        context['form_sinonims'] = Add_sinonim()
        return context

class PointCreateView(UserPassesTestMixin, CreateView):
    print('------------------1')
    fields = ('pointKey', 'pointLabel', 'commercialType', 'pointType', 'point_id', 'point_map_x', 'point_map_y', 'point_export_from')
    model = Point
    success_url = reverse_lazy('gas:point_list')
    template_name = 'gaspoints/new_point.html'
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
    template_name = 'gaspoints/point_detail.html'

class PointDeleteView(DeleteView):
    template_name = 'gaspoints/point_confirm_delete.html'
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

    def post(self, request, *args, **kwargs):
        self.point_pk = kwargs['pk']
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.root_point = get_object_or_404(Point, pk=self.point_pk)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('gas:point_detail', kwargs={'pk':self.point_pk})
