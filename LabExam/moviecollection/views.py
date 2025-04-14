from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Review
from django.contrib.auth.decorators import login_required
from .forms import MovieForm, ReviewForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages


@login_required
def home(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    reviews = movie.reviews.all()  # Uses related_name defined in the model.
    return render(request, 'movie_detail.html', {'movie': movie, 'reviews': reviews})


@login_required
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.owner = request.user
            movie.save()
            return redirect('home')
    else:
        form = MovieForm()
    return render(request, 'movie_form.html', {'form': form})


@login_required
def review_create(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            # Optionally, validate that the rating is between 1 and 5.
            if 1 <= review.rating <= 5:
                review.save()
                return redirect('movie_detail', pk=movie.id)
            else:
                form.add_error('rating', 'Rating must be between 1 and 5.')
    else:
        form = ReviewForm()
    return render(request, 'review_form.html', {'form': form, 'movie': movie})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log in the newly registered user.
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
