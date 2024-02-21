from crispy_forms.layout import Submit, Layout, Row
from django import forms
from crispy_forms.helper import FormHelper

# ChoiceField must be tuple - (Data, Display)
from teams.models import Human_Player_Match

DRIVETRAINS = (
    ("Swerve", "Swerve"),
    ("WestCoast", "WestCoast"))

INTAKE_LOCATION = (
    ("Source", "Source"),
    ("Ground", "Ground"))

SCORING_LOCATION = (
    ("Speaker", "Speaker"),
    ("Amp", "Amp"),
    ("Trap", "Trap"),
    ("None of the above :(", "None of the above :("))


class NewPitScoutingData(forms.Form):
    drivetrain = forms.ChoiceField(choices=DRIVETRAINS,
                                   widget=forms.RadioSelect)
    weight = forms.IntegerField()
    length = forms.IntegerField()
    width = forms.IntegerField()
    intake_location = forms.ChoiceField(choices=INTAKE_LOCATION,
                                        widget=forms.RadioSelect)
    scoring_locations = forms.MultipleChoiceField(choices=SCORING_LOCATION,
                                                  widget=forms.CheckboxSelectMultiple)
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
            'intake_location',
            'scoring_locations',
            'robot_picture',
            'additional_info',
            Submit('submit', 'Submit'))


class NewHumanScoutingData(forms.ModelForm):
    class Meta:
        model = Human_Player_Match
        fields = ["match_number", "human_player_timing", "human_player_spotlit", "strategist_name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['human_player_timing'].widget.attrs['min'] = 0
        self.fields['human_player_timing'].widget.attrs['max'] = 5

        self.fields['human_player_spotlit'].widget.attrs['min'] = 0
        self.fields['human_player_spotlit'].widget.attrs['max'] = 3

        self.helper = FormHelper()
        self.helper.attrs = {"novalidate": ''}
        self.helper.layout = Layout(
            'match_number',
            'human_player_timing',
            'human_player_spotlit',
            'strategist_name',
            Submit('submit', 'Submit'))
