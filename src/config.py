"""
Brand Sites - Configuration
"""

import os

# Project paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
DOCS_DIR = os.path.join(BASE_DIR, "docs")
POSTS_DIR = os.path.join(DOCS_DIR, "_posts")
SUMMARIES_DIR = os.path.join(DATA_DIR, "summaries")

# Data files
BRANDS_FILE = os.path.join(DATA_DIR, "brands.json")
HISTORY_FILE = os.path.join(DATA_DIR, "history.json")

# AI Configuration
AI_PROVIDER = "openai"  # or "anthropic"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Selection settings
DAILY_BRAND_COUNT = 5
REPEAT_THRESHOLD_DAYS = 30  # Don't repeat brands within 30 days

# Scoring weights
SCORE_WEIGHTS = {
    "design": 0.4,
    "user_experience": 0.3,
    "innovation": 0.3
}

# Categories
CATEGORIES = [
    "Fashion",
    "Beauty",
    "Home",
    "Health",
    "Travel",
    "Food",
    "Tech",
    "Lifestyle"
]

# Regions
REGIONS = ["US", "UK", "EU", "Global"]
