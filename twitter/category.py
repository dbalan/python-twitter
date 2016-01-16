#!/usr/bin/env python

import json


class Category(object):
    """ A class representing the suggested user category structure used
    by the twitter API.

    The Category structure exposes the following properties:
        category.name
        category.slug
        category.size
    """

    def __init__(self, **kwargs):
        """ An object to hold a Twitter suggested  user category.
        This class is normally instantiated by the twitter.Api class and
        returned in a sequence.

        Args:
            name:
                Name of the category
            slug:
                Slugified name of Category (a-zA-Z0-9-_ only)
            size:
                Number of users in Category
        """
        param_defaults = {
            'name': None,
            'slug': None,
            'size': None,
        }

        for (param, default) in param_defaults.items():
            setattr(self, param, kwargs.get(param, default))

    @property
    def Name(self):
        return self.name or False

    @property
    def Slug(self):
        return self.slug or False

    @property
    def Size(self):
        return self.size or False

    def __eq__(self, other):
        return other and \
            self.AsDict() == other.AsDict()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        """ A string representation of this twitter.Category instance.

        Returns:
            String representation containing name, slug, and size of
            category.
        """
        return "Category(Name={name}, Slug={slug}, Size={size})".format(
            name=self.name,
            slug=self.slug,
            size=self.size)

    def __str__(self):
        return self.AsJsonString()

    def AsDict(self):
        data = {}

        if self.name:
            data['name'] = self.name
        if self.slug:
            data['slug'] = self.slug
        if self.size:
            data['size'] = self.size

        return data

    def AsJsonString(self):
        return json.dumps(self.AsDict(), sort_keys=True)

    @staticmethod
    def NewFromJsonDict(data):
        """Create a new instance based on a JSON dict.

        Args:
            data: A JSON dict, as converted from the JSON in the twitter
            API.

        Returns:
            A twitter.Category instance
        """

        return Category(name=data.get('name', None),
                        slug=data.get('slug', None),
                        size=data.get('size', None))
