data = {
    'alice': [
        'first_blood',
        'speed_runner',
        'pixel_perfect',
        'first_blood',
        'pixel_perfect',
        'first_blood',
    ],
    'bob': [
        'mounire',
        'first_blood',
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


def Tracker(data):
    print("=== Achievement Tracker System ===\n")
    unique_achievements = set()
    all_common = None
    # all_unique = None
    for player, achivement in data.items():
        # for player, achivement in data.items():
        print(f"Player {player} achievements: {set(achivement)}")
        # for ach in achivement:
        unique_achievements = unique_achievements.union(achivement)
        
        # for common achievements:
        if (all_common is None):
            all_common = set(achivement)
        else:
            all_common = all_common.intersection(set(achivement))
        # for items that owned by one player and not owned by another player:
        # if (all_unique is None):
        #     all_unique = set(achivement)
        # else:
        #     all_unique = all_unique.difference(set(achivement))
        #     # unique = unique.difference(all_unique)
        #     # final_unique = final_unique.union(unique)
    print()
    print("=== Achievement Analytics ===")

    print(f"All unique achievements unlocked: {unique_achievements}")
    print(f"Total unique achievements unlocked: {len(unique_achievements)}\n")
    
    print(f"Common to all players: {all_common}")
    # print(f"Rare achievements (1 player):  {all_unique}")


        
Tracker(data)



