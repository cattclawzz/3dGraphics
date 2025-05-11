import tkinter as tk

'''
(formulas from from @MathMathMath on scratch)

screen x = focalLength * x/z
screen y = focalLength * y/z

'''

window = tk.Tk()
canX,canY,canZ = 500,500,100
canvas = tk.Canvas(window, width=canX, height=canY, bg='light grey')
canvas.pack()

def drawSquare(x1,y1, x2,y2):
    points = [[x1,y1], [x2,y1], [x2,y2], [x1,y2]]
    for i in range(4):
        canvas.create_line(*points[i], *points[(i+1)%4], fill= 'red')


def plotPoint(x, y, z, focalLength):
    def plotCoord(w, can): #defining a function within a function? functionseption
        return (focalLength * ((w-(can/2)) / z)) + (can/2) #The original formulas worked assuming (0,0) is the center of the plane
                                                           #removing can before and after running the formula adjusts it for the tkinter canvas
    return[plotCoord(x,canX), plotCoord(y,canY)]

def drawLine(x1,y1,z1, x2,y2,z2, focalLength, colour='black'):
    canvas.create_line(*plotPoint(x1,y1,z1,focalLength), *plotPoint(x2,y2,z2,focalLength), fill= colour)

def drawCube(x1,y1,z1, x2,y2,z2, focalLength):
    points = [[x1,y1], [x2,y1], [x2,y2], [x1,y2]] #find a better way to do this
    for i in range(4):
        drawLine(*points[i],z1, *points[(i+1)%4],z1, focalLength)
    for i in range(4):
        drawLine(*points[i],z2, *points[(i+1)%4],z2, focalLength)
    for i in points:
        drawLine(*i,z1, *i,z2, focalLength)

def render():
    canvas.delete("all")

    #drawSquare(100,100, 400,400)
    drawCube(200,200,100, 500,500,150, canZ)

    window.after(16, render)

render()
window.mainloop()