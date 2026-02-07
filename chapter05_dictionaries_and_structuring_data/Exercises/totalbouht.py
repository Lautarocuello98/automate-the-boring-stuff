all_guest = {'alice': {'apples': 5, 'pretzels': 12},
             'bob': {'ham sandwiches': 3, 'apples': 2},
             'carol': {'cups': 3, 'apple pie': 1}}


def total_brought(guests, item):
    num_brought = 0
    for k, v in guests.items():
        num_brought = num_brought + v.get(item, 0)
    return num_brought

print("number of things being brought: ")
print(f"- apples:   {str(total_brought(all_guest, 'apples'))}")
print(f"- pretzels: {str(total_brought(all_guest, 'pretzels'))}")
print(f"- cakes:    {str(total_brought(all_guest, 'cakes'))}")
print(f"- cups:     {str(total_brought(all_guest, 'cups'))}")