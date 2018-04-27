def create_groups(items, num_groups):
    try:

        size = len(items) // num_groups
    except ZeroDivisionError:
        print('Warning : Returning empty list. Please user a nonzero number.')
        return []
    else:
        groups = []
        for i in range(0, len(items), size):
            groups.append(items[i:i + size])

        return groups
    finally:
        print("{} groups returned.".format(num_groups))

print("Creating 6 groups...")
for group in create_groups(range(32), 6):
    print(list(group))

print("\nCreating 1 groups...")
for group in create_groups(range(32), 1):
    print(list(group))