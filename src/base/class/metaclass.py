# 应用场景：当你需要创建具有特殊行为或结构的类时，比如实现单例模式的类，元类会很有用。
class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['new_attribute'] = 'this is a new attribute'
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass = MyMeta):
    pass

object = MyClass()
print(object.new_attribute)

