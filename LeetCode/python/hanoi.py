#coding=utf-8

def one_move(n, from_p, via_p, to_p):
    if n == 0:
        return

    one_move(n - 1, from_p, to_p, via_p)
    print "move %s from %s to %s" % (n, from_p, to_p)
    one_move(n - 1, via_p, from_p, to_p)

if __name__ == "__main__":
    n = 3
    one_move(n, "a", "b", "c")