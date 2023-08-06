from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from .forms import UserCreationForm, UserUpdateForm
from django.contrib import messages


class RegisterUser(APIView):

    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request: Request):
        form = UserCreationForm()
        return Response({'form': form}, template_name='users/register.html')

    def post(self, request: Request):
        form = UserCreationForm(request.data)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success = (request, f'User {username} was created successful')

            return HttpResponseRedirect(redirect_to = reverse('home'))

        return Response({'form': form}, template_name='users/register.html')


class ProfileAPIView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        upd_form = UserUpdateForm(instance=request.user)
        return Response({'upd_form': upd_form}, template_name='users/profile.html')

    def post(self, request: Request):
        upd_form = UserUpdateForm(request.data, instance=request.user)

        if upd_form.is_valid():
            upd_form.save()
            messages.success(request, 'Your profile was updated successful')
            return HttpResponseRedirect(redirect_to= reverse('profile'))

        return Response({'upd_form': upd_form}, template_name='users/profile.html')