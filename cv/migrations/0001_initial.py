# Generated by Django 2.2.6 on 2020-01-20 12:53

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('joining_year', models.DateField()),
                ('job_description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='works', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=60)),
                ('project_image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='profile_pics', width_field='width_field')),
                ('project_year', models.DateField()),
                ('project_url', models.URLField(blank=True, help_text='Enter Youtube URL', null=True, unique=True)),
                ('project_description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('tagline', models.CharField(blank=True, help_text='i.e: Web Developer', max_length=50, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('nationality', models.CharField(max_length=50)),
                ('contact_no', models.CharField(blank=True, max_length=14, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(max_length=100)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('language', models.CharField(blank=True, help_text='Sparate languages by comma', max_length=200, null=True)),
                ('interest', models.CharField(blank=True, help_text='Sparate interests by comma', max_length=400, null=True)),
                ('skills', models.CharField(blank=True, help_text='Skills of Web Development , Doctor or any field Related', max_length=100, null=True)),
                ('skills_one', models.CharField(blank=True, help_text='You Can Add 4 Skills', max_length=400, null=True)),
                ('skills_one_percentage', models.CharField(blank=True, help_text='Use  %  Sign at End', max_length=100, null=True)),
                ('skills_two', models.CharField(blank=True, help_text='You Can Add 4 Skills', max_length=400, null=True)),
                ('skills_two_percentage', models.CharField(blank=True, help_text='Use  % Sign at End', max_length=100, null=True)),
                ('skills_three', models.CharField(blank=True, help_text='You Can Add 4 Skills', max_length=400, null=True)),
                ('skills_three_percentage', models.CharField(blank=True, help_text='Use  % Sign at End', max_length=100, null=True)),
                ('skills_four', models.CharField(blank=True, help_text='You Can Add 4 Skills', max_length=400, null=True)),
                ('skills_four_percentage', models.CharField(blank=True, help_text='Use  % Sign at End', max_length=100, null=True)),
                ('bio', models.TextField(help_text='Invite Your Friend And Get 1 Premium Bio Template For Free ')),
                ('happy_client', models.IntegerField(default=1)),
                ('telephonic_talk', models.IntegerField(default=0)),
                ('total_projects', models.IntegerField(default=0)),
                ('photo_capture', models.IntegerField(blank=True, default=0, help_text='Hobby')),
                ('banner_picture_1', models.ImageField(blank=True, height_field='height_field', help_text='Please Use 3046 x 4733 For Banner Picture Which Makes Your Resume Attractive  ', null=True, upload_to='profile_pics', width_field='width_field')),
                ('banner_picture_2', models.ImageField(blank=True, height_field='height_field', help_text='Please Use 3046 x 4733 For Banner Picture Which Makes Your Resume Attractive  ', null=True, upload_to='profile_pics', width_field='width_field')),
                ('round_cirlce_picture', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='profile_pics', width_field='width_field')),
                ('height_field', models.IntegerField(blank=True, default=1200, null=True)),
                ('width_field', models.IntegerField(blank=True, default=800, null=True)),
                ('resume_upload', models.FileField(help_text='Please Upload Your Resume Otherwise Your Profile Will Not be Created', upload_to='profile_pics', validators=[django.core.validators.FileExtensionValidator(['pdf', 'docx', 'doc'])])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute_name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('year', models.DateField()),
                ('description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contact_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gform_link', models.URLField(blank=True, help_text='GForm Provided Free Contact Email Service So Please Watch Tutorial From Main Page to Implamenet on Your Profile', null=True, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contactform', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
