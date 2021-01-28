
import os
import pygame

class PS4Controller(object):
    """Class representing the PS4 controller. Pretty straightforward functionality."""

    controller = None
    axis_data = None

    def init(self):
        """Initialize the joystick components"""
        
        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

    def listen(self):
        """Listen for events to happen"""
        
        if not self.axis_data:
            self.axis_data = {}


        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    if event.axis == 0:
                        print("Left LR   " +str(round(event.value,2)))
                    if event.axis == 1:
                        print("Left UP   " +str(round(event.value,2)))
                    if event.axis == 2:
                        print("Right LR  " +str(round(event.value,2)))
                    if event.axis == 5:   
                        print("Right UP  " +str(round(event.value,2)))         
                    #self.axis_data[event.axis] = round(event.value,2)
                

                
                #os.system('clear')
                #print(self.axis_data)
                


if __name__ == "__main__":
    ps4 = PS4Controller()
    ps4.init()
    ps4.listen()