import typing
import subprocess, re


def ping_command():
    res = subprocess.run("ping google.com", capture_output=True)
    str_res = res.stdout.decode('utf-8')
    str_pattern = r'Sent = ([0-9]*).*Received = ([0-9]*).*Lost = ([0-9]*).*Minimum = ([0-9]*).*Maximum = ([0-9]*)'
    search_res = re.search(str_pattern, str_res, re.DOTALL)
    Sent, Received, Lost, Minimum, Maximum = search_res.groups()
    print("Sent = {}, Received = {}, Lost = {}\nMinimum = {}, Maximum = {}".format(
        Sent, Received, Lost, Minimum, Maximum
    ))


def get_russion_cell_phones(input_list: typing.List) -> typing.List:
    rus_cell_phone_template = r'[(\+7)9].*'
    for number in input_list:
        res = re.match(rus_cell_phone_template, number)
        if res:
            print("Yes")
        else:
            print("No")


def my_decorator(f):
    def decorated_function(*args, **kwargs):
        res = f(*args, **kwargs)
        return res + 5
    return decorated_function

# @my_decorator
# def my_function(i: int):
#     return i ** 3 + i ** 2

res_list = list()


class My_class_decorator(object):
    def __init__(self, n):
        #global res_list
        self.n = n
        self.i = 0
        self.res_list = [0 for i in range(n)]

    def __call__(self, f):

        def wrapped_func(*args, **kwargs):
            #global res_list
            res = f(*args, **kwargs)
            if self.i == self.n:
                self.i = 0
            self.res_list[self.i] = res
            self.i += 1
            return res
        return wrapped_func

    def get_values(self):
        return self.res_list


# @My_class_decorator(5)
def my_function(j: int):
    return j ** 3 + j ** 2

dec_class = My_class_decorator(5)

wrapped_func = dec_class(my_function)



for i in range(10):
    wrapped_func(i)

print(dec_class.res_list)
















number_list = [
                "+79236765O97",
                 "89136645101",
                 "83812640423",
                 "8(904)541-02-03",
                 "+1(555)345-11-21",
                 "+8(3812) 360-263",
                 "904-333-22-12",
                 "9333026455"
                ]

#get_russion_cell_phones(number_list)