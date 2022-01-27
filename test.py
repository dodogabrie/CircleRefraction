import sys 
sys.path.append('src/')

from circle import circle

def test_entering():
    water_idx = 1.333 # water's refraction index
    n = 200 # number of light beams
    
    circ = circle(water_idx) # initialize the circle
    # Entering from the right 
    circ.std_cases(n, kind = 'right')
    circ.std_cases(n, kind = 'left')
    circ.std_cases(n, kind = 'upper')
    circ.std_cases(n, kind = 'lower')
    circ.refract_in_beams() # refract the beams inside
    circ.bouncing_beams(3)  # 1 internal reflections
    circ.refract_out_beams()# refract the beams outside
    circ.setup_figure(axis_lim = 1, c='w', lw = 0.2)
    circ.save_figure('docs/figures/more_dir_ref_water.png', dpi = 200)
    circ.plot()

if __name__ == '__main__':
    test_entering()
