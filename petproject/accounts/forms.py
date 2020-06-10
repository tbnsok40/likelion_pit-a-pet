from django.forms import ModelForm
from .models import UserLocation, RegiProfile, PlusPhoto

class LocationForm(ModelForm):
    class Meta:
        model = UserLocation
        fields= ('ispermit',)


class ProfileCreationForm(ModelForm):
    class Meta:
        model = RegiProfile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProfileCreationForm, self).__init__(**kwargs)
        self.fields['pet_name'].widget.attrs.update({
            'class':"hello",
            'placeholder':'ex)김태훈'
        })


class PlusPhotoForm(ModelForm):
    class Meta:
        model = PlusPhoto
        fields = ('plus_image',)