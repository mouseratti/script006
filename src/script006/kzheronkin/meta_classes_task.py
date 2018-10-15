
def repr(this): return "object of {}".format(this.__class__)


class MetaClassForUpperCase(type):

    def __new__(mcs, name, inheritance, props):
        for prop in props:
            if prop[0:2] != "__":
                props[str.upper(prop)] = props.pop(prop)
        new_class = super().__new__(mcs, name, inheritance, props)
        return new_class


class B(object, metaclass= MetaClassForUpperCase):

    prop1 ="prop1"

    def __repr__(self):
        return "instance of {} with id {}".format(self.__class__, id(self))

    def __init__(self):
        self.sailor = "Long John"
        self.doctor = "Doctor Livesley"


def fake_init(object):
    print("The new lord object has arrived.")


if __name__ == '__main__':
    b = B()
    c = MetaClassForUpperCase("C", (), {"__init__": fake_init, "__repr__": repr, "abc": "my_abc"})

    c_object = c()

