"""
Реализовать на python:
- генератор +
- декоратор +
- итератор +
- контекстный менеджер
"""
import socket


# generator
def simple_generator(dir_list: list) -> str:
    """Simple generator"""
    for sample in dir_list:
        yield sample.__doc__


local_dir = dir()
watch_locals = simple_generator(local_dir)
print(next(watch_locals))
print(next(watch_locals))

# wrapper
def decorator_function(func):
    """Translate string too Leet-string"""

    translate = {
        'A': "4", 'B': "8", 'C': "<", 'D': "|)", 'E': "3",
        'F': "|#", 'G': "[+", 'H': "#", 'I': "!", 'J': "_7",
        'K': "|{", 'L': "|_", 'M': "44", 'N': r"|\|", 'O': "0",
        'P': "|*", 'Q': "O_", 'R': "|2", 'S': "5", 'T': "`|`",
        'U': "|_|", 'V': r"\/", 'W': "VV", 'X': "%", 'Y': "¥", 'Z': "7_",
    }

    def wrapper(string: str):
        """wrapper function"""

        string = list(tuple(string))

        for count, value in enumerate(string):
            if value.isalpha():
                string[count] = translate[value.upper()]
        string = ''.join(string)

        func(string.center(100))
    return wrapper

@decorator_function
def crazy_strings(string):
    """test of wraper"""
    print(string)


STRING = "The quick brown fox jumps over the lazy dog."
print(crazy_strings(STRING))


class Iterator:
    """Simple iterator class"""

    def __init__(self, string):
        """Init"""
        self.string = string
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        """Realization of Next"""
        if self.counter >= len(self.string):
            raise StopIteration
        res = self.string[self.counter]
        self.counter += 1
        return res


simple = Iterator(STRING)
for i in simple:
    print(i)


class SocketConn:
    """Socket connection class"""

    def __init__(self, addr, port):
        """constructor"""
        self.port = port
        self.addr = addr
        self.sock = None

    def __enter__(self):
        """Open connection with socket"""
        self.sock = socket.socket()
        self.sock.connect((self.addr, self.port))
        return self.sock

    def send_msg(self, msg):
        """Send message"""
        self.sock.send(msg)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close connection"""
        self.sock.close()


# addr = 'localhost'
# port = 4242
# with SocketConn(addr, port) as conn:
#     send = conn.sendmsg(string)
