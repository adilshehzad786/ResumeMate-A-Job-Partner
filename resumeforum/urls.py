from django.urls import path


from .views.question import (IndexView, QuestionCreateView,
                             QuestionDeleteView, QuestionDetailView,
                             QuestionUpdateView, like_or_dislike_question,
                             mark_question_as_solved)
from resumeforum.views import question
from .views.replies import (ReplyDeleteView, ReplyUpdateView,
                            like_or_dislike_reply)
from .views.categories import CategoryDetailView
from resumeforum.views import compiler
from resumeforum.views import Tutorial
urlpatterns = [
    path('main/', question.index, name='homepage_black'),
    path('search', IndexView.as_view(), name='search'),
    path('new', QuestionCreateView.as_view(), name='new_question'),
    path('<slug:slug>', QuestionDetailView.as_view(), name='question'),
    path('<slug:slug>/edit', QuestionUpdateView.as_view(), name='update_question'),
    path('<slug:slug>/delete', QuestionDeleteView.as_view(), name='delete_question'),
    path('<int:id>/solved', mark_question_as_solved, name='solve_question'),
    path('categories/<slug:slug>', CategoryDetailView.as_view(), name='category'),
    path('<slug:slug>/replies/<int:pk>/edit',ReplyUpdateView.as_view(), name='update_reply'),
    path('<slug:slug>/replies/<int:pk>/delete', ReplyDeleteView.as_view(), name='delete_reply'),

    path('questions/<int:id>/like-or-dislike',like_or_dislike_question, name='like_dislike'),
    path('replies/<int:id>/like-or-dislike',like_or_dislike_reply, name='like_dislike'),
    path('compiler/',compiler.index,name='compiler_page'),
    path('tutorials/',Tutorial.home,name='Tutorial_page'),

]