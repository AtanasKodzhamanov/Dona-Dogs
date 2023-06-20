from django.db import models
from django.forms import CharField, EmailField
from django.utils.timezone import now
from django.template.defaultfilters import slugify

import datetime

from DogShelter.web.validators import validate_bulgarian, validate_english, validate_url

MAX_URL_LENGTH = 300
NAME_MAX_LENGTH = 60
ORDER = 99
EMAIL_MAX_LENGTH = 60
SUBJECT_MAX_LENGTH = 60
MESSAGE_MAX_LENGTH = 1000

# Help text is provided for the Bulgarian speaking admin staff.


class Dog(models.Model):

    """

    This model represents a dog. 
    It stores information about a dog, such as its name, gender, and status.
    It is the core model of the application.

    """

    def __str__(self):
        return self.name_eng

    OPTIONS_CHOICES = [(x, x) for x in ("Y", "N", "Unknown")]
    GENDER_CHOICES = [(x, x) for x in ("F", "M")]
    STATUS_CHOICES = [(x, x)
                      for x in ("Active", "New", "Dead", "Adopted", "Sick")]

    DEFAULT_UNKNOWN_YEAR = 0
    DOG_STATUS_LENGTH = 10
    GENDER_MAX_LENGTH = 7
    DISEASES_MAX_LENGTH = 7
    DEFAULT_STATUS = "New"

    # Fields(Columns)

    name_eng = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True,
        null=True,
        help_text="Име на куче на Английски.",
        validators=[validate_english]
    )
    name_bg = models.CharField(
        max_length=NAME_MAX_LENGTH,
        default="",
        help_text="Име на куче на Български.",
        validators=[validate_bulgarian]
    )

    va_name_eng = models.CharField(
        max_length=NAME_MAX_LENGTH,
        default="",
        blank=True,
        help_text="Име на виртуален осиновител на Английски.",
        validators=[validate_english]
    )
    va_name_bg = models.CharField(
        max_length=NAME_MAX_LENGTH,
        default="",
        blank=True,
        help_text="Име на виртуален осиновител на Български.",
        validators=[validate_bulgarian]
    )

    # Chronic
    diseases = models.CharField(
        max_length=DISEASES_MAX_LENGTH,
        choices=OPTIONS_CHOICES,
        default="",
        help_text="Флаг за хронични болести, например сляпота, трудно-подвижност..."
    )

    gender = models.CharField(
        max_length=GENDER_MAX_LENGTH,
        choices=GENDER_CHOICES,
        default="",
        help_text="Пол на куче."
    )

    profile_pic = models.URLField(
        null=True,
        max_length=MAX_URL_LENGTH,
        help_text="Профилна снимка.",
        validators=[validate_url]
    )

    pic_2 = models.URLField(
        blank=True,
        max_length=MAX_URL_LENGTH,
        default="",
        help_text="Албумна снимка.",
        validators=[validate_url]
    )

    pic_3 = models.URLField(
        blank=True,
        max_length=MAX_URL_LENGTH,
        default="",
        help_text="Албумна снимка.",
        validators=[validate_url]
    )

    pic_4 = models.URLField(
        blank=True,
        max_length=MAX_URL_LENGTH,
        default="",
        help_text="Албумна снимка.",
        validators=[validate_url]
    )

    pic_5 = models.URLField(
        blank=True,
        max_length=MAX_URL_LENGTH,
        default="",
        help_text="Албумна снимка.",
        validators=[validate_url]
    )

    pic_6 = models.URLField(
        blank=True,
        max_length=MAX_URL_LENGTH,
        default="",
        help_text="Албумна снимка.",
        validators=[validate_url]
    )

    # If alive, adopted or sick. If alive keep in the gallery, if adopted send put it inside the adoption page, if sick put at the top of the gallery.
    status = models.CharField(
        max_length=DOG_STATUS_LENGTH,
        blank=True,
        choices=STATUS_CHOICES,
        default=DEFAULT_STATUS,
        help_text="Статус на кучето: Активно, Починало, Осиновено, Болно. Активните кучета ще се показват в началната страница. Болните в страницата на клиниката. Осиновените в страницата за осиновяване. Починалите не се показват никъде. ДА СЕ ПОПЪЛВА НА ВРЕМЕ СЪГЛАСУВАНО СЪС СТАТУСА ВЪВ ФЕЙСБУК!"
    )

    story_eng = models.TextField(
        blank=True,
        default="",
        help_text="История на кучето на Английски.",
        validators=[validate_english]
    )
    story_bg = models.TextField(
        blank=True,
        default="",
        help_text="История на кучето на Български.",
        validators=[validate_bulgarian]
    )

    arrival_year = models.IntegerField(
        blank=True,
        default=DEFAULT_UNKNOWN_YEAR,
        help_text="Година на пристигане на кучето."
    )

    adoption_country_eng = models.CharField(
        max_length=NAME_MAX_LENGTH,
        blank=True,
        default="",
        help_text="Държава на осиновяване на Английски.",
        validators=[validate_english]
    )

    adoption_country_bg = models.CharField(
        max_length=NAME_MAX_LENGTH,
        blank=True,
        default="",
        help_text="Държава на осиновяване на Български.",
        validators=[validate_bulgarian]
    )

    adoption_year = models.IntegerField(
        blank=True,
        default=DEFAULT_UNKNOWN_YEAR,
        help_text="Година на осиновяване (ако е осиновено)."
    )

    adoption_pic_after_1 = models.URLField(
        blank=True,
        max_length=MAX_URL_LENGTH,
        default="",
        help_text="Снимка 1 на кучето след осиновяване.",
        validators=[validate_url]
    )

    adoption_pic_after_2 = models.URLField(
        blank=True,
        max_length=MAX_URL_LENGTH,
        default="",
        help_text="Снимка 2 на кучето след осиновяване.",
        validators=[validate_url]
    )

    adoption_pic_after_3 = models.URLField(
        blank=True,
        max_length=MAX_URL_LENGTH,
        default="",
        help_text="Снимка 3 на кучето след осиновяване.",
        validators=[validate_url]
    )

    adoption_story_eng = models.TextField(
        blank=True,
        default="",
        help_text="История на осиновяване на кучето на Английски.",
        validators=[validate_english]
    )
    adoption_story_bg = models.TextField(
        blank=True,
        default="",
        help_text="История на осиновяване на кучето на Български.",
        validators=[validate_bulgarian]
    )

    # slug = models.SlugField(
    #     null=False,
    #     blank=True
    # )

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     if not self.slug:
    #         self.slug = slugify(f"{self.name_eng}--{self.pk}")
    #     return super().save(*args, **kwargs)

    class Meta:
        ordering = ('-pk',)


class NoticeBoard(models.Model):

    """

    This model represents a notice board. It allows the user to post a notice on the website.
    The notice can be applied to any of the main pages in the website by specifying the location.
    It can also support up to two pictures. The user can also choose to order the notice in relation to other notices.
    The notice will be displayed in the order of the "order" field.

    This model is essentially used to display short/quick messages on the website such as:
    "Please visit us this Sunday", or "Check out our new dog, Bob".

    """

    class Meta:
        verbose_name_plural = "Notice Board Posts"

    def __str__(self):
        return self.note_eng

    LOCATION_CHOICES = [(x, x) for x in ("Gallery", "About", "Infirmary",
                                         "Adoptions", "Donations", "Home")]
    FLEX_DIRECTION_CHOICES = [
        ('row', 'Row'),
        ('row-reverse', 'Row Reverse'),
        ('column', 'Column'),
        ('column-reverse', 'Column Reverse'),
    ]
    LOCATION_LENGTH = 25
    DEFAULT_LOCATION = "About"
    MAX_TITLE_LENGTH = 100

    note_eng = models.TextField(
        blank=True,
        default="",
        help_text="Съобщение на Английски.",
        validators=[validate_english]
    )

    note_bg = models.TextField(
        blank=True,
        default="",
        help_text="Съобщение на Български.",
        validators=[validate_bulgarian]
    )

    note_pic_1 = models.URLField(
        max_length=MAX_URL_LENGTH,
        blank=True,
        default="",
        help_text="Снимка 1 в съобщението (не задължителни).",
        validators=[validate_url]
    )

    note_pic_2 = models.URLField(
        max_length=MAX_URL_LENGTH,
        blank=True,
        default="",
        help_text="Снимка 2 в съобщението (не задължителни).",
        validators=[validate_url]
    )

    note_video = models.URLField(
        max_length=MAX_URL_LENGTH,
        blank=True,
        default="",
        help_text="Видео линк",
        validators=[validate_url]
    )

    flex_direction = models.CharField(
        max_length=15,
        choices=FLEX_DIRECTION_CHOICES,
        default='row',
        help_text='Flexbox direction options',
    )

    order = models.IntegerField(
        default=ORDER,
        help_text="Подредба на съобщението. По подразбиране е 99. Стойност по-малка от 99 ще покаже съобщението по-нагоре."
    )

    location = models.CharField(
        max_length=LOCATION_LENGTH,
        blank=True,
        choices=LOCATION_CHOICES,
        default=DEFAULT_LOCATION,
        help_text="Място на съобщението - всяка страница разполага със способност за съобщения."
    )

    section_title_eng = models.TextField(
        max_length=MAX_TITLE_LENGTH,
        blank=True,
        help_text="Заглавие на секцията на Английски. Не е задължително.",
        validators=[validate_english]
    )

    section_title_bg = models.TextField(
        max_length=MAX_TITLE_LENGTH,
        blank=True,
        help_text="Заглавие на секцията на Български. Не е задължително.",
        validators=[validate_bulgarian]
    )

    visible = models.BooleanField(
        default=True,
        help_text="Скриване или показване на публикацията. Показва се по подразбиране."
    )

# class AboutPhoto(models.Model):
#     """

#     To store an unlimited amount of photos for each section in About model.

#     """
#     url = models.URLField(
#         max_length=MAX_URL_LENGTH,
#         validators=[validate_url]
#         )


class LongPost(models.Model):

    """

    This model is used to create larger sections with more content than a typical notice.
    Similar to the notice board, the user can specify the location of the section.

    """

    class Meta:
        verbose_name_plural = "Long Posts"

    def __str__(self):
        return self.section_title_eng

    LOCATION = [(x, x) for x in ("Gallery", "About", "Infirmary",
                                 "Adoptions", "Donations", "Home")]

    MAX_TITLE_LENGTH = 100
    MAX_LOCATION_LENGTH = 25
    DEFAULT_ENGLISH_DESC = "Info coming soon..."
    DEFAULT_LOCATON = "Donations"

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        blank=True,
        choices=LOCATION,
        default=DEFAULT_LOCATON,
        help_text="Място на секцията - всяка страница разполага със способност за секции."
    )

    section_desc_eng = models.TextField(
        blank=True,
        default=DEFAULT_ENGLISH_DESC,
        help_text="Описание на секцията на Английски.",
        validators=[validate_english]
    )

    section_desc_bg = models.TextField(
        blank=True,
        default="",
        help_text="Описание на секцията на Български.",
        validators=[validate_bulgarian]
    )

    about_pic_1 = models.URLField(
        max_length=MAX_URL_LENGTH,
        blank=True,
        default="",
        help_text="Снимка 1 в секцията.",
        validators=[validate_url]
    )

    about_pic_2 = models.URLField(
        max_length=MAX_URL_LENGTH,
        blank=True,
        default="",
        help_text="Снимка 2 в секцията.",
        validators=[validate_url]
    )

    about_pic_3 = models.URLField(
        max_length=MAX_URL_LENGTH,
        blank=True,
        default="",
        help_text="Снимка 3 в секцията.",
        validators=[validate_url]
    )

    about_pic_4 = models.URLField(
        max_length=MAX_URL_LENGTH,
        blank=True,
        default="",
        help_text="Снимка 4 в секцията.",
        validators=[validate_url]
    )

    about_pic_5 = models.URLField(
        max_length=MAX_URL_LENGTH,
        blank=True,
        default="",
        help_text="Снимка 5 в секцията.",
        validators=[validate_url]
    )

    about_pic_6 = models.URLField(
        max_length=MAX_URL_LENGTH,
        blank=True,
        default="",
        help_text="Снимка 6 в секцията.",
        validators=[validate_url]
    )

    about_pic_7 = models.URLField(
        max_length=MAX_URL_LENGTH,
        blank=True,
        default="",
        help_text="Снимка 7 в секцията.",
        validators=[validate_url]
    )

    about_pic_8 = models.URLField(
        max_length=MAX_URL_LENGTH,
        blank=True,
        default="",
        help_text="Снимка 8 в секцията.",
        validators=[validate_url]
    )

    about_pic_9 = models.URLField(
        max_length=MAX_URL_LENGTH,
        blank=True,
        default="",
        help_text="Снимка 9 в секцията.",
        validators=[validate_url]
    )

    about_pic_10 = models.URLField(
        max_length=MAX_URL_LENGTH,
        blank=True,
        default="",
        help_text="Снимка 10 в секцията.",
        validators=[validate_url]
    )

    order = models.IntegerField(
        default=ORDER,
        help_text="Подредба на секцията в страницата. 1 е първата, 2 е втората и т.н"
    )

    section_title_eng = models.TextField(
        max_length=MAX_TITLE_LENGTH,
        help_text="Заглавие на секцията на Английски.",
        validators=[validate_english]
    )

    section_title_bg = models.TextField(
        max_length=MAX_TITLE_LENGTH,
        help_text="Заглавие на секцията на Български.",
        validators=[validate_bulgarian]
    )

    text_color = models.CharField(
        max_length=7,
        blank=True,
        help_text="Въведете шестнадесетичен код на цвета, за да промените цвета на текста (#414141)."
    )

    title_color = models.CharField(
        max_length=7,
        blank=True,
        help_text="Въведете шестнадесетичен код на цвета, за да промените цвета на заглавието (#414141)."
    )

    background_color = models.CharField(
        max_length=7,
        blank=True,
        help_text="Въведете шестнадесетичен код на цвета, за да промените цвета на контейнера (#F5F5F5)."
    )

    text_align = models.CharField(
        max_length=6,
        choices=[('left', 'Left'), ('center', 'Center'), ('right', 'Right')],
        default='left',
        help_text="Изберете подравняването на текста за известието. Ляво, дясно или централно."
    )

    text_position = models.CharField(
        max_length=6,
        choices=[('top', 'Top'), ('bottom', 'Bottom')],
        default='top',
        help_text="Изберете позицията на текста в контейнера. Горе или долу."
    )

    visible = models.BooleanField(
        default=True,
        help_text="Скриване или показване на публикацията. Показва се по подразбиране."
    )

    # photos = models.ManyToManyField(AboutPhoto)

# The following is used to get the last day of the previous month for the "last_month" variable.
# This is used to set the default value for the "date_of_donation" field in the donations models.
# Donations are added to the database on the first day of the month, so the default value for the "date_of_donation" field is the last day of the previous month.


today = datetime.date.today()
first = today.replace(day=1)
last_month = first - datetime.timedelta(days=1)


class Donation(models.Model):

    """

    This model is used to keep track of donations made to the shelter.
    The list of people is then published every month. 

    """

    def __str__(self):
        return "--".format(self.person_name_eng, self.date)

    date = models.DateField(
        blank=True,
        default=last_month,
        help_text="Дата на дарението. По подразбиране е последният ден на предходния месец. Например ако дарението е направено на 1.01.2020, то по подразбиране ще се показва на 31.12.2019. Това е за да се показват даренията в последния месец."
    )

    person_name_eng = models.CharField(
        max_length=NAME_MAX_LENGTH,
        default="",
        help_text="Име на дарителя на Английски.",
        validators=[validate_english]
    )
    person_name_bg = models.CharField(
        max_length=NAME_MAX_LENGTH,
        default="",
        help_text="Име на дарителя на Български.",
        validators=[validate_bulgarian]
    )


class NewsletterSubscriber(models.Model):
    email = models.EmailField(
        max_length=EMAIL_MAX_LENGTH
    )
    name = models.CharField(
        max_length=NAME_MAX_LENGTH
    )


class ContactFormModel(models.Model):
    class Meta:
        verbose_name_plural = "User messages"

    email = models.EmailField(
        max_length=EMAIL_MAX_LENGTH
    )
    name = models.CharField(
        max_length=NAME_MAX_LENGTH
    )
    subject = models.TextField(
        max_length=SUBJECT_MAX_LENGTH
    )
    message = models.TextField(
        max_length=MESSAGE_MAX_LENGTH
    )


class AdoptionForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    dog = models.CharField(max_length=255)


class DonationStory(models.Model):

    """

    This model will be used to create more notable donations that can be displayed on the home page. For example, if someone donates a large amount of food, or if someone donates equipment, or volunteers etc. There is a separate section for these donations. The donations will be refreshed every month and past donations will go to archive.

    """

    class Meta:
        verbose_name_plural = "DonationStories"

    MAX_TITLE_LENGTH = 100

    title_eng = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        default="",
        help_text="Заглавие на дарението на Английски.",
        validators=[validate_english]
    )

    title_bg = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        default="",
        help_text="Заглавие на дарението на Български.",
        validators=[validate_bulgarian]
    )

    donation_text_eng = models.TextField(
        blank=True,
        default="",
        help_text="Текст на дарението на Английски (за секцията със снимки на дарания).",
        validators=[validate_english]
    )

    donation_text_bg = models.TextField(
        blank=True,
        default="",
        help_text="Текст на дарението на Български (за секцията със снимки на дарания).",
        validators=[validate_bulgarian]
    )
    date = models.DateField(
        blank=True,
        default=last_month,
        help_text="Дата на дарението. По подразбиране е последният ден на предходния месец. Например ако дарението е направено на 1.01.2020, то по подразбиране ще се показва на 31.12.2019. Това е за да се показват даренията в последния месец."
    )

    date_pk = models.CharField(
        max_length=8,
        blank=True,
        editable=False
    )

    # This is a custom save method that will save the date in a format that can be used as a primary key - 2022-Dec
    def save(self, *args, **kwargs):
        self.date_pk = self.date.strftime("%Y-%b")
        super().save(*args, **kwargs)

    donation_pic_1 = models.URLField(
        max_length=MAX_URL_LENGTH,
        blank=True,
        default="",
        help_text="Снимка 1 в секцията.",
        validators=[validate_url]
    )

    donation_pic_2 = models.URLField(
        max_length=MAX_URL_LENGTH,
        blank=True,
        default="",
        help_text="Снимка 2 в секцията.",
        validators=[validate_url]
    )

    donation_pic_3 = models.URLField(
        max_length=MAX_URL_LENGTH,
        blank=True,
        default="",
        help_text="Снимка 3 в секцията.",
        validators=[validate_url]
    )

    donation_pic_4 = models.URLField(
        max_length=MAX_URL_LENGTH,
        blank=True,
        default="",
        help_text="Снимка 4 в секцията.",
        validators=[validate_url]
    )

    donation_pic_5 = models.URLField(
        max_length=MAX_URL_LENGTH,
        blank=True,
        default="",
        help_text="Снимка 4 в секцията.",
        validators=[validate_url]
    )

    donation_pic_6 = models.URLField(
        max_length=MAX_URL_LENGTH,
        blank=True,
        default="",
        help_text="Снимка 4 в секцията.",
        validators=[validate_url]
    )

    priority = models.CharField(
        choices=[('low', 'Low'), ('high', 'High')],
        default='low',
        max_length=6,
        help_text="Приоритетът ще определя сортирането на донациите и дизайнът на това как се показват. low е нисък, high е висок.",
    )
