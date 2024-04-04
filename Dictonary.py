# Create a simple collection 
users = {'Hans': 'active', 'Eleonore': 'active', 'Ben': 'inactive'}

# Strategy: Iterate over a copy
for user, status in users.copy()
    if status =='inactive': 
        del users