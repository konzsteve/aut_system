from django import forms
from .models import *
from account.forms import FormSettings


class VoterForm(FormSettings):
    class Meta:
        model = Voter
        fields = ['phone']


class PositionForm(FormSettings):
    class Meta:
        model = Position
        fields = ['name', 'max_vote']


class CandidateForm(FormSettings):
    class Meta:
        model = Candidate
        fields = ['fullname', 'bio', 'position', 'photo']

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageOTP
        fields = ["otp_image"]
    
