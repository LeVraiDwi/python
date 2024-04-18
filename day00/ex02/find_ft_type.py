def all_thing_is_obj(object: any) -> int:
    if type(object) is str:
        print("%s is in the kitchen: %s" % (str(object), type(object)))
    elif type(object) is list:
        print("List : %s" % (type(object)))
    elif type(object) is tuple:
        print("Tuple : %s" % (type(object)))
    elif type(object) is set:
        print("Set : %s" % (type(object)))
    elif type(object) is dict:
        print("Dict : %s" % (type(object)))
    else:
        print("Type not found")
    return 42

