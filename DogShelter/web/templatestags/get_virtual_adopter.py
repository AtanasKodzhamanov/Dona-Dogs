from django import template 

register = template.Library()

@register.filter(name="virtual_adopter")
def get_adopter(id, dataP):
    return dataP["id"==id]["fields"]["person_name_eng"]


#not in use