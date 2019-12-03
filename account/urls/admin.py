from django.conf.urls import url

from ..views.admin import UserAdminAPI, GenerateUserAPI, GroupAPI, GroupUserAPI

urlpatterns = [
    url(r"^user/?$", UserAdminAPI.as_view(), name="user_admin_api"),
    url(r"^generate_user/?$", GenerateUserAPI.as_view(), name="generate_user_api"),
    url(r"^group/?$", GroupAPI.as_view(), name="group_api"),
    url(r"^group_user/?$", GroupUserAPI.as_view(), name="group_user_api"),
]
