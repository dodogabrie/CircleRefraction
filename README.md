# CircleRefraction Module

Simulator of a light beams that affects a circular drop of any material.

## Examples of use

### Entering in a drop of water with 1 inner reflection

```
import sys
sys.path.append('src/')

from circle import circle

water_idx = 1.333 # water's refraction index
n = 20 # number of light beams

circ = circle(water_idx) # initialize the circle
# Entering from the right 
circ.std_cases(n, kind = 'right', interval = [0.6, 1])
circ.refract_in_beams() # refract the beams inside
circ.bouncing_beams(1)  # 1 internal reflections
circ.refract_out_beams()# refract the beams outside
circ.setup_figure(c='w')
circ.plot()
```


![Alt text](https://github.com/dodogabrie/CircleRefraction/blob/main/docs/figures/1_water.png "a title")
