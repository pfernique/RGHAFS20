import numpy as np
import math
from scipy.spatial import Delaunay, ConvexHull
from random import uniform
from pandas import DataFrame
from scipy.stats import f as F
from scipy.special import gamma

def radiuses(X, Y, Z, sort=True):
    if sort:
        return sorted(radiuses(X,Y,Z,False))
    else:
        return [x**2+y**2+z**2 for x, y, z in zip(X, Y, Z)]

def convex_hull_concentration(X, Y, Z, radius=float("inf"), nmin=3):
    r = [r < radius for r in radiuses(X, Y, Z, False)]
    X, Y, Z = X[r], Y[r], Z[r]
    n = sum(r)
    if n > nmin:
        pts = np.vstack((X, Y, Z)).T
        ch = ConvexHull(pts)
        dt = Delaunay(pts[ch.vertices])
        tets = dt.points[dt.simplices]
        def tetrahedron_volume(a, b, c, d):
            return np.abs(np.einsum('ij,ij->i', a-d, np.cross(b-d, c-d)))/6.
        vol = np.sum(tetrahedron_volume(tets[:, 0], tets[:, 1],
            tets[:, 2], tets[:, 3]))
        return n/vol
    else:
        return float("nan")

def gaussian_concentration(dataframe, unity, alpha=0.05):
    """
    """
    if dataframe.shape[0] > 1:
        X, Y, Z = SI(dataframe, unity)
        Sigma = np.cov(np.vstack((X, Y, Z)))
        U, axes, R = np.linalg.svd(Sigma)
        p, n = axes.size, min(len(X), len(Y), len(Z))
        fppf = F.ppf(1-alpha, p, n-p)*(n-1)*p*(n+1)/n/(n-p)
        axes = np.sqrt(axes*fppf)
        vol = (np.pi**(p/2)/gamma(p/2+1)* np.prod(axes))
        return (1-alpha)*dataframe.shape[0]/vol
    else:
        return float("nan")
"""
def convex_hull_concentration(dataframe, unity):
    if dataframe.shape[0] > 1:
        X, Y, Z = SI(dataframe, unity)
        pts = np.vstack((X, Y, Z)).T
        ch = ConvexHull(pts)
        dt = Delaunay(pts[ch.vertices])
        tets = dt.points[dt.simplices]
        def tetrahedron_volume(a, b, c, d):
            return np.abs(np.einsum('ij,ij->i', a-d, np.cross(b-d, c-d)))/6.
        vol = np.sum(tetrahedron_volume(tets[:, 0], tets[:, 1],
            tets[:, 2], tets[:, 3]))
        return dataframe.shape[0]/vol
    else:
        return float("nan")
"""
def simulate(n):
    simulation = []
    r = (3.*n/(4*np.pi))**(1./3.)
    while not len(simulation) == n:
        x, y, z = uniform(-r,r), uniform(-r,r), uniform(-r,r)
        if x**2+y**2+z**2 <= r:
            simulation.append([x, y, z])
    return DataFrame(simulation, columns=['X', 'Y', 'Z'])

