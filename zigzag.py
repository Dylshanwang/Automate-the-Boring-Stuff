import time, sys
import random as rand

indent = 20


def zig():
    global indent
    try:
        if indent <= 20:
            print(' ' * indent, end='')
            print('********')
            indent += rand.randint(0, 10)
            time.sleep(0.1)
            zig()
        if indent > 20:
            print(' ' * indent, end='')
            print('********')
            indent -= rand.randint(0, 10)
            time.sleep(0.1)
            zig()
    except KeyboardInterrupt:
        sys.exit()


zig()
