from django.test import TestCase

from backend.models import Keyword


class KeywordsTest(TestCase):
    def setUp(self):
        Keyword.objects.create(name="talent")
        Keyword.objects.create(name="developer")
        Keyword.objects.create(name="very fun")
        self.keywords = Keyword.objects.all()

    def test_get_keywords(self):
        """
        Testing for getting existing keywords.
        Endpoint: "/api/keywords/ - GET"
        """
        response = self.client.get("/api/keywords/")
        self.assertEqual(response.status_code, 200)

        # All keywords result.
        expected = {
            "count": 3,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 1,
                    "name": "talent",
                },
                {
                    "id": 2,
                    "name": "developer",
                },
                {
                    "id": 3,
                    "name": "very fun",
                },
            ],
        }
        self.assertJSONEqual(response.content, expected)

        # Phrase filter.
        response = self.client.get("/api/keywords/", {"phrase": "fun"})
        expected = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 3,
                    "name": "very fun",
                }
            ],
        }
        self.assertJSONEqual(response.content, expected)
