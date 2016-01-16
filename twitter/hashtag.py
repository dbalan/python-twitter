#!/usr/bin/env python

import json


class Hashtag(object):
    """ A class representing a twitter hashtag """

    def __init__(self,
                 text=None):
        self.text = text

    def __eq__(self, other):
        return other and \
            self.text == other.text

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return self.AsJsonString()

    def __repr__(self):
        return "Hashtag(Text={text})".format(text=self.text)

    def AsDict(self):
        data = {}

        if self.text:
            data['text'] = self.text

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
          A twitter.Hashtag instance
        """
        return Hashtag(text=data.get('text', None))

