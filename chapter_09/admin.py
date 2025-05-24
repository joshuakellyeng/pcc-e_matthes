# 9.11 Imported Admin
from exercises_09 import Admin

wizard_of_earthsea = Admin('ged', 'sparrowhawk', 'wizard', 'isle of gont')

wizard_of_earthsea.privileges.privileges = ['cast spells', 'sailing', 'knowing the true names of things', 'roke alumni']

wizard_of_earthsea.privileges.show_privileges()

