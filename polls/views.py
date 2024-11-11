# from django.shortcuts import render
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm

from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))


# This function does nearly the same as results function, but it doesn't
# use shortcuts, so it is longer. It has one layer of abstraction less.
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question of id %d does not exist" % question_id)
    template = loader.get_template("polls/detail.html")
    context = {"question": question}
    return HttpResponse(template.render(context, request))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

@login_required
def home(request):
    
    return HttpResponse("ez")

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log the user in after registration
            return redirect('/polls/home')  # redirect to a home page
    else:
        form = RegisterForm()
    return render(request, 'polls/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/polls/home')
    else:
        form = LoginForm()
    return render(request, 'polls/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('/polls/home')

# def mlogout(request):
#     logout(request)
#     return HttpResponse("cos")

# def login(request):
#     context = {"test": "nie post"}
#     if request.user.is_authenticated:
#         context["test"] = "authenticated user"
#     if request.method == "POST":
#         if "submit" in request.POST:
#             login = request.POST["login"]
#             password = request.POST["password"]
#             # mozna zhashowac haslo
#             user = get_object_or_404(User, login=login, password=password)
#             print(user)
#             context["test"] = "logged in"
#             try:
#                 login(request, user)
#             except Exception as e:
#                 print(e)
#         else:
#             raise Http404("Wrong form submitted")
#     template = loader.get_template("polls/login.html")
#     return HttpResponse(template.render(context, request))
    