from vpython import *
rubiks_lst = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
scene = canvas(title="MODEL CUBE", width=1500, height=700, center=vec(0, 0, 0), background=color.black)

def draw(colors):

    # cubie 1:
    centre = [-1, 1, 1]
    py1 = pyramid(pos=vec(centre[0], centre[1], centre[2]+0.5), size=vec(0.5, 1, 1), color=vec(colors[0][2][2]/200,
                                                                                               colors[0][2][1]/200,
                                                                                               colors[0][2][0]/200), axis=vec(0, 0, -1))
    py2 = pyramid(pos=vec(centre[0], centre[1]+0.5, centre[2]), size=vec(0.5, 1, 1), color=vec(colors[1][8][2]/200,
                                                                                               colors[1][8][1]/200,
                                                                                               colors[1][8][0]/200), axis=vec(0, -1, 0))
    py3 = pyramid(pos=vec(centre[0]-0.5, centre[1], centre[2]), size=vec(0.5, 1, 1), color=vec(colors[2][6][2]/200,
                                                                                               colors[2][6][1]/200,
                                                                                               colors[2][6][0]/200), axis=vec(1, 0, 0))
    rect1 = box(pos=vec(-1, 0.5, 1), size=vec(1.02, 0.03, 1.02), color=color.black)
    rect2 = box(pos=vec(-0.5, 1, 1), size=vec(0.03, 1.02, 1.02), color=color.black)
    rect3 = box(pos=vec(-1, 1, 0.5), size=vec(1.02, 1.02, 0.03), color=color.black)
    rubiks_lst[0][0][0] = compound([py1, py2, py3,rect3,rect2,rect1])

    # cubie 2:
    centre = [0, 1, 1]
    py1 = pyramid(pos=vec(centre[0], centre[1], centre[2]+0.5), size=vec(0.5, 1, 1), color=vec(colors[0][1][2]/200,
                                                                                               colors[0][1][1]/200,
                                                                                               colors[0][1][0]/200), axis=vec(0, 0, -1))
    py2 = pyramid(pos=vec(centre[0], centre[1]+0.5, centre[2]), size=vec(0.5, 1, 1), color=vec(colors[1][7][2]/200,
                                                                                               colors[1][7][1]/200,
                                                                                               colors[1][7][0]/200), axis=vec(0, -1, 0))

    rubiks_lst[1][0][0] = compound([py1, py2])

    # cubie 3:
    centre = [1, 1, 1]
    py1 = pyramid(pos=vec(centre[0], centre[1], centre[2]+0.5), size=vec(0.5, 1, 1), color=vec(colors[0][0][2]/200,
                                                                                               colors[0][0][1]/200,
                                                                                               colors[0][0][0]/200), axis=vec(0, 0, -1))
    py2 = pyramid(pos=vec(centre[0], centre[1]+0.5, centre[2]), size=vec(0.5, 1, 1), color=vec(colors[1][6][2]/200,
                                                                                               colors[1][6][1]/200,
                                                                                               colors[1][6][0]/200), axis=vec(0, -1, 0))
    py3 = pyramid(pos=vec(centre[0]+0.5, centre[1], centre[2]), size=vec(0.5, 1, 1), color=vec(colors[5][2][2]/200,
                                                                                               colors[5][2][1]/200,
                                                                                               colors[5][2][0]/200), axis=vec(-1, 0, 0))
    rect1 = box(pos=vec(0.5, 1, 1), size=vec(0.03, 1.02, 1.02), color=color.black)
    rect2 = box(pos=vec(1, 0.5, 1), size=vec(1.02, 0.03, 1.02), color=color.black)
    rect3 = box(pos=vec(1, 1, 0.5), size=vec(1.02, 1.02, 0.03), color=color.black)

    rubiks_lst[2][0][0] = compound([py1, py2, py3,rect1,rect2,rect3])

    # cubie 4:
    centre = [-1, 0, 1]
    py1 = pyramid(pos=vec(centre[0], centre[1], centre[2]+0.5), size=vec(0.5, 1, 1), color=vec(colors[0][5][2]/200,
                                                                                               colors[0][5][1]/200,
                                                                                               colors[0][5][0]/200), axis=vec(0, 0, -1))
    py2 = pyramid(pos=vec(centre[0]-0.5, centre[1], centre[2]), size=vec(0.5, 1, 1), color=vec(colors[2][7][2]/200,
                                                                                               colors[2][7][1]/200,
                                                                                               colors[2][7][0]/200), axis=vec(1, 0, 0))

    rubiks_lst[0][1][0] = compound([py1, py2])

    # cubie 5:
    centre = [0, 0, 1]
    py1 = pyramid(pos=vec(centre[0], centre[1], centre[2]+0.5), size=vec(0.5, 1, 1), color=vec(colors[0][4][2]/200,
                                                                                               colors[0][4][1]/200,
                                                                                               colors[0][4][0]/200), axis=vec(0, 0, -1))
    rect1 = box(pos=vec(0, 0.5, 1), size=vec(1.02, 0.03, 1.02), color=color.black)
    rect2 = box(pos=vec(0, -0.5, 1), size=vec(1.02, 0.03, 1.02), color=color.black)
    rect3 = box(pos=vec(-0.5, 0, 1), size=vec(0.03, 1.02, 1.02), color=color.black)
    rect4 = box(pos=vec(0.5, 0, 1), size=vec(0.03, 1.02, 1.02), color=color.black)

    rubiks_lst[1][1][0] = compound([py1,rect1,rect2,rect3,rect4])

    # cubie 6:
    centre = [1, 0, 1]
    py1 = pyramid(pos=vec(centre[0], centre[1], centre[2]+0.5), size=vec(0.5, 1, 1), color=vec(colors[0][3][2]/200,
                                                                                               colors[0][3][1]/200,
                                                                                               colors[0][3][0]/200), axis=vec(0, 0, -1))

    py3 = pyramid(pos=vec(centre[0]+0.5, centre[1], centre[2]), size=vec(0.5, 1, 1), color=vec(colors[5][5][2]/200,
                                                                                               colors[5][5][1]/200,
                                                                                               colors[5][5][0]/200), axis=vec(-1, 0, 0))
    rubiks_lst[2][1][0] = compound([py1, py3])

    # cubie 7:
    centre = [-1, -1, 1]
    py1 = pyramid(pos=vec(centre[0], centre[1], centre[2]+0.5), size=vec(0.5, 1, 1), color=vec(colors[0][8][2]/200,
                                                                                               colors[0][8][1]/200,
                                                                                               colors[0][8][0]/200), axis=vec(0, 0, -1))
    py2 = pyramid(pos=vec(centre[0], centre[1]-0.5, centre[2]), size=vec(0.5, 1, 1), color=vec(colors[4][8][2]/200,
                                                                                               colors[4][8][1]/200,
                                                                                               colors[4][8][0]/200), axis=vec(0, 1, 0))
    py3 = pyramid(pos=vec(centre[0]-0.5, centre[1], centre[2]), size=vec(0.5, 1, 1), color=vec(colors[2][8][2]/200,
                                                                                               colors[2][8][1]/200,
                                                                                               colors[2][8][0]/200), axis=vec(1, 0, 0))
    rect3 = box(pos=vec(-0.5, -1, 1), size=vec(0.03, 1.02, 1.02), color=color.black)
    rect2 = box(pos=vec(-1, -0.5, 1), size=vec(1.02, 0.03, 1.02), color=color.black)
    rect1 = box(pos=vec(-1, -1, 0.5), size=vec(1.02, 1.02, 0.03), color=color.black)

    rubiks_lst[0][2][0] = compound([py1, py2, py3, rect1, rect2, rect3])

    # cubie 8:
    centre = [0, -1, 1]
    py1 = pyramid(pos=vec(centre[0], centre[1], centre[2]+0.5), size=vec(0.5, 1, 1), color=vec(colors[0][7][2]/200,
                                                                                               colors[0][7][1]/200,
                                                                                               colors[0][7][0]/200), axis=vec(0, 0, -1))
    py2 = pyramid(pos=vec(centre[0], centre[1]-0.5, centre[2]), size=vec(0.5, 1, 1), color=vec(colors[4][5][2]/200,
                                                                                               colors[4][5][1]/200,
                                                                                               colors[4][5][0]/200), axis=vec(0, 1, 0))

    rubiks_lst[1][2][0] = compound([py1, py2])

    # cubie 9:
    centre = [1, -1, 1]
    py1 = pyramid(pos=vec(centre[0], centre[1], centre[2]+0.5), size=vec(0.5, 1, 1), color=vec(colors[0][6][2]/200,
                                                                                               colors[0][6][1]/200,
                                                                                               colors[0][6][0]/200), axis=vec(0, 0, -1))
    py2 = pyramid(pos=vec(centre[0], centre[1]-0.5, centre[2]), size=vec(0.5, 1, 1), color=vec(colors[4][2][2]/200,
                                                                                               colors[4][2][1]/200,
                                                                                               colors[4][2][0]/200), axis=vec(0, 1, 0))
    py3 = pyramid(pos=vec(centre[0]+0.5, centre[1], centre[2]), size=vec(0.5, 1, 1), color=vec(colors[5][8][2]/200,
                                                                                               colors[5][8][1]/200,
                                                                                               colors[5][8][0]/200), axis=vec(-1, 0, 0))
    rect3 = box(pos=vec(0.5, -1, 1), size=vec(0.03, 1.02, 1.02), color=color.black)
    rect2 = box(pos=vec(1, -0.5, 1), size=vec(1.02, 0.03, 1.02), color=color.black)
    rect1 = box(pos=vec(1, -1, 0.5), size=vec(1.02, 1.02, 0.03), color=color.black)
    rubiks_lst[2][2][0] = compound([py1, py2, py3, rect1,rect2,rect3])
 #####################################################################################################################################################
 #####################################################################################################################################################
    # cubie 18:
    centre = [-1, 1, -1]
    py1 = pyramid(pos=vec(centre[0], centre[1], centre[2] - 0.5), size=vec(0.5, 1, 1), color=vec(colors[3][6][2] / 200,
                                                                                                 colors[3][6][1] / 200,
                                                                                                 colors[3][6][0] / 200),
                  axis=vec(0, 0, 1))
    py2 = pyramid(pos=vec(centre[0], centre[1] + 0.5, centre[2]), size=vec(0.5, 1, 1), color=vec(colors[1][2][2] / 200,
                                                                                                 colors[1][2][1] / 200,
                                                                                                 colors[1][2][0] / 200),
                  axis=vec(0, -1, 0))
    py3 = pyramid(pos=vec(centre[0] - 0.5, centre[1], centre[2]), size=vec(0.5, 1, 1), color=vec(colors[2][0][2] / 200,
                                                                                                 colors[2][0][1] / 200,
                                                                                                 colors[2][0][0] / 200),
                  axis=vec(1, 0, 0))
    rect1 = box(pos=vec(-1, 0.5, -1), size=vec(1.02, 0.03, 1.02), color=color.black)
    rect2 = box(pos=vec(-0.5, 1, -1), size=vec(0.03, 1.02, 1.02), color=color.black)
    rect3 = box(pos=vec(-1, 1, -0.5), size=vec(1.02, 1.02, 0.03), color=color.black)
    rubiks_lst[0][0][2] = compound([py1, py2, py3,rect1,rect2,rect3])

    # cubie 19:
    centre = [0, 1, -1]
    py1 = pyramid(pos=vec(centre[0], centre[1], centre[2] - 0.5), size=vec(0.5, 1, 1), color=vec(colors[3][3][2] / 200,
                                                                                                 colors[3][3][1] / 200,
                                                                                                 colors[3][3][0] / 200),
                  axis=vec(0, 0, 1))
    py2 = pyramid(pos=vec(centre[0], centre[1] + 0.5, centre[2]), size=vec(0.5, 1, 1), color=vec(colors[1][1][2] / 200,
                                                                                                 colors[1][1][1] / 200,
                                                                                                 colors[1][1][0] / 200),
                  axis=vec(0, -1, 0))
    rubiks_lst[1][0][2] = compound([py1, py2])

    # cubie 20:
    centre = [1, 1, -1]
    py1 = pyramid(pos=vec(centre[0], centre[1], centre[2] - 0.5), size=vec(0.5, 1, 1), color=vec(colors[3][0][2] / 200,
                                                                                                 colors[3][0][1] / 200,
                                                                                                 colors[3][0][0] / 200),
                  axis=vec(0, 0, 1))
    py2 = pyramid(pos=vec(centre[0], centre[1] + 0.5, centre[2]), size=vec(0.5, 1, 1), color=vec(colors[1][0][2] / 200,
                                                                                                 colors[1][0][1] / 200,
                                                                                                 colors[1][0][0] / 200),
                  axis=vec(0, -1, 0))
    py3 = pyramid(pos=vec(centre[0] + 0.5, centre[1], centre[2]), size=vec(0.5, 1, 1), color=vec(colors[5][0][2] / 200,
                                                                                                 colors[5][0][1] / 200,
                                                                                                 colors[5][0][0] / 200),
                  axis=vec(-1, 0, 0))
    rect1 = box(pos=vec(0.5, 1, -1), size=vec(0.03, 1.02, 1.02), color=color.black)
    rect2 = box(pos=vec(1, 0.5, -1), size=vec(1.02, 0.03, 1.02), color=color.black)
    rect3 = box(pos=vec(1, 1, -0.5), size=vec(1.02, 1.02, 0.03), color=color.black)
    rubiks_lst[2][0][2] = compound([py1, py2, py3,rect1,rect2,rect3])

    # cubie 21:
    centre = [-1, 0, -1]
    py1 = pyramid(pos=vec(centre[0], centre[1], centre[2] - 0.5), size=vec(0.5, 1, 1), color=vec(colors[3][7][2] / 200,
                                                                                                 colors[3][7][1] / 200,
                                                                                                 colors[3][7][0] / 200),
                  axis=vec(0, 0, 1))
    py2 = pyramid(pos=vec(centre[0] - 0.5, centre[1], centre[2]), size=vec(0.5, 1, 1), color=vec(colors[2][1][2] / 200,
                                                                                                 colors[2][1][1] / 200,
                                                                                                 colors[2][1][0] / 200),
                  axis=vec(1, 0, 0))

    rubiks_lst[0][1][2] = compound([py1, py2])

    # cubie 22:
    centre = [0, 0, -1]
    py1 = pyramid(pos=vec(centre[0], centre[1], centre[2] - 0.5), size=vec(0.5, 1, 1), color=vec(colors[3][4][2] / 200,
                                                                                                 colors[3][4][1] / 200,
                                                                                                 colors[3][4][0] / 200),
                  axis=vec(0, 0, 1))
    rect1 = box(pos=vec(0, 0.5, -1), size=vec(1.02, 0.03, 1.02), color=color.black)
    rect2 = box(pos=vec(0, -0.5, -1), size=vec(1.02, 0.03, 1.02), color=color.black)
    rect3 = box(pos=vec(0.5, 0, -1), size=vec(0.03, 1.02, 1.02), color=color.black)
    rect4 = box(pos=vec(-0.5, 0, -1), size=vec(0.03, 1.02, 1.02), color=color.black)

    rubiks_lst[1][1][2] = compound([py1,rect1,rect2,rect3,rect4])

    # cubie 23:
    centre = [1, 0, -1]
    py1 = pyramid(pos=vec(centre[0], centre[1], centre[2] - 0.5), size=vec(0.5, 1, 1), color=vec(colors[3][1][2] / 200,
                                                                                                 colors[3][1][1] / 200,
                                                                                                 colors[3][1][0] / 200),
                  axis=vec(0, 0, 1))

    py3 = pyramid(pos=vec(centre[0] + 0.5, centre[1], centre[2]), size=vec(0.5, 1, 1), color=vec(colors[5][3][2] / 200,
                                                                                                 colors[5][3][1] / 200,
                                                                                                 colors[5][3][0] / 200),
                  axis=vec(-1, 0, 0))
    rubiks_lst[2][1][2] = compound([py1, py3])

    # cubie 24:
    centre = [-1, -1, -1]
    py1 = pyramid(pos=vec(centre[0], centre[1], centre[2] - 0.5), size=vec(0.5, 1, 1), color=vec(colors[3][8][2] / 200,
                                                                                                 colors[3][8][1] / 200,
                                                                                                 colors[3][8][0] / 200),
                  axis=vec(0, 0, 1))
    py2 = pyramid(pos=vec(centre[0], centre[1] - 0.5, centre[2]), size=vec(0.5, 1, 1), color=vec(colors[4][6][2] / 200,
                                                                                                 colors[4][6][1] / 200,
                                                                                                 colors[4][6][0] / 200),
                  axis=vec(0, 1, 0))
    py3 = pyramid(pos=vec(centre[0] - 0.5, centre[1], centre[2]), size=vec(0.5, 1, 1), color=vec(colors[2][2][2] / 200,
                                                                                                 colors[2][2][1] / 200,
                                                                                                 colors[2][2][0] / 200),
                  axis=vec(1, 0, 0))
    rect3 = box(pos=vec(-0.5, -1, -1), size=vec(0.03, 1.02, 1.02), color=color.black)
    rect2 = box(pos=vec(-1, -0.5, -1), size=vec(1.02, 0.03, 1.02), color=color.black)
    rect1 = box(pos=vec(-1, -1, -0.5), size=vec(1.02, 1.02, 0.03), color=color.black)
    rubiks_lst[0][2][2] = compound([py1, py2, py3,rect1,rect2,rect3])

    # cubie 25:
    centre = [0, -1, -1]
    py1 = pyramid(pos=vec(centre[0], centre[1], centre[2] - 0.5), size=vec(0.5, 1, 1), color=vec(colors[3][5][2] / 200,
                                                                                                 colors[3][5][1] / 200,
                                                                                                 colors[3][5][0] / 200),
                  axis=vec(0, 0, 1))
    py2 = pyramid(pos=vec(centre[0], centre[1] - 0.5, centre[2]), size=vec(0.5, 1, 1), color=vec(colors[4][3][2] / 200,
                                                                                                 colors[4][3][1] / 200,
                                                                                                 colors[4][3][0] / 200),
                  axis=vec(0, 1, 0))

    rubiks_lst[1][2][2] = compound([py1, py2])

    # cubie 26:
    centre = [1, -1, -1]
    py1 = pyramid(pos=vec(centre[0], centre[1], centre[2] - 0.5), size=vec(0.5, 1, 1), color=vec(colors[3][2][2] / 200,
                                                                                                 colors[3][2][1] / 200,
                                                                                                 colors[3][2][0] / 200),
                  axis=vec(0, 0, 1))
    py2 = pyramid(pos=vec(centre[0], centre[1] - 0.5, centre[2]), size=vec(0.5, 1, 1), color=vec(colors[4][0][2] / 200,
                                                                                                 colors[4][0][1] / 200,
                                                                                                 colors[4][0][0] / 200),
                  axis=vec(0, 1, 0))
    py3 = pyramid(pos=vec(centre[0] + 0.5, centre[1], centre[2]), size=vec(0.5, 1, 1), color=vec(colors[5][6][2] / 200,
                                                                                                 colors[5][6][1] / 200,
                                                                                                 colors[5][6][0] / 200),
                  axis=vec(-1, 0, 0))
    rect3 = box(pos=vec(0.5, -1, -1), size=vec(0.03, 1.02, 1.02), color=color.black)
    rect2 = box(pos=vec(1, -0.5, -1), size=vec(1.02, 0.03, 1.02), color=color.black)
    rect1 = box(pos=vec(1, -1, -0.5), size=vec(1.02, 1.02, 0.03), color=color.black)
    rubiks_lst[2][2][2] = compound([py1, py2, py3,rect1,rect2,rect3])
    ###########################################################################################################################
    ###########################################################################################################################
    # cubie 10:
    centre = [-1, 1, 0]

    py2 = pyramid(pos=vec(centre[0], centre[1] + 0.5, centre[2]), size=vec(0.5, 1, 1), color=vec(colors[1][5][2] / 200,
                                                                                                 colors[1][5][1] / 200,
                                                                                                 colors[1][5][0] / 200),
                  axis=vec(0, -1, 0))
    py3 = pyramid(pos=vec(centre[0] - 0.5, centre[1], centre[2]), size=vec(0.5, 1, 1), color=vec(colors[2][3][2] / 200,
                                                                                                 colors[2][3][1] / 200,
                                                                                                 colors[2][3][0] / 200),
                  axis=vec(1, 0, 0))
    rubiks_lst[0][0][1] = compound([py2, py3])

    # cubie 11:
    centre = [0, 1, 0]

    py2 = pyramid(pos=vec(centre[0], centre[1] + 0.5, centre[2]), size=vec(0.5, 1, 1), color=vec(colors[1][4][2] / 200,
                                                                                                 colors[1][4][1] / 200,
                                                                                                 colors[1][4][0] / 200),
                  axis=vec(0, -1, 0))
    rect1 = box(pos=vec(0.5, 1, 0), size=vec(0.03, 1.02, 1.02), color=color.black)
    rect2 = box(pos=vec(-0.5, 1, 0), size=vec(0.03, 1.02, 1.02), color=color.black)
    rect3 = box(pos=vec(0, 1, 0.5), size=vec(1.02, 1.02, 0.03), color=color.black)
    rect4 = box(pos=vec(0, 1, -0.5), size=vec(1.02, 1.02, 0.03), color=color.black)
    rubiks_lst[1][0][1] = compound([py2,rect1,rect2,rect3,rect4])

    # cubie 12:
    centre = [1, 1, 0]

    py2 = pyramid(pos=vec(centre[0], centre[1] + 0.5, centre[2]), size=vec(0.5, 1, 1), color=vec(colors[1][3][2] / 200,
                                                                                                 colors[1][3][1] / 200,
                                                                                                 colors[1][3][0] / 200),
                  axis=vec(0, -1, 0))
    py3 = pyramid(pos=vec(centre[0] + 0.5, centre[1], centre[2]), size=vec(0.5, 1, 1), color=vec(colors[5][1][2] / 200,
                                                                                                 colors[5][1][1] / 200,
                                                                                                 colors[5][1][0] / 200),
                  axis=vec(-1, 0, 0))
    rubiks_lst[2][0][1] = compound([py2, py3])

    # cubie 13:
    centre = [-1, 0, 0]

    py2 = pyramid(pos=vec(centre[0] - 0.5, centre[1], centre[2]), size=vec(0.5, 1, 1), color=vec(colors[2][4][2] / 200,
                                                                                                 colors[2][4][1] / 200,
                                                                                                 colors[2][4][0] / 200),
                  axis=vec(1, 0, 0))
    rect1 = box(pos=vec(-1, 0.5, 0), size=vec(1.02, 0.03, 1.02), color=color.black)
    rect2 = box(pos=vec(-1, -0.5, 0), size=vec(1.02, 0.03, 1.02), color=color.black)
    rect3 = box(pos=vec(-1, 0, 0.5), size=vec(1.02, 1.02, 0.03), color=color.black)
    rect4 = box(pos=vec(-1, 0, -0.5), size=vec(1.02, 1.02, 0.03), color=color.black)

    rubiks_lst[0][1][1] = compound([py2,rect1,rect2,rect3,rect4])

    # cubie 14:
    centre = [1, 0, 0]


    py3 = pyramid(pos=vec(centre[0] + 0.5, centre[1], centre[2]), size=vec(0.5, 1, 1), color=vec(colors[5][4][2] / 200,
                                                                                                 colors[5][4][1] / 200,
                                                                                                 colors[5][4][0] / 200),
                  axis=vec(-1, 0, 0))
    rect1 = box(pos=vec(1, 0.5, 0), size=vec(1.02, 0.03, 1.02), color=color.black)
    rect2 = box(pos=vec(1, -0.5, 0), size=vec(1.02, 0.03, 1.02), color=color.black)
    rect3 = box(pos=vec(1, 0, 0.5), size=vec(1.02, 1.02, 0.03), color=color.black)
    rect4 = box(pos=vec(1, 0, -0.5), size=vec(1.02, 1.02, 0.03), color=color.black)
    rubiks_lst[2][1][1] = compound([py3,rect1,rect2,rect3,rect4])

    # cubie 15:
    centre = [-1, -1, 0]
    py2 = pyramid(pos=vec(centre[0], centre[1] - 0.5, centre[2]), size=vec(0.5, 1, 1), color=vec(colors[4][7][2] / 200,
                                                                                                 colors[4][7][1] / 200,
                                                                                                 colors[4][7][0] / 200),
                  axis=vec(0, 1, 0))
    py3 = pyramid(pos=vec(centre[0] - 0.5, centre[1], centre[2]), size=vec(0.5, 1, 1), color=vec(colors[2][5][2] / 200,
                                                                                                 colors[2][5][1] / 200,
                                                                                                 colors[2][5][0] / 200),
                  axis=vec(1, 0, 0))
    rubiks_lst[0][2][1] = compound([py2, py3])

    # cubie 16:
    centre = [0, -1, 0]

    py2 = pyramid(pos=vec(centre[0], centre[1] - 0.5, centre[2]), size=vec(0.5, 1, 1), color=vec(colors[4][4][2] / 200,
                                                                                                 colors[4][4][1] / 200,
                                                                                                 colors[4][4][0] / 200),
                  axis=vec(0, 1, 0))
    rect1 = box(pos=vec(0.5, -1, 0), size=vec(0.03, 1.02, 1.02), color=color.black)
    rect2 = box(pos=vec(-0.5, -1, 0), size=vec(0.03, 1.02, 1.02), color=color.black)
    rect3 = box(pos=vec(0, -1, 0.5), size=vec(1.02, 1.02, 0.03), color=color.black)
    rect4 = box(pos=vec(0, -1, -0.5), size=vec(1.02, 1.02, 0.03), color=color.black)

    rubiks_lst[1][2][1] = compound([py2,rect1,rect2,rect3,rect4])

    # cubie 17:
    centre = [1, -1, 0]

    py2 = pyramid(pos=vec(centre[0], centre[1] - 0.5, centre[2]), size=vec(0.5, 1, 1), color=vec(colors[4][1][2] / 200,
                                                                                                 colors[4][1][1] / 200,
                                                                                                 colors[4][1][0] / 200),
                  axis=vec(0, 1, 0))
    py3 = pyramid(pos=vec(centre[0] + 0.5, centre[1], centre[2]), size=vec(0.5, 1, 1), color=vec(colors[5][7][2] / 200,
                                                                                                 colors[5][7][1] / 200,
                                                                                                 colors[5][7][0] / 200),
                  axis=vec(-1, 0, 0))
    rubiks_lst[2][2][1] = compound([py2, py3])

L = label(pos = vec(-1.5,0,0), text = "press 'n' for next move\npress 'p' for previous move\npress 'f' for complete solve\npress 'b' for original unsolved\nSHIFT+mouse : Pan\nALT+mouse: Zoom\nCTRL + mouse; Rotate "
          ,yoffset=0, xoffset= -200,height= 25, border = 2, font= 'sans' )


# draw(my_list)
def rot_f_():
    m = 0
    t = 0
    angle = 0
    go_on = True
    obj = None
    while go_on:
        rate(100)  # No. of frames per second
        t = (1 * 2 * pi) / 180
        angle += t
        if angle > (pi / 2):
            t = (pi / 2) - angle + t
            go_on = False

        (rubiks_lst[0][0][0]).rotate(angle=t, axis=vec(0, 0, 1), origin=vec(0, 0, 0)) #0
        (rubiks_lst[1][0][0]).rotate(angle=t, axis=vec(0, 0, 1), origin=vec(0, 0, 0)) #z
        (rubiks_lst[2][0][0]).rotate(angle=t, axis=vec(0, 0, 1), origin=vec(0, 0, 0)) #1
        (rubiks_lst[0][1][0]).rotate(angle=t, axis=vec(0, 0, 1), origin=vec(0, 0, 0)) #c
        (rubiks_lst[1][1][0]).rotate(angle=t, axis=vec(0, 0, 1), origin=vec(0, 0, 0))
        (rubiks_lst[2][1][0]).rotate(angle=t, axis=vec(0, 0, 1), origin=vec(0, 0, 0)) #a
        (rubiks_lst[0][2][0]).rotate(angle=t, axis=vec(0, 0, 1), origin=vec(0, 0, 0)) #3
        (rubiks_lst[1][2][0]).rotate(angle=t, axis=vec(0, 0, 1), origin=vec(0, 0, 0)) #b
        (rubiks_lst[2][2][0]).rotate(angle=t, axis=vec(0, 0, 1), origin=vec(0, 0, 0)) #2
    obj = rubiks_lst[0][0][0]
    rubiks_lst[0][0][0] = rubiks_lst[2][0][0]  #1
    rubiks_lst[2][0][0] = rubiks_lst[2][2][0]  #2
    rubiks_lst[2][2][0] = rubiks_lst[0][2][0]  #3
    rubiks_lst[0][2][0] = obj
    obj = rubiks_lst[1][0][0]
    rubiks_lst[1][0][0] = rubiks_lst[2][1][0] #a
    rubiks_lst[2][1][0] = rubiks_lst[1][2][0] #b
    rubiks_lst[1][2][0] = rubiks_lst[0][1][0] #c
    rubiks_lst[0][1][0] = obj

def rot_f():
    m = 0
    t = 0
    angle = 0
    go_on = True
    obj = None
    while go_on:
        rate(100)  # No. of frames per second
        t = (1 * 2 * pi) / 180
        angle += t
        if angle > (pi / 2):
            t = (pi / 2) - angle + t
            go_on = False

        (rubiks_lst[0][0][0]).rotate(angle=t, axis=vec(0, 0, -1), origin=vec(0, 0, 0)) #0
        (rubiks_lst[1][0][0]).rotate(angle=t, axis=vec(0, 0, -1), origin=vec(0, 0, 0)) #z
        (rubiks_lst[2][0][0]).rotate(angle=t, axis=vec(0, 0, -1), origin=vec(0, 0, 0)) #1
        (rubiks_lst[0][1][0]).rotate(angle=t, axis=vec(0, 0, -1), origin=vec(0, 0, 0)) #c
        (rubiks_lst[1][1][0]).rotate(angle=t, axis=vec(0, 0, -1), origin=vec(0, 0, 0))
        (rubiks_lst[2][1][0]).rotate(angle=t, axis=vec(0, 0, -1), origin=vec(0, 0, 0)) #a
        (rubiks_lst[0][2][0]).rotate(angle=t, axis=vec(0, 0, -1), origin=vec(0, 0, 0)) #3
        (rubiks_lst[1][2][0]).rotate(angle=t, axis=vec(0, 0, -1), origin=vec(0, 0, 0)) #b
        (rubiks_lst[2][2][0]).rotate(angle=t, axis=vec(0, 0, -1), origin=vec(0, 0, 0)) #2
    obj = rubiks_lst[0][0][0]
    rubiks_lst[0][0][0] = rubiks_lst[0][2][0]  #1
    rubiks_lst[0][2][0] = rubiks_lst[2][2][0]  #2
    rubiks_lst[2][2][0] = rubiks_lst[2][0][0]  #3
    rubiks_lst[2][0][0] = obj
    obj = rubiks_lst[1][0][0]
    rubiks_lst[1][0][0] = rubiks_lst[0][1][0] #a
    rubiks_lst[0][1][0] = rubiks_lst[1][2][0] #b
    rubiks_lst[1][2][0] = rubiks_lst[2][1][0] #c
    rubiks_lst[2][1][0] = obj

def rot_u_():
    m = 0
    t = 0
    angle = 0
    go_on = True
    obj = None
    while go_on:
        rate(100)  # No. of frames per second
        t = (1 * 2 * pi) / 180
        angle += t
        if angle > (pi / 2):
            t = (pi / 2) - angle + t
            go_on = False

        (rubiks_lst[0][0][2]).rotate(angle=t, axis=vec(0, 1, 0), origin=vec(0, 0, 0)) #0
        (rubiks_lst[1][0][2]).rotate(angle=t, axis=vec(0, 1, 0), origin=vec(0, 0, 0)) #z
        (rubiks_lst[2][0][2]).rotate(angle=t, axis=vec(0, 1, 0), origin=vec(0, 0, 0)) #1
        (rubiks_lst[0][0][1]).rotate(angle=t, axis=vec(0, 1, 0), origin=vec(0, 0, 0)) #c
        (rubiks_lst[1][0][1]).rotate(angle=t, axis=vec(0, 1, 0), origin=vec(0, 0, 0))
        (rubiks_lst[2][0][1]).rotate(angle=t, axis=vec(0, 1, 0), origin=vec(0, 0, 0)) #a
        (rubiks_lst[0][0][0]).rotate(angle=t, axis=vec(0, 1, 0), origin=vec(0, 0, 0)) #3
        (rubiks_lst[1][0][0]).rotate(angle=t, axis=vec(0, 1, 0), origin=vec(0, 0, 0)) #b
        (rubiks_lst[2][0][0]).rotate(angle=t, axis=vec(0, 1, 0), origin=vec(0, 0, 0)) #2
    obj = rubiks_lst[0][0][2]
    rubiks_lst[0][0][2] = rubiks_lst[2][0][2]  #1
    rubiks_lst[2][0][2] = rubiks_lst[2][0][0]  #2
    rubiks_lst[2][0][0] = rubiks_lst[0][0][0]  #3
    rubiks_lst[0][0][0] = obj
    obj = rubiks_lst[1][0][2]
    rubiks_lst[1][0][2] = rubiks_lst[2][0][1] #a
    rubiks_lst[2][0][1] = rubiks_lst[1][0][0] #b
    rubiks_lst[1][0][0] = rubiks_lst[0][0][1] #c
    rubiks_lst[0][0][1] = obj

def rot_u():
    m = 0
    t = 0
    angle = 0
    go_on = True
    obj = None
    while go_on:
        rate(100)  # No. of frames per second
        t = (1 * 2 * pi) / 180
        angle += t
        if angle > (pi / 2):
            t = (pi / 2) - angle + t
            go_on = False

        (rubiks_lst[0][0][2]).rotate(angle=t, axis=vec(0, -1, 0), origin=vec(0, 0, 0)) #0
        (rubiks_lst[1][0][2]).rotate(angle=t, axis=vec(0, -1, 0), origin=vec(0, 0, 0)) #z
        (rubiks_lst[2][0][2]).rotate(angle=t, axis=vec(0, -1, 0), origin=vec(0, 0, 0)) #1
        (rubiks_lst[0][0][1]).rotate(angle=t, axis=vec(0, -1, 0), origin=vec(0, 0, 0)) #c
        (rubiks_lst[1][0][1]).rotate(angle=t, axis=vec(0, -1, 0), origin=vec(0, 0, 0))
        (rubiks_lst[2][0][1]).rotate(angle=t, axis=vec(0, -1, 0), origin=vec(0, 0, 0)) #a
        (rubiks_lst[0][0][0]).rotate(angle=t, axis=vec(0, -1, 0), origin=vec(0, 0, 0)) #3
        (rubiks_lst[1][0][0]).rotate(angle=t, axis=vec(0, -1, 0), origin=vec(0, 0, 0)) #b
        (rubiks_lst[2][0][0]).rotate(angle=t, axis=vec(0, -1, 0), origin=vec(0, 0, 0)) #2
    obj = rubiks_lst[0][0][2]
    rubiks_lst[0][0][2] = rubiks_lst[0][0][0]  #1
    rubiks_lst[0][0][0] = rubiks_lst[2][0][0]  #2
    rubiks_lst[2][0][0] = rubiks_lst[2][0][2]  #3
    rubiks_lst[2][0][2] = obj
    obj = rubiks_lst[1][0][2]
    rubiks_lst[1][0][2] = rubiks_lst[0][0][1] #a
    rubiks_lst[0][0][1] = rubiks_lst[1][0][0] #b
    rubiks_lst[1][0][0] = rubiks_lst[2][0][1] #c
    rubiks_lst[2][0][1] = obj

def rot_l_():
    m = 0
    t = 0
    angle = 0
    go_on = True
    obj = None
    while go_on:
        rate(100)  # No. of frames per second
        t = (1 * 2 * pi) / 180
        angle += t
        if angle > (pi / 2):
            t = (pi / 2) - angle + t
            go_on = False

        (rubiks_lst[0][0][2]).rotate(angle=t, axis=vec(-1, 0, 0), origin=vec(0, 0, 0)) #0
        (rubiks_lst[0][0][1]).rotate(angle=t, axis=vec(-1, 0, 0), origin=vec(0, 0, 0)) #z
        (rubiks_lst[0][0][0]).rotate(angle=t, axis=vec(-1, 0, 0), origin=vec(0, 0, 0)) #1
        (rubiks_lst[0][1][2]).rotate(angle=t, axis=vec(-1, 0, 0), origin=vec(0, 0, 0)) #c
        (rubiks_lst[0][1][1]).rotate(angle=t, axis=vec(-1, 0, 0), origin=vec(0, 0, 0))
        (rubiks_lst[0][1][0]).rotate(angle=t, axis=vec(-1, 0, 0), origin=vec(0, 0, 0)) #a
        (rubiks_lst[0][2][2]).rotate(angle=t, axis=vec(-1, 0, 0), origin=vec(0, 0, 0)) #3
        (rubiks_lst[0][2][1]).rotate(angle=t, axis=vec(-1, 0, 0), origin=vec(0, 0, 0)) #b
        (rubiks_lst[0][2][0]).rotate(angle=t, axis=vec(-1, 0, 0), origin=vec(0, 0, 0)) #2
    obj = rubiks_lst[0][0][2]
    rubiks_lst[0][0][2] = rubiks_lst[0][0][0]  #1
    rubiks_lst[0][0][0] = rubiks_lst[0][2][0]  #2
    rubiks_lst[0][2][0] = rubiks_lst[0][2][2]  #3
    rubiks_lst[0][2][2] = obj
    obj = rubiks_lst[0][0][1]
    rubiks_lst[0][0][1] = rubiks_lst[0][1][0] #a
    rubiks_lst[0][1][0] = rubiks_lst[0][2][1] #b
    rubiks_lst[0][2][1] = rubiks_lst[0][1][2] #c
    rubiks_lst[0][1][2] = obj

def rot_l():
    m = 0
    t = 0
    angle = 0
    go_on = True
    obj = None
    while go_on:
        rate(100)  # No. of frames per second
        t = (1 * 2 * pi) / 180
        angle += t
        if angle > (pi / 2):
            t = (pi / 2) - angle + t
            go_on = False

        (rubiks_lst[0][0][2]).rotate(angle=t, axis=vec(1, 0, 0), origin=vec(0, 0, 0)) #0
        (rubiks_lst[0][0][1]).rotate(angle=t, axis=vec(1, 0, 0), origin=vec(0, 0, 0)) #z
        (rubiks_lst[0][0][0]).rotate(angle=t, axis=vec(1, 0, 0), origin=vec(0, 0, 0)) #1
        (rubiks_lst[0][1][2]).rotate(angle=t, axis=vec(1, 0, 0), origin=vec(0, 0, 0)) #c
        (rubiks_lst[0][1][1]).rotate(angle=t, axis=vec(1, 0, 0), origin=vec(0, 0, 0))
        (rubiks_lst[0][1][0]).rotate(angle=t, axis=vec(1, 0, 0), origin=vec(0, 0, 0)) #a
        (rubiks_lst[0][2][2]).rotate(angle=t, axis=vec(1, 0, 0), origin=vec(0, 0, 0)) #3
        (rubiks_lst[0][2][1]).rotate(angle=t, axis=vec(1, 0, 0), origin=vec(0, 0, 0)) #b
        (rubiks_lst[0][2][0]).rotate(angle=t, axis=vec(1, 0, 0), origin=vec(0, 0, 0)) #2
    obj = rubiks_lst[0][0][2]
    rubiks_lst[0][0][2] = rubiks_lst[0][2][2]  #1
    rubiks_lst[0][2][2] = rubiks_lst[0][2][0]  #2
    rubiks_lst[0][2][0] = rubiks_lst[0][0][0]  #3
    rubiks_lst[0][0][0] = obj
    obj = rubiks_lst[0][0][1]
    rubiks_lst[0][0][1] = rubiks_lst[0][1][2] #a
    rubiks_lst[0][1][2] = rubiks_lst[0][2][1] #b
    rubiks_lst[0][2][1] = rubiks_lst[0][1][0] #c
    rubiks_lst[0][1][0] = obj

def rot_r():
    m = 0
    t = 0
    angle = 0
    go_on = True
    obj = None
    while go_on:
        rate(100)  # No. of frames per second
        t = (1 * 2 * pi) / 180
        angle += t
        if angle > (pi / 2):
            t = (pi / 2) - angle + t
            go_on = False

        (rubiks_lst[2][0][2]).rotate(angle=t, axis=vec(-1, 0, 0), origin=vec(0, 0, 0)) #0
        (rubiks_lst[2][0][1]).rotate(angle=t, axis=vec(-1, 0, 0), origin=vec(0, 0, 0)) #z
        (rubiks_lst[2][0][0]).rotate(angle=t, axis=vec(-1, 0, 0), origin=vec(0, 0, 0)) #1
        (rubiks_lst[2][1][2]).rotate(angle=t, axis=vec(-1, 0, 0), origin=vec(0, 0, 0)) #c
        (rubiks_lst[2][1][1]).rotate(angle=t, axis=vec(-1, 0, 0), origin=vec(0, 0, 0))
        (rubiks_lst[2][1][0]).rotate(angle=t, axis=vec(-1, 0, 0), origin=vec(0, 0, 0)) #a
        (rubiks_lst[2][2][2]).rotate(angle=t, axis=vec(-1, 0, 0), origin=vec(0, 0, 0)) #3
        (rubiks_lst[2][2][1]).rotate(angle=t, axis=vec(-1, 0, 0), origin=vec(0, 0, 0)) #b
        (rubiks_lst[2][2][0]).rotate(angle=t, axis=vec(-1, 0, 0), origin=vec(0, 0, 0)) #2
    obj = rubiks_lst[2][0][2]
    rubiks_lst[2][0][2] = rubiks_lst[2][0][0]  #1
    rubiks_lst[2][0][0] = rubiks_lst[2][2][0]  #2
    rubiks_lst[2][2][0] = rubiks_lst[2][2][2]  #3
    rubiks_lst[2][2][2] = obj
    obj = rubiks_lst[2][0][1]
    rubiks_lst[2][0][1] = rubiks_lst[2][1][0] #a
    rubiks_lst[2][1][0] = rubiks_lst[2][2][1] #b
    rubiks_lst[2][2][1] = rubiks_lst[2][1][2] #c
    rubiks_lst[2][1][2] = obj

def rot_r_():
    m = 0
    t = 0
    angle = 0
    go_on = True
    obj = None
    while go_on:
        rate(100)  # No. of frames per second
        t = (1 * 2 * pi) / 180
        angle += t
        if angle > (pi / 2):
            t = (pi / 2) - angle + t
            go_on = False

        (rubiks_lst[2][0][2]).rotate(angle=t, axis=vec(1, 0, 0), origin=vec(0, 0, 0)) #0
        (rubiks_lst[2][0][1]).rotate(angle=t, axis=vec(1, 0, 0), origin=vec(0, 0, 0)) #z
        (rubiks_lst[2][0][0]).rotate(angle=t, axis=vec(1, 0, 0), origin=vec(0, 0, 0)) #1
        (rubiks_lst[2][1][2]).rotate(angle=t, axis=vec(1, 0, 0), origin=vec(0, 0, 0)) #c
        (rubiks_lst[2][1][1]).rotate(angle=t, axis=vec(1, 0, 0), origin=vec(0, 0, 0))
        (rubiks_lst[2][1][0]).rotate(angle=t, axis=vec(1, 0, 0), origin=vec(0, 0, 0)) #a
        (rubiks_lst[2][2][2]).rotate(angle=t, axis=vec(1, 0, 0), origin=vec(0, 0, 0)) #3
        (rubiks_lst[2][2][1]).rotate(angle=t, axis=vec(1, 0, 0), origin=vec(0, 0, 0)) #b
        (rubiks_lst[2][2][0]).rotate(angle=t, axis=vec(1, 0, 0), origin=vec(0, 0, 0)) #2
    obj = rubiks_lst[2][0][2]
    rubiks_lst[2][0][2] = rubiks_lst[2][2][2]  #1
    rubiks_lst[2][2][2] = rubiks_lst[2][2][0]  #2
    rubiks_lst[2][2][0] = rubiks_lst[2][0][0]  #3
    rubiks_lst[2][0][0] = obj
    obj = rubiks_lst[2][0][1]
    rubiks_lst[2][0][1] = rubiks_lst[2][1][2] #a
    rubiks_lst[2][1][2] = rubiks_lst[2][2][1] #b
    rubiks_lst[2][2][1] = rubiks_lst[2][1][0] #c
    rubiks_lst[2][1][0] = obj

def rot_d():
    m = 0
    t = 0
    angle = 0
    go_on = True
    obj = None
    while go_on:
        rate(100)  # No. of frames per second
        t = (1 * 2 * pi) / 180
        angle += t
        if angle > (pi / 2):
            t = (pi / 2) - angle + t
            go_on = False

        (rubiks_lst[0][2][2]).rotate(angle=t, axis=vec(0, 1, 0), origin=vec(0, 0, 0)) #0
        (rubiks_lst[1][2][2]).rotate(angle=t, axis=vec(0, 1, 0), origin=vec(0, 0, 0)) #z
        (rubiks_lst[2][2][2]).rotate(angle=t, axis=vec(0, 1, 0), origin=vec(0, 0, 0)) #1
        (rubiks_lst[0][2][1]).rotate(angle=t, axis=vec(0, 1, 0), origin=vec(0, 0, 0)) #c
        (rubiks_lst[1][2][1]).rotate(angle=t, axis=vec(0, 1, 0), origin=vec(0, 0, 0))
        (rubiks_lst[2][2][1]).rotate(angle=t, axis=vec(0, 1, 0), origin=vec(0, 0, 0)) #a
        (rubiks_lst[0][2][0]).rotate(angle=t, axis=vec(0, 1, 0), origin=vec(0, 0, 0)) #3
        (rubiks_lst[1][2][0]).rotate(angle=t, axis=vec(0, 1, 0), origin=vec(0, 0, 0)) #b
        (rubiks_lst[2][2][0]).rotate(angle=t, axis=vec(0, 1, 0), origin=vec(0, 0, 0)) #2
    obj = rubiks_lst[0][2][2]
    rubiks_lst[0][2][2] = rubiks_lst[2][2][2]  #1
    rubiks_lst[2][2][2] = rubiks_lst[2][2][0]  #2
    rubiks_lst[2][2][0] = rubiks_lst[0][2][0]  #3
    rubiks_lst[0][2][0] = obj
    obj = rubiks_lst[1][2][2]
    rubiks_lst[1][2][2] = rubiks_lst[2][2][1] #a
    rubiks_lst[2][2][1] = rubiks_lst[1][2][0] #b
    rubiks_lst[1][2][0] = rubiks_lst[0][2][1] #c
    rubiks_lst[0][2][1] = obj

def rot_d_():
    m = 0
    t = 0
    angle = 0
    go_on = True
    obj = None
    while go_on:
        rate(100)  # No. of frames per second
        t = (1 * 2 * pi) / 180
        angle += t
        if angle > (pi / 2):
            t = (pi / 2) - angle + t
            go_on = False

        (rubiks_lst[0][2][2]).rotate(angle=t, axis=vec(0, -1, 0), origin=vec(0, 0, 0)) #0
        (rubiks_lst[1][2][2]).rotate(angle=t, axis=vec(0, -1, 0), origin=vec(0, 0, 0)) #z
        (rubiks_lst[2][2][2]).rotate(angle=t, axis=vec(0, -1, 0), origin=vec(0, 0, 0)) #1
        (rubiks_lst[0][2][1]).rotate(angle=t, axis=vec(0, -1, 0), origin=vec(0, 0, 0)) #c
        (rubiks_lst[1][2][1]).rotate(angle=t, axis=vec(0, -1, 0), origin=vec(0, 0, 0))
        (rubiks_lst[2][2][1]).rotate(angle=t, axis=vec(0, -1, 0), origin=vec(0, 0, 0)) #a
        (rubiks_lst[0][2][0]).rotate(angle=t, axis=vec(0, -1, 0), origin=vec(0, 0, 0)) #3
        (rubiks_lst[1][2][0]).rotate(angle=t, axis=vec(0, -1, 0), origin=vec(0, 0, 0)) #b
        (rubiks_lst[2][2][0]).rotate(angle=t, axis=vec(0, -1, 0), origin=vec(0, 0, 0)) #2
    obj = rubiks_lst[0][2][2]
    rubiks_lst[0][2][2] = rubiks_lst[0][2][0]  #1
    rubiks_lst[0][2][0] = rubiks_lst[2][2][0]  #2
    rubiks_lst[2][2][0] = rubiks_lst[2][2][2]  #3
    rubiks_lst[2][2][2] = obj
    obj = rubiks_lst[1][2][2]
    rubiks_lst[1][2][2] = rubiks_lst[0][2][1] #a
    rubiks_lst[0][2][1] = rubiks_lst[1][2][0] #b
    rubiks_lst[1][2][0] = rubiks_lst[2][2][1] #c
    rubiks_lst[2][2][1] = obj

def rot_b():
    m = 0
    t = 0
    angle = 0
    go_on = True
    obj = None
    while go_on:
        rate(100)  # No. of frames per second
        t = (1 * 2 * pi) / 180
        angle += t
        if angle > (pi / 2):
            t = (pi / 2) - angle + t
            go_on = False

        (rubiks_lst[0][0][2]).rotate(angle=t, axis=vec(0, 0, 1), origin=vec(0, 0, 0)) #0
        (rubiks_lst[1][0][2]).rotate(angle=t, axis=vec(0, 0, 1), origin=vec(0, 0, 0)) #z
        (rubiks_lst[2][0][2]).rotate(angle=t, axis=vec(0, 0, 1), origin=vec(0, 0, 0)) #1
        (rubiks_lst[0][1][2]).rotate(angle=t, axis=vec(0, 0, 1), origin=vec(0, 0, 0)) #c
        (rubiks_lst[1][1][2]).rotate(angle=t, axis=vec(0, 0, 1), origin=vec(0, 0, 0))
        (rubiks_lst[2][1][2]).rotate(angle=t, axis=vec(0, 0, 1), origin=vec(0, 0, 0)) #a
        (rubiks_lst[0][2][2]).rotate(angle=t, axis=vec(0, 0, 1), origin=vec(0, 0, 0)) #3
        (rubiks_lst[1][2][2]).rotate(angle=t, axis=vec(0, 0, 1), origin=vec(0, 0, 0)) #b
        (rubiks_lst[2][2][2]).rotate(angle=t, axis=vec(0, 0, 1), origin=vec(0, 0, 0)) #2
    obj = rubiks_lst[0][0][2]
    rubiks_lst[0][0][2] = rubiks_lst[2][0][2]  #1
    rubiks_lst[2][0][2] = rubiks_lst[2][2][2]  #2
    rubiks_lst[2][2][2] = rubiks_lst[0][2][2]  #3
    rubiks_lst[0][2][2] = obj
    obj = rubiks_lst[1][0][2]
    rubiks_lst[1][0][2] = rubiks_lst[2][1][2] #a
    rubiks_lst[2][1][2] = rubiks_lst[1][2][2] #b
    rubiks_lst[1][2][2] = rubiks_lst[0][1][2] #c
    rubiks_lst[0][1][2] = obj

def rot_b_():
    m = 0
    t = 0
    angle = 0
    go_on = True
    obj = None
    while go_on:
        rate(100)  # No. of frames per second
        t = (1 * 2 * pi) / 180
        angle += t
        if angle > (pi / 2):
            t = (pi / 2) - angle + t
            go_on = False

        (rubiks_lst[0][0][2]).rotate(angle=t, axis=vec(0, 0, -1), origin=vec(0, 0, 0)) #0
        (rubiks_lst[1][0][2]).rotate(angle=t, axis=vec(0, 0, -1), origin=vec(0, 0, 0)) #z
        (rubiks_lst[2][0][2]).rotate(angle=t, axis=vec(0, 0, -1), origin=vec(0, 0, 0)) #1
        (rubiks_lst[0][1][2]).rotate(angle=t, axis=vec(0, 0, -1), origin=vec(0, 0, 0)) #c
        (rubiks_lst[1][1][2]).rotate(angle=t, axis=vec(0, 0, -1), origin=vec(0, 0, 0))
        (rubiks_lst[2][1][2]).rotate(angle=t, axis=vec(0, 0, -1), origin=vec(0, 0, 0)) #a
        (rubiks_lst[0][2][2]).rotate(angle=t, axis=vec(0, 0, -1), origin=vec(0, 0, 0)) #3
        (rubiks_lst[1][2][2]).rotate(angle=t, axis=vec(0, 0, -1), origin=vec(0, 0, 0)) #b
        (rubiks_lst[2][2][2]).rotate(angle=t, axis=vec(0, 0, -1), origin=vec(0, 0, 0)) #2
    obj = rubiks_lst[0][0][2]
    rubiks_lst[0][0][2] = rubiks_lst[0][2][2]  #1
    rubiks_lst[0][2][2] = rubiks_lst[2][2][2]  #2
    rubiks_lst[2][2][2] = rubiks_lst[2][0][2]  #3
    rubiks_lst[2][0][2] = obj
    obj = rubiks_lst[1][0][2]
    rubiks_lst[1][0][2] = rubiks_lst[0][1][2] #a
    rubiks_lst[0][1][2] = rubiks_lst[1][2][2] #b
    rubiks_lst[1][2][2] = rubiks_lst[2][1][2] #c
    rubiks_lst[2][1][2] = obj


def move(solution):
    forward = False
    backward = False
    length = len(solution)
    i = -1
    while True:
        # print(forward)
        # if take_input:
        #     inp = input()
        #     if inp == 'f' or inp == 'b':
        #         take_input = False
        ev = scene.waitfor('keydown')
        if ev.key == 'f':
            while(i< length-1):
                i = i + 1
                if solution[i] == "U1":
                    rot_u()
                elif solution[i] == "U2":
                    rot_u()
                    rot_u()
                elif solution[i] == "U3":
                    rot_u_()
                elif solution[i] == "F1":
                    rot_f()
                elif solution[i] == "F2":
                    rot_f()
                    rot_f()
                elif solution[i] == "F3":
                    rot_f_()
                elif solution[i] == "R1":
                    rot_r()
                elif solution[i] == "R2":
                    rot_r()
                    rot_r()
                elif solution[i] == "R3":
                    rot_r_()
                elif solution[i] == "L1":
                    rot_l()
                elif solution[i] == "L2":
                    rot_l()
                    rot_l()
                elif solution[i] == "L3":
                    rot_l_()
                elif solution[i] == "D1":
                    rot_d()
                elif solution[i] == "D2":
                    rot_d()
                    rot_d()
                elif solution[i] == "D3":
                    rot_d_()
                elif solution[i] == "B1":
                    rot_b()
                elif solution[i] == "B2":
                    rot_b()
                    rot_b()
                elif solution[i] == "B3":
                    rot_b_()

        if ev.key == 'n':
            if i < length-1:
                i = i+1
                if solution[i]=="U1":
                    rot_u()
                elif solution[i]=="U2":
                    rot_u()
                    rot_u()
                elif solution[i]=="U3":
                    rot_u_()
                elif solution[i]=="F1":
                    rot_f()
                elif solution[i]=="F2":
                    rot_f()
                    rot_f()
                elif solution[i]=="F3":
                    rot_f_()
                elif solution[i]=="R1":
                    rot_r()
                elif solution[i]=="R2":
                    rot_r()
                    rot_r()
                elif solution[i]=="R3":
                    rot_r_()
                elif solution[i]=="L1":
                    rot_l()
                elif solution[i]=="L2":
                    rot_l()
                    rot_l()
                elif solution[i]=="L3":
                    rot_l_()
                elif solution[i]=="D1":
                    rot_d()
                elif solution[i]=="D2":
                    rot_d()
                    rot_d()
                elif solution[i]=="D3":
                    rot_d_()
                elif solution[i]=="B1":
                    rot_b()
                elif solution[i]=="B2":
                    rot_b()
                    rot_b()
                elif solution[i]=="B3":
                    rot_b_()

        elif ev.key == 'p':
            if i > -1:
                if solution[i]=="U1":
                    rot_u_()
                elif solution[i]=="U2":
                    rot_u()
                    rot_u()
                elif solution[i]=="U3":
                    rot_u()
                elif solution[i]=="F1":
                    rot_f_()
                elif solution[i]=="F2":
                    rot_f()
                    rot_f()
                elif solution[i]=="F3":
                    rot_f()
                elif solution[i]=="R1":
                    rot_r_()
                elif solution[i]=="R2":
                    rot_r()
                    rot_r()
                elif solution[i]=="R3":
                    rot_r()
                elif solution[i]=="L1":
                    rot_l_()
                elif solution[i]=="L2":
                    rot_l()
                    rot_l()
                elif solution[i]=="L3":
                    rot_l()
                elif solution[i]=="D1":
                    rot_d_()
                elif solution[i]=="D2":
                    rot_d()
                    rot_d()
                elif solution[i]=="D3":
                    rot_d()
                elif solution[i]=="B1":
                    rot_b_()
                elif solution[i]=="B2":
                    rot_b()
                    rot_b()
                elif solution[i]=="B3":
                    rot_b()
                i = i-1

        elif ev.key == 'b':
            while (i > -1):
                if solution[i] == "U1":
                    rot_u_()
                elif solution[i] == "U2":
                    rot_u()
                    rot_u()
                elif solution[i] == "U3":
                    rot_u()
                elif solution[i] == "F1":
                    rot_f_()
                elif solution[i] == "F2":
                    rot_f()
                    rot_f()
                elif solution[i] == "F3":
                    rot_f()
                elif solution[i] == "R1":
                    rot_r_()
                elif solution[i] == "R2":
                    rot_r()
                    rot_r()
                elif solution[i] == "R3":
                    rot_r()
                elif solution[i] == "L1":
                    rot_l_()
                elif solution[i] == "L2":
                    rot_l()
                    rot_l()
                elif solution[i] == "L3":
                    rot_l()
                elif solution[i] == "D1":
                    rot_d_()
                elif solution[i] == "D2":
                    rot_d()
                    rot_d()
                elif solution[i] == "D3":
                    rot_d()
                elif solution[i] == "B1":
                    rot_b_()
                elif solution[i] == "B2":
                    rot_b()
                    rot_b()
                elif solution[i] == "B3":
                    rot_b()
                i = i - 1