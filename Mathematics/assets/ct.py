#!/usr/bin/python3

def main():
    import numpy as np
    import os, argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('-s','--subPlots',
                        help='Add subplots of the normalized TNP vectors')
    parser.add_argument('-c','--osculatingCircle',
                        help='Adds the osculating circle to the main plot')
    parser.add_argument('-f','--fileOutput', type=str, default='default',
                        help='Name of the output video (.mp4 is appended)')

    args = parser.parse_args()

    # Currently functions must be written here in main()
    # as opposed to some other more elegant solution.
    
    # Example x and y functions
    # which can be passed to trace2D
    #xf = lambda t: t*np.cos(t) if t.any() > 4*np.pi else (t-4*np.pi)*np.cos(t)
    #yf = lambda t: t*np.sin(t) if t.any() > 4*np.pi else (t-4*np.pi)*np.sin(t)

    # Example x, y, and z functions
    # which can be passed to trace3D
    xf = lambda t: (2*np.pi-t)*np.cos(5*t)
    yf = lambda t: (2*np.pi-t)*np.sin(5*t)
    zf = lambda t: 1.5*t

    # Create an iterable to use as an interval for the
    # parametrized functions to map over. Note that there
    # will be one frame in the resulting video per element.
    lin = np.linspace(0.1, 4*np.pi-0.1, num=1500)
    
    trace3D(xf, yf, zf, lin, fileName=args.fileOutput,
            subPlot=args.subPlots, oscCircle=args.osculatingCircle)
    #trace2D(xf, yf, lin, xLimit=[-1,7], yLimit=[-1,3], fileName='trace')

# trace3D: for making animations of curves in 3D
def trace3D(xf, yf, zf, lin, xLimit=None, yLimit=None, zLimit=None,
            fileName='default', subPlot=None, oscCircle=None):
    import numpy as np
    from numpy import linalg as LA
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d.axes3d import Axes3D
    import matplotlib.animation as animation

    fig = plt.figure()

    ax = fig.add_subplot(1, 1, 1, projection='3d')

    # Add subplots of the normalized TNP vectors
    if subPlot:
        at = fig.add_subplot(4, 5, 5, projection='3d')
        an = fig.add_subplot(4, 5, 10, projection='3d')
        ab = fig.add_subplot(4, 5, 15, projection='3d')
        ac = fig.add_subplot(4, 5, 20, projection='3d')

    def animate(i):
        ax.clear()

        path, = ax.plot(xf(lin), yf(lin), zf(lin))
        T, = ax.plot([0], [0], [0])
        N, = ax.plot([0], [0], [0])
        B, = ax.plot([0], [0], [0])

        if oscCircle:
            osc, = ax.plot([0], [0], [0])

        # Clear previously drawn subplots of TNP vectors.
        # Redraw subplot "frames" and assign the first point to vectors.
        if subPlot:
            at.clear()
            an.clear()
            ab.clear()
            ac.clear()

            at.title.set_text('Tangent')
            at.set_xlim(-1.2, 1.2)
            at.set_ylim(-1.2, 1.2)
            at.set_zlim(-1.2, 1.2)

            an.title.set_text('Normal')
            an.set_xlim(-1.2, 1.2)
            an.set_ylim(-1.2, 1.2)
            an.set_zlim(-1.2, 1.2)

            ab.title.set_text('Binormal')
            ab.set_xlim(-1.2, 1.2)
            ab.set_ylim(-1.2, 1.2)
            ab.set_zlim(-1.2, 1.2)

            ac.title.set_text('Combination')
            ac.set_xlim(-1.2, 1.2)
            ac.set_ylim(-1.2, 1.2)
            ac.set_zlim(-1.2, 1.2)

            aTp, = at.plot([0], [0], [0])
            aT, = at.plot([0], [0], [0])
            aTn, = at.plot([0], [0], [0])
            aTb, = at.plot([0], [0], [0])
            aNp, = an.plot([0], [0], [0])
            aNt, = an.plot([0], [0], [0])
            aN, = an.plot([0], [0], [0])
            aNb, = an.plot([0], [0], [0])
            aBp, = ab.plot([0], [0], [0])
            aBt, = ab.plot([0], [0], [0])
            aBn, = ab.plot([0], [0], [0])
            aB, = ab.plot([0], [0], [0])
            aCP, = ac.plot([0], [0], [0])
            aCT, = ac.plot([0], [0], [0])
            aCN, = ac.plot([0], [0], [0])
            aCB, = ac.plot([0], [0], [0])

        if xLimit:
            ax.set_xlim(xLimit[0], xLimit[1])
        if yLimit:
            ax.set_ylim(yLimit[0], yLimit[1])
        if zLimit:
            ax.set_zlim(zLimit[0], zLimit[1])

        # Calculations for when only the initial points are present.
        if i == 0:
            dt = np.array([xf(lin[i+1]) - xf(lin[i]),
                           yf(lin[i+1]) - yf(lin[i]),
                           zf(lin[i+1]) - zf(lin[i])])

            tNorm = LA.norm(dt)
            t = dt/tNorm
            T.set_data([xf(lin[i]), xf(lin[i])+t[0]],
                       [yf(lin[i]), yf(lin[i])+t[1]])
            T.set_3d_properties([zf(lin[i]), zf(lin[i])+t[2]])

        # Calculations after the first step (still limited number of points).
        elif i == 1:
            s = np.array([xf(lin[i]), yf(lin[i]), zf(lin[i])])
            
            dt = np.array([xf(lin[i]) - xf(lin[i-1]),
                           yf(lin[i]) - yf(lin[i-1]),
                           zf(lin[i]) - zf(lin[i-1])])
            tOld = dt/LA.norm(dt)
            
            dt = np.array([xf(lin[i+1]) - xf(lin[i]),
                           yf(lin[i+1]) - yf(lin[i]),
                           zf(lin[i+1]) - zf(lin[i])])
            t = dt/LA.norm(dt)
            
            dn = t - tOld
            n = dn/LA.norm(dn)

            b = np.cross(t,n)
            
            k = LA.norm(dn)/LA.norm(dt)

            if oscCircle:
                oscRad = np.absolute(LA.norm(dt)/LA.norm(dn))
                oscPath = np.linspace(0, 2*np.pi, num=200*np.pi*oscRad)

                oscVecs = oscRad*(np.outer(t, np.cos(oscPath)) +
                                  np.outer(n, np.sin(oscPath)))

                oscP = oscRad*n + s

                osc.set_data(oscVecs[0] + oscP[0],
                             oscVecs[1] + oscP[1])
                osc.set_3d_properties(oscVecs[2] + oscP[2])
            
            T.set_data([xf(lin[i]), xf(lin[i])+t[0]],
                       [yf(lin[i]), yf(lin[i])+t[1]])
            T.set_3d_properties([zf(lin[i]), zf(lin[i])+t[2]])

            N.set_data([xf(lin[i]), xf(lin[i])+n[0]],
                       [yf(lin[i]), yf(lin[i])+n[1]])
            N.set_3d_properties([zf(lin[i]), zf(lin[i])+n[2]])

            B.set_data([xf(lin[i]), xf(lin[i])+b[0]],
                       [yf(lin[i]), yf(lin[i])+b[1]])
            B.set_3d_properties([zf(lin[i]), zf(lin[i])+b[2]])

            ax.text2D(0.2, 0.95, 'Curvature: ' + format(k, '.2f'),
                      transform=ax.transAxes, fontsize=11)

            if subPlot:
                aT.set_data([0, t[0]], [0, t[1]])
                aT.set_3d_properties([0, t[2]])
            
                aN.set_data([0, n[0]], [0, n[1]])
                aN.set_3d_properties([0, n[2]])

                aB.set_data([0, b[0]], [0, b[1]])
                aB.set_3d_properties([0, b[2]])

                aCT.set_data([0, t[0]], [0, t[1]])
                aCT.set_3d_properties([0, t[2]])
            
                aCN.set_data([0, n[0]], [0, n[1]])
                aCN.set_3d_properties([0, n[2]])

                aCB.set_data([0, b[0]], [0, b[1]])
                aCB.set_3d_properties([0, b[2]])

        # Once at least three points are present to calculate T, N, and P with.
        else:
            s = np.array([xf(lin[i-1]), yf(lin[i-1]), zf(lin[i-1])])
            
            dt = np.array([xf(lin[i-1]) - xf(lin[i-2]),
                           yf(lin[i-1]) - yf(lin[i-2]),
                           zf(lin[i-1]) - zf(lin[i-2])])
            tOld = dt/LA.norm(dt)
            
            dt = np.array([xf(lin[i]) - xf(lin[i-1]),
                           yf(lin[i]) - yf(lin[i-1]),
                           zf(lin[i]) - zf(lin[i-1])])
            t = dt/LA.norm(dt)

            dn = t - tOld
            n = dn/LA.norm(dn)

            b = np.cross(t,n)
            
            k = LA.norm(dn)/LA.norm(dt)

            if oscCircle:
                oscRad = np.absolute(LA.norm(dt)/LA.norm(dn))
                oscPath = np.linspace(0, 2*np.pi, num=200*np.pi*oscRad)

                oscVecs = oscRad*(np.outer(t, np.cos(oscPath)) +
                                  np.outer(n, np.sin(oscPath)))

                oscP = oscRad*n + s

                osc.set_data(oscVecs[0] + oscP[0],
                             oscVecs[1] + oscP[1])
                osc.set_3d_properties(oscVecs[2] + oscP[2])
            
            T.set_data([xf(lin[i]), xf(lin[i])+t[0]],
                       [yf(lin[i]), yf(lin[i])+t[1]])
            T.set_3d_properties([zf(lin[i]), zf(lin[i])+t[2]])
            
            N.set_data([xf(lin[i]), xf(lin[i])+n[0]],
                       [yf(lin[i]), yf(lin[i])+n[1]])
            N.set_3d_properties([zf(lin[i]), zf(lin[i])+n[2]])

            B.set_data([xf(lin[i]), xf(lin[i])+b[0]],
                       [yf(lin[i]), yf(lin[i])+b[1]])
            B.set_3d_properties([zf(lin[i]), zf(lin[i])+b[2]])

            ax.text2D(0.2, 0.95, 'Curvature: ' + format(k, '.2f'),
                      transform=ax.transAxes, fontsize=11)

            if subPlot:
                aT.set_data([0, t[0]], [0, t[1]])
                aT.set_3d_properties([0, t[2]])
            
                aN.set_data([0, n[0]], [0, n[1]])
                aN.set_3d_properties([0, n[2]])

                aB.set_data([0, b[0]], [0, b[1]])
                aB.set_3d_properties([0, b[2]])

                aCT.set_data([0, t[0]], [0, t[1]])
                aCT.set_3d_properties([0, t[2]])
            
                aCN.set_data([0, n[0]], [0, n[1]])
                aCN.set_3d_properties([0, n[2]])

                aCB.set_data([0, b[0]], [0, b[1]])
                aCB.set_3d_properties([0, b[2]])

    # Create the animation using the just defined animate() function.
    trace = animation.FuncAnimation(fig, animate,frames=len(lin),
                                    interval=20, blit=False)
    trace.save(fileName + '.mp4', fps=120)
    fig.show()
    
# trace2D: for making animations of curves in 2D    
def trace2D(xFunc, yFunc, tLine, xLimit=[-4,4], yLimit=[-4,4], fileName='default'):
    import numpy as np
    from numpy import linalg as LA
    import matplotlib.pyplot as plt
    from matplotlib import animation
    
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                         xlim=(xLimit[0], xLimit[1]), ylim=(yLimit[0], yLimit[1]))

    ax.grid()
    x = xFunc(tLine)
    y = yFunc(tLine)
    
    path, = ax.plot([], [], lw=1.25)
    t, = ax.plot([], [], lw=1.25)
    n, = ax.plot([], [], lw=1.25)
    curveText = ax.text(0.60, 0.95, '', transform=ax.transAxes, fontsize=11)
    tText = ax.text(0.58, 0.50, '', transform=ax.transAxes, fontsize=8)
    nText = ax.text(0.50, 0.58, '', transform=ax.transAxes, fontsize=8)

    def init():
        path.set_data(x, y)
        t.set_data([], [])
        n.set_data([], [])
        curveText.set_text('')
        tText.set_text('')
        nText.set_text('')
        
        return path, t, n, curveText, tText, nText

    def animate(i):
        path.set_data(x, y)
        if i == 0:
            dx = xFunc(tLine[i+1]) - xFunc(tLine[i])
            dy = yFunc(tLine[i+1]) - yFunc(tLine[i])

            nText.set_text('')
            n.set_data([], [])
            tNorm = LA.norm([dx, dy])
            
        elif i == 1:
            dx = xFunc(tLine[i]) - xFunc(tLine[i-1])
            dy = yFunc(tLine[i]) - yFunc(tLine[i-1])

            nText.set_text('')
            n.set_data([], [])
            tNorm = LA.norm([dx, dy])
            
        else:
            dx = xFunc(tLine[i-1]) - xFunc(tLine[i-2])
            dy = yFunc(tLine[i-1]) - yFunc(tLine[i-2])
            
            tNorm = LA.norm([dx, dy])

            tOld = np.array([dx/tNorm, dy/tNorm])

            dx = xFunc(tLine[i]) - xFunc(tLine[i-1])
            dy = yFunc(tLine[i]) - yFunc(tLine[i-1])
            
            tNorm = LA.norm([dx, dy])

            dn = np.array([dx/tNorm, dy/tNorm]) - tOld
            nNorm = LA.norm(dn)
            k = nNorm/tNorm

            nx = [xFunc(tLine[i]), xFunc(tLine[i])+(dn[0]/nNorm)*np.log(np.abs(k)+1)]
            ny = [yFunc(tLine[i]), yFunc(tLine[i])+(dn[1]/nNorm)*np.log(np.abs(k)+1)]

            nText.set_text('')
            nText.set_x(xFunc(tLine[i])+(dn[0]/nNorm)*1.2)
            nText.set_y(yFunc(tLine[i])+(dn[1]/nNorm)*1.2)
            
            curveText.set_text('Curvature: ' + format(k, '.2f'))
            n.set_data(nx, ny)

        tx = [xFunc(tLine[i]), xFunc(tLine[i])+(dx/tNorm)]
        ty = [yFunc(tLine[i]), yFunc(tLine[i])+(dy/tNorm)]

        tText.set_text('')
        tText.set_x(xFunc(tLine[i])+(dx/tNorm))
        tText.set_y(yFunc(tLine[i])+(dy/tNorm))

        t.set_data(tx, ty)
        
        return path, t, n, curveText, tText, nText
        

    trace = animation.FuncAnimation(fig, animate, init_func=init,
                                    frames=len(tLine), interval=20, blit=True)
    trace.save(fileName + '.mp4', fps=120)

    
main()
