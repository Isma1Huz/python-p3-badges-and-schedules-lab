def badge_maker(name):
    return (f"Hello, my name is {name}.")

def batch_badge_creator(names):
    badge_messages = []
    for name in names:
        badge_messages.append("Hello, my name is {}.".format(name))
    return badge_messages

def assign_rooms(names):
    badge_messages = []
    rooms = range(1, 8)  # Assuming you have 7 rooms (room numbers 1-7)
    
    for i, name in enumerate(names):
        if i < len(rooms):
            room_number = rooms[i]
            badge_messages.append(f"Hello, {name}! You'll be assigned to room {room_number}!")
            return badge_messages
    room_assignments = assign_rooms(speakers)
    for assignment in room_assignments:
        return assignment
    
speakers = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"]

def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)
    
    for badge in badges:
        print(badge)
    
    for assignment in room_assignments:
        print(assignment)