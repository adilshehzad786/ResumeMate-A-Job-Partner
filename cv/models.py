from django.conf import settings
from django.db import models
from django.urls import reverse
from PIL import Image
from django.core.validators import FileExtensionValidator
# Create your models here.

User = settings.AUTH_USER_MODEL


class PersonalInfo(models.Model):
    GENDER_CHOICE = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    tagline = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="i.e: Web Developer"
        )


    gender = models.CharField(max_length=6, choices=GENDER_CHOICE)
    nationality = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=14, null=True, blank=True)
    email = models.EmailField()

    address = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=100)
    facebook=models.URLField(null=True, blank=True)
    linkedin=models.URLField(null=True, blank=True)
    twitter=models.URLField(null=True, blank=True)

    language = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text="Sparate languages by comma"
        )

    interest = models.CharField(
        max_length=400,
        null=True,
        blank=True,
        help_text="Sparate interests by comma"
        )
    skills= models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Skills of Web Development , Doctor or any field Related"
    )


    skills_one = models.CharField(
        max_length=400,
        null=True,
        blank=True,
        help_text="You Can Add 4 Skills"
        )
    skills_one_percentage = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Use  %  Sign at End"
    )
    skills_two = models.CharField(
        max_length=400,
        null=True,
        blank=True,
        help_text="You Can Add 4 Skills"
    )
    skills_two_percentage = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Use  % Sign at End"
    )
    skills_three = models.CharField(
        max_length=400,
        null=True,
        blank=True,
        help_text="You Can Add 4 Skills"
    )
    skills_three_percentage = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Use  % Sign at End"
    )
    skills_four = models.CharField(
        max_length=400,
        null=True,
        blank=True,
        help_text="You Can Add 4 Skills"
    )
    skills_four_percentage = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Use  % Sign at End"
    )

    bio = models.TextField(help_text="Invite Your Friend And Get 1 Premium Bio Template For Free ")
    happy_client=models.IntegerField(default=1)
    telephonic_talk=models.IntegerField(default=0)
    total_projects=models.IntegerField(default=0)
    photo_capture=models.IntegerField(default=0,blank=True,help_text="Hobby")
    banner_picture_1 = models.ImageField(
        upload_to='profile_pics',
        null=True,
        blank=True,
        height_field="height_field",
        width_field="width_field",
    help_text = "Please Use 3046 x 4733 For Banner Picture Which Makes Your Resume Attractive  "
        )

    height_field = models.IntegerField(
        default=1200,
        null=True,
        blank=True,
        )

    width_field = models.IntegerField(
        default=800,
        null=True,
        blank=True,
        )



    def __str__(self):
        return str(self.user.username)

    def get_update_url(self):
        return reverse("update_personal_info", kwargs={"pk": self.pk})

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)


class WorkExperience(models.Model):

    user = models.ForeignKey(User, related_name="works",on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    joining_year = models.DateField()
    job_description = models.TextField()

    round_cirlce_picture = models.ImageField(
        upload_to='profile_pics',
        null=True,
        blank=True,
        height_field="height_field",
        width_field="width_field"
    )

    height_field = models.IntegerField(
        default=1200,
        null=True,
        blank=True,
    )

    width_field = models.IntegerField(
        default=800,
        null=True,
        blank=True,
    )
    resume_upload = models.FileField(upload_to='profile_pics',null=False,help_text="Please Upload Your Resume Otherwise Your Profile Will Not be Created",blank=False,validators=[
        FileExtensionValidator(['pdf', 'docx', 'doc'])])

    def get_delete_url(self):
        return reverse("delete_work_experience", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("update_work_experience", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.user.username)


class Education(models.Model):
    user = models.ForeignKey(User, related_name="educations",on_delete=models.CASCADE)
    institute_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    year = models.DateField()
    description = models.TextField()

    def get_delete_url(self):
        return reverse("delete_education", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("update_education", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.user.username)

class Project_detail(models.Model):
    user = models.ForeignKey(User, related_name="projects", on_delete=models.CASCADE)
    project_name=models.CharField(max_length=60)
    project_image=models.ImageField(
        upload_to='profile_pics',
        null=True,
        blank=True,
        height_field="height_field",
        width_field="width_field"
        )
    project_year = models.DateField()
    project_url=models.URLField(unique=True,blank=True,null=True,help_text="Enter Youtube URL")
    project_description = models.TextField()

    def get_delete_url(self):
        return reverse("delete_project", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("update_project", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.user.username)

    @property
    def get_photo_url(self):
        if self.project_image and hasattr(self.project_image, 'url'):
            return self.project_image.url
        else:
            return "/media/default.png"

class Contact_info(models.Model):
    user = models.ForeignKey(User, related_name="contactform", on_delete=models.CASCADE)
    gform_link=models.URLField(blank=True,unique=True,null=True,help_text="GForm Provided Free Contact Email Service So Please Watch Tutorial From Main Page to Implamenet on Your Profile")

    def get_delete_url(self):
        return reverse("delete_gform_link", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("update_gform_link", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.user.username)
