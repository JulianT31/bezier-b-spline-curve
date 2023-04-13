# Bezier & B-Spline curve

This project provide to create 

## Installation

The code needs These libraries to run :

```bash
pip install pascal-tri
pip install numpy
pip install matplotlib
```

## Example of execution

Run main or create un example such as the following code :

Create a list with all your points with 2 coordinates just like this :

```python
points = [(0, 32), (20, 32), (20, 25), (10, 25), (20, 0)]
```

Then, use the Bezier and BSpline class to generate curve like this : 

```python
curve = Bezier(points).get_curve()
# or 
k = 3
curve2 = Bspline(k, points, NodalType.UNIFORME).get_curve()
```

Here is an illustration of a Bezier curve :

![Bezier curve](/assets/beziers/lettre_c_sans_m_2.png)