# default argument
# default argument is used when the value is not passed by the user then default is used on that place.


# def default_arg(first_name,last_name,age):
#     print(f"your first name {first_name} last name {last_name} and age is {age}")  # simply func define
# default_arg("waseem"," tahir",24)


def default_arg1(first_name,last_name='unknown',age=None):        # remember always the default name should be at last
    print(f"your first name is {first_name} last_name is {last_name} age is {age}")          # other wise it generate error.

default_arg1('waseem',23)



   