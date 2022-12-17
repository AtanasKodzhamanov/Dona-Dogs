from django import forms 
from django.forms import CharField, Select

from DogShelter.web.models import AdoptionForm, NewsletterSubscriber

# Subscribe for the newsletter form
class SubscribeForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = "__all__"

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

    class Meta:
        model = AdoptionForm

# Dog filter form
class DogFilterForm(forms.Form):
    dog_name = forms.CharField(required=False, initial='Input name', label="")
    dog_name.widget.attrs.update({
            'name': 'dogName',
            'id': 'dogName',
        })


class vaStatusForm(forms.Form):
    # Define the form fields
    adoption_status = CharField(
        label="Virtual Adopter Status",
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

class genderFilterForm(forms.Form):
    gender = forms.CharField(
        label="Filter Gender",
        widget=Select(choices=(
            ("all", "All genders"),
            ("male", "Male"),
            ("female", "Female"),
        ))
    )
    gender.widget.attrs.update({
        'name': 'gender',
        'id': 'gender',
    })
