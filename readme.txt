api/articles/ :  list of articles
api/articles/?status=d&author=pk : filter by status d= draft and p= publish and also by author primary key
...................................................
api/users/  :  list of users
api/users/?search=reza : shearch by name and email address
api/users/?ordering=is_active  ~is_active:for people who active their account via email.
				~is_admin:for students admin.
				~is_staff : for school emploeis.
api/users/<pk>/  : for one user