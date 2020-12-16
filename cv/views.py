from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from accounts.models import User
from .forms import PersonalInfoForm, WorkExperienceForm, EducationForm,ProjectForm,ContactForm
from .models import PersonalInfo, WorkExperience, Education,Project_detail,Contact_info


def cv_detail_view(request, username):
    user = get_object_or_404(User, username=username)
    try:
        personal_info = PersonalInfo.objects.get(user=user)

    except PersonalInfo.DoesNotExist:
        # if personal info doesn't exist redirect to create or 404 page.
        if user == request.user:
            return redirect("create_personal_info")
        else:
            raise Http404("CV Does Not Exist.")

    work_experience = WorkExperience.objects.filter(user=user)
    education = Education.objects.filter(user=user)
    project = Project_detail.objects.filter(user=user)
    contact=Contact_info.objects.filter(user=user)
    context = {
                "personal_info": personal_info,
                "work_experience": work_experience,
                "education": education,
                 "project": project,
                 "contact_info":contact,

              }

    return render(request, "cv/detail.html", context)


@login_required
def create_personal_info(request):
    try:
        # if personal_info exists user cannot create another one.
        info = PersonalInfo.objects.get(user=request.user)
        raise Http404
    except PersonalInfo.DoesNotExist:
        form = PersonalInfoForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            personal_info = form.save(commit=False)
            personal_info.user = request.user
            personal_info.save()
            return redirect("cv_detail", username=request.user.username)

        context = {
            "form": form,
            "title": "Create Personal Information",
        }

        return render(request, "cv/create.html", context)


@login_required
def update_personal_info(request, pk):
    instance = get_object_or_404(PersonalInfo, pk=pk)

    if not request.user == instance.user:
        raise Http404
    else:
        form = PersonalInfoForm(
            request.POST or None,
            request.FILES or None,
            instance=instance
        )

        if form.is_valid():
            personal_info = form.save(commit=False)
            personal_info.user = request.user
            personal_info.save()

        context = {
            "form": form,
            "title": "Update Personal Information",
        }

        return render(request, "cv/create.html", context)


@login_required
def create_work_experience(request):
    form = WorkExperienceForm(request.POST or None)

    if form.is_valid():
        work_experience = form.save(commit=False)
        work_experience.user = request.user
        work_experience.save()
        return redirect("cv_detail", username=request.user.username)

    context = {
        "form": form,
        "title": "Create Work Experiance",
    }

    return render(request, "cv/create.html", context)


@login_required
def update_work_experience(request, pk):
    instance = get_object_or_404(WorkExperience, pk=pk)

    if not request.user == instance.user:
        raise Http404
    else:
        form = WorkExperienceForm(request.POST or None, instance=instance)

        if form.is_valid():
            work_experience = form.save(commit=False)
            work_experience.user = request.user
            work_experience.save()
            return redirect("cv_detail", username=request.user.username)

        context = {
            "form": form,
            "title": "Update Work Experience",
        }

        return render(request, "cv/create.html", context)


@login_required
def delete_work_experience(request, pk):
    work_experience = get_object_or_404(WorkExperience, pk=pk)

    if not request.user == work_experience.user:
        raise Http404
    else:
        work_experience.delete()

        return redirect("cv_detail", username=request.user.username)


@login_required
def create_education(request):
    form = EducationForm(request.POST or None)

    if form.is_valid():
        education = form.save(commit=False)
        education.user = request.user
        education.save()
        return redirect("cv_detail", username=request.user.username)

    context = {
        "form": form,
        "title": "Create Educational Information",
    }

    return render(request, "cv/create.html", context)


@login_required
def update_education(request, pk):
    instance = get_object_or_404(Education, pk=pk)

    if not request.user == instance.user:
        raise Http404
    else:
        form = EducationForm(request.POST or None, instance=instance)

        if form.is_valid():
            education = form.save(commit=False)
            education.user = request.user
            education.save()
            return redirect("cv_detail", username=request.user.username)

        context = {
            "form": form,
            "title": "Update Educational Information",
        }

        return render(request, "cv/create.html", context)


@login_required
def delete_education(request, pk):
    education = get_object_or_404(Education, pk=pk)

    if not request.user == education.user:
        raise Http404
    else:
        education.delete()

        return redirect("cv_detail", username=request.user.username)

###########################
@login_required
def create_gform_link(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():

        contact = form.save(commit=False)
        contact.user = request.user
        contact.save()
        return redirect("cv_detail", username=request.user.username)

    context = {
        "form": form,
        "title": "Create Gform Link ",
    }

    return render(request, "cv/create.html", context)


@login_required
def update_gform_link(request, pk):
    instance = get_object_or_404(Contact_info, pk=pk)

    if not request.user == instance.user:
        raise Http404
    else:
        form = ContactForm(request.POST or None, instance=instance)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect("cv_detail", username=request.user.username)

        context = {
            "form": form,
            "title": "Update GForm Link ",
        }

        return render(request, "cv/create.html", context)


@login_required
def delete_gform_link(request, pk):
    project = get_object_or_404(Contact_info, pk=pk)

    if not request.user == project.user:
        raise Http404
    else:
        project.delete()

        return redirect("cv_detail", username=request.user.username)
########################
@login_required
def create_project(request):
    form = ProjectForm(request.POST or None)

    if form.is_valid():
        project = form.save(commit=False)
        project.user = request.user
        project.save()
        return redirect("cv_detail", username=request.user.username)

    context = {
        "form": form,
        "title": "Create Project Information",
    }

    return render(request, "cv/create.html", context)


@login_required
def update_project(request, pk):
    instance = get_object_or_404(Project_detail, pk=pk)

    if not request.user == instance.user:
        raise Http404
    else:
        form = ProjectForm(request.POST or None, instance=instance)

        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect("cv_detail", username=request.user.username)

        context = {
            "form": form,
            "title": "Update Project Informations ",
        }

        return render(request, "cv/create.html", context)


@login_required
def delete_project(request, pk):
    project = get_object_or_404(Project_detail, pk=pk)

    if not request.user == project.user:
        raise Http404
    else:
        project.delete()

        return redirect("cv_detail", username=request.user.username)

###############
def template_view(request):
    return render(request,'cv/Template Demo.html')
def pricing(request):
    return render(request,'cv/pricing.html')

def feedback(request):
    return render(request,'cv/feedback.html')

def contactme(request):
    return render(request,'cv/contactme.html')

def share_resume(request):
    return render(request,'cv/shareresume.html')
def tutorial(request):
    return render(request,'cv/tutorial.html')

