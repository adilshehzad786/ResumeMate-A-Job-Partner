from django.conf.urls import url

from .views import (
    cv_detail_view,
    create_personal_info,
    update_personal_info,
    create_work_experience,
    create_education,
    update_work_experience,
    update_education,
create_project,delete_project,update_project,
    delete_work_experience,
    delete_education,template_view,pricing,feedback,contactme,share_resume,create_gform_link,update_gform_link,delete_gform_link,tutorial
    )
from django.urls import path
urlpatterns = [
    url(r'^create/personal_info/$',
        create_personal_info,
        name='create_personal_info'
        ),
    url(r'^update/personal_info/(?P<pk>\d+)/$',
        update_personal_info,
        name='update_personal_info'
        ),
    url(r'^create/work_experience/$',
        create_work_experience,
        name='create_work_experience'
        ),
    url(r'^update/work_experience/(?P<pk>\d+)/$',
        update_work_experience,
        name='update_work_experience'
        ),
    url(r'^delete/work_experience/(?P<pk>\d+)/$',
        delete_work_experience,
        name='delete_work_experience'),
    url(r'^create/education/$',
        create_education,
        name='create_education'
        ),
    url(r'^update/education/(?P<pk>\d+)/$',
        update_education,
        name='update_education'
        ),
    url(r'^delete/education/(?P<pk>\d+)/$',
        delete_education,
        name='delete_education'
        ),
url(r'^create/project/$',
        create_project,
        name='create_project'
        ),
    url(r'^update/project/(?P<pk>\d+)/$',
        update_project,
        name='update_project'
        ),
    url(r'^delete/project/(?P<pk>\d+)/$',
        delete_project,
        name='delete_project'
        ),
url(r'^create/gform/$',
        create_gform_link,
        name='create_gform_link'
        ),
    url(r'^update/gform/(?P<pk>\d+)/$',
        update_gform_link,
        name='update_gform_link'
        ),
    url(r'^delete/gform/(?P<pk>\d+)/$',
        delete_gform_link,
        name='delete_gform_link'
        ),

    url(r'^(?P<username>[\w._-]+)/$',
        cv_detail_view,
        name='cv_detail'
        ),


    path('template_view',template_view,name='template_view'),
    path('pricing',pricing,name='pricing_page'),
    path('feedback',feedback,name='feedback'),
path('contact',contactme,name='contactme'),
    path('share_resume',share_resume,name='share_resume'),
    path('tutorial',tutorial,name='tutorial'),


]