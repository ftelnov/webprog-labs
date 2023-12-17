from django.shortcuts import render

from .forms import FeedbackForm


def main(request):
    if request.method == "GET":
        return render(request, "main.html")


def about_dev(request):
    if request.method == "GET":
        return render(request, "about.html")


def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            return render(request, "feedback_thanks.html")
    else:
        form = FeedbackForm()
    return render(request, "feedback.html", {"form": form})
