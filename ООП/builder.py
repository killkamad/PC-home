# Пример 1

# class Singleton:
#    __instance = None
#    @staticmethod
#    def getInstance():
#       """ Static access method. """
#       if Singleton.__instance == None:
#          Singleton()
#       return Singleton.__instance
#    def __init__(self):
#       """ Virtually private constructor. """
#       if Singleton.__instance != None:
#          raise Exception("This class is a singleton!")
#       else:
#          Singleton.__instance = self
#
# s = Singleton()
# print (s)
#
# s = Singleton.getInstance()
# print (s)
#
# s = Singleton.getInstance()
# print (s)
# print("--------------------------------")







# Пример 2

class OneOnly:
    singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls.singleton:
            cls.singleton = object.__new__(OneOnly)
        return cls.singleton

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)


if __name__ == "__main__":
    test1 = OneOnly("DAdaDada")
    # k=OneOnly(['da',1,3])
    if OneOnly.singleton:
        test2 = OneOnly.singleton
    else:
        test2 = OneOnly("NeNeNeene")
assert test1 == test2
print("test1.name: ", test1.name)
print("test2.name: ", test2.name)
# print("test2.name: ", test3.name)
# test1.print_name()










# Пример 3
# def singleton(class_):
#     instances = {}
#     def getinstance(*args, **kwargs):
#         if class_ not in instances:
#             instances[class_] = class_(*args, **kwargs)
#         return instances[class_]
#     return getinstance
#
# @singleton
# class MyClass(BaseClass):
#     pass
#
# class Singleton(object):
#     _instance = None
#     def __new__(class_, *args, **kwargs):
#         if not isinstance(class_._instance, class_):
#             class_._instance = object.__new__(class_, *args, **kwargs)
#         return class_._instance
#
# class MyClass(Singleton, BaseClass):
#     pass


# Пример 4
# class SingleTone(object):
#     __instance = None
#     def __new__(cls, val):
#         if SingleTone.__instance is None:
#             SingleTone.__instance = object.__new__(cls)
#         SingleTone.__instance.val = val
#         return SingleTone.__instance