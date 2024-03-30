def total_Comb(N_dice):
    N_faces = 6
    Total_Comb = pow(N_faces, N_dice)
    return Total_Comb

def prob_Sum():
    dist = {}
    for die_A in range(1, 7):
        for die_B in range(1, 7):
            total_Sum = die_A + die_B
            if total_Sum not in dist:
                dist[total_Sum] = 1
            else:
                dist[total_Sum] += 1
    Total_Comb = total_Comb(2)
    for Sum in dist:
        Tot = (dist[Sum]) / Total_Comb
        print(f"Sum {Sum}: {dist[Sum]} / {Total_Comb} = {Tot:.2f}")

prob_Sum()