from srcs.utils.log import logerr
"""
this file contains utils fonctions
"""


def predict(X, theta):
    """
    predict one or a list of data with given values of theta
    """
    return theta[0] + X * theta[1]


def normalize(X):
    """
    to train the model, we need to normalize the data
    """
    return (X - min(X)) / (max(X) - min(X))


def cost(X, y, theta):
    """
    this function is used to determine the cost with given theta values
    """
    return 1 / (2 * X.shape[0]) * sum((predict(X, theta) - y) ** 2)


def fit(X, y, theta, alpha, num_iters, cost_function=None):
    """
    fit a dataset with only one parameter (using linear_regression)
    if cost_function is not None, save and return a cost history
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
        if cost_function is not None:
            J_history.append(cost_function(X, y, theta))

    return theta, J_history


def set_theta_after_norm(X, theta):
    """
    after a normalization x = (x - min) / (max - min), the value of the theta are not correct.
    we need to update the values with this function
    """
    xmin = min(X)  # min value in X
    xmax = max(X)  # max value in X
    x1 = xmin  # we need to test with 2 value of X to determine the result
    x2 = xmax  # here we chose min and max values

    # we have some calcule to do to know the new values of theta
    res1 = theta[0] + theta[1] * ((x1 - xmin) / (xmax - xmin))
    res2 = theta[0] + theta[1] * ((x2 - xmin) / (xmax - xmin))

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
