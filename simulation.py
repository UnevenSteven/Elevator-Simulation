from graphics import *
import sys
import time
class Elevator:
    width = 30
    height = 30         #TODO Make height = to the floor division from the building class
    def __init__(self, x, y, width, height, color, window):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.color = color
        self.window = window

    def draw(self):
        print("Draw Elevator")
        elevator = Rectangle(Point(self.x, self.y), Point(self.x + self.width, self.y + self.height))
        elevator.setOutline("Grey")
        elevator.setFill(self.color)
        elevator.draw(self.window)


        print(elevator)

class Building:
    def __init__(self, window, floors):
        self.window = window
        self.floors = floors
        self.elevators = []
        self.elevatorButtons = []
        self.floorSpacing = window.width / floors
    def draw(self):
        # Draws the building
        windowWidth = self.window.width
        windowHeight = self.window.height
        #floorSpacing = windowHeight/self.floors
        buttonGap = 100

        for i in range(self.floors):
            # Floor Lines
            floorStart = Point(0, self.floorSpacing * (i) + 5)
            floorEnd = Point(windowWidth, self.floorSpacing * (i) + 5)
            floorLine = Line(floorStart, floorEnd)
            floorLine.setFill("GREY")
            floorLine.draw(self.window)

            # Elevator Buttons
            upButton = None
            downButton = None

            if i != 0:
                upButton = Rectangle(Point(windowWidth - buttonGap, self.floorSpacing * i + 5), Point(windowWidth - buttonGap + (buttonGap/2), self.floorSpacing * (i+1) + 5))
                upButton.setFill("#2ecc71")
                upButton.setOutline("Grey")
                upButton.draw(self.window)

            if i != self.floors - 1:
                downButton = Rectangle(Point(windowWidth - buttonGap/2, self.floorSpacing * i + 5), Point(windowWidth - buttonGap + (buttonGap), self.floorSpacing * (i+1) + 5))
                downButton.setFill("#e74c3c")
                downButton.setOutline("Grey")
                downButton.draw(self.window)

            self.elevatorButtons.insert(0, [upButton, downButton])


        self.window.flush()

    def processButtonClick(self, x, y):
        start = time.time()
        for i in range(len(self.elevatorButtons)):
            for j in range(2):
                if self.elevatorButtons[i][j]:
                    if x > self.elevatorButtons[i][j].getP1().x and \
                       x < self.elevatorButtons[i][j].getP2().x and \
                       y > self.elevatorButtons[i][j].getP1().y and \
                       y < self.elevatorButtons[i][j].getP2().y:
                        print(x, y, i, j, time.time() - start)
                        break


    def addElevator(self):
        print("Add Elevator")
        x = 0
        y = 575
        color = "yellow"
        elevator = Elevator(x, y, 50, self.floorSpacing, color, self.window)
        self.elevators.append(elevator)
        self.drawElevators()

    def drawElevators(self):
        for elevator in self.elevators:
            elevator.draw()


def main():


    window = GraphWin("Elevator simulation", 600, 600, autoflush=False)
    window.flush()
    window.setBackground("#000021")

    building = Building(window, 20)
    building.draw()
    building.addElevator()

    window.flush()

    while True:
        mousePoint = window.checkMouse()
        if mousePoint:
            # Mouse has been clicked
            building.processButtonClick(mousePoint.x, mousePoint.y)




main()
