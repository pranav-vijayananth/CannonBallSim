import math
import matplotlib.pyplot as plt 
import numpy as np
from scipy.interpolate import make_interp_spline

class Cannon: 
    def __init__(self, gravity, time, theta, velocity, height=0) -> None:
        self.gravity = gravity
        self.time = time 
        self.theta = theta * (math.pi / 180)
        self.velocity = velocity
        self.height = height


    def time_travelled(self) -> float: 
        return (2*self.velocity*math.sin(self.velocity))/(self.gravity)
    
    def ball_displacement(self) -> float:

        return ((self.velocity**2)*math.sin(2*self.theta))/(self.gravity)
  
    def ball_motion(self):

        ending_pos = self.ball_displacement()

        # x = np.linspace(0, ending_pos, 20)
        # y = (self.height + (self.velocity*math.sin(self.theta)*x) - (0.5*self.gravity*(x**2)))

        # fig = plt.figure()
        # ax = fig.add_subplot(1, 1, 1)
        # ax.spines['left'].set_position('center')
        # ax.spines['bottom'].set_position('center')
        # ax.spines['right'].set_color('none')
        # ax.spines['top'].set_color('none')
        # ax.xaxis.set_ticks_position('bottom')
        # ax.yaxis.set_ticks_position('left')
        
        # plt.plot(x, y, 'g')

        # plt.show()

        inputs = []
        outputs = []
        
        for x in range(0, int(ending_pos)+1):
            y = (self.height + (self.velocity*math.sin(self.theta)*x) - (0.5*self.gravity*(x**2))) 
            inputs.append(x)
            outputs.append(y) 
        
        fig = plt.figure()
        axes = fig.add_subplot(111)
        plt.xlim(0, 10)
        plt.ylim(0, 30)

        #define x as 200 equally spaced values between the min and max of original x 
        xnew = np.linspace(inputs.min(), inputs.max(), 200) 

        #define spline
        spl = make_interp_spline(inputs, outputs, k=2)
        y_smooth = spl(xnew)

        #create smooth line chart 
        axes.plot(xnew, y_smooth)

        plt.show()