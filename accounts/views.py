from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from accounts.forms import RegistrationForm, EditProfileForm, ProfileForm, SearchUser, SendMessage
from accounts.models import UserProfile, UserProfiles, Messages
from home.models import Friend, Friend_Request

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = RegistrationForm()

	args = {'form': form,}
	return render(request, 'accounts/reg_form.html', args)


def view_profile(request, pk=None):
	if pk:
		user = User.objects.get(pk=pk)
		profile = UserProfiles.objects.get(user_id=pk)
	else:
		user = request.user
		profile = UserProfiles.objects.get(user=request.user)
	args = {
		'user': user,
		'profile': profile,
		}
	return render(request, 'accounts/profile.html', args)
	

def edit_profile(request):
	if request.method == 'POST':
		user_form = EditProfileForm(request.POST, instance=request.user)
		profile_form = ProfileForm(request.POST, request.FILES, instance=UserProfiles.objects.get(user=request.user))
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			return redirect('view_profile')
	else:
		user_form = EditProfileForm(instance=request.user)
		profile_form = ProfileForm(instance=UserProfiles.objects.get(user=request.user))
		args = {
			'user_form': user_form,
			'profile_form': profile_form,
			}
		return render(request, 'accounts/edit_profile.html', args)

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('view_profile')
		else:
			return redirect('change_password')
	else:
		form = PasswordChangeForm(user=request.user)
		
		args = {'form': form}
		return render(request, 'accounts/change_password.html', args)
		
def friend_list(request):
		friend, created = Friend.objects.get_or_create(
			current_user=request.user
			)
		friends = friend.users.all()
		frequest = Friend_Request.objects.filter(current_user=request.user)
		args = {
			'friends': friends,
			'frequest': frequest,
		}
		return render(request, 'accounts/friend_list.html', args)
		
def search_user(request):
		users = User.objects.exclude(id = request.user.id)
		users = users.exclude(id = 1)
		if request.method == 'POST':
			text = request.POST.get('textfield', None)
			try:
				users = users.filter(username__icontains= text)
			except:
				return redirect('search_user')
		friend, created = Friend.objects.get_or_create(current_user=request.user)
		friends = friend.users.all()
		frequest = Friend_Request.objects.filter(current_user=request.user)
		args = {
			'users': users,
			'friends': friends,
			'frequest': frequest,
			}
		return render(request, 'accounts/search_user.html', args)

class friend_message(TemplateView):
	template_name = 'accounts/message.html'

	def get(self, request, pk=None):
		form = SendMessage()
		mes = Messages.objects.all()
		if pk:
			friend_user = User.objects.get(pk=pk)
			mes0 = mes.filter(current_user=request.user, friend_user=friend_user)
			mes1 = mes.filter(current_user=friend_user, friend_user=request.user)
			mes2 = mes0 | mes1
			mes = mes2.all().order_by('-created_date', '-updated_date')
		else:
			return redirect('home')
		args = {
		'form': form,
		'mes': mes,
		}
		return render(request, self.template_name, args)
		
	def post(self, request, pk=None):
		form = SendMessage(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.current_user = request.user
			post.friend_user = User.objects.get(pk=pk)
			post.message = request.POST.get('post')
			post.save()
			form = SendMessage()
			return redirect('friend_message', pk=pk)

class NotifyView(TemplateView):
	template_name = 'accounts/notify.html'

	def get(self, request):
		frequest = Friend_Request.objects.filter(request_user=request.user)
		args = {
			'frequest': frequest,
		}
		return render(request, self.template_name, args)