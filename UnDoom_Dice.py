
import itertools
# Define the ranges
range1 = range(1,5)
range2 = range(11,0,-1)
def total_Comb(N_dice):
    N_faces = 6
    Total_Comb = pow(N_faces, N_dice)
    return Total_Comb
def pos_Comb(a,b):
    dist = []
    for dA in a:
        for dB in b:
            total_Comb = dA + dB
            if total_Comb not in dist:
                dist.append(total_Comb)
    return dist
def check(l):
    l=sorted(l)
    a=2
    for i in range(11):
        if l[i]!=a:
            return False
        a+=1
    return True
def prob_Sum():
    dist = {}
    l=[]
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
        Tot=f"{Tot:.2f}"
        l.append(Tot)
    return l

def newSum(a,b):
    dist = {}
    l=[]
    for die_A in a:
        for die_B in b:
            total_Sum = die_A + die_B
            if total_Sum not in dist:
                dist[total_Sum] = 1
            else:
                dist[total_Sum] += 1
    Total_Comb = total_Comb(2)
    d=dict(sorted(dist.items()))
    for Sum in d:
        Tot = (d[Sum]) / 36
        Tot=f"{Tot:.2f}"
        l.append(Tot)
    return l
# Generate all possible combinations of the two ranges
c = itertools.product(range1, repeat=6)
b=itertools.combinations(range2,6)
c=list(c)[::-1]
b=list(b)[::-1]
for i in c:
    for j in b:
        f=0
        i=list(i)
        j=list(j)
        if max(i)+max(j)==12:
            l=pos_Comb(i,j)
            if check(l):
                new=newSum(i,j)
                old=prob_Sum()
                for k in range(6):
                    if new[k]!=old[k]:
                        break
                    else:
                        f+=1
                if f==6:
                    print([i,j])
                    quit()
