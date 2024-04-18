def NULL_not_found(object: any) -> int:
    if type(object) is type(None):
        print("Nothing: %s %s" % (str(object), type(object)))
    elif type(object) is float and object != object:
        print("Cheese: %s %s" % (str(object), type(object)))
    elif type(object) is int and not int(object):
        print("Zero: %s %s" % (str(object), type(object)))
    elif type(object) is str and not str(object):
        print("Empty:%s %s" % (str(object), type(object)))
    elif type(object) is bool and not bool(object):
        print("Fake: %s %s" % (str(object), type(object)))
    else:
        print("Type not Found")
    return 1