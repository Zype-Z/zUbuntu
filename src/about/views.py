from django.shortcuts import render

# Create your views here.
def about_view(request):
    template_name = "about.html"
    return render(request, template_name)