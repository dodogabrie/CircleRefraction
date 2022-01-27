import sys 
sys.path.append('src/')

from circle import circle

def test_entering():
    circ = circle(1.333)
    n = 200
    circ.std_cases(n, kind = 'right',)# interval = [0.6, 1])
    circ.std_cases(n, kind = 'left',)# interval = [0.6, 1])
    circ.std_cases(n, kind = 'upper',)# interval = [0.6, 1])
    circ.std_cases(n, kind = 'lower',)# interval = [0.6, 1])
    circ.refract_in_beams()
    circ.bouncing_beams(5)
    circ.refract_out_beams()
    circ.plot_beams(c='w', alpha = 0.1)

if __name__ == '__main__':
    test_entering()
