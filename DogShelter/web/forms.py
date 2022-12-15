from django import forms 
from django.forms import Form, CharField, Select

from DogShelter.web.models import NewsletterSubscriber

# Subscribe for the newsletter form
class SubscribeForm(forms.Form):
    email = forms.EmailField(required=True, label='Email')
    name = forms.CharField(required=True, label='Name')
    
    class Meta:
        model = NewsletterSubscriber

# Contact form
class ContactForm(forms.Form):
    name = forms.CharField(required=True, label='Name')
    email = forms.EmailField(required=True, label='Email')
    subject = forms.CharField(required=True, label='Subject')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Message')

# Adopt form
class AdoptForm(forms.Form):
    name = forms.CharField(required=True, label='Name')
    email = forms.EmailField(required=True, label='Email')
    phone = forms.CharField(required=True, label='Phone')   
    city = forms.CharField(required=True, label='City')
    country = forms.CharField(required=True, label='Country')
    dog = forms.CharField(required=True, label='Dog Name')

# Dog filter form
class DogFilterForm(forms.Form):
    dog_name = forms.CharField(required=False, label='Dog Name')
    dog_name.widget.attrs.update({
            'name': 'dogName',
            'id': 'dogName',
        })


class vaStatusForm(Form):
    # Define the form fields
    adoption_status = CharField(
        label="Adoption Status",
        widget=Select(choices=(
            ("all", "All dogs"),
            ("va", "Virtually Adopted"),
            ("no", "No Adoptors"),
        ))
    )
    adoption_status.widget.attrs.update({
        'name': 'adoptionStatus',
        'id': 'adoptionStatus',
    })
