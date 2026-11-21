# kwargs
# **kwargs

# def kw(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# kw( name='waseem',last_name='bai')


# def kw2(**kwargs2):
#     for l,m in kwargs2.items():
#         print(f"{l}:{m}")
# kw2(f_name='waseem',l_name='bai')


# dictionary unpacking

def kw3(**kwargs3):
    for l,m in kwargs3.items():
        print(f"{l}:{m}")
e={'first_name':' waseem','last_name':' bai'}
kw3(**e)
