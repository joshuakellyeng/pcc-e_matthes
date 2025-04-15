# USING get() TO ACCESS VALUES
alien_0 = {'color': 'green', 'speed': 'slow'}
# This gets a traceback error if no key by that name exists
# print(alien_0['points'])
# for better error handling use the get method like so
# .get(key, what to return if no value exists)
point_value = alien_0.get('points', 'No point value assigned.')
# print(point_value)
