from django import forms


from .models import PersonalInfo, WorkExperience, Education,Project_detail,Contact_info
from django.forms.widgets import SelectDateWidget

class PersonalInfoForm(forms.ModelForm):



    class Meta:
        model = PersonalInfo
        fields = [
            "first_name",
            "last_name",

            "skills",

            "gender",
            "nationality",
            "contact_no",
            "email",

            "address",
            "country",
            "language",
            "skills_one",
            "skills_one_percentage",

            "skills_two",
            "skills_two_percentage",
            "skills_three",
            "skills_three_percentage",
            "skills_four",
            "skills_four_percentage",
            "happy_client",
            'telephonic_talk',
            'photo_capture',
            'total_projects',
            "interest",
            "bio",
            "banner_picture_1",



            ]


class WorkExperienceForm(forms.ModelForm):
    joining_year = forms.DateField(
        widget=SelectDateWidget(years=range(2000, 2020))
    )


    class Meta:
        model = WorkExperience
        fields = [
            "company_name",
            "job_title",
            "joining_year",
            "job_description",
            "round_cirlce_picture",
            "resume_upload",
            ]


class EducationForm(forms.ModelForm):
    year = forms.DateField(widget=SelectDateWidget(years=range(2000, 2018)))

    class Meta:
        model = Education
        fields = [
            "institute_name",
            "subject",
            "year",
            "description"
            ]

class ProjectForm(forms.ModelForm):
    project_year= forms.DateField(widget=SelectDateWidget(years=range(2000, 2020)))

    class Meta:
        model = Project_detail
        fields = [
            "project_name",
            "project_url",
            "project_image",
            "project_description",
            "project_year",

            ]
class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact_info
        fields = [
            "gform_link",
            ]