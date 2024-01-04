import time


def test_speed(loop_size, loop_count, operation):
    start = time.time()
    i = 0
    while i < loop_count:
        operation(loop_size, i)
        i += 1

    end = time.time()
    print(f"delta:{end - start}")


def test_while_loop(loop_size, id):
    i = 0
    while i < loop_size:
        id += 5
        i += 1
    return id


def test_for_loop(loop_size, id):
    for i in range(0, loop_size, 1):
        id += 5

    return id


test_speed(50000, 300, test_for_loop)
