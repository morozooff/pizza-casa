from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from .forms import UserCreationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import login


class RegisterUser(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request: Request):
        user_form = UserCreationForm()

        return Response({'user_form': user_form, }, template_name='users/register.html')

    def post(self, request: Request):

        user_form = UserCreationForm(request.data)


        if user_form.is_valid():
            user = user_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success = (request, f'User {username} was created successful')
            user.is_active = True
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)

            return HttpResponseRedirect(redirect_to=reverse('profile'))

        return Response({'user_form': user_form, }, template_name='users/register.html')


class ProfileAPIView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        user_upd_form = UserUpdateForm(instance=request.user)
        profile_upd_form = ProfileUpdateForm(instance=request.user.profile)
        return Response({'user_upd_form': user_upd_form, 'profile_upd_form': profile_upd_form}, template_name='users/profile.html')

    def post(self, request: Request):
        user_upd_form = UserUpdateForm(request.data, instance=request.user)
        profile_upd_form = ProfileUpdateForm(request.data, instance=request.user.profile)

        if user_upd_form.is_valid() and profile_upd_form.is_valid():
            user_upd_form.save()
            profile_upd_form.save()
            messages.success(request, 'Your profile was updated successful')
            return HttpResponseRedirect(redirect_to= reverse('profile'))

        return Response({'user_upd_form': user_upd_form, 'profile_upd_form': profile_upd_form}, template_name='users/profile.html')