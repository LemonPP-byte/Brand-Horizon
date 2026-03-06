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
AI_PROVIDER = "deepseek"  # "openai", "anthropic", or "deepseek"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "sk-0438686478f34f54aca3e27cee5c4a0a")
DEEPSEEK_BASE_URL = "https://api.deepseek.com"

# Selection settings
DAILY_BRAND_COUNT = 5
REPEAT_THRESHOLD_DAYS = 30  # Don't repeat brands within 30 days

# Scoring weights
SCORE_WEIGHTS = {
    "design": 0.4,
    "user_experience": 0.3,
    "innovation": 0.3
}

# Import extended categories
from categories_extended import EXTENDED_CATEGORIES, SEARCH_KEYWORDS

# Legacy categories (for backward compatibility)
CATEGORIES = [
    "Fashion & Apparel",
    "Beauty & Personal Care",
    "Home & Living",
    "Food & Beverage",
    "Health & Wellness",
    "Baby & Kids",
    "Pet Care",
    "Electronics & Tech",
    "Outdoor & Sports",
    "Personal Electronics"
]

# Regions
REGIONS = ["US", "UK", "EU", "Global", "Asia"]
