import numpy as np
import srcs.const as const
from srcs.utils.log import logerr, loginfo
"""
this file contains utils fonctions
"""


def predict_float(X, theta):
    """
    predict and return a float (precise method)
    """
    return theta[0] + X * theta[1]


def predict_int(X, theta):
    """
    predict and retrun an int (or a list of int)
    this method is enouth for predict the price of a car
    """
    if type(X) is int:
        return int(theta[0] + X * theta[1])
    return np.array(theta[0] + X * theta[1], int)


def predict(X, theta, predict_method=predict_float):
    """
    predict one or a list of data with given values of theta
    """
    return predict_method(X, theta)


def normalize(X):
    """
    to train the model, we need to normalize the data
    """
    return (X - min(X)) / (max(X) - min(X))


def normalize_theta(X, theta):
    """
    in input we have a theta for non-normalized values.
    we need to update the theta to fit with normalised values

    theta0 + theta1 * x = theta0_norm + theta1_norm * x_norm
    we resolve this equation with min(X) and x max(X)
    """
    xmin = min(X)  # min value in X
    xmax = max(X)  # max value in X
    x1 = xmin  # we need to test with 2 value of X to determine the result
    x2 = xmax  # here we chose min and max values

    # we have some calcule to do to know the new values of theta
    res1 = theta[0] + theta[1] * x1
    res2 = theta[0] + theta[1] * x2

    theta[1] = (res1 - res2) / (min(normalize(X)) - max(normalize(X)))
    theta[0] = res1 - (((x1 - xmin) / (xmax - xmin)) * theta[1])
    return theta


def cost(X, y, theta):
    """
    this function is used to determine the cost with given theta values
    """
    return 1 / (2 * X.shape[0]) * sum((predict(X, theta) - y) ** 2)


def fit(X, y, theta, alpha, num_iters, auto_stop=False):
    """
    fit a dataset with only one parameter (using linear_regression)
    return (theta, cost_history)
    """
    m = X.shape[0]
    tmp = [0, 0]
    J_history = []

    for iter_ in range(num_iters):
        tmp[0] = theta[0] - alpha * 1 / m * sum((predict(X, theta) - y) * 1)
        tmp[1] = theta[1] - alpha * 1 / m * sum((predict(X, theta) - y) * X)
        theta[0] = tmp[0]
        theta[1] = tmp[1]

        J_history.append(cost(X, y, theta))
        if len(J_history) >= 2:

            # test is thecost increase
            if J_history[-1] - const.INCREASE_THRESHOLD > J_history[0]:  # the cost increase
                logerr('wrong value of alpha (%f), the cost inscrease -> stop fit' % (alpha))
                return theta, J_history

            # test is the fit is done
            if auto_stop:
                if J_history[-2] <= J_history[-1] + (const.STOP_THRESHOLD * alpha):
                    loginfo('auto stopped at %d iterations' % (iter_))
                    return theta, J_history

    return theta, J_history


def set_theta_after_norm(X, theta):
    """
    after a normalization x = (x - min) / (max - min), the value of the theta are not correct.
    we need to update the values with this function

    theta0 + theta1 * x = theta0_norm + theta1_norm * x_norm
    we resolve this equation with min(X) and x max(X)
    """
    xmin = min(X)  # min value in X
    xmax = max(X)  # max value in X
    x1 = xmin  # we need to test with 2 value of X to determine the result
    x2 = xmax  # here we chose min and max values

    # we have some calcule to do to know the new values of theta
    res1 = theta[0] + theta[1] * min(normalize(X))
    res2 = theta[0] + theta[1] * max(normalize(X))

    theta[1] = (res1 - res2) / (x1 - x2)
    theta[0] = res1 - (x1 * theta[1])
    return theta


def check_theta(theta):
    """
    check theta values
    """
    if type(theta) is not list:
        logerr('theta is not a list %s' % (theta))
        return False
    if len(theta) is not 2:
        logerr('invalid theta size (%d: excpected 2) -> %s' % (len(theta), theta))
        return False
    try:
        theta[0] = float(theta[0])
        theta[1] = float(theta[1])
    except (ValueError, TypeError):
        logerr('cannot convert theta values to float %s' % (theta))
        return False
    return True
