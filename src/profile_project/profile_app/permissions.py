from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    #allows users to edit only their own profile

    def has_object_permission(self, request, view, obj):

        #check user trying to edit profile

        if request.method in permissions.SAFE_METHODS:

            return True

        return obj.id == request.user.id

class PostOwnStatus(permissions.BasePermission):
    #allows users to updata only their own status

    def has_object_permission(self, request, view, obj):

        #check user trying to edit their own status

        if request.method in permissions.SAFE_METHODS:

            return True

        return obj.user_profile.id == request.user.id
