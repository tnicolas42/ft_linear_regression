import os
import json
import numpy as np
import pandas as pd
from srcs.functions import check_theta
from srcs.utils.log import logerr, loginfo

"""
import / export theta
import data
"""


def get_theta_in_args(all_args):
    if all_args['theta']['value'] is not None:
        theta = all_args['theta']['value']
    else:
        theta = import_theta(all_args['theta_filename']['value'])
    return theta


def import_theta(filename):
    if not os.path.isfile(filename):
        logerr('cannot import theta: %s is not a file' % (filename))
        return None

    with open(filename, 'r') as f:
        try:
            theta_data = json.load(f)
        except ValueError:
            logerr('cannot import theta')
            return None

    if not check_theta(theta_data):
        return None
    loginfo('import theta from %s' % (filename))
    return theta_data


def export_theta(filename, theta):
    try:
        with open(filename, 'w') as f:
            json.dump(theta, f)
    except (os.NotADirectoryError, os.FileNotFoundError):
        logerr('unable to write theta in', filename)
    loginfo('export theta in %s' % (filename))


def import_data(all_args):
    try:
        data = pd.read_csv(all_args['data_filename']['value'])
    except (pd.errors.ParserError, pd.errors.EmptyDataError):
        logerr('unable to read the csv:', all_args['data_filename']['value'])
        return None, None, None
    try:
        X = np.array(data[all_args['data_km']['value']])
    except KeyError:
        logerr('invalid column %s in the csv: %s' %
               (all_args['data_km']['value'], all_args['data_filename']['value']))
        return None, None, None
    try:
        y = np.array(data[all_args['data_price']['value']])
    except KeyError:
        logerr('invalid column %s in the csv: %s' %
               (all_args['data_price']['value'], all_args['data_filename']['value']))
        return None, None, None
    return data, X, y
