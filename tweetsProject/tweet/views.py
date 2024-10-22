from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# from .models import Post


# Create your views here.

def index(request):
    return render(request, 'tweet/index.html') 

def tweet_List(request):
    query=request.GET.get('q')
    
    if query:
        tweets=Tweet.objects.filter(text__icontains=query) .order_by('-created_date')
        return render(request, 'tweet/search/search_results.html', {'tweets':tweets})
    else:
        tweets=Tweet.objects.all().order_by('-created_date')
    return render(request,'tweet/tweet_List.html', {'tweets':tweets})

# def tweet_List(request):
#     query = request.GET.get('q')  # Get the search query from the URL parameters
#     if query:
#         # Filter tweets based on the search query
#         tweets = Tweet.objects.filter(text__icontains=query).order_by('-created_date')
#         return render(request, 'tweet/search/search_results.html', {'tweets': tweets})
#     else:
#         # Default to all tweets if no search query is provided
#         tweets = Tweet.objects.all().order_by('-created_date')
    
#     return render(request, 'tweet/tweet_List.html', {'tweets': tweets})

@login_required
def tweet_create(request):
    if request.method=='POST':
        form=TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('tweet_List')
    else:
        form=TweetForm()
    return render(request, 'tweet/tweet_form.html', {'form':form})


@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)  # Get the tweet object for the current user
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)  # Populate the form with the tweet instance
        if form.is_valid():
            tweet = form.save(commit=False)  # Save the form but don't commit yet
            tweet.user = request.user  # Assign the current user to the tweet
            tweet.save()  # Now save the tweet
            return redirect('tweet_List')  # Redirect to the tweet list after saving
    else:
        form = TweetForm(instance=tweet)  # Create a form instance with the existing tweet data

    return render(request, 'tweet/tweet_form.html', {'form': form})  # Render the form


login_required
def tweet_delete(request, tweet_id):
    tweet=get_object_or_404(Tweet, pk=tweet_id, user=request.user)

    if request.method =='POST':
        tweet.delete()
    
        return redirect('tweet_List')
    return render(request, 'tweet/tweet_confirm_delete.html', {'tweet':tweet})



def register(request):
    if request.method== 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_List')
    else:
       form=UserRegistrationForm()
    return render(request, 'registration/register.html', {'form':form})

# def search(request):
#     if request.method=='POST':
#         search_query=request.POST['search_query']
#         posts=Post.objects.filter(Q(text__contains=search_query)| Q (content__contains=search_query))
#         return render(request, 'search_results.html', {'posts':posts})
#     return render(request. 'search')

