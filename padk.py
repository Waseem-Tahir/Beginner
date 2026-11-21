# PADK FORMULA
# paramater  ,  argument   ,  default parameter   ,  kwards
def padk(name,*args,defau_name="unkown",**kwards):                # Note( in padk order to maintain order necessary
    print(name)                                                   #      for args need to remember that argument should be
    print(args)                                                   #      tuple or at calling to write * other wise error
    print(defau_name)                                             #      list etc not acceptable.
    print(kwards)
padk('waseem bai',1,2,3,f_name='waseem',l_name='bai')



def padk2(name,*args,defau_name="unkown",**kwards):               
    print(name)                                                   
    print(args)                                                   
    print(defau_name)                                             
    print(kwards)
padk2('maisum',1,2,3,f_name='waseem',l_name='bai')