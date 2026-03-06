"""
Brand Discovery Tool
Uses search keywords to discover and collect consumer brands
"""

import json
import os
from typing import List, Dict
from datetime import datetime
from categories_extended import SEARCH_KEYWORDS, EXTENDED_CATEGORIES
from config import BRANDS_FILE, DATA_DIR


class BrandDiscovery:
    def __init__(self):
        self.keywords = SEARCH_KEYWORDS
        self.categories = EXTENDED_CATEGORIES
        self.discovered_brands = []

    def get_category_from_keyword(self, keyword: str) -> tuple:
        """Map keyword to category and subcategory"""
        keyword_lower = keyword.lower()

        # Fashion & Apparel
        if any(term in keyword_lower for term in ['fashion', 'shoes', 'clothing', 'footwear', 'denim', 'activewear', 'underwear', 'outerwear', 'accessories', 'jewelry', 'eyewear', 'watch', 'luggage', 'handbag']):
            if 'shoes' in keyword_lower or 'footwear' in keyword_lower:
                return ("Fashion & Apparel", "Footwear")
            elif 'activewear' in keyword_lower:
                return ("Fashion & Apparel", "Activewear & Sportswear")
            elif 'denim' in keyword_lower:
                return ("Fashion & Apparel", "Denim & Casual Wear")
            elif 'underwear' in keyword_lower:
                return ("Fashion & Apparel", "Underwear & Intimates")
            elif 'eyewear' in keyword_lower:
                return ("Fashion & Apparel", "Eyewear")
            elif 'watch' in keyword_lower:
                return ("Fashion & Apparel", "Watches")
            elif 'luggage' in keyword_lower or 'handbag' in keyword_lower:
                return ("Fashion & Apparel", "Bags & Luggage")
            elif 'jewelry' in keyword_lower or 'accessories' in keyword_lower:
                return ("Fashion & Apparel", "Accessories & Jewelry")
            else:
                return ("Fashion & Apparel", "Sustainable Fashion")

        # Beauty & Personal Care
        elif any(term in keyword_lower for term in ['beauty', 'skincare', 'makeup', 'cosmetics', 'haircare', 'grooming', 'fragrance', 'nail']):
            if 'skincare' in keyword_lower:
                return ("Beauty & Personal Care", "Skincare")
            elif 'makeup' in keyword_lower or 'cosmetics' in keyword_lower:
                return ("Beauty & Personal Care", "Makeup & Cosmetics")
            elif 'hair' in keyword_lower:
                return ("Beauty & Personal Care", "Haircare")
            elif 'grooming' in keyword_lower:
                return ("Beauty & Personal Care", "Men's Grooming")
            elif 'fragrance' in keyword_lower:
                return ("Beauty & Personal Care", "Fragrance")
            elif 'nail' in keyword_lower:
                return ("Beauty & Personal Care", "Nail Care")
            else:
                return ("Beauty & Personal Care", "Clean Beauty")

        # Home & Living
        elif any(term in keyword_lower for term in ['furniture', 'mattress', 'bedding', 'home', 'kitchen', 'lighting', 'decor', 'linens', 'cookware']):
            if 'furniture' in keyword_lower:
                return ("Home & Living", "Furniture")
            elif 'mattress' in keyword_lower:
                return ("Home & Living", "Mattresses & Sleep")
            elif 'bedding' in keyword_lower or 'linens' in keyword_lower:
                return ("Home & Living", "Bedding & Linens")
            elif 'kitchen' in keyword_lower or 'cookware' in keyword_lower:
                return ("Home & Living", "Kitchenware & Cookware")
            elif 'lighting' in keyword_lower:
                return ("Home & Living", "Lighting")
            elif 'smart home' in keyword_lower:
                return ("Home & Living", "Smart Home")
            else:
                return ("Home & Living", "Home Decor")

        # Food & Beverage
        elif any(term in keyword_lower for term in ['food', 'snacks', 'coffee', 'tea', 'meal', 'protein', 'chocolate', 'beverage', 'nutrition']):
            if 'snacks' in keyword_lower:
                return ("Food & Beverage", "Snacks & Chips")
            elif 'coffee' in keyword_lower:
                return ("Food & Beverage", "Coffee & Tea")
            elif 'meal' in keyword_lower:
                return ("Food & Beverage", "Meal Kits & Prepared Foods")
            elif 'protein' in keyword_lower or 'nutrition' in keyword_lower:
                return ("Food & Beverage", "Protein & Nutrition")
            elif 'chocolate' in keyword_lower:
                return ("Food & Beverage", "Chocolate & Candy")
            elif 'tea' in keyword_lower:
                return ("Food & Beverage", "Coffee & Tea")
            else:
                return ("Food & Beverage", "Specialty Foods")

        # Health & Wellness
        elif any(term in keyword_lower for term in ['vitamin', 'supplement', 'fitness', 'wellness', 'meditation', 'sexual', 'health', 'cbd', 'sleep aid', 'mental']):
            if 'vitamin' in keyword_lower or 'supplement' in keyword_lower:
                return ("Health & Wellness", "Vitamins & Supplements")
            elif 'fitness' in keyword_lower:
                return ("Health & Wellness", "Fitness Equipment")
            elif 'sexual' in keyword_lower:
                return ("Health & Wellness", "Sexual Wellness")
            elif 'meditation' in keyword_lower or 'mental' in keyword_lower:
                return ("Health & Wellness", "Mental Health & Meditation")
            elif 'sleep' in keyword_lower:
                return ("Health & Wellness", "Sleep & Recovery")
            elif 'women' in keyword_lower:
                return ("Health & Wellness", "Women's Health")
            elif 'cbd' in keyword_lower:
                return ("Health & Wellness", "CBD & Hemp Products")
            else:
                return ("Health & Wellness", "Vitamins & Supplements")

        # Baby & Kids
        elif any(term in keyword_lower for term in ['baby', 'kids', 'children', 'toys']):
            if 'toys' in keyword_lower:
                return ("Baby & Kids", "Toys & Games")
            elif 'gear' in keyword_lower:
                return ("Baby & Kids", "Baby Gear & Strollers")
            elif 'furniture' in keyword_lower:
                return ("Baby & Kids", "Kids Furniture")
            elif 'food' in keyword_lower:
                return ("Baby & Kids", "Baby Food & Feeding")
            else:
                return ("Baby & Kids", "Baby Gear & Strollers")

        # Pet Care
        elif any(term in keyword_lower for term in ['pet', 'dog', 'cat']):
            if 'food' in keyword_lower:
                return ("Pet Care", "Pet Food")
            elif 'toys' in keyword_lower:
                return ("Pet Care", "Pet Toys & Accessories")
            elif 'wellness' in keyword_lower or 'health' in keyword_lower:
                return ("Pet Care", "Pet Health & Wellness")
            else:
                return ("Pet Care", "Pet Toys & Accessories")

        # Electronics & Tech
        elif any(term in keyword_lower for term in ['headphones', 'audio', 'smartwatch', 'wearable', 'phone', 'tech']):
            if 'headphones' in keyword_lower or 'audio' in keyword_lower:
                return ("Electronics & Tech", "Audio & Headphones")
            elif 'smartwatch' in keyword_lower or 'wearable' in keyword_lower:
                return ("Electronics & Tech", "Wearables & Smartwatches")
            elif 'phone' in keyword_lower:
                return ("Electronics & Tech", "Phone Accessories")
            else:
                return ("Electronics & Tech", "Smart Devices")

        # Outdoor & Sports
        elif any(term in keyword_lower for term in ['outdoor', 'camping', 'cycling', 'yoga', 'hiking', 'sports']):
            if 'camping' in keyword_lower or 'hiking' in keyword_lower:
                return ("Outdoor & Sports", "Camping & Hiking")
            elif 'cycling' in keyword_lower:
                return ("Outdoor & Sports", "Cycling")
            elif 'yoga' in keyword_lower:
                return ("Outdoor & Sports", "Fitness & Yoga")
            else:
                return ("Outdoor & Sports", "Camping & Hiking")

        # Default
        return ("Lifestyle", "General")

    def generate_search_plan(self) -> Dict:
        """Generate a search plan with all keywords organized by category"""
        plan = {
            "total_keywords": len(self.keywords),
            "categories": {},
            "keywords": []
        }

        for keyword in self.keywords:
            category, subcategory = self.get_category_from_keyword(keyword)

            if category not in plan["categories"]:
                plan["categories"][category] = {
                    "count": 0,
                    "subcategories": {},
                    "keywords": []
                }

            plan["categories"][category]["count"] += 1
            plan["categories"][category]["keywords"].append(keyword)

            if subcategory not in plan["categories"][category]["subcategories"]:
                plan["categories"][category]["subcategories"][subcategory] = []

            plan["categories"][category]["subcategories"][subcategory].append(keyword)

            plan["keywords"].append({
                "keyword": keyword,
                "category": category,
                "subcategory": subcategory
            })

        return plan

    def save_search_plan(self, filename: str = "search_plan.json"):
        """Save the search plan to a file"""
        plan = self.generate_search_plan()
        filepath = os.path.join(DATA_DIR, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(plan, f, indent=2, ensure_ascii=False)

        print(f"Search plan saved to {filepath}")
        print(f"Total keywords: {plan['total_keywords']}")
        print(f"Categories covered: {len(plan['categories'])}")

        return plan


if __name__ == '__main__':
    # Generate and save search plan
    discovery = BrandDiscovery()
    plan = discovery.save_search_plan()

    # Print summary
    print("\n=== Search Plan Summary ===")
    for category, data in plan["categories"].items():
        print(f"\n{category}: {data['count']} keywords")
        for subcat, keywords in data["subcategories"].items():
            print(f"  - {subcat}: {len(keywords)} keywords")
