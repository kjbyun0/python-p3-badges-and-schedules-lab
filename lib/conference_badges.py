def badge_maker(name):
    return str(f'Hello, my name is {name}.')

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]
    # badges = []
    # for name in names:
    #     badges.append(badge_maker(name))
    # return badges

def assign_rooms(names):
    room_assignments = []
    for i in range(len(names)):
        room_assignments.append(f"Hello, {names[i]}! You'll be assigned to room {i+1}!")
    return room_assignments

def printer(names):
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)

    room_assignments = assign_rooms(names)
    for room_assignment in room_assignments:
        print(room_assignment)
