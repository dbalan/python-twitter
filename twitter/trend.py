#!/usr/bin/env python

import json


class Trend(object):
    """ A class representing a trending topic """

    def __init__(self, name=None, query=None, timestamp=None, url=None):
        self.name = name
        self.query = query
        self.timestamp = timestamp
        self.url = url

    def __repr__(self):
        return self.name.encode('utf-8')

    def __str__(self):
        return 'Name: %s\nQuery: %s\nTimestamp: %s\nSearch URL: %s\n' % \
               (self.name, self.query, self.timestamp, self.url)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        try:
            return other and \
                   self.name == other.name and \
                   self.query == other.query and \
                   self.timestamp == other.timestamp and \
                   self.url == self.url
        except AttributeError:
            return False

    def AsDict(self):
        """ A dict representation of this twitter.Trend instance.

        The return value uses the same key names as the JSON representation.

        Return:
            A dict representing this twitter.Trend instance
        """
        data = {}
        if self.name:
            data['name'] = self.name
        if self.query:
            data['query'] = self.query
        if self.timestamp:
            data['timestamp'] = self.timestamp
        if self.url:
            data['url'] = self.url
        return data

    def AsJsonString(self):
        """ A JSON string representation of this twitter.Trend instance.

        Returns:
            A JSON string representation of this twitter.Trend instance.
        """
        return json.dumps(self.AsDict(), sort_keys=True)

    @staticmethod
    def NewFromJsonDict(data, timestamp=None):
        """Create a new instance based on a JSON dict

        Args:
          data:
            A JSON dict
          timestamp:
            Gets set as the timestamp property of the new object

        Returns:
          A twitter.Trend object
        """
        return Trend(name=data.get('name', None),
                     query=data.get('query', None),
                     url=data.get('url', None),
                     timestamp=timestamp)
