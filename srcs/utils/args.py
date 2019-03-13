import json
from srcs.utils.log import logerr

"""
this file contains some function for the arguments

the arguments types must be
>>> python3 pgrm.py --argname=value

you just have to create an arg dict:
>>> all_args = dict(
...     <arg_name>=dict(
...         value=<def_value>,
...         type=[<type1>, [type2], ...],
...         argnames=[<argname1>, [argname2, ...]],
...         info=<info about this arg>,  # optional
...     ),
...     value=dict(
...         value=12,
...         type=[int, float],
...         argnames=['--value', '--val'],
...         info="this is the value",
...     ),
...    ...
... )

in the main program you just have to put:
>>> for arg in sys.argv[1:]:
...     if not setarg(all_args, arg):
...         exit(1)

if you want to have some others args:
>>> for arg in sys.argv[1:]:
...     if arg in ['--usage']:
...         print_usage(all_args, sys.argv[0])
...         exit(0)
...     if not setarg(all_args, arg):
...         exit(1)
"""


def print_usage(all_args, filename):
    print('usage: python3 %s [arg1=value1, ...]' % (filename))
    print('args list:')
    for key, arg_dict in all_args.items():
        types = ''
        for t in arg_dict['type']:
            if types is not '':
                types += ', '
            types += str(t).split("'")[1]
        info = ''
        if 'info' in arg_dict:
            info = ' ' + arg_dict['info']
        print('\t%s=%s  # [%s]%s' % (arg_dict['argnames'][0], str(arg_dict['value']), types, info))


def convert_from_str(data_str, types):
    """
    try ton convert the data to one of types (list of all possible types)
    return
        a boolean -> success or error
        the data converted (or None)
    """
    if str in types:
        return True, data_str
    try:
        value = json.loads(data_str)
    except (json.JSONDecodeError, IndexError):
        value = data_str
    if type(value) in types:
        return True, value
    return False, None


def setarg(all_args, arg):
    if '=' in arg and len(arg.split('=')) == 2:
        arg_name, arg_value = arg.split('=')
        for key, arg_dict in all_args.items():
            if arg_name in arg_dict['argnames']:
                if convert_from_str(arg_value, arg_dict['type'])[0]:
                    arg_dict['value'] = convert_from_str(arg_value, arg_dict['type'])[1]
                    return True
                logerr('in arg %s -> unable to convert %s to %s' % (arg, arg_value, str(arg_dict['type'])))
                return False
    logerr('invalid argument ->', arg)
    return False
