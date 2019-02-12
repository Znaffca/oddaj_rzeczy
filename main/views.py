from django.shortcuts import render
from django.views import View


# landing page

class IndexView(View):
    def get(self, request):
        return render(request, 'main/index.html')


class FormView(View):
    def get(self, request):
        return render(request, 'main/form.html')
