from django.shortcuts import render


from django.http import HttpResponse
from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError
import os


def index(request):
	return render(request,'upload.html')

def list(request):
	# If you already have an access/refresh pair in hand
	client_id = '17e6ca4e5c3785d'
	client_secret = '0032aba7460da31f80c779f640696cef151d7f8b'
	access_token = '873e4f5b386ad9c69e0a090b33e0c812d2a1bff5'
	refresh_token = '647e47f5518aa2b23c2cd09cd69fdce6e91f91ac'
	username = 'Catkic'
# Note since access tokens expire after an hour, only the refresh token is required (library handles autorefresh)



	client = ImgurClient(client_id, client_secret, access_token, refresh_token)

	config = {
			'album': None,
			'name':  'Test!',
			'title': 'Test',
			'description': 'Cute kitten being cute on '
	}
	path = "g:/testte.jpg"

	images = client.get_account_images(username, page=0)

	for item in images:
		print(item.link)

	context = {
		'images': images,
	}

	#img = client.upload_from_path(path, config=config, anon=False)


	return render(request, 'upload.html', context)

def test(request):
	return render(request,'test.html')

def api(request):
	p2 = request.GET.get('access_token')
	p1 = request.GET.get(request.get_full_path())
	return HttpResponse(p1)