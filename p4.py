from graphics import *

def isClicked(p, button):
    p1 = button.getP1()
    p2 = button.getP2()
    return p1.getX() <= p.getX() <= p2.getX() and p1.getY() <= p.getY() <= p2.getY()

def main():
    print("This program checks whether a button was clicked")
    win = GraphWin("Button", 400, 400)
    win.setCoords(-150, -150, 150, 150)
    button = Rectangle(Point(-50, -20), Point(50, 20))
    button.setFill("lightgray")
    button.draw(win)
    Text(Point(0, 0), "Click Me").draw(win)
    message = Text(Point(0, -100), "Click anywhere 10 times")
    message.draw(win)
    for i in range(10):
        p = win.getMouse()
        if isClicked(p, button):
            message.setText("Click " + str(i + 1) + ": the button was clicked")
        else:
            message.setText("Click " + str(i + 1) + ": the button was not clicked")
    Text(Point(0, 130), "Click anywhere to exit").draw(win)
    win.getMouse()
    win.close()

main()
