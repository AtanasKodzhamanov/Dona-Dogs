from django.test import TestCase
from DogShelter.web.models import Dog, NoticeBoard, About

# Print to console the number of dogs in the shelter
print("There are " + str(len(Dog)) + " dogs in the shelter.")
# Check if they all have a description in english
for dog in Dog:
    if dog.description_eng == "":
        print("Dog " + dog.name_eng + " has no description in english.")
# Check if they all have a description in bulgarian
for dog in Dog:
    if dog.description_bg == "":
        print("Dog " + dog.name_eng + " has no description in bulgarian.")
