import logging
import os

import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:

    @staticmethod
    def getLogger():
        return logging.getLogger(os.environ.get('PYTEST_CURRENT_TEST'))