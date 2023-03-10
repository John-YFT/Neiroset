from .models import Bb, Rubric
from django.template import loader
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse

from django.views.generic.edit import CreateView
from .forms import BbForm

def index(request):
   for bb in Bb.objects.all():
       s = (bb.Xol_v * 52.96) + (bb.El * 4.5) + (bb.Gaz * 69.3417)
       bb.price = int(s)
       bb.save()
   template =  loader.get_template('bboard/index.html')
   bbs = Bb.objects.order_by('-published')
   rubrics = Rubric.objects.all()
   context = {'bbs':bbs,'rubrics':rubrics}
   return HttpResponse(template.render(context,request))



def by_rubric(request, rubric_id):
    for bb in Bb.objects.all():
        s = (bb.Xol_v*52.96) + (bb.El*4.5) + (bb.Gaz*69.3417)
        bb.price = int(s)
        bb.save()
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


