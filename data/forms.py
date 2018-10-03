from django import forms
from .models import Data

class UserDataForm(forms.ModelForm):
	class Meta:
		model=Data
		fields={
		'name',
		'roll_no',
		}
