from django import forms
from django.forms import CharField, Select
from django.utils.translation import gettext_lazy as _
from DogShelter.web.models import NewsletterSubscriber, AdoptionForm, ContactFormModel
from captcha.fields import ReCaptchaField

NAME_MAX_LENGTH = 60
EMAIL_MAX_LENGTH = 60
SUBJECT_MAX_LENGTH = 60
MESSAGE_MAX_LENGTH = 1000

# Contact form


class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = ContactFormModel
        fields = ["email", "name", "subject", "message"]
        widgets = {
            "email": forms.EmailInput(attrs={"maxlength": EMAIL_MAX_LENGTH}),
            "name": forms.TextInput(attrs={"maxlength": NAME_MAX_LENGTH}),
            "subject": forms.Textarea(attrs={"maxlength": SUBJECT_MAX_LENGTH}),
            "message": forms.Textarea(attrs={"maxlength": MESSAGE_MAX_LENGTH}),
        }


# Adopt form


class AdoptForm(forms.Form):
    name = forms.CharField(required=True, label="Name")
    email = forms.EmailField(required=True, label="Email")
    phone = forms.CharField(required=True, label="Phone")
    city = forms.CharField(required=True, label="City")
    country = forms.CharField(required=True, label="Country")
    dog = forms.CharField(required=True, label="Dog Name")

    class Meta:
        model = AdoptionForm


# Dog filter form


class DogFilterForm(forms.Form):
    dog_name = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "name": "dogName",
                "id": "dogName",
                "placeholder": _("Type name"),
            }
        ),
    )


class vaStatusForm(forms.Form):
    # Define the form fields
    adoption_status = forms.CharField(
        # label=_("Virtual Adoption Status"),
        label="",
        widget=Select(
            choices=(
                ("all", _("All dogs")),
                ("va", _("Virtual sponsor")),
                ("no", _("No sponsor")),
            )
        ),
    )
    adoption_status.widget.attrs.update(
        {
            "name": "adoptionStatus",
            "id": "adoptionStatus",
        }
    )


class genderFilterForm(forms.Form):
    gender = forms.CharField(
        widget=Select(
            choices=(
                ("all", _("Gender")),
                ("male", _("M")),
                ("female", _("F")),
            )
        )
    )
    gender.widget.attrs.update(
        {
            "name": "genderFilter",
            "id": "genderFilter",
        }
    )

    def __init__(self, *args, **kwargs):
        super(genderFilterForm, self).__init__(*args, **kwargs)
        self.fields["gender"].label = ""


# Subscribe for the newsletter form


class SubscribeForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        label=_(""),
        widget=forms.TextInput(attrs={"placeholder": _("Email")}),
    )
    name = forms.CharField(
        required=True,
        label=_(""),
        widget=forms.TextInput(attrs={"placeholder": _("Name")}),
    )

    class Meta:
        model = NewsletterSubscriber
        fields = "__all__"
