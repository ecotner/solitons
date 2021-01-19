import sympy as sp
from typing import Union

from sympy.vector.functions import laplacian


def get_laplacian(n_dim: int, coord_sys: str):
    psi = sp.Function("\psi")
    if coord_sys == "euclidean":
        laplacian
        for i in range(n_dim):



def get_kinetic_term(kind: str, n_dim: int = 1, coord_sys: str = "euclidean"):
    """Gets the kinetic term associated with a specific field

    :param kind: the type of kinetic term to generate. options are "schrodinger"
    :type kind: str
    :param n_dim: number of dimensions, defaults to 1
    :type n_dim: int, optional
    :param coord_sys: coordinate system to use, defaults to "euclidean"
    :type coord_sys: str, optional
    """
    m = sp.symbols("m", positive=True)
    psi = sp.Function("\psi")
    if kind.lower() in ["schrodinger"]:
        K = -(1 / (2 * m)) * sp.diff(psi)
