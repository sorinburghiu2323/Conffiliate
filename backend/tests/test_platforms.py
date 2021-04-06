from django.test import TestCase

from backend.models import Platform


class PlatformsTest(TestCase):
    def setUp(self):
        Platform.objects.create(name="instagram")
        Platform.objects.create(name="tik tok")
        Platform.objects.create(name="youtube")
        self.platforms = Platform.objects.all()

    def test_get_platforms(self):
        """
        Testing for getting existing platforms.
        Endpoint: "/api/platforms/ - GET"
        """
        response = self.client.get("/api/platforms/")
        self.assertEqual(response.status_code, 200)

        # All platforms result.
        expected = {
            "count": 3,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 1,
                    "name": "instagram",
                },
                {
                    "id": 2,
                    "name": "tik tok",
                },
                {
                    "id": 3,
                    "name": "youtube",
                },
            ],
        }
        self.assertJSONEqual(response.content, expected)

        # Phrase filter.
        response = self.client.get("/api/platforms/", {"phrase": "tik tok"})
        expected = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 2,
                    "name": "tik tok",
                }
            ],
        }
        self.assertJSONEqual(response.content, expected)
