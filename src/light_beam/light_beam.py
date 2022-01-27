"""
This file contains the class light beam, a class with the 
properties of a light beam that enter in a drop of any material.
"""

import numpy as np
from .properties import change_coordinates, refraction

class light_on_circle(change_coordinates, refraction):
    def __init__(self, x0, y0, m0, q0, idx):
        super().__init__()
        self.x = [x0]
        self.y = [y0]
        self.m = [m0]
        self.q = [q0]
        self.circle_idx = idx

    def reflect_transform(self):
        mt, _ = self.transform(self.m[-1], self.q[-1], self.x[-1], self.y[-1])
        new_m, new_q = self.inverse_transform(- mt, self.x[-1], self.y[-1])
        self.m.append(new_m)
        self.q.append(new_q)

    def refract_transform(self, entering = True):
        mt, _ = self.transform(self.m[-1], self.q[-1], self.x[-1], self.y[-1])
        theta_inc = np.arctan(mt)
        m_refracted = self.snell(self.circle_idx, 1, theta_inc, entering)
        new_m, new_q = self.inverse_transform(m_refracted, self.x[-1], self.y[-1])
        self.m.append(new_m)
        self.q.append(new_q)

    def norm_circle(self):
        x = self.x[-1]
        y = self.y[-1]
        if y == 0: self.m_n = 0 # oriz. case
        elif x == 0: self.m_n = np.infty # singular case
        else: self.m_n = y/x

    def circle_intersection(self, external = True, return_intersection = False):
        m, q = self.m[-1], self.q[-1]
        x_start, y_start = self.x[-1], self.y[-1]

        a = 1 + self.m[-1]**2
        b = 2 * self.m[-1] * self.q[-1]
        c = q**2 - 1
        delta = b**2 - 4 * a * c
        if delta < 0:
            raise Exception("No circle interception")
        elif (m == np.infty) or (m == -np.infty):
            yp = np.sqrt(1-x_start**2)
            ym = -np.sqrt(1-x_start**2)
            y = self.choose_interception(yp, ym, y_start, external)
            x_fin = x_start
            y_fin = y
        else:
            xp = (- b + np.sqrt(delta) )/(2 * a)
            xm = (- b - np.sqrt(delta) )/(2 * a)
            x = self.choose_interception(xp, xm, x_start, external)
            x_fin = x
            y_fin = m * x + q
        if return_intersection:
            return x_fin, y_fin
        else:
            self.x.append(x_fin)
            self.y.append(y_fin)
    
    def choose_interception(self, val_pos, val_neg, start, external):
        dp = np.abs(val_pos-start)
        dm = np.abs(val_neg-start)
        if external: return val_pos if dp < dm else val_neg
        else: return val_neg if dp < dm else val_pos
