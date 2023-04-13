from matplotlib import pyplot as plt


def display_plot(points, curve, title="", legend=""):
    """
    :param points: 1-D array with control point [(x,y), ...]
    :param curve: 2-D array ex : [curve1, curve2 , ... curveN]
    :param title: string
    :param legend:  1-D array ex : ["legend_curve1", "legend_curve2" , ... ]
    :return:
    """

    # check if dimension error
    if len(curve) != len(legend):
        print("Error display_plot(), affichage dimension error ")
        return

    # Gestion d'erreur
    if len(curve) != len(legend):
        print("Error display_plot(), affichage dimension error ")
        return

    # display control point
    plt.plot([pt[0] for pt in points], [pt[1] for pt in points])

    # display all curves
    for i in range(len(curve)):
        plt.plot([pt[0] for pt in curve[i]], [pt[1] for pt in curve[i]], label=legend[i])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc="upper left")
    plt.title(title)
    plt.show()


def display_plot_3D(points, curve):
    """
    :param points: 1-D array with control point [(x,y,z), ...]
    :param curve: 2-D array ex : [curve1, curve2 , ... curveN]
    :param legend:  1-D array ex : ["legend_curve1", "legend_curve2" , ... ]
    :return:
    """

    plt.figure()
    ax = plt.axes(projection='3d')
    ax.grid()

    # Display points to follow
    x_point = [pt[0] for pt in points]
    y_point = [pt[1] for pt in points]
    z_point = [pt[2] for pt in points]
    ax.plot3D(x_point, y_point, z_point)

    # Display curve
    x_curve = [pt[0] for pt in curve]
    y_curve = [pt[1] for pt in curve]
    z_curve = [pt[2] for pt in curve]
    ax.plot3D(x_curve, y_curve, z_curve)

    # Set axes label
    ax.set_xlabel('x', labelpad=20)
    ax.set_ylabel('y', labelpad=20)
    ax.set_zlabel('z', labelpad=20)

    plt.show()

