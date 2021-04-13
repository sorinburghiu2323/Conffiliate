from django.core.management import BaseCommand

from backend.models import Platform, Keyword


class Command(BaseCommand):
    """
    Bootstrap command to populate the database with starting data.
    Run it with: python manage.py bootstrap
    """

    def handle(self, *args, **options):
        print("Initializing bootstrap...")

        # Create platforms.
        platforms = ["Facebook", "Instagram", "Tik Tok", "YouTube"]
        for platform in platforms:
            Platform.objects.get_or_create(name=platform)

        # Create keywords.
        keywords = [
            "influencer",
            "marketing",
            "sport",
            "media",
            "technology",
            "books",
            "education",
            "gaming",
            "cosplay",
            "clothing",
            "e-sports",
            "design",
            "food",
            "healthcare",
            "model",
            "makeup",
            "animals",
            "travel",
            "workout",
            "perfumes",
            "kids",
            "university",
        ]
        for keyword in keywords:
            Keyword.objects.get_or_create(name=keyword)

        print("Bootstrap finalized.")
