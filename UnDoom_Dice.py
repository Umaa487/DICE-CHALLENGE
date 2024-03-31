def unDoom():
    list1 = list(range(1, 5))
    list2 = list(range(1, 12))
    die_comb1 = []
    die_comb2 = []
    old_List = [0.0, 0.0, 0.027777777777777776, 0.05555555555555555, 0.08333333333333333, 0.1111111111111111, 0.1388888888888889, 0.16666666666666666, 0.1388888888888889, 0.1111111111111111, 0.08333333333333333, 0.05555555555555555, 0.027777777777777776]

    def total_comb(dice_A,dice_B):
         return len(dice_A)*len(dice_B)
         
    def comb_A(N,temp):
        if len(temp)==6:
            die_comb1.append(temp)
            return
        if N<0:
            return
        comb_A(N-1,temp+[list1[N]])
        comb_A(N-1,temp)

    def comb_B(N,temp):
        if len(temp)==6:
            die_comb2.append(temp)
            return
        if N<0:
            return
        comb_B(N-1,temp+[list2[N]])
        comb_B(N-1,temp)

    def pos_Dist(dice_A,dice_B):
        ans = [0 for i in range(max(dice_A)+max(dice_B)+1)]
        for i in dice_A:
            for j in dice_B:
                ans[i+j] += 1
        return ans
        
    def prob_Dice(dice_A,dice_B):
        if max(dice_A) + max(dice_B) == 12:
            dist = pos_Dist(dice_A,dice_B)
            ln = total_comb(dice_A,dice_B)
            for i in range(max(dice_A)+max(dice_B)+1):
                if dist[i]:
                    if old_List[i] != dist[i]/ln:
                        return False
            return True

        return False

    comb_A(len(list1) - 1, [])
    comb_B(len(list2) - 1, [])
    
    New_Dices = []

    for dice_A in die_comb1:
        for dice_B in die_comb2:
            if prob_Dice(dice_A, dice_B):
                New_Dices.append((dice_A, dice_B))
                
    return New_Dices

print(unDoom())