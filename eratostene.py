def crivello_di_eratostene(n):
    if n < 2:
        return []   
    primi = []
    veri = [True] * (n + 1)

    veri[0] = veri[1] = False
    for i in range(2, n + 1):
        if veri[i]:
            primi.append(i)
            for j in range(i * i, n + 1, i):
                veri[j] = False
    return primi

n = 20

print(crivello_di_eratostene(n))






