from crispy_forms.layout import Submit, Layout, Row
from django import forms
from crispy_forms.helper import FormHelper

# ChoiceField must be tuple - (Data, Display)
DRIVETRAINS = (
    ("Swerve", "Swerve"),
    ("WestCoast", "WestCoast"),
    ("Logan", "Logan"),
    ("Wong", "Wong"),
)


class NewPitScoutingData(forms.Form):
    drivetrain = forms.ChoiceField(choices=DRIVETRAINS)
    weight = forms.IntegerField()
    length = forms.IntegerField()
    width = forms.IntegerField()
    robot_picture = forms.ImageField()
    additional_info = forms.CharField(max_length=512)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.attrs = {"novalidate": ''}
        self.helper.layout = Layout(
            'drivetrain',
            'weight',
            'length',
            'width',
            'robot_picture',
            'additional_info',
            FormHelper(),
            Submit('submit', 'Submit'))
