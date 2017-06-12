
class MyDescriptor():
    """
    A simple descriptor"
    """

    def __init__(self, init_val=None, name='myvar'):
        self.var_name = name
        self.value = init_val

    def __get__(self, obj, objtype):
        print('Getting', self.var_name)
        return self.value

    def __set__(self, obj, value):
        msg = 'setting {name} to {value}'
        print(msg.format(name=self.var_name, value=value))
        self.value = value


class MyClass():
    desc = MyDescriptor(init_val='This', name='description')
    normal = 10

if __name__ == '__main__':
    c = MyClass()
    print(c.desc)
    print(c.normal)
    c.desc = 100
    print(c.desc)
