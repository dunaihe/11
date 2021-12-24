global a
a = 0

def function():
    global a
    a += 1
    return a

for realcallcount in range(1, 5):
    assert function() == realcallcount
