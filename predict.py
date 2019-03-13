import sys
import srcs.const as const
import srcs.utils.args as args
from srcs.utils.log import loginfo, logerr
from srcs.functions import check_theta, predict
from srcs.files import get_theta_in_args

"""
if --theta=[<float>, <float>] -> use this theta
else -> use the theta read in the file
"""

all_args = dict(
    theta=dict(
        value=None,
        type=[list],
        argnames=['--theta'],
    ),
    theta_filename=dict(
        value=const.THETA_FILENAME,
        type=[str],
        argnames=['--theta_filename'],
    ),
    data_predict=dict(
        value=None,
        type=[int, list],
        argnames=['--car_km', '--data_predict'],
    ),
)


def start_predict(all_args):
    theta = get_theta_in_args(all_args)
    if theta is None:
        exit(1)
    loginfo('using theta ->', theta)
    if all_args['data_predict']['value'] is None:
        try:
            all_args['data_predict']['value'] = [int(input('car km (int): '))]
        except ValueError:
            logerr('km should be an int')
            exit(1)

    for i in all_args['data_predict']['value']:
        print('for %8dkm -> estimated price: %d' % (i, predict(i, theta)))


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        if arg in ['--usage']:
            args.print_usage(all_args, sys.argv[0])
            exit(0)
        elif not args.setarg(all_args, arg):
            exit(1)

    if all_args['theta']['value'] is not None and not check_theta(all_args['theta']['value']):
        exit(1)

    if all_args['data_predict']['value'] is not None:
        if type(all_args['data_predict']['value']) is int:
            all_args['data_predict']['value'] = [all_args['data_predict']['value']]
        for data in all_args['data_predict']['value']:
            if type(data) is not int:
                logerr('we can predict only with int data')
                exit(1)

    start_predict(all_args)
