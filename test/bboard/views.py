from .models import Bb, Rubric, Rez
from django.template import loader
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
import cv2 
from PIL import Image


from django.views.generic.edit import CreateView
from .forms import BbForm

def Neiro(immage):
    imaging = cv2.imread(r'C:\Users\John\Desktop\Documents\Ynic\4 semac\Neiroset\test\media\\' + immage)
    imaging_gray = cv2.cvtColor(imaging, cv2.COLOR_BGR2GRAY) 
    imaging_rgb = cv2.cvtColor(imaging, cv2.COLOR_BGR2RGB) 
    xml_data = cv2.CascadeClassifier(r'C:\Users\John\Downloads\opencv\build\x64\vc14\bin\data\cascade.xml') 
    detecting = xml_data.detectMultiScale(imaging_gray,  minSize =(40, 40)) 
    amountDetecting = len(detecting) 
    if amountDetecting != 0: 
        for(a, b, width, height) in detecting: 
            cv2.rectangle(imaging_rgb,(a, b), 
                     (a + height, b + width),  
                     (0, 275, 0), 9)
    cv2.imwrite(r'C:\Users\John\Desktop\Documents\Ynic\4 semac\Neiroset\test\media\images\\' + 'Rez_' + immage, imaging_rgb)        


def index(request, rubric_id):
    for b in Bb.objects.filter(rubric=rubric_id):
        Neiro(str(b.image))
    rez = Rez.objects.create(image_rez = Image.open(r'C:\Users\John\Desktop\PhotoPol\1.jpg'))
    template =  loader.get_template('bboard/index.html')
    bbs = Bb.objects.order_by('-published')
    rubrics = Rubric.objects.all()
    context = {'rez': rez,'bbs':bbs,'rubrics':rubrics}
    return HttpResponse(template.render(context,request))



def by_rubric(request, rubric_id):
    for b in Bb.objects.filter(rubric=rubric_id):
        Neiro(str(b.image))
    rez = Rez.objects.create(image_rez = Image.open(r'C:\Users\John\Desktop\PhotoPol\1.jpg'))
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'rez': rez, 'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context



