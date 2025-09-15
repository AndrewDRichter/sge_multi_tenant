from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
# from .models import Client, TenantUser

from django.http import HttpResponse

def index(request):
    # print(request.session)
    # if not request.user.is_authenticated:
    #     return redirect('login')
    return HttpResponse('<h1>Welcome to public page</h1>')

# @csrf_exempt
# def login_view(request):
#     if request.method == 'GET':
#         clients = Client.objects.all()
#         return HttpResponse(f'''
#                             <h1>Login page</h1>
#                             <form action='/login' method='POST'>
#                                 <select name='tenant'>
#                                     {[f'<option>{client}</option>' for client in clients]}
#                                 </select>
#                                 <input type='text' name='username' placeholder='username' />
#                                 <input type='password' name='password' placeholder='password'/>
#                                 <button type='submit'>Log in</button>
#                             </form>
#         ''')
#     if request.method == 'POST':
#         tenant = request.POST.get('tenant')
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user=user)
            

#         return redirect('login')
    