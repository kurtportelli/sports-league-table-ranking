def compute_ranks(number, games):
    #initializing the lists
    points = [0] * number
    goal_diff = [0] * number
    goals_for = [0] * number
            
    #computing the lists
    for game in games:
        if game[2] > game[3]:
            points[game[0]] += 2
        elif game[3] > game[2]:
            points[game[1]] += 2
        else:
            points[game[0]] += 1
            points[game[1]] += 1
        
        goal_diff[game[0]] += game[2] - game[3]
        goal_diff[game[1]] += game[3] - game[2]
        
        goals_for[game[0]] += game[2]
        goals_for[game[1]] += game[3]
    
    #sorting the lists
    from operator import itemgetter
    sorted_lists = list(zip(range(number), points, goal_diff, goals_for))
    sorted_lists.sort(key = itemgetter(1, 2, 3), reverse=True)
    
    #determining the positions
    positions = [0] * number
    pos = 1
    positions[sorted_lists[0][0]] = 1
    for i in range(1, number):
        if sorted_lists[i][1:] != sorted_lists[i-1][1:]:
            pos = i + 1
        positions[sorted_lists[i][0]] = pos
    
    return positions
