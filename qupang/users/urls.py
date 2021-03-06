from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("explore/", view=views.ExploreUsers.as_view(), name="explore_users"),
    path("<int:user_id>/follow", view=views.FollowUser.as_view(), name="follow_user"),
    path("<int:user_id>/unfollow", view=views.UnFollowUser.as_view(), name="unfollow_user"),
    path("search/", view=views.Search.as_view(), name="search_user"),
    path("<str:username>/", view=views.UserProfile.as_view(), name="user_profile"),
    path("<str:username>/followers", view=views.UserFollowers.as_view(), name="user_followers"),
    path("<str:username>/followings", view=views.UserFollowing.as_view(), name="user_followings"),
    path("<str:username>/password", view=views.ChangePassword.as_view(), name="change_password"),
]
