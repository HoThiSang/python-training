def find_captains_room(k, room_numbers):
    room_count = {}
    for room in room_numbers:
        room_count[room] = room_count.get(room, 0) + 1
    
    for room, count in room_count.items():
        if count != k:
            return room

k = int(input())
room_numbers = list(map(int, input().split()))
print(find_captains_room(k, room_numbers))