# from django.shortcuts import render
# from django.http import HttpResponse

# # Create your views here.

# def main(request):
#     omdb_url= "http://www.omdbapi.com/?i=tt3896198&apikey=94043787"
#     api_key="94043787"
#     return HttpResponse('hello its working yay')

from requests import get
from django.shortcuts import render
from django.http import JsonResponse

# Your OMDb API key
OMDB_API_KEY = '94043787'

def home(request):
    # Replace 'your_favorite_movie' with a default movie title
    favorite_movie = 'summer'
    url = f"http://www.omdbapi.com/?s={favorite_movie}&apikey={OMDB_API_KEY}&page=1"
    response = get(url)
    movies = response.json().get('Search', [])
    # response = get(f'http://www.omdbapi.com/?apikey={OMDB_API_KEY}&s=avengers&page=1')
    # movies = response.json()
    print(movies)
    return render(request, 'home.html', {'movies': movies})

def movie_details(request, title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
    response = requests.get(url)
    movie = response.json()
    return render(request, 'movie_details.html', {'movie': movie})
