class Floraison:

    def __init__(self, U, ptc, k):
        # ordre
        self.k = k

        self.dec = 0
        # not define yet
        self.u = None
        # res
        self.P = []
        self.Ptc = []

        # control points
        self.ptc = ptc
        # Nodal vector
        self.U = U

    def __get_dec(self):
        self.dec = 0
        while self.u > self.U[self.dec + self.k]:
            self.dec += 1

        # get all control point from dec to dec + k -1
        self.P = []
        for i in range(0, self.k):
            self.P.append(self.ptc[self.dec + i])

    def evalBspline(self, u):
        self.u = u

        # get the offset (dec)
        self.__get_dec()

        for j in range(self.k - 1):
            for i in range(self.k - 1 - j):
                term1 = ((self.U[self.dec + self.k + i] - u) / (
                        self.U[self.dec + self.k + i] - self.U[self.dec + i + 1 + j])) * self.P[i]
                term2 = ((u - self.U[self.dec + i + 1 + j]) / (
                        self.U[self.dec + self.k + i] - self.U[self.dec + i + 1 + j])) * self.P[
                            i + 1]

                self.P[i] = term1 + term2

        return self.P[0]
