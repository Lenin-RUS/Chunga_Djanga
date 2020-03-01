from django.shortcuts import render, get_object_or_404
from .models import Point, Sinonim
from .forms import Sinonim_form

# Create your views here.
def main_view(request):
    points=Point.objects.all()
    return render(request, 'gaspoints/index.html', context={'points':points})

def add_name(request):
    if request.method == 'POST':
        pass
    else:
        form=Sinonim_form
        return render(request, 'gaspoints/add_name.html')

def point(request, id):
    point=get_object_or_404(Point, id=id)
    sinonim=Sinonim.objects.filter(root_point=id)
    if request.method == 'POST':
        form=Sinonim_form(request.POST)
        if form.is_valid():
            new_sinonim=form.cleaned_data['point_sinonim']
            try:
                Sinonim.objects.create(name=new_sinonim, root_point= Point.objects.filter(id=id).first())
            except:
                pass
            return render(request, 'gaspoints/point.html', context={'point':point, 'sinonims':sinonim, 'form':form })
        else:
            return render(request, 'gaspoints/point.html', context={'point':point, 'sinonims':sinonim, 'form':form })
    else:
        form=Sinonim_form
        return render(request, 'gaspoints/point.html', context={'point':point, 'sinonims':sinonim, 'form':form })

