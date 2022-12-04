from datetime import datetime
import re

"""
This module contains utilities and common function related to generic task
"""


def get_formatted_tms(date_time_format="%d/%m/%Y %H:%M:%S") -> str:

    """Transform the current timestamp with a specific format

    Args:
        date_time_format: format of the datetime to return, default is %d/%m/%Y %H:%M:%S

    Returns:
        str: Formatted datetime string

    """

    tms = datetime.now()
    tms_login_formatted = tms.strftime(date_time_format)
    return tms_login_formatted


def mask_credentials(cred: str, mask_char="X") -> str:
    """Mask with a specific character all the string passed as parameters

    Args:
        cred: string to mask

    Returns:
        str: masked string

    """
    return re.sub(".", mask_char, cred)
