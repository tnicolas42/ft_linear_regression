import sys
import srcs.utils.const_utils as const_utils


def log(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
    """
    print only if we are in debug mode
    take exactly same params as print function
    """
    if const_utils.DEBUG:
        print(*objects, sep=sep, end=end, file=file, flush=flush)


def loginfo(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
    """
    print only if we are in debug mode
    take exactly same params as print function
    """
    if const_utils.DEBUG:
        print(const_utils.PR_INFO, *objects, sep=sep, end=end, file=file,
              flush=flush)


def logerr(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
    """
    print only if we are in debug mode
    take exactly same params as print function
    """
    if const_utils.DEBUG:
        print(const_utils.PR_ERROR, *objects, sep=sep, end=end, file=file,
              flush=flush)
