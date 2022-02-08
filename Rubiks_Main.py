                                   #### MADE BY ABHIJEET BHATTA ####
import cv2
import numpy as np
from Rubiks_draw import *
from solve import *
# CALIBRATION OF COLOURS
calib_vid = cv2.VideoCapture(0)
calib_vid.set(3, 900)
calib_vid.set(4, 900)
count = 0  # for list index
capture = 0
color = np.zeros([6, 3])  # stores the average values of Y Cr Cb over a particular cubelet
lsts = ["white", "blue", "yellow", "green", "orange", "red"]  # for displaying which colour to show
while count < 6:
    success, calib_img = calib_vid.read()
    calib_img = cv2.flip(calib_img, 1)
    calib_ycb = cv2.cvtColor(calib_img, cv2.COLOR_BGR2YCR_CB)

    cv2.rectangle(calib_img, (490, 10), (880, 70), (255, 255, 255), -1)
    cv2.putText(calib_img, "Put the correct color in the square", (500, 50), cv2.FONT_ITALIC, 1, (0, 0, 255), 3)
    cv2.rectangle(calib_img, (490, 70), (880, 120), (255, 255, 255), -1)
    cv2.putText(calib_img, "press 'S' to save", (530, 110), cv2.FONT_ITALIC, 1, (0, 0, 255), 3)
    # Red rectangle when normal; green flash when capture
    if capture != 0:
        capture = (capture + 1) % 10
        cv2.rectangle(calib_img, (260, 260), (320, 320), (0, 255, 0), 2)
    else:
        cv2.rectangle(calib_img, (260, 260), (320, 320), (0, 0, 255), 2)

    Cr = 0
    Cb = 0
    luma = 0
    averager = 0
    cv2.rectangle(calib_img, (210, 170), (430, 245), (255, 255, 255), -1)
    cv2.putText(calib_img, lsts[count], (215, 230), cv2.FONT_ITALIC, 2, (0, 0, 0), 5)
    if cv2.waitKey(10) == ord('s'):
        for x in range(275, 306):
            for y in range(275, 306):
                luma += calib_ycb[x, y, 0]
                Cb += calib_ycb[x, y, 1]
                Cr += calib_ycb[x, y, 2]
                averager += 1
        Cr = Cr / averager
        Cb = Cb / averager
        luma = luma / averager
        color[count] = [luma, Cb, Cr]
        count += 1
        capture = 1
    cv2.imshow("CALIBRATE COLOUR", calib_img)
    # cv2.imshow("hsv", calib_ycb)

cv2.destroyWindow("CALIBRATE COLOUR")


# Returns which particular colour is a given cubelet
def get_color(image, xlow_bound, xup_bound, ylow_bound, yup_bound):
    diff_orange = 0
    diff_red = 0
    diff_blue = 0
    diff_white = 0
    diff_green = 0
    diff_yellow = 0
    avg = 0
    for i in range(1, 3):
        avg = 0
        for b in range(xlow_bound, xup_bound):
            for a in range(ylow_bound, yup_bound):
                avg += 1
                diff_orange += abs(image[a, b, i] - color[4][i])
                diff_red += abs(image[a, b, i] - color[5][i])
                diff_blue += abs(image[a, b, i] - color[1][i])
                diff_white += abs(image[a, b, i] - color[0][i])
                diff_yellow += abs(image[a, b, i] - color[2][i])
                diff_green += abs(image[a, b, i] - color[3][i])
    diff_orange = diff_orange/avg
    diff_red = diff_red / avg
    diff_blue = diff_blue / avg
    diff_white = diff_white / avg
    diff_yellow = diff_yellow / avg
    diff_green = diff_green / avg

    sort_list = [diff_white, diff_blue, diff_yellow, diff_green, diff_orange, diff_red]
    index = 0
    element = sort_list[0]
    for i in range(6):
        if sort_list[i] < element:
            element = sort_list[i]
            index = i
    if index == 4:
        return [0, 165, 255]
    elif index == 5:
        return [0, 0, 255]
    elif index == 1:
        return [255, 0, 0]
    elif index == 0:
        return [255, 255, 255]
    elif index == 2:
        return [0, 255, 255]
    elif index == 3:
        return [0, 255, 0]


border_offset = 20  # it  excludes these many pixels from the borders of a cubelet
face_count = 0
face_list = []
total_list = []
capture = 0
while face_count < 6:
    face_list = []
    success, img = calib_vid.read()
    img = cv2.flip(img, 1)
    img_ycb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    cv2.rectangle(img, (90, 70), (410, 120), (255, 255, 255), -1)
    cv2.putText(img, "press 'S' to save", (130, 110), cv2.FONT_ITALIC, 1, (0, 0, 255), 3)

    if face_count == 1 or face_count == 3 or face_count == 5:
        cv2.arrowedLine(img, (420, 200), (420, 380), (255, 0, 0), 10)
        cv2.arrowedLine(img, (160, 200), (160, 380), (255, 0, 0), 10)
    elif face_count == 2 or face_count == 4:
        cv2.arrowedLine(img, (380, 160), (200, 160), (255, 0, 0), 10)
        cv2.arrowedLine(img, (380, 420), (200, 420), (255, 0, 0), 10)
    # centre red grid
    if capture != 0:
        capture = (capture + 1) % 5
        cv2.rectangle(img, (200, 200), (380, 380), (0, 255, 0), 2)
        cv2.line(img, (200, 260), (380, 260), (0, 255, 0), 2)
        cv2.line(img, (200, 320), (380, 320), (0, 255, 0), 2)
        cv2.line(img, (260, 200), (260, 380), (0, 255, 0), 2)
        cv2.line(img, (320, 200), (320, 380), (0, 255, 0), 2)
    else:
        cv2.rectangle(img, (200, 200), (380, 380), (0, 0, 255), 2)
        cv2.line(img, (200, 260), (380, 260), (0, 0, 255), 2)
        cv2.line(img, (200, 320), (380, 320), (0, 0, 255), 2)
        cv2.line(img, (260, 200), (260, 380), (0, 0, 255), 2)
        cv2.line(img, (320, 200), (320, 380), (0, 0, 255), 2)

    # finding colours and displaying at the top right corner
    c = get_color(img_ycb, 200 + border_offset, 260 - border_offset, 200 + border_offset, 260 - border_offset)
    cv2.rectangle(img, (550, 10), (590, 50), c, -1)   # top left
    face_list.append(c)

    c = get_color(img_ycb, 260 + border_offset, 320 - border_offset, 200 + border_offset, 260 - border_offset)
    cv2.rectangle(img, (590, 10), (630, 50), c, -1)    # top  mid
    face_list.append(c)

    c = get_color(img_ycb, 320 + border_offset, 380 - border_offset, 200 + border_offset, 260 - border_offset)
    cv2.rectangle(img, (630, 10), (670, 50), c, -1)    # top right
    face_list.append(c)

    c = get_color(img_ycb, 200 + border_offset, 260 - border_offset, 260 + border_offset, 320 - border_offset)
    cv2.rectangle(img, (550, 50), (590, 90), c, -1)     # mid left
    face_list.append(c)

    c = get_color(img_ycb, 260 + border_offset, 320 - border_offset, 260 + border_offset, 320 - border_offset)
    cv2.rectangle(img, (590, 50), (630, 90), c, -1)      # mid mid
    face_list.append(c)

    c = get_color(img_ycb, 320 + border_offset, 380 - border_offset, 260 + border_offset, 320 - border_offset)
    cv2.rectangle(img, (630, 50), (670, 90), c, -1)     # mid right
    face_list.append(c)

    c = get_color(img_ycb, 200 + border_offset, 260 - border_offset, 320 + border_offset, 380 - border_offset)
    cv2.rectangle(img, (550, 90), (590, 130), c, -1)    # bottom left
    face_list.append(c)

    c = get_color(img_ycb, 260 + border_offset, 320 - border_offset, 320 + border_offset, 380 - border_offset)
    cv2.rectangle(img, (590, 90), (630, 130), c, -1)     # bottom mid
    face_list.append(c)

    c = get_color(img_ycb, 320 + border_offset, 380 - border_offset, 320 + border_offset, 380 - border_offset)
    cv2.rectangle(img, (630, 90), (670, 130), c, -1)     # bottom right
    face_list.append(c)

    cv2.rectangle(img, (550, 10), (670, 130), (0, 0, 0), 1)
    cv2.line(img, (550, 50), (670, 50), (0, 0, 0), 1)
    cv2.line(img, (550, 90), (670, 90), (0, 0, 0), 1)
    cv2.line(img, (590, 10), (590, 130), (0, 0, 0), 1)
    cv2.line(img, (630, 10), (630, 130), (0, 0, 0), 1)

    cv2.imshow("video", img)
    if cv2.waitKey(1) == ord('s'):
        total_list.append(face_list)
        face_count += 1
        capture = 1

    elif cv2.waitKey(1) == ord('q'):
        cv2.destroyWindow("video")
        break

if face_count == 6:
    cv2.destroyAllWindows()
    calib_vid.release()

    solution = solve_string(total_list)
    draw(total_list)
    move(solution)
