class Sensorless_Wheeled_Robot:

    def __init__(self, orig_x=0, orig_y=0):
        self.orig_x, self.orig_y = orig_x, orig_y

    def move_robot_by_unit_distance(self, x=0, y=0):
        if -1 <= x <= 1 and y == 0:  # ONLY PASS X AND Y AS -1,0,1. SO THAT ROBOT MOVES BY UNIT DISTANCE ONLY.
            self.orig_x += x

        if x == 0 and -1 <= y <= 1:
            self.orig_y += y
            print("position of robot is: ", self.orig_x, self.orig_y)
            return self.orig_x, self.orig_y

    def move_to_destination(self, des, obs):  # des is the list containing positions of destination .
        print("moving towards x")  # obs is the list containing positions of obstacle

        if des[0] < 0:
            while des[0] < self.orig_x:
                if (self.orig_x - 1) == obs[0] and self.orig_y == obs[1]:
                    print("obstacle is detected at :", obs[0], obs[1])

                    # if obstacle position is found right ahead of robot then robot will go sideways avoiding the
                    # obstacle.
                    self.move_robot_by_unit_distance(0, 1)
                    self.move_robot_by_unit_distance(-1, 0)
                    self.move_robot_by_unit_distance(-1, 0)
                    self.move_robot_by_unit_distance(0, -1)
        else:
            self.move_robot_by_unit_distance(-1, 0)

        if des[0] > 0:
            while des[0] > self.orig_x:
                if (self.orig_x + 1) == obs[0] and self.orig_y == obs[1]:
                    print("obstacle is detectedat :", obs[0], obs[1])

                    self.move_robot_by_unit_distance(0, 1)
                    self.move_robot_by_unit_distance(1, 0)
                    self.move_robot_by_unit_distance(1, 0)
                    self.move_robot_by_unit_distance(0, -1)
        else:
            self.move_robot_by_unit_distance(1, 0)

        if des[1] < 0:
            while des[1] < self.orig_y:

                if self.orig_x == obs[0] and (self.orig_y - 1) == obs[1]:
                    print("obstacle is detected at :", obs[0], obs[1])
                    self.move_robot_by_unit_distance(1, 0)
                    self.move_robot_by_unit_distance(0, -1)
                    self.move_robot_by_unit_distance(0, -1)
                    self.move_robot_by_unit_distance(-1, 0)

        else:
            self.move_robot_by_unit_distance(0, -1)

        if des[1] > 0:

            while des[1] > self.orig_y:

                if self.orig_x == obs[0] and (self.orig_y + 1) == obs[1]:
                    print("obstacle is detected at ", obs[0], obs[1])

                    self.move_robot_by_unit_distance(1, 0)
                    self.move_robot_by_unit_distance(0, 1)
                    self.move_robot_by_unit_distance(0, 1)
                    self.move_robot_by_unit_distance(-1, 0)

        else:
            self.move_robot_by_unit_distance(0, 1)
        print("final position of robot is: ", self.orig_x, self.orig_y)
        return self.orig_x, self.orig_y
