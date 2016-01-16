#!/usr/bin/env python

import json


class Url(object):
    """A class representing an URL contained in a tweet"""

    def __init__(self,
                 url=None,
                 expanded_url=None):
        self.url = url
        self.expanded_url = expanded_url

    def __str__(self):
        return self.AsJsonString()

    def __repr__(self):
        return "URL(url={0}, expanded_url={1})".format(
            self.url,
            self.expanded_url)

    def __eq__(self, other):
        """ Compares two twitter.Url objects. """

        return other and \
            self.AsDict() == other.AsDict()

    def __ne__(self, other):
        return not self.__eq__(other)

    def AsDict(self):
        data = {}

        if self.url:
            data['url'] = self.url
        if self.expanded_url:
            data['expanded_url'] = self.expanded_url

        return data

    def AsJsonString(self):
        return json.dumps(self.AsDict(), sort_keys=True)

    @staticmethod
    def NewFromJsonDict(data):
        """Create a new instance based on a JSON dict.

        Args:
          data:
            A JSON dict, as converted from the JSON in the twitter API

        Returns:
          A twitter.Url instance
        """
        return Url(url=data.get('url', None),
                   expanded_url=data.get('expanded_url', None))
