import numpy as np
from wideboost.objectives import binarylogloss

def test_basic_value():
    X = np.zeros([1,1])
    B = np.ones([1,1])
    Y = np.ones([1,1])

    g,h = binarylogloss.binarylogloss_gradient_hessian(X,B,Y)
    ### g = P - Y
    ### h = P * (1-P)
    P = 0.5

    gmatches = g == P - 1
    hmatches = h == P * (1-P)

    assert gmatches and hmatches

# eventually deprecated
def test_old_v_new():
    np.random.seed(789)
    X = np.random.random([100,10])
    B = np.random.random([10,5])
    Y = np.random.random([100,5])

    g,h = binarylogloss.binarylogloss_gradient_hessian(X,B,Y)
    go,ho = binarylogloss.binarylogloss_gradient_hessian_old(X,B,Y)

    eps = 1e-8
    gmatches = np.max(np.abs(g - go)) < eps
    hmatches = np.max(np.abs(h - ho)) < eps

    assert gmatches and hmatches