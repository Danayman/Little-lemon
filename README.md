# LittleLemon
Meta Back-End Developer Capstone project: little lemon restaurant

API paths: 

admin/

auth/
auth/users/
auth/users/me/
auth/token/login/
auth/token/logout/

restaurant/

Requires Authentication (Token):

restaurant/booking/
restaurant/menu/

Token not required:

restaurant/menu/<id>

###############################

Changed urls.py to use DTL so that booking and menu links are accessible from the landing page.

###############################

Default database credentials and settings taken from the last course:

See settings.py