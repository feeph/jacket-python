#!/usr/bin/env python3
"""
<enter description>

this is the entrypoint for an AWS Lambda function
"""

# standard imports
import logging
import os
import sys

# extra imports (make sure to add to requirements.txt!)
# <add extra imports here>

from typing import Dict, Optional

sys.path.insert(0, os.path.dirname(__file__) + "/src")

# pylint: disable=wrong-import-position
import {{cookiecutter.pypackage_name}}


def lambda_handler(event: Dict, context: Dict) -> Optional[Dict]:
    """
    called by AWS Lambda
    """
    # <this is just an example - replace as needed>
    logging.debug("event:   %s", event)
    logging.debug("context: %s", context)
    values = os.environ.get('VALUES', [])
    result = {{cookiecutter.pypackage_name}}.{{cookiecutter.main_function}}(values)
    # </this is just an example - replace as needed>
    return result
