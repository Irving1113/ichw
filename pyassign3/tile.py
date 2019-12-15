def tile(k, a, b, m, n):
    """Returns: the numbers in one tile.

    Through this function, the user can know the whole numbers in a 
    tile if the smallest number in this tile is given. The value 
    returned represents the numbers which form the tile.

    The value returned has type tuple.

    Parameter k: the smallest number in a tile
    Precondition: k is a integer which ranges from 0 to n * m

    Parameter a: the length of the tiles
    Precondition: a is a integer given by the user

    Parameter b: the width of the tiles
    Precondition: b is a integer given by the user
    
    Parameter m: the length of the wall
    Precondition: m is a integer given by the user
    
    Parameter n: the width of the wall
    Precondition: n is a integer given by the user"""
    t = []
    if k <= m*(n-b+1)-a:
        for j in range(b):
            for i in range(a):
                t.append(k + j * m + i)
    return tuple(t)


def available(wall, a, b, m, n):
    """Returns: the smallest number in a tile which is available
    for tiling.

    Through this function, the user can know which place on the wall
    can be tiled. The value returned represents the smallest number in
    the available tile.

    The value returned has type integer.

    Parameter wall: the wall to be tiled
    Precondition: wall is a list which contains n * m zeros

    Parameter a: the length of the tiles
    Precondition: a is a integer given by the user

    Parameter b: the width of the tiles
    Precondition: b is a integer given by the user
    
    Parameter m: the length of the wall
    Precondition: m is a integer given by the user
    
    Parameter n: the width of the wall
    Precondition: n is a integer given by the user"""
    for i in range(m):
        for j in range(n):
            if wall[i][j] == 0:
                k = i + j * m
                return k


def test_tile(k, a, b, wall, m, n):
    """Returns: whether a tile can be placed on a certain place on
    the wall.

    Through this function, the user can know whether a certain place 
    on the wall can be placed. The value returned represents whether
    the tile can be placed.

    The value returned is True or False.

    Parameter k: the smallest number in a tile
    Precondition: k is a integer which ranges from 0 to n * m
    
    Parameter wall: the wall to be tiled
    Precondition: wall is a list which contains n * m zeros

    Parameter a: the length of the tiles
    Precondition: a is a integer given by the user

    Parameter b: the width of the tiles
    Precondition: b is a integer given by the user
    
    Parameter m: the length of the wall
    Precondition: m is a integer given by the user
    
    Parameter n: the width of the wall
    Precondition: n is a integer given by the user"""
    t = 0
    if k % m + a < m + 1 and k // m + b < n + 1:
        for i in range(a):
            for j in range(b):
                if wall[k % m + i][k // m + j] == 1:
                    t += 1
            if t == 0:
                return True
    else:
        return False


def paving(ans, wall, a, b, m, n, all_ans):
    """Returns: ways to tile the wall with the given
    tiles.

    Through this function, the user can know all different ways
    to pave the given wall with given tiles. The value returned 
    represents the different ways.

    The value returned has type list.

    Parameter ans: the list to contain a tiling way
    Precondition: ans is an empty list
    
    Parameter wall: the wall to be tiled
    Precondition: wall is a list which contains n * m zeros

    Parameter a: the length of the tiles
    Precondition: a is a integer given by the user

    Parameter b: the width of the tiles
    Precondition: b is a integer given by the user
    
    Parameter m: the length of the wall
    Precondition: m is a integer given by the user
    
    Parameter n: the width of the wall
    Precondition: n is a integer given by the user
    
    Parameter all_ans: the list to contain all ways
    Precondition: all_ans is an empty list"""
    k = available(wall, a, b, m, n)
    if k is None:
        all_ans.append(ans.copy())
    elif a != b:
        if test_tile(k, a, b, wall, m, n) is True:
            for i in range(a):
                for j in range(b):
                    wall[k % m + i][k // m + j] = 1
            ans.append(tile(k, a, b, m, n))
            paving(ans, wall, a, b, m, n, all_ans)
            for i in range(a):
                for j in range(b):
                    wall[k % m + i][k // m + j] = 0
            ans.pop()
        if test_tile(k, b, a, wall, m, n) is True:
            for i in range(b):
                for j in range(a):
                    wall[k % m + i][k // m + j] = 1
            ans.append(tile(k, b, a, m, n))
            paving(ans, wall, a, b, m, n, all_ans)
            for i in range(b):
                for j in range(a):
                    wall[k % m + i][k // m + j] = 0
            ans.pop()
        return all_ans
    else:
        if test_tile(k, a, b, wall, m, n) is True:
            for i in range(a):
                for j in range(b):
                    wall[k % m + i][k // m + j] = 1
            ans.append(tile(k, a, b, m, n))
            paving(ans, wall, a, b, m, n, all_ans)
            for i in range(a):
                for j in range(b):
                    wall[k % m + i][k // m + j] = 0
            ans.pop()
        return [all_ans[0]]


def fail(result):
    """Returns: a string reads 'The tiles cannot pave the wall.'

    Through this function, the user can judge whether the given wall
    can be exactly tiled with given tiles. The value returned 
    represents the result if the tiles fail to pave the wall.

    The value returned has type string.
    
    Parameter result: the result of fuction paving
    Precondition: result is a list"""
    if result == []:
        result = 'The tiles cannot pave the wall.'
    return result


def main_paving():
    """Returns: different ways to pave the wall.

    Through this function, the user can realize the process of paving.
    The value returned represents the different ways to pave the wall 
    with the certain size of tiles."""
    m = int(input('Please input the length of the wall: '))
    n = int(input('Please input the width of the wall: '))
    a = int(input('Please input the length of the tiles: '))
    b = int(input('Please input the width of the tiles: '))
    all_ans = []
    wall = [0]*m
    for i in range(m):
        wall[i] = [0]*n
    result = paving([], wall, a, b, m, n, all_ans)
    result = fail(result)
    if type(result) == list:
        if len(result) == 1:
            print('There is one way to pave the wall:')
            print(result)
        else:
            print('There are ' + str(len(result)) + ' ways to pave the wall:')
            print(result)
    else:
        print(result)
    return result, a, b, m, n


def draw_thewall(t, a, b, m, n):
    """Through this function, the user can draw a table to represent 
    the wall. The value returned is a table drawn by the turtle.

    Parameter t: a turtle to draw the wall
    Precondition: t is a turtle
    
    Parameter a: the length of the tiles
    Precondition: a is a integer given by the user

    Parameter b: the width of the tiles
    Precondition: b is a integer given by the user
    
    Parameter m: the length of the wall
    Precondition: m is a integer given by the user
    
    Parameter n: the width of the wall
    Precondition: n is a integer given by the user"""
    t.color('blue')
    t.pu()
    for i in range(n+1):
        t.goto(-25*m, 25*n-50*i)
        t.pd()
        t.fd(50*m)
        t.pu()
    t.rt(90)
    for j in range(m+1):
        t.goto(-25*m+50*j, 25*n)
        t.pd()
        t.fd(50*n)
        t.pu()
    t.lt(90)


def draw_number(t, a, b, m, n):
    """Through this function, the user can number the blanks of the
    wall. The value returned is a table with numbers.

    Parameter t: a turtle to write numbers on the wall
    Precondition: t is a turtle
    
    Parameter a: the length of the tiles
    Precondition: a is a integer given by the user

    Parameter b: the width of the tiles
    Precondition: b is a integer given by the user
    
    Parameter m: the length of the wall
    Precondition: m is a integer given by the user
    
    Parameter n: the width of the wall
    Precondition: n is a integer given by the user"""
    t.color('blue')
    for i in range(n):
        t.goto(-25*m+25, -25*n+25+50*i)
        for j in range(m):
            t.write(j + i * m, False, 'center')
            t.fd(50)


def draw_tiles(m_start, m_stop, n_start, n_stop, t, a, b, m, n):
    """Through this function, the user can choose a way amomng different
    ways and draw it on the wall. The value returned is a tile on the wall.

    Parameter m_start: the abscissa values to begin with
    Precondition: m_start is a integer
    
    Parameter m_stop: the abscissa values to end up with
    Precondition: m_start is a integer
    
    Parameter n_start: the ordinate values to begin with
    Precondition: m_start is a integer
    
    Parameter n_stop: the ordinate values to end up with
    Precondition: m_start is a integer
    
    Parameter t: a turtle to write numbers on the wall
    Precondition: t is a turtle
    
    Parameter a: the length of the tiles
    Precondition: a is a integer given by the user

    Parameter b: the width of the tiles
    Precondition: b is a integer given by the user
    
    Parameter m: the length of the wall
    Precondition: m is a integer given by the user
    
    Parameter n: the width of the wall
    Precondition: n is a integer given by the user"""
    t.pensize(2)
    t.color('black')
    t.pu()
    t.goto(-25*m+50*m_start, -25*n+50*n_start)
    t.pd()
    t.goto(-25*m+50*m_start, -25*n+50*n_stop)
    t.goto(-25*m+50*m_stop, -25*n+50*n_stop)
    t.goto(-25*m+50*m_stop, -25*n+50*n_start)
    t.goto(-25*m+50*m_start, -25*n+50*n_start)
    t.pu()


def exchange_tiles(plan, t, a, b, m, n):
    """Through this function, the user can confirm the place of a tile
    by four integers. The value returned is four integers.

    Parameter plan: the way to pave the wall
    Precondition: plan is a list chosen by the user
    
    Parameter t: a turtle to write numbers on the wall
    Precondition: t is a turtle
    
    Parameter a: the length of the tiles
    Precondition: a is a integer given by the user

    Parameter b: the width of the tiles
    Precondition: b is a integer given by the user
    
    Parameter m: the length of the wall
    Precondition: m is a integer given by the user
    
    Parameter n: the width of the wall
    Precondition: n is a integer given by the user"""
    for i in range(len(plan)):
        k1 = (plan[i][0] % m, plan[i][0] // m)
        k2 = (plan[i][-1] % m, plan[i][-1] // m)
        m_start = k1[0]
        m_stop = k2[0]+1
        n_start = k1[1]
        n_stop = k2[1]+1
        draw_tiles(m_start, m_stop, n_start, n_stop, t, a, b, m, n)


def main_drawing(result, a, b, m, n):
    """Returns: drawing a certain paving way on the wall.

    Through this function, the user can realize the process of choosing
    a paving way and then it on the wall.The value returned represents 
    the choosen way to pave the wall with the certain size of tiles."""
    import turtle
    t = turtle.Turtle()
    t.ht()
    t.speed(100)
    draw_thewall(t, a, b, m, n)
    draw_number(t, a, b, m, n)
    k = int(turtle.numinput('Select plan', 'Input number of 0' +
                            str(len(result)-1), 1, 0, len(result)-1))
    plan = result[k]
    exchange_tiles(plan, t, a, b, m, n)


def main():
    x = main_paving()
    if type(x[0]) == list:
        main_drawing(x[0], x[1], x[2], x[3], x[4])
if __name__ == '__main__':
    main()

