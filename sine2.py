import launchpad_py as lpad
import math as m

if lpad.LaunchpadMiniMk3().Check(1):
    lp = lpad.LaunchpadMiniMk3()
    if lp.Open(1, "minimk3"):
        print("Connected to Launchpad Mini Mk3.\n")
    else:
        print("Did not find any Launchpad Mini Mk3...\n")
        exit(0)

A = 31
B = 2*m.pi / 81
RGB = [0, 0, 0]
while True:
    for i in range(1, 81):
        for y in range(9):
            for x in range(9):
                x1 = 8*y+x
                RGB[0] = int(A * m.sin(B*x1 + B*i) + A)             # RED
                RGB[1] = int(A * m.sin(B*x1 + B*i + m.pi/3) + A)    # GREEN
                RGB[2] = int(A * m.sin(B*x1 + B*i + 2*m.pi/3) + A)  # BLUE
                lp.LedCtrlXYByRGB(x, y, RGB)

lp.Close()  # close the Launchpad
