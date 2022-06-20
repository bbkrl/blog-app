from django.urls import path
from django.contrib.auth import views as auth_views


from . import views
from .views import UpdatePostView, activate, ResetPasswordView


urlpatterns = [
    #     blogs
    path("", views.blogs, name="blogs"),
    path("blog/<str:slug>/", views.blogs_comments, name="blogs_comments"),
    path("add_blogs/", views.add_blogs, name="add_blogs"),
    path("edit_blog_post/<str:slug>/", UpdatePostView.as_view(), name="edit_blog_post"),
    path("delete_blog_post/<str:slug>/", views.Delete_Blog_Post, name="delete_blog_post"),
    path("search/", views.search, name="search"),

    #     profile
    path("profile/", views.Profile, name="profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("user_profile/<int:myid>/", views.user_profile, name="user_profile"),

    #    user authentication
    path("register/", views.register, name="register"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
         activate, name='activate'),

    # reset password
    # path('password-reset/', ResetPasswordView.as_view(template_name='reset/password_reset.html)', name='password_reset')),
    # path('password-reset/', auth_views.PasswordResetView.as_view(template_name='reset/password_reset.html'),
    #      name='password_reset'),
    # path('password-reset-confirm/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(template_name='reset/password_reset_confirm.html'),
    #      name='password_reset_confirm'),
    # path('password-reset-complete/',
    #      auth_views.PasswordResetCompleteView.as_view(template_name='reset/password_reset_complete.html'),
    #      name='password_reset_complete'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='reset/password_reset.html'),
         name='password_reset'),
    path('password-reset-sent/', auth_views.PasswordResetDoneView.as_view(template_name='reset/password_reset_sent.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='reset/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='reset/password_reset_complete.html'),
         name='password_reset_complete'),

]
