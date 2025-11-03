def mode(numbers):
  dic = {}
  for num in numbers:
    if num in dic:
      dic[num] += 1
    else:
      dic[num] = 1

  mode_list = dic.values()
  mode = max(mode_list)
  for key, value in dic.items():
    if value == mode:
      return key
  
