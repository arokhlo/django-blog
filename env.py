import os

# Secret key for Django
os.environ["SECRET_KEY"] = "django-insecure-your-secret-key-here-123456"

# Use SQLite for initial development (simpler)
os.environ["DATABASE_URL"] = "postgresql://neondb_owner:npg_FgsZR9MWb8Sr@ep-long-dust-aggdj4tj.c-2.eu-central-1.aws.neon.tech/alive_smell_rank_585650"  # Start with SQLite for development


# Debug mode
os.environ["DEBUG"] = "True"
