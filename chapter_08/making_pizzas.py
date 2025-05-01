# Importing an Entire Module

# import pizza
# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing Specific Functions

# from pizza import make_pizza
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing Specific Functions - can add more specific functions with ','
# eg. from pizza import make_pizza, deliver_pizza, collect_payment

# Using 'as' to Give a Function an Alias
# The general syntax for providing an alias is: 
# `from module_name import function_name as fn`

# from pizza import make_pizza as mp
# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using as to Give a Module an Alias
# The general syntax for providing an alias is: 
# `import module_name as mn`

import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing All Functions in a Module
# You can tell python to import every function in a module by using the 
# asterisk(*) operator

# `from module_name import *`
# USE WITH CAUTION - best not to use when working with larger modules



