# github_api

- To get a token
POST api/v1/signup/ 
	{"email":"jason.5001001@gmail.com", "password":"password"}

- To get a list of repos of the organization
GET api/v1/repos/<org_name>/
	header: token:<token>

- To add a repo to the organization
POST api/v1/repos/<org_name>/
	header: token:<token>
	{"repo_name":"Sub repo", "private":true}

- To get a list of teams of the organization
GET api/v1/teams/<org_name>/
	header: token:<token>

- To add a team to the organization
POST api/v1/teams/<org_name>/
	header: token:<token>
	{"team_name":"Sub team", "privacy": "closed"}

- To get a list of members of the team in the organization
GET api/v1/members/<org_name>/<team_id>/	
	header: token:<token>

- To add a member to a team in the organization
POST api/v1/members/<org_name>/<team_id>/
	header: token:<token>
	{"member_login":"234234", "action":"invite"}

- To remove a member to a team in the organization
POST api/v1/members/<org_name>/<team_id>/
	header: token:<token>
	{"member_login":"234234", "action":"remove"}

- To assign a repo to a team
POST api/v1/assign_repo/<org_name>/<team_id>/
	header: token:<token>
	{"repo_name":"Sub-repo", "permission": "admin"}
