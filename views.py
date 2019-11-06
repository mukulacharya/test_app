from django.http import HttpResponse
from django.views.generic import DetailView

class ResultView(DetailView):
    def get(self, request):
        return HttpResponse("test")
		
		
		#hi me
