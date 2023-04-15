import random

from Bezier import Bezier
from Bspline import Bspline
from tools_plot import display_plot, display_plot_3D
from NodalType import NodalType


def test_bspline():
    # Test points de controles carrés avec vecteur nodal UNIFORME
    points = [(0, 0), (0, 24), (24, 24), (24, 0), (0, 0), (0, 24)]
    k = 3
    curve0_uni = Bspline(k, points, NodalType.UNIFORME).get_curve()
    curve0_any = Bspline(k, points, NodalType.QUELCONQUE).get_curve()

    display_plot(points, [curve0_uni, curve0_any],
                 title="Affichage Bspline avec k=" + str(k),
                 legend=[NodalType.UNIFORME.__str__(), NodalType.QUELCONQUE.__str__()])

    # Test avec 13 points de controles aléatoires entre -15 et 15 en 2D
    points = [(5, 0), (10, 0), (15, 10), (10, 10), (20, 0), (25, 0)]
    k = 3
    curve0_uni = Bspline(k, points, NodalType.OUVERT_UNIFORME).get_curve()
    curve0_any = Bspline(k + 1, points, NodalType.OUVERT_UNIFORME).get_curve()

    display_plot(points, [curve0_uni, curve0_any],
                 title="Affichage Bspline avec " + NodalType.OUVERT_UNIFORME.__str__(),
                 legend=["k=" + str(k), "k=" + str(k + 1)])

    # OK
    # Test points de controles carrés avec vecteur nodal UNIFORME
    points = [(0, 0), (0, 24), (24, 24), (24, 0), (0, 0), (0, 24)]
    k = 3
    curve1 = Bspline(k, points, NodalType.UNIFORME).get_curve()
    curve1_k_plus_1 = Bspline(k + 1, points, NodalType.UNIFORME).get_curve()
    curve1_k_plus_2 = Bspline(k + 2, points, NodalType.UNIFORME).get_curve()

    display_plot(points, [curve1, curve1_k_plus_1, curve1_k_plus_2],
                 title="Affichage Bspline avec " + NodalType.UNIFORME.__str__(),
                 legend=["k=" + str(k), "k=" + str(k + 1), "k=" + str(k + 2)])

    # Test points de controles carrés avec vecteur nodal OUVERT UNIFORME
    points = [(0, 0), (0, 24), (24, 24), (24, 0), (0, 0), (0, 24)]
    k = 3
    curve2 = Bspline(k, points, NodalType.OUVERT_UNIFORME).get_curve()
    curve2_k_plus_1 = Bspline(k + 1, points, NodalType.OUVERT_UNIFORME).get_curve()
    curve2_k_plus_2 = Bspline(k + 2, points, NodalType.OUVERT_UNIFORME).get_curve()

    display_plot(points, [curve2, curve2_k_plus_1, curve2_k_plus_2],
                 title="Affichage Bspline avec " + NodalType.OUVERT_UNIFORME.__str__(),
                 legend=["k=" + str(k), "k=" + str(k + 1), "k=" + str(k + 2)])

    # Test de la lettre C
    points = [(1, 6), (0, 8), (3, 9), (5, 7), (7, 5), (9, 5), (10, 7), (9, 10),
              (7, 10), (5, 7), (3, 4), (3, 1), (5, 0), (8, 0), (9, 1)]
    k = 4
    curve3_uniform = Bspline(k, points, NodalType.UNIFORME).get_curve()
    curve3_open_uniform = Bspline(k, points, NodalType.OUVERT_UNIFORME).get_curve()
    curve3_any = Bspline(k, points, NodalType.QUELCONQUE).get_curve()

    display_plot(points, [curve3_uniform, curve3_open_uniform, curve3_any],
                 title="Affichage Bspline avec k=" + str(k),
                 legend=[NodalType.UNIFORME.__str__(), NodalType.OUVERT_UNIFORME.__str__(),
                         NodalType.QUELCONQUE.__str__()])


def test_bezier():
    # Test avec 4/5 points de controles
    points = [(0, 32), (20, 32), (20, 25), (10, 25), (20, 0)]
    curve = Bezier(points).get_curve()
    display_plot(points, [curve],
                 title="Affichage courbe de Bézier avec " + str(len(points)) + " points de controles",
                 legend=["Courbe de Bézier"])

    # Test avec une boucle
    points = [(5, 0), (10, 0), (12.5, 5), (15, 10), (10, 10), (15, 5), (20, 0), (25, 0)]
    curve = Bezier(points).get_curve()
    display_plot(points, [curve],
                 title="Affichage courbe de Bézier avec " + str(len(points)) + " points de controles",
                 legend=["Courbe de Bézier"])

    curve_boucle_sans_morceau = Bezier(points).get_curve()

    # Test de la lettre C avec morceau
    all_points = [points[:3], points[2:6], points[5:]]
    curve_boucle_avec_morceau = []
    for pt in all_points:
        curve_boucle_avec_morceau += Bezier(pt).get_curve()

    display_plot(points, [curve_boucle_sans_morceau, curve_boucle_avec_morceau],
                 title="Affichage courbe de Bézier d'une boucle", legend=["sans morceau", "par morceau"])

    # Test avec 5 points de controles aléatoires entre -15 et 15 en 3D
    points = [(random.randint(-15, 15), random.randint(-15, 15), random.randint(-15, 15)) for i in range(5)]
    curve = Bezier(points).get_curve()
    display_plot_3D(points, curve)

    # Test de la lettre C
    points = [(1, 6), (0, 8), (3, 9), (5, 7), (7, 5), (9, 5), (10, 7), (9, 10),
              (7, 10), (5, 7), (3, 4), (3, 1), (5, 0), (8, 0), (9, 1)]
    b_lettre_c_sans_morceau = Bezier(points).get_curve()

    # Test de la lettre C avec morceau
    all_points = [points[:4], points[3:10], points[9:]]
    b_lettre_c_avec_morceau = []
    for pt in all_points:
        b_lettre_c_avec_morceau += Bezier(pt).get_curve()

    display_plot(points, [b_lettre_c_sans_morceau, b_lettre_c_avec_morceau],
                 title="Affichage de la lettre C", legend=["sans morceau", "par morceau"])


if __name__ == '__main__':
    test_bezier()
    test_bspline()
