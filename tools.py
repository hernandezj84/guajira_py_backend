"""Provides different types of tool to help the other modules"""

import time

class Tools:
    """Provides tools that will help to operate with data
    """

    def get_time(self):
        """Returns mktime of current time"""
        return time.mktime(time.localtime())
