def tree(length=200):
    if length <= 10:
        fd(length)
        bk(length)
        return

    fd(length*3/8)

    rt(30)
    tree(length * 2/3)
    lt(30)

    fd(length/4)

    lt(35)
    tree(length * 3/4)
    rt(35)

    fd(length/8)

    rt(25)
    tree(length/2)
    lt(25)

    fd(length/4)

    bk(length)

lt(90)
speed(0)
tree()
done()