# 9.12 Multiple Modules
from exercises_09 import Admin

the_mentor = Admin('ogion', 'of roke', 'archmage', 'isle of roke')
the_mentor.privileges.privileges = ['protecting the isle of gont']
the_mentor.privileges.show_privileges()

