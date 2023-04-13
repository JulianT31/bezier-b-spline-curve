import random

import numpy as np

from Floraison import Floraison
from NodalType import NodalType
from tools_plot import display_plot


class Bspline:
    def __init__(self, k, points, type_vec_nodal, Te=0.01):
        # conversion tuple to array
        self.points = np.asarray(points)
        self.nb_points = len(points)
        self.k = k

        # init vec nodal
        self.vec_nodal = self.__generate_vec_nodal(type_vec_nodal)
        print(self.vec_nodal)

        self.curve = []
        self.Te = Te

    def __generate_vec_nodal(self, type_vec_nodal):
        if type_vec_nodal == NodalType.UNIFORME:
            return [i for i in range(self.k + self.nb_points)]
        elif type_vec_nodal == NodalType.OUVERT_UNIFORME:
            # generate vec nodal
            first = [0 for i in range(self.k)]
            mid = [i for i in range(1, (self.k + self.nb_points - 1) - 2 * self.k + 2)]
            end = [mid[-1] + 1 for i in range(self.k)]
            return first + mid + end
        else:
            return [i * 10 + random.randint(1, 10) for i in range(self.k + self.nb_points)]

    def one_point(self, u):
        f = Floraison(self.vec_nodal, self.points, self.k)
        return f.evalBspline(u)

    def get_curve(self):
        f = Floraison(self.vec_nodal, self.points, self.k)

        # definition interval for u (table indice)
        def_min = self.vec_nodal[self.k - 1]
        def_max = self.vec_nodal[self.nb_points]

        self.curve = []
        # get for each u value the points
        for u in np.arange(def_min, def_max, self.Te):
            self.curve.append(f.evalBspline(u))
            # self.curve.append(f.evalBspline(4.5))

        return self.curve
