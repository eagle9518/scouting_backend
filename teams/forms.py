from crispy_forms.layout import Submit
from django import forms
from crispy_forms.helper import FormHelper

DEMO_CHOICES =(
    ("1", "Swerve"),
    ("2", "Westcoast"),
    ("3", "Hybrid"),
    ("4", "Hightide"),
)


class NewPitScoutingData(forms.Form):
    drivetrain = forms.ChoiceField(choices=DEMO_CHOICES)
    weight = forms.CharField(max_length=32)
    width = forms.CharField(max_length=32)
    length = forms.CharField(max_length=32)
    comments = forms.CharField(max_length=512)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit'))
