

data = {
    'alice': [
        'first_blood',
        'pixel_perfect',
        'speed_runner',
        'first_blood',
        'first_blood',
    ],
    'bob': [
        'level_master',
        'boss_hunter',
        'treasure_seeker',
        'level_master',
        'level_master',
    ],
    'charlie': [
        'treasure_seeker',
        'boss_hunter',
        'combo_king',
        'first_blood',
        'boss_hunter',
        'first_blood',
        'boss_hunter',
        'first_blood',
    ],
    'diana': [
        'first_blood',
        'combo_king',
        'level_master',
        'treasure_seeker',
        'speed_runner',
        'combo_king',
        'combo_king',
        'level_master',
    ],
    'eve': [
        'level_master',
        'treasure_seeker',
        'first_blood',
        'treasure_seeker',
        'first_blood',
        'treasure_seeker',
    ],
    'frank': [
        'explorer',
        'boss_hunter',
        'first_blood',
        'explorer',
        'first_blood',
        'boss_hunter',
    ],
}

alice = { 
    'first_blood',
    'pixel_perfect',
    'speed_runner',
    'first_blood',
    'first_blood',
}
bob = { 
        'level_master',
        'boss_hunter',
        'treasure_seeker',
        'level_master',
        'level_master',
}
charlie = { 
        'treasure_seeker',
        'boss_hunter',
        'combo_king',
        'first_blood',
        'boss_hunter',
        'first_blood',
        'boss_hunter',
        'first_blood',
}



unique = set()

unique = unique.union(set(charlie)).union(set(charlie)).union(set(charlie))
print(unique)


# unique = []
# for player, achievements in data.items():
#     for achievements in data[player]:
#     	unique.append(achievements)
    
    
# unique_ach = (unique)
# # unique_ach = unique_ach.union(unique_ach)
# print(f"Unique achievements across all players: {unique}")
    
# # add b to add and the duplicate will be removed means if there is two same items will add just one
# print(A | B) # {'collector', 'level_10', 'first_kill', 'speed_demon', 'boss_slayer'}
# print(A.union(B)) # {'collector', 'level_10', 'first_kill', 'speed_demon', 'boss_slayer'}

# print(A & B) # the element that is in both A and B ==> {'level_10'}
# print(A.intersection(B)) # the element that is in both A and B ==> {'level_10'}

# print(A - B) # elements in A but not in B | {'boss_slayer', 'collector'}
# print(A.difference(B)) # elements in A but not in B | {'boss_slayer', 'collector'}

# print(A ^ B) # elements that is in A but not in B and in B but not in A => element that is not in both of them
# print(A.symmetric_difference(B)) # elements that is in A but not in B and in B but not in A => element that is not in both of them