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
        return Response({'error': 'Please provide a valid email and password!'})

    try:
        user = User.objects.create(username=email, email=email)
        user.set_password(password)
        user.save()
    except Exception, e:
        return Response({'error': 'The user already exists!'})

    token = guser.create_authorization(["user", "repo", "admin:org"], "token for "+email).token
    GAuth.objects.create(user=user, token=token)

    return Response({"success": 1,
                     "token": token})


@api_view(["POST", "GET"])
def repos(request, org):
    token = request.META.get('HTTP_TOKEN')

    if not GAuth.objects.filter(token=token).exists():
        return Response({'error': 'Please provide a valid token!'})

    try:
        g = Github(token)
        org = g.get_organization(org)
    except Exception, e:
        return Response({'error': 'Please provide a valid organization!'})

    if request.method == "POST":        # create a repo
        try:
            repo_name = request.data.get('repo_name')
            repo = org.create_repo(repo_name)
        except Exception, e:
            return Response({'error': 'Please provide a valid repo name!'})

        return Response({"success": 1,
                         "id": repo.id})
    else:
        repos = [{"name": item.name, "id": item.id} for item in org.get_repos()]
        return Response({"success": 1,
                         "repos": repos})


@api_view(["POST", "GET"])
def teams(request, org):
    token = request.META.get('HTTP_TOKEN')

    if not GAuth.objects.filter(token=token).exists():
        return Response({'error': 'Please provide a valid token!'})

    try:
        g = Github(token)
        org = g.get_organization(org)
    except Exception, e:
        return Response({'error': 'Please provide a valid organization!'})

    if request.method == "POST":        # create a repo
        try:
            team_name = request.data.get('team_name')
            team = org.create_team(team_name)
        except Exception, e:
            return Response({'error': 'Please provide a valid team name!'})
            
        return Response({"success": 1,
                         "id": team.id})
    else:
        teams = [{"name": item.name, "id": item.id} for item in org.get_teams()]
        return Response({"success": 1,
                         "teams": teams})


@api_view(["POST", "GET"])
def members(request, org, team):
    token = request.META.get('HTTP_TOKEN')

    if not GAuth.objects.filter(token=token).exists():
        return Response({'error': 'Please provide a valid token!'})

    try:
        g = Github(token)
        org = g.get_organization(org)
    except Exception, e:
        return Response({'error': 'Please provide a valid organization!'})

    try:
        team = org.get_team(int(team))
    except Exception, e:
        return Response({'error': 'Please provide a valid team id!'})

    if request.method == "POST":        # create a repo
        try:
            member = g.get_user(request.data.get('member_login'))
        except Exception, e:
            return Response({'error': 'Please provide a valid member login!'})
            
        action = request.data.get('action')
        if action == 'remove':
            team.remove_from_members(member)
        else:
            team.add_membership(member)

        return Response({"success": 1})
    else:
        members = [{"login": item.login, "id": item.id} for item in team.get_members()]
        return Response({"success": 1,
                         "members": members})
