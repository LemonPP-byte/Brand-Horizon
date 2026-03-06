"""
Extended Categories and Keywords for Consumer Brands
Covers all consumer product categories with 60-70 search keywords
"""

# Extended category hierarchy with subcategories
EXTENDED_CATEGORIES = {
    "Fashion & Apparel": {
        "subcategories": [
            "Footwear",
            "Activewear & Sportswear",
            "Denim & Casual Wear",
            "Outerwear & Jackets",
            "Underwear & Intimates",
            "Accessories & Jewelry",
            "Eyewear",
            "Watches",
            "Bags & Luggage",
            "Sustainable Fashion"
        ]
    },
    "Beauty & Personal Care": {
        "subcategories": [
            "Skincare",
            "Makeup & Cosmetics",
            "Haircare",
            "Fragrance",
            "Men's Grooming",
            "Clean Beauty",
            "K-Beauty & J-Beauty",
            "Nail Care",
            "Bath & Body"
        ]
    },
    "Home & Living": {
        "subcategories": [
            "Furniture",
            "Bedding & Linens",
            "Mattresses & Sleep",
            "Home Decor",
            "Kitchenware & Cookware",
            "Lighting",
            "Storage & Organization",
            "Smart Home",
            "Plants & Gardening"
        ]
    },
    "Food & Beverage": {
        "subcategories": [
            "Snacks & Chips",
            "Coffee & Tea",
            "Meal Kits & Prepared Foods",
            "Protein & Nutrition",
            "Chocolate & Candy",
            "Beverages & Drinks",
            "Alcohol & Wine",
            "Specialty Foods",
            "Baby Food & Formula"
        ]
    },
    "Health & Wellness": {
        "subcategories": [
            "Vitamins & Supplements",
            "Fitness Equipment",
            "Sexual Wellness",
            "Mental Health & Meditation",
            "Sleep & Recovery",
            "Women's Health",
            "Men's Health",
            "CBD & Hemp Products",
            "Medical Devices"
        ]
    },
    "Baby & Kids": {
        "subcategories": [
            "Baby Gear & Strollers",
            "Diapers & Wipes",
            "Baby Clothing",
            "Toys & Games",
            "Kids Furniture",
            "Educational Products",
            "Baby Food & Feeding"
        ]
    },
    "Pet Care": {
        "subcategories": [
            "Pet Food",
            "Pet Toys & Accessories",
            "Pet Health & Wellness",
            "Pet Furniture & Beds"
        ]
    },
    "Electronics & Tech": {
        "subcategories": [
            "Audio & Headphones",
            "Wearables & Smartwatches",
            "Phone Accessories",
            "Cameras & Photography",
            "Gaming Accessories",
            "Smart Devices"
        ]
    },
    "Outdoor & Sports": {
        "subcategories": [
            "Camping & Hiking",
            "Cycling",
            "Water Sports",
            "Fitness & Yoga",
            "Golf",
            "Running"
        ]
    },
    "Personal Electronics": {
        "subcategories": [
            "E-readers & Tablets",
            "Laptops & Computers",
            "Phone Cases & Protection"
        ]
    }
}

# 60-70 search keywords covering all consumer product categories
SEARCH_KEYWORDS = [
    # Fashion & Apparel (13 keywords)
    "sustainable fashion brand",
    "direct-to-consumer shoes",
    "minimalist clothing brand",
    "activewear brand",
    "denim brand",
    "luxury accessories",
    "eyewear brand",
    "watch brand",
    "jewelry brand",
    "luggage brand",
    "underwear brand",
    "outerwear brand",
    "sustainable footwear",

    # Beauty & Personal Care (11 keywords)
    "clean beauty brand",
    "skincare brand",
    "makeup brand",
    "haircare brand",
    "men's grooming",
    "fragrance brand",
    "k-beauty brand",
    "natural cosmetics",
    "vegan beauty",
    "anti-aging skincare",
    "organic beauty",

    # Home & Living (10 keywords)
    "modern furniture brand",
    "mattress brand",
    "bedding brand",
    "home decor brand",
    "kitchenware brand",
    "smart home brand",
    "lighting brand",
    "sustainable furniture",
    "luxury linens",
    "cookware brand",

    # Food & Beverage (10 keywords)
    "healthy snacks brand",
    "coffee brand",
    "meal kit delivery",
    "protein bar brand",
    "craft beverage",
    "specialty food brand",
    "organic food brand",
    "chocolate brand",
    "tea brand",
    "nutrition brand",

    # Health & Wellness (10 keywords)
    "vitamin brand",
    "supplement brand",
    "fitness equipment",
    "wellness brand",
    "meditation app",
    "sexual wellness",
    "women's health",
    "cbd brand",
    "sleep aid brand",
    "mental health app",

    # Baby & Kids (5 keywords)
    "baby products brand",
    "kids toys brand",
    "baby gear brand",
    "children's furniture",
    "baby food brand",

    # Pet Care (4 keywords)
    "pet food brand",
    "dog toys brand",
    "pet wellness",
    "pet accessories",

    # Electronics & Tech (4 keywords)
    "headphones brand",
    "smartwatch brand",
    "audio brand",
    "wearable tech",

    # Outdoor & Sports (3 keywords)
    "outdoor gear brand",
    "yoga brand",
    "camping equipment"
]

# Verify we have 60-70 keywords
assert 60 <= len(SEARCH_KEYWORDS) <= 70, f"Expected 60-70 keywords, got {len(SEARCH_KEYWORDS)}"

print(f"Total search keywords: {len(SEARCH_KEYWORDS)}")
