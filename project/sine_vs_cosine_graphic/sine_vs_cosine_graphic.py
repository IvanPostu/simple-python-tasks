from numpy import sin, cos, arange, pi

import matplotlib.pyplot as plot


def sine_vs_cosine_graphic():
    x = arange(0, 4 * pi - 1, 0.1)   # start,stop,step
    y = sin(x)
    z = cos(x)
    plot.plot(x, y, x, z)

    plot.xlabel('x values from 0 to 4pi')
    plot.ylabel('sin(x) and cos(x)')
    plot.title('Plot of sin and cos from 0 to 4pi')

    plot.legend(['sin(x)', 'cos(x)'])
    plot.show()
