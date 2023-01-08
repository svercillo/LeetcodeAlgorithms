# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        '''
        idea:
            Map of all nodes and directions tried
        
            Robot starts facing west. 

            1. go until stopped (includes nodes all have been tried)
            2. try other directions 

            if other directions: 
                3. go until stopped (includes nodes all have been tried)
            
            4. Back track until every square on path has direction tried
        '''
            
        directions = [i for i in range(4)]
        self.visited = set() 
        
        self.robot = robot
        self.dfs(0, 0, 0)

    
    def turnLeft(self):
        # print("turn left")
        self.robot.turnLeft()

    def turnRight(self):
        # print("turn right")
        self.robot.turnRight()
    
    def go_back(self, numturns):
        self.turnLeft()
        self.turnLeft()
        self.robot.move()
        self.turnLeft()
        self.turnLeft()


        
    def new_coords(self, i, j, direct):
        ti, tj = i, j
        match direct:
            case 0: # west
                tj -= 1
            case 1: # north
                ti -= 1
            case 2: # east
                tj += 1
            case 3: # south
                ti += 1

        return ti, tj


    def move(self, i, j, current_direction, desired_direction):
        numturns = 0
        while current_direction != desired_direction: 
            numturns += 1
            current_direction = (current_direction + 1) % 4
            self.turnRight()

        successful_move = self.robot.move()
        if successful_move:
            self.dfs(i, j, desired_direction)
            self.go_back(numturns)

        for _ in range(numturns):
            self.turnLeft()

    
    def dfs(self, i, j, direct):
        self.visited.add((i, j))
        self.robot.clean()
        for d in range(4): 
            ti, tj = self.new_coords(i,j, d)

            if (ti, tj) in self.visited:
                continue

            numturns = 0
            tdirect = direct

            self.move(ti, tj, direct, d)
