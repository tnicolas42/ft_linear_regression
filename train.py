import sys
import srcs.const as const
import srcs.utils.args as args
from srcs.utils.log import loginfo
from srcs.files import export_theta, import_data, get_theta_in_args
from srcs.functions import check_theta, normalize, fit, set_theta_after_norm

"""
if --theta=[<float>, <float>] -> use this theta
else -> use the theta read in the file
"""

all_args = dict(
    learning_rate=dict(
        value=const.LEARNING_RATE,
        type=[float, int],
        argnames=['--learning_rate'],
    ),
    theta=dict(
        value=None,
        type=[list],
        argnames=['--theta'],
    ),
    nb_iter=dict(
        value=const.NB_ITER,
        type=[int],
        argnames=['--nb_iter'],
    ),
    data_filename=dict(
        value=const.DATA_FILENAME,
        type=[str],
        argnames=['--data', '--data_filename'],
    ),
    data_km=dict(
        value=const.DATA_KM,
        type=[str],
        argnames=['--data_km'],
    ),
    data_price=dict(
        value=const.DATA_PRICE,
        type=[str],
        argnames=['--data_price'],
    ),
    theta_filename=dict(
        value=const.THETA_FILENAME,
        type=[str],
        argnames=['--theta_filename'],
    ),
)


def start_train(all_args):
    theta = get_theta_in_args(all_args)
    if theta is None:
        exit(1)
    data, X, y = import_data(all_args)
    if data is None:
        exit(1)
    norm_X = normalize(X)
    loginfo('start train: learning_rate=%f, nb_iter=%d, theta=%s' %
            (all_args['learning_rate']['value'], all_args['nb_iter']['value'], str(theta)))
    theta, J_history = fit(norm_X, y, theta, all_args['learning_rate']['value'], all_args['nb_iter']['value'])
    theta = set_theta_after_norm(X, theta)
    loginfo('after train, new theta ->', theta)
    export_theta(all_args['theta_filename']['value'], theta)


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        if arg in ['--usage']:
            args.print_usage(all_args, sys.argv[0])
            exit(0)
        elif not args.setarg(all_args, arg):
            exit(1)

    if all_args['theta']['value'] is not None and not check_theta(all_args['theta']['value']):
        exit(1)

    start_train(all_args)
