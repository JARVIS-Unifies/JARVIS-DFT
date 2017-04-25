def merge(lsts):
  sets = [set(lst) for lst in lsts if lst]
  merged = 1
  while merged:
    merged = 0
    results = []
    while sets:
      common, rest = sets[0], sets[1:]
      sets = []
      for x in rest:
        if x.isdisjoint(common):
          sets.append(x)
        else:
          merged = 1
          common |= x
      results.append(common)
    sets = results
  return sets

lst = [[65, 17, 5, 30, 79, 56, 48, 62],
       [6, 97, 32, 93, 55, 14, 70, 32],
       [75, 37, 83, 34, 9, 19, 14, 64],
       [43, 71],
       [],
       [89, 49, 1, 30, 28, 3, 63],
       [35, 21, 68, 94, 57, 94, 9, 3],
       [16],
       [29, 9, 97, 43],
       [17, 63, 24]]
print merge(lst)
