import unittest
import responses
import twitter


class TestCategory(unittest.TestCase):

    def setUp(self):
        self.api = twitter.Api(consumer_key='test',
                               consumer_secret='test',
                               access_token_key='test',
                               access_token_secret='test')

    @responses.activate
    def test_category_methods(self):
        with open('testdata/get_user_suggestion_categories.json') as f:
            resp_data = f.read()
        responses.add(
            responses.GET,
            self.api.base_url + '/users/suggestions.json',
            body=resp_data)
        categories = self.api.GetUserSuggestionCategories()
        first_cat = categories[0]
        second_cat = categories[1]

        # test __eq__ / __ne__ methods
        self.assertFalse(first_cat == second_cat)
        self.assertTrue(first_cat == first_cat)
        self.assertTrue(first_cat != second_cat)

        # test representation/str
        repr_str = "Category(Name={0}, Slug={1}, Size={2})".format(
            first_cat.Name,
            first_cat.Slug,
            first_cat.Size)
        self.assertEqual(first_cat.__repr__(), repr_str)
        self.assertEqual(str(first_cat), first_cat.AsJsonString())

        cat_dict = first_cat.AsDict()
        self.assertEqual(cat_dict['name'], first_cat.name)
        self.assertEqual(cat_dict['slug'], first_cat.slug)
        self.assertEqual(cat_dict['size'], first_cat.size)
