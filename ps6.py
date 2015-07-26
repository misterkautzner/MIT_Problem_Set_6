# coding=utf-8
# Problem Set 6: Simulating robots
# Name: John Kautzner
# Collaborators: None
# Time: 5:40

import math
import random

import ps6_visualize
import pylab
import numpy

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):
        print "position =", (self.getX(), self.getY())
        return " "
# === Problems 1

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        #raise NotImplementedError
        self.width = width
        self.height = height
        self.clean = []
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        #raise NotImplementedError
        tile = (int(math.floor(pos.getX())), int(math.floor(pos.getY())))
        if tile not in self.clean:
            self.clean += [tile]

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        #raise NotImplementedError
        if (m, n) in self.clean:
            return True
        return False
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        #raise NotImplementedError
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        #raise NotImplementedError
        numClean = len(self.clean)
        return numClean

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        #raise NotImplementedError
        #randomPosition = Position(random.uniform(0.0, self.width), random.uniform(0.0, self.height))
        randx = random.uniform(0.0, self.width)
        randy = random.uniform(0.0, self.height)
        randomPosition = Position(randx, randy)
        return randomPosition


    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        #raise NotImplementedError
        x = pos.getX()
        y = pos.getY()
        if 0 <= x and 0 <= y and x < self.width and y < self.height:
            return True
        return False


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        #raise NotImplementedError
        self.speed = speed
        self.room = room
        self.pos = room.getRandomPosition()
        self.direc = random.randrange(0, 360, 1)
        self.room.cleanTileAtPosition(self.pos)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        #raise NotImplementedError
        return self.pos
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        #raise NotImplementedError
        return self.direc

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        #raise NotImplementedError
        self.pos = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        #raise NotImplementedError
        self.direc = direction

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        #raise NotImplementedError
        '''
        potentialDirec = self.getRobotDirection()
        #while the new position is not in the room, change the direction until it is
        pos = self.getRobotPosition()
        potentialPos = pos.getNewPosition(potentialDirec, self.speed)
        while(not self.room.isPositionInRoom(potentialPos)):
            potentialDirec = random.randrange(0, 360, 1)
            potentialPos = pos.getNewPosition(potentialDirec, self.speed)

        #update direction and position
        self.setRobotDirection(potentialDirec)
        self.setRobotPosition(potentialPos)
        self.room.cleanTileAtPosition(self.pos)
        '''



# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current direction; when
    it hits a wall, it chooses a new direction randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        #raise NotImplementedError
        potentialDirec = self.getRobotDirection()
        #while the new position is not in the room, change the direction until it is
        pos = self.getRobotPosition()
        potentialPos = pos.getNewPosition(potentialDirec, self.speed)
        while(not self.room.isPositionInRoom(potentialPos)):
            potentialDirec = random.randrange(0, 360, 1)
            potentialPos = pos.getNewPosition(potentialDirec, self.speed)

        #update direction and position
        self.setRobotDirection(potentialDirec)
        self.setRobotPosition(potentialPos)
        self.room.cleanTileAtPosition(self.pos)

# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    """
    #raise NotImplementedError
    timeSteps = 0

    for t in range(num_trials):
        #anim = ps6_visualize.RobotVisualization(num_robots, width, height)

        room = RectangularRoom(width, height)

        robot = [robot_type(room, speed) for i in range(num_robots)]

        #for i in range(num_robots):
         #   robot[i] = robot_type(room, speed)

        while(room.getNumCleanedTiles() < min_coverage * room.getNumTiles()):
            #anim.update(room, robot)

            for i in range(num_robots):
                robot[i].updatePositionAndClean()
            timeSteps += 1

        #anim.done()

    return timeSteps/(num_trials + 0.0)


# === Problem 4
#
# 1) How long does it take to clean 80% of a 20×20 room with each of 1-10 robots?
#
# 2) How long does it take two robots to clean 80% of rooms with dimensions 
#	 20×20, 25×16, 40×10, 50×8, 80×5, and 100×4?

def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """ 
    #raise NotImplementedError

    xValues = []
    yValues = []

    for num_robots in range(1, 11):
        xValues += [num_robots]
        speed = 1
        width = 20
        height = 20
        min_coverage = .8
        num_trials = 100
        robot_type = StandardRobot
        y = runSimulation(num_robots, speed, width, height, min_coverage, num_trials, robot_type)
        yValues += [y]

    pylab.plot(xValues,yValues)

    pylab.xlabel("Number of Robots")
    pylab.ylabel("Time / Steps")
    pylab.title("How long it takes 80% of a room to be cleaned by 1-10 robots")

    pylab.show()

#showPlot1()


def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    #raise NotImplementedError

    xValues = []
    yValues = []

    for width in [20, 25, 40, 50, 80, 100]:
        xValues += [width]
        height = 400/width
        speed = 1
        num_robots = 2
        min_coverage = .8
        num_trials = 100
        robot_type = StandardRobot
        y = runSimulation(num_robots, speed, width, height, min_coverage, num_trials, robot_type)
        yValues += [y]

    pylab.plot(xValues, yValues)

    pylab.xlabel("Widths")
    pylab.ylabel("Time / Steps")
    pylab.title("How Long it Takes Two Robots to Clean 80% of Rooms With Area of 400 Units")

    pylab.show()

#showPlot2()

# === Problem 5

class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random after each time-step.
    """
    #raise NotImplementedError

    def updatePositionAndClean(self):

        potentialDirec = random.randrange(0, 360, 1)

        pos = self.getRobotPosition()
        potentialPos = pos.getNewPosition(potentialDirec, self.speed)

        #while the new position is not in the room, change the direction until it is
        while(not self.room.isPositionInRoom(potentialPos)):
            potentialDirec = random.randrange(0, 360, 1)
            potentialPos = pos.getNewPosition(potentialDirec, self.speed)

        #update direction and position
        self.setRobotDirection(potentialDirec)
        self.setRobotPosition(potentialPos)
        self.room.cleanTileAtPosition(self.pos)


# === Problem 6

# For the parameters tested below (cleaning 80% of a 20x20 square room),
# RandomWalkRobots take approximately twice as long to clean the same room as
# StandardRobots do.
def showPlot3():
    """
    Produces a plot comparing the two robot strategies.
    """
    #raise NotImplementedError

    xValues = []
    yStandValues = []
    yRandValues = []

    for num_robots in range(1, 11):
        xValues += [num_robots]
        speed = 1
        width = 20
        height = 20
        min_coverage = .8
        num_trials = 100

        robot_type = StandardRobot
        yStand = runSimulation(num_robots, speed, width, height, min_coverage, num_trials, robot_type)
        yStandValues += [yStand]

        robot_type = RandomWalkRobot
        yRand = runSimulation(num_robots, speed, width, height, min_coverage, num_trials, robot_type)
        yRandValues += [yRand]


    pylab.plot(xValues,yStandValues, '-b', label = "StandardRobot")
    pylab.plot(xValues,yRandValues, '-r', label = "RandomWalkRobot")
    pylab.legend(loc = 'upper right')

    pylab.xlabel("Number of Robots")
    pylab.ylabel("Time / Steps")
    pylab.title("How long it takes 80% of a room to be cleaned by 1-10 robots")

    pylab.show()

#showPlot3()


def showPlot4():
    """
    Produces a plot comparing StandardRobots' and RandomWalkRobots' dependence of cleaning time on room shape.
    """
    #raise NotImplementedError

    xValues = []
    yStandValues = []
    yRandValues = []

    for width in [20, 25, 40, 50, 80, 100]:
        xValues += [width]
        height = 400/width
        speed = 1
        num_robots = 2
        min_coverage = .8
        num_trials = 100
        robot_type = StandardRobot
        yStand = runSimulation(num_robots, speed, width, height, min_coverage, num_trials, robot_type)
        yStandValues += [yStand]

        robot_type = RandomWalkRobot
        yRand = runSimulation(num_robots, speed, width, height, min_coverage, num_trials, robot_type)
        yRandValues += [yRand]


    pylab.plot(xValues,yStandValues, '-b', label = "StandardRobot")
    pylab.plot(xValues,yRandValues, '-r', label = "RandomWalkRobot")
    pylab.legend(loc = 'upper left')

    pylab.xlabel("Widths")
    pylab.ylabel("Time / Steps")
    pylab.title("How Long it Takes Two Robots to Clean 80% of Rooms With Area of 400 Units")

    pylab.show()

#showPlot4()

'''
for num_robots in range(10, 11):
    print num_robots, "robots"
    speed = 1
    width = 20
    height = 20
    min_coverage = .75
    num_trials = 100
    robot_type = RandomWalkRobot
    print "average timeSteps = ", runSimulation(num_robots, speed, width, height, min_coverage, num_trials, robot_type)
    '''