from django.shortcuts import render




def contact_view(request):
    return render(request,'html_files/contact.htm')

def home_view(request):
    return render(request, 'html_files/home.htm')


def about_view(request):
    return render(request, 'html_files/about.htm')

