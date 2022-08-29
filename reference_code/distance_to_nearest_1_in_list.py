def calc(lst):

    # initialize the distances to infinity
    distances = [float('inf')] * len(lst)

    # loop over the list twice, once from the left and once from the right
    for indices in [range(len(lst)), range(len(lst)-1, -1, -1)]:
        # keep track of the distance to the last seen non-zero value
        distance = float('inf')

        for i in indices:
            # when we find a non-zero value, set the distance to 0
            if lst[i] != 0:
                distance = 0

            distances[i] = min(distances[i], distance)

            # with each step we take, increase the distance by 1
            distance += 1

    return distances

blocks = [{"gym": False, "school": True, "store": False},
{"gym": True, "school": False, "store": False},
{"gym": True, "school": True, "store": False},
{"gym": False, "school": True, "store": False},
{"gym": False, "school": True, "store": True}]

gym_list = []
school_list = []
store_list = []

max_index = len(blocks)

for block in blocks:

    if block["gym"] == True:
        gym_list.append(1)
    else:
        gym_list.append(0)
    if block["school"] == True:
        school_list.append(1)
    else:
        school_list.append(0)
    if block["store"] == True:
        store_list.append(1)
    else:
        store_list.append(0)

print(gym_list)
print(school_list)
print(store_list)

gym_dist = calc(gym_list)
school_dist = calc(school_list)
store_dist = calc(store_list)

print(gym_dist)
print(school_dist)
print(store_dist)

building_rating = []
for i in range(max_index):
    # i is the block of a particular building
    local_dist = []
    local_dist.append(gym_dist[i])
    local_dist.append(school_dist[i])
    local_dist.append(store_dist[i])
    building_rating.append(max(local_dist))

print(building_rating)