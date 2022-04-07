from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    #list, create
    def has_permission(self, request, view):
        print(SAFE_METHODS)
        print(request.user)
        print(request.user.is_authenticated)
        print(request.user.is_staff)
        if request.method == 'GET':
            return True
        return request.user.is_authenticated and request.user.is_staff

    #delete put retrive
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_staff


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(dir(obj))
        return request.user.is_authenticated and (request.user == obj.owner or request.user.is_staff)


