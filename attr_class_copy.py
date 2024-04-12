class Building:
    total = 0

    def __init__(self):
        Building.total += 1

objects = []
while len(objects) < 40:
    new_object = Building()
    objects.append(new_object)
    print(new_object.total)
    print(f'{Building.total = }')


print(Building.__dict__)

