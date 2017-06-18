# Programmierung 2 Beleg
# Aufgabe 6
# Mandelbrotmenge
# Yuan Chen MAB14 4060920


#--------------------------------------------------------------------------
# Import module

from tkinter import *                                                           # All modules of TKinter have been imported

#--------------------------------------------------------------------------
# Create a funktion that draw the rectangles with selected color of the
# every single pixels in the canvas

def Mandelbrot(Xmin, Xmax, Ymin, Ymax):

    xscale = float(canvas["width"]) / (Xmax - Xmin)                             # Calculate the x axis zoom scale of canvas width and range of real part of c
    yscale = float(canvas["height"]) / (Ymax - Ymin)                            # Calculate the y axis zoom scale of canvas height and range of imaginary part of c
    xstep = (Xmax - Xmin) / (float(canvas["width"]))                            # Calculate the changing step im x axis
    ystep = (Ymax - Ymin) / (float(canvas["height"]))                           # Calculate the changing step im y axis

    x = Xmin                                                                    # x change from the inputed minimum value Xmin to the inputed maximum value Xmax
    while x < Xmax:
        y = Ymin                                                                # y change from the inputed minimum value Ymin to the inputed maximum value Ymax
        while y < Ymax:
            c = c_count(complex(x, y))                                          # Read c for the current x and y with help of the c_count funktion
            if c == i_limit:                                                    # Judge if c is equal to the limit which in this case 20
                color = "red"                                                   # If ture give it the color red
            else:
                color = colorlist[c]                                            # If not give it the color with help of the getColor funktion

            canvas.create_rectangle((x - Xmin)*xscale, (y - Ymin)*yscale,       # Draw the squares of every single pixels with side length 1 and selected color
                                    (x - Xmin)*xscale, (y - Ymin)*yscale,       # The positions have been also multiplied by the zoom scale so it can fit to the
                                    fill=color, outline = color)                # canvas when it has been changed
            y += ystep
        x += xstep

#--------------------------------------------------------------------------
# Create a funktion that calculate the time of iterations with gived c and
# the gived maximum absolute value of z_n+1 which is 2 in this case

def c_count(c):

    z = complex(0,0)                                                            # Defined a complex number z with intial value (0,0)
    for ite in range(i_limit):                                                  # Time of iterations changes from 0 to the count limit which is 20 in this case
        z = z*z + c                                                             # The calculation fomula
        if abs(z) > 2:                                                          # Judge if the absolute value of z has exceeded 2
            return ite                                                          # If it is exceeded, return the time of iterations
    return i_limit                                                              # If not then return the limit

#--------------------------------------------------------------------------
# Create a funktion that add different colors to the setcolorlist for the
# different section of time of iterations

def getColor(iter):

    for iter in range(i_limit):                                                 # The time of iterations changes from 0 to the count limit.
        if iter < 3 :                                                           # If it's 0 - 2(time of interations: 1 - 3), set the color as 'magenta'.
            colorlist.append('magenta')
        elif iter < 7 :                                                         # If it's 3 - 6(time of interations: 4 - 7), set the color as 'blue' .
            colorlist.append('blue')
        elif iter < 11 :                                                        # If it's 7 - 10(time of interations: 8 - 11), set the color as 'green'.
            colorlist.append('#00FF00')                                         # I tried just 'green' but it showed dark green instead, so I used rgb color here so the right color can be showed
        elif iter < 15 :                                                        # If it's 11 - 14(time of interations: 12 - 15), set the color as 'yellow'.
            colorlist.append('yellow')
        else :                                                                  # If it's 15 or greater(time of interations: 16 or greater), set the color as 'red'.
            colorlist.append('red')

#------------------------------------------------------------------------------
# Main programm

i_limit = 20                                                                    # The time of iterations will be limited within 20
Xmin = -2.0                                                                     # The minimum of real part set -2
Xmax = 0.5                                                                      # The maxmimum of real part set 0.5
Ymin = -1                                                                       # The minimum of imaginary part set -1
Ymax = 1                                                                        # The maximum of imaginary part set 1

iter = 0                                                                        # Iterations has been initialized
colorlist = []                                                                  # Colorlist has been initialized
getColor(iter)                                                                  # Colors has been added to the Colorlist with help of getColor funktion

root = Tk()                                                                     # The TK class has been initialized
root.title("Mandelbrotmenge - By Yuan Chen")                                    # The title has been set

canvas = Canvas(root, width=400, height=400, bg="white")                        # The size and background of the window has been set
canvas.pack()                                                                   # The window will be showed

Mandelbrot(Xmin, Xmax, Ymin, Ymax)                                              # The color of every pixel in the canvas has been calculated with help of the Mandelbrot funktion

root.mainloop()
