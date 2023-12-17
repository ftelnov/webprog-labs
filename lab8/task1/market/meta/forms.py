from django import forms


class FeedbackForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=100)
    last_name = forms.CharField(label="Last name", max_length=100)
    speed_rate = forms.IntegerField(label="Speed rate", min_value=0, max_value=10)
    comfort_rate = forms.IntegerField(label="Comfort rate", min_value=0, max_value=10)
    price_rate = forms.IntegerField(label="Price rate", min_value=0, max_value=10)
