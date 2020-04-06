
def RemoveDuplicates(a_list): 
    final_list = [] 
    for item in a_list: 
        if item not in final_list: 
            final_list.append(item) 
    return final_list 
      
a_list = [10, 12, 14, 14, 16, 28, 28, 30]
a_list = RemoveDuplicates(a_list)
print(RemoveDuplicates(a_list)) 

def sortList(a_list):
  m = len(a_list)
  for i in range(m-1):
      for j in range(m , i+1):
           if a_list[j] > a_list[i]:
            a_list[j],a_list[i] = a_list[i],a_list[j]
  return a_list

print(sortList(a_list))         

def Remove(a_dict):
  final_dict={}
  for key,item in a_dict.items():
    if item not in final_dict.values():
       final_dict[key] = item
  return final_dict

a_dict= {"a":10, "b":12, "c":14, "d":14, "e":16, "f":28, "g":28, "h":30}
a_dict = Remove(a_dict)
print(Remove(a_dict))


   