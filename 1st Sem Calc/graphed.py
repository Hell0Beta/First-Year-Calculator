import numpy as np
import matplotlib.pyplot as plt


def fun(Px, Py):
    # Enter x and y coordinates of points and colors
    xs = Px
    ys = Py

    colorable = ["m", "r", "g", "b", "g","m", "r", "g", "b", "g","m", "r", "g", "b", "g","m", "r", "g", "b", "g"]
    colors = (colorable[0:(len(Px))])
    axes_x = max(Px)
    axes_x += 10
    axes_y = max(Py)
    axes_y += 10

    axes_x_neg, axes_y_neg = -1, -1
    for i in Px:
        if i < 0:
            axes_x_neg = min(Px) - 5
            print(axes_x_neg)

    for i in Py:
        if i < 0:
            axes_y_neg = min(Py) - 5



    # Select length of axes and the space between tick labels
    xmin, xmax, ymin, ymax = axes_x_neg, axes_x, axes_y_neg, axes_y

    if axes_x > axes_y:
        ticked = axes_x/5
    else:
        ticked = axes_y/10
    ticks_frequency = int(ticked)

    # Plot points
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.scatter(xs, ys, c=colors)

    # Draw lines connecting points to axes
    for x, y, c in zip(xs, ys, colors):
        ax.plot([x, x], [0, y], c=c, ls='--', lw=1.5, alpha=0.5)
        ax.plot([0, x], [y, y], c=c, ls='--', lw=1.5, alpha=0.5)

    # Set identical scales for both axes
    ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')

    # Set bottom and left spines as x and y axes of coordinate system
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Create 'x' and 'y' labels placed at the end of the axes
    ax.set_xlabel('a', size=14, labelpad=-24, x=1.03)
    ax.set_ylabel('ib', size=14, labelpad=-21, y=1.02, rotation=0)

    # Create custom major ticks to determine position of tick labels
    x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
    y_ticks = np.arange(ymin, ymax+1, ticks_frequency)
    ax.set_xticks(x_ticks[x_ticks != 0])
    ax.set_yticks(y_ticks[y_ticks != 0])

    # Create minor ticks placed at each integer to enable drawing of minor grid
    # lines: note that this has no effect in this example with ticks_frequency=1
    ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
    ax.set_yticks(np.arange(ymin, ymax+1), minor=True)

    # Draw major and minor grid lines
    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

    # Draw arrows
    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)

    #plt.savefig("imaginary_graph.png")
    print(Px, " ", Py)
    plt.show()

