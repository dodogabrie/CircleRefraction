"""
This file generate standar directions for the light beams entering in the circle.
"""

import numpy as np 

def std_cases(self, n, kind = 'right', interval = None):
    if kind.startswith('diag'): val_lim = np.sqrt(2)
    else: val_lim = 1
    if interval == None:
        interval = [-val_lim + val_lim/n**2, val_lim-val_lim/n**2]
    else:
        # Solve problem with tangent beams
        if interval[0] == -1: interval[0] = -val_lim + val_lim/n**2
        else: interval[0] = interval[0] * val_lim
        if interval[1] == 1:  interval[1] =  val_lim - val_lim/n**2
        else: interval[1] = interval[1] * val_lim

    if kind == 'right':
        mm = [0]*n
        qq = np.linspace(interval[0], interval[1], n)
        xx = [2]*n
        yy = qq
    elif kind == 'left':
        mm = [0]*n
        qq = np.linspace(interval[0], interval[1], n)
        xx = [-2]*n
        yy = qq
    elif kind == 'upper':
        mm = [np.infty]*n
        qq = [0]*n
        xx = np.linspace(interval[0], interval[1], n)
        yy = [2]*n
    elif kind == 'lower':
        mm = [np.infty]*n
        qq = [0]*n
        xx = np.linspace(interval[0], interval[1], n)
        yy = [-2]*n
    elif kind == 'diag upper right':
        mm = [1]*n
        qq = np.linspace(interval[0], interval[1], n)
        xx = [2]*n
        yy = [m * x + q for m, x, q in zip(mm, xx, qq)]
    elif kind == 'diag upper left':
        mm = [-1]*n
        qq = np.linspace(interval[0], interval[1], n)
        xx = [-2]*n
        yy = [m * x + q for m, x, q in zip(mm, xx, qq)]
    elif kind == 'diag lower left':
        mm = [1]*n
        qq = np.linspace(interval[0], interval[1], n)
        xx = [-2]*n
        yy = [m * x + q for m, x, q in zip(mm, xx, qq)]
    elif kind == 'diag lower right':
        mm = [-1]*n
        qq = np.linspace(interval[0], interval[1], n)
        xx = [2]*n
        yy = [m * x + q for m, x, q in zip(mm, xx, qq)]

    else: raise Exception(f'Unknown initialization name {kind}')
    for x0, y0, m0, q0 in zip(xx, yy, mm, qq):
        self.new_beam(x0, y0, m0, q0)
