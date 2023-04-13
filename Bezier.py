import numpy as np
import pascal as pa

"""
2A SRI Julian TRANI
"""


class Bezier:
    """
    Génération a Bezier curve in 2D or 3D with a given list of points
    """

    def __init__(self, points, Te=0.01):
        self.points = points
        self.nb_points = len(points)
        self.dimension = len(points[0])
        # points to generate curve
        self.curve = []
        self.Te = Te

    def __add_point(self, point):
        # dimension error
        if len(point) != self.dimension:
            print("error the point has an incorrect dimension")
        else:
            self.points.append(point)
            self.nb_points += 1

    def __generate_points(self):
        # Pascal triangle
        coeff_pa = pa.calculate_row(self.nb_points - 1)

        # generate curve point
        for u in np.arange(0, 1 + self.Te, self.Te):
            b = np.array([coeff_pa[i] * (u ** i) * (1 - u) ** (self.nb_points - 1 - i) for i in range(len(coeff_pa))])
            c = np.array([b[i] * np.array(self.points[i]) for i in range(len(b))])
            # add the new point to curve list
            self.curve.append(np.sum(c, axis=0))

    def get_curve(self):
        self.__generate_points()
        return self.curve
