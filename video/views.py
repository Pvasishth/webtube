from django.shortcuts import render
from .models import *
import random
from django.shortcuts import get_object_or_404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
    TemplateView,
    View
)

# class HomeView(View):
#     def get(self,request):
#
#         context = {
#             "name":"paras",
#             "random_number": random.randint(500, 1000)
#
#         }
#         return render(request, 'video/index.html', context)



class VideoCreateView(CreateView):
    # template_name = 'video/index.html'
    queryset = Video.objects.all()



class VideoDetailView(DetailView):
    template_name = 'video/test.html'
    # queryset = Video.objects.get()
    model = Video
    context_object_name = "video_detail"



    # def get_context_data(self,**kwargs):
    #     context = super(VideoDetailView, self).get_context_data()
    #     print(context)
    #     return context





class VideoListView(ListView):
    template_name = 'video/index.html'
    queryset = Video.objects.all

    def get_context_data(self, **kwargs):
        context = super(VideoListView, self).get_context_data()
        print(context)
        return context



class VideoCreateView(UpdateView):
    queryset = Video.objects.all()

class VideoDeleteView(DeleteView):
    queryset = Video.objects.all()