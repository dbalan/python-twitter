# encoding: utf-8

from types import FunctionType, MethodType
import unittest

import twitter


class TwitterCompletenessTests(unittest.TestCase):

    """ Tests to ensure that all twitter objects contain at least the following
    methods:
        __eq__,
        __ne__,
        __str__,
        __repr__,
        AsDict,
        NewFromJsonDict,
        AsJsonString
    """

    def test_object_completeness(self):
        objects = [
            twitter.Trend,
            twitter.Status,
            twitter.List,
            twitter.Media,
            twitter.Category,
            twitter.DirectMessage,
            twitter.UserStatus,
            twitter.User,
            twitter.Url,
            twitter.Hashtag,
        ]

        for obj in objects:
            object_methods = [x for x, y in obj.__dict__.items() if type(y) is FunctionType or MethodType]
            expected_methods = [
                '__eq__',
                '__ne__',
                '__str__',
                '__repr__',
                'AsDict',
                'AsJsonString',
                'NewFromJsonDict',
            ]

            for expected_method in expected_methods:
                self.assertIn(
                    expected_method,
                    object_methods,
                    "Unable to find '{0}' in {1}".format(expected_method, obj))
