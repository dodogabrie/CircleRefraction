"""
This file contains the reflection and refraction properties of 
a light beam that impresses in a circle (in the origin).
"""

import numpy as np

class change_coordinates:
    def __init__(self):
        self._m_n = 0

    @property 
    def theta(self):
        return np.arctan(-self.m_n)

    @property 
    def m_n(self):
        return self._m_n

    @m_n.setter
    def m_n(self, new_m_n):
        self._m_n = new_m_n

    def transform(self, m, q, x, y):
        if m == np.infty:
            if self.m_n == np.infty: m_prime = 0
            else: m_prime = -np.cos(self.theta)/np.sin(self.theta)
            q_prime = 0
        else:
            q = q - (y + m * x)
            up = m * np.cos(self.theta) + np.sin(self.theta)
            down = np.cos(self.theta) - m * np.sin(self.theta)
            m_prime = up/down
            q_prime = q/down
        return m_prime, q_prime

    def inverse_transform(self, m_prime, x, y):
        up = m_prime * np.cos(self.theta)  - np.sin(self.theta)
        down = np.cos(self.theta) + m_prime * np.sin(self.theta)
        m = up/down
        q = y - m * x
        return m, q

class refraction:
    def __init__(self):
        self._idx = 0

    def snell(self, idx_inner, idx_outer, theta_inc, entering = True):
        if entering: angle = np.arcsin(np.sin(theta_inc)*idx_outer/idx_inner)
        else: angle = np.arcsin(np.sin(-theta_inc)*idx_inner/idx_outer)
        return np.tan(angle)

