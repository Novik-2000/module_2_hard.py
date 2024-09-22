

for n in range(3, 21):
    for j in range(1, 21):
        for k in range (1, 21):
             if n % sum([j] + [k]) == 0:
               print( f' { j } +  { k } = {n} , {n % (j + k)} '),
             else:
                 continue
