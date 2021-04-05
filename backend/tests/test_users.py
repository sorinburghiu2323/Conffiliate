from django.test import TestCase

from backend.serializers import MAX_USER_KEYWORDS


class UsersTest(TestCase):
    def test_post_users(self):
        """
        Testing creating new users.
        Endpoint: "/api/users/ - POST"
        """
        test_user = {
            "first_name": "Bad",
            "last_name": "User",
            "user_type": "influencer",
            "email": "user@user.com",
            "password": "123",  # Purposely bad password
        }

        # Empty body test.
        response = self.client.post("/api/users/", {})
        self.assertEqual(response.status_code, 400)

        # Bad password.
        response = self.client.post("/api/users/", test_user)
        self.assertEqual(response.status_code, 400)
        test_user["password"] = "Password1"  # Valid password

        # Too many keywords.
        keywords = []
        for i in range(MAX_USER_KEYWORDS + 1):
            keywords.append(str(i))
        test_user["keywords"] = keywords
        response = self.client.post("/api/users/", test_user)
        self.assertEqual(response.status_code, 400)
        test_user["keywords"] = []  # Valid keywords

        # Successful user creation.
        response = self.client.post("/api/users/", test_user)
        self.assertEqual(response.status_code, 201)

        # Create another user with the same email.
        response = self.client.post("/api/users/", test_user)
        self.assertEqual(response.status_code, 400)
        test_user["email"] = "new@email.com"  # New email
