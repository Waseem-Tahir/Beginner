# store the user key values in key using dictionary
user=['name','class','fav-movies','fav-songs']
dic=dict()
# print("please if you type more option then write in this format [a,b,c]")
for i in user:
    if i=='fav-movies':
      s=input(f"enter you {i} : ")
      dic[i]=[s]
    elif i=='fav-songs':
      s=input(f"enter you {i} : ")
      dic[i]=[s]
    else:
      s=input(f"enter your {i} : ")
      dic[i]=s
    # print(i)
    
     
    
        
    
print(dic)
print(type(dic))
di=dic.pop('fav-songs')
print(type(di))




    