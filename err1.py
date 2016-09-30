def foo(s):
    n = int(s)
    assert n != 0,"n is zero!"
    return 10 / n
def main():
    foo(0)
main()
# import os
# os.system(" python errLogging.py >> logging1.txt 2>&1")