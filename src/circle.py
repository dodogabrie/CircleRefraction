"""
This file contains the class circle, it create a matplotlib figure with a circle
in the origin and it manages the light beams entering in that circle.
"""

import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from light_beam.light_beam import light_on_circle

class circle:
    def __init__(self, refraction_idx, r = 1, xc = 0, yc = 0):
        self.r = r
        self.xc = xc
        self.yc = yc
        self.idx = refraction_idx
        self.beams = []

    from _standard_directions import std_cases

    def new_beam(self, x0, y0, m0, q0):
        beam = light_on_circle(x0, y0, m0, q0, self.idx)
        self.beams.append(beam)
    
    def refract_in_beams(self):
        for beam in self.beams:
            if len(beam.x)==1:
                beam.circle_intersection(external=True)
                beam.norm_circle()
                beam.refract_transform()

    def refract_out_beams(self):
        for beam in self.beams:
            if len(beam.x)==1: 
                raise Exception('Beam still out of circle')
            else:
                beam.norm_circle()
                beam.refract_transform(entering = False)
                x_int, _ = beam.circle_intersection(external = False, 
                                                    return_intersection = True)
                sign_move = (beam.x[-1] - x_int)/np.abs(beam.x[-1] - x_int)
                final_x = 2*sign_move
                final_y = beam.m[-1] * final_x + beam.q[-1]
                beam.x.append(final_x)
                beam.y.append(final_y)

    def bouncing_beams(self, k):
        for beam in self.beams:
            for _ in range(k+1):
                beam.circle_intersection(external=False)
                beam.norm_circle()
                beam.reflect_transform()

    def setup_beams(self, **kwargs):
        for beam in self.beams:
            self.ax.plot(beam.x, beam.y, **kwargs)

    def setup_figure(self, circle_color = 'blue', **kwargs):
        self.setup_circle_figure(circle_color=circle_color)
        self.setup_beams(**kwargs)

    def setup_circle_figure(self, circle_color = 'blue'):
        plt.style.use('dark_background')
        fig = plt.figure(figsize = (8, 8))
        ax = fig.add_subplot(111, aspect='equal')
        plt.xlim(-2*self.r + self.xc, 2*self.r + self.xc)
        plt.ylim(-2*self.r + self.yc, 2*self.r + self.yc)
        ax.add_patch(
            patches.Circle(
                (self.xc, self.yc),
                self.r,
                fill = True,
                color = circle_color
            )
        )
        self.fig = fig
        self.ax = ax
        
    def save_figure(self, path_to_fig, **kwargs):
        plt.savefig(path_to_fig, **kwargs)

    def plot(self):
        plt.show()


