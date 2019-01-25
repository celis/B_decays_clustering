#!/usr/bin/env python3

import os

ENV_VAR_TESTING_MODE = "B_decays_clustering_TESTMODE"


def set_testing_mode(testing_mode: bool) -> None:
    """
    Set an environment variable signalling if we are in testing mode.
    
    Args:
        testing_mode (bool): True if we are in testing mode 

    Returns:
        None
    """
    if testing_mode:
        os.environ[ENV_VAR_TESTING_MODE] = "true"
    else:
        os.environ[ENV_VAR_TESTING_MODE] = "false"


def is_testing_mode():
    testing_mode = os.environ[ENV_VAR_TESTING_MODE]
    if testing_mode == "true":
        return True
    elif testing_mode == "false":
        return False
    else:
        raise ValueError("{} set to invalid value {}.".format(
            ENV_VAR_TESTING_MODE, testing_mode))
