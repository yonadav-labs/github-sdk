from github import Github

from rest_framework.decorators import api_view
from rest_framework.response import Response

from gauth.models import *

@api_view(["POST"])
def signup(request):
    email = request.data.get('email', '')
    password = request.data.get('password', '')
    # first_name = request.data.get('first_name')
    # last_name = request.data.get('last_name')   

    try:
        g = Github(email, password)
        guser = g.get_user()
        email = guser.email
    except Exception, e:
        return Response({'error': 'Please provide valid email and password!'})

    user = User.objects.create(username=email, email=email)
    user.set_password(password)
    user.save()

    token = guser.create_authorization(["repo"], "Note created by GAuth").token
    GAuth.objects.create(user=user, token=token)

    return Response({"success": 1,
                     "token": token})