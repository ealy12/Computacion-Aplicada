# Dado tres numeros indica si son o no consecutivos

import os;os.system('cls')
print('Dame 3 numeros para saber si son consecutivos ')
n1, n2, n3 = int(input()), int(input()), int(input())
if n2 - n1 == 1 and n3 - n2 == 1:
    print('\nSi son numeros consecutivos\n')
  
else:
    print('\nNo son numeros consecutivos\n')    