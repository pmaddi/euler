'''

15=mod7 1
20=mod7 6
35=mod7 0

'''
base = 7
last_row_mod = [1]
for i in range(160):
  # print(str(last_row_mod), i)
  print(''.join([' ' if x == 0 else '■' for x in last_row_mod]), i)
  nxt = [1]
  for idx in range(len(last_row_mod) - 1):
    val = last_row_mod[idx] + last_row_mod[idx + 1]
    # nxt.append(val)
    nxt.append(val % base)
  nxt.append(1)
  last_row_mod = nxt


      
