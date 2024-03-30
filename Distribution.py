def pos_Comb():
    dist = {}
    for dA in range(1, 7):
        for dB in range(1, 7):
            total_Comb = dA + dB
            if total_Comb not in dist:
                dist[total_Comb] = []
            dist[total_Comb].append((dA, dB))
    return dist

result = pos_Comb()
for key, value in result.items():
    print(f"Sum {key}: {value}")