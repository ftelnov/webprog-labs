from django.shortcuts import render

from .forms import FeedbackForm
from .models import Feedback


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
            data = form.cleaned_data
            instance = Feedback(first_name=data["first_name"], last_name=data["last_name"],
                                speed_rate=data["speed_rate"],
                                price_rate=data["price_rate"], comfort_rate=data["comfort_rate"])
            instance.save()
            return render(request, "feedback_thanks.html")
    else:
        form = FeedbackForm()
    return render(request, "feedback.html", {"form": form})
