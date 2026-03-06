"""
Brand Selector - Selects 5 brands daily based on algorithm
"""

import json
import random
from datetime import datetime, timedelta
from typing import List, Dict
from config import BRANDS_FILE, HISTORY_FILE, DAILY_BRAND_COUNT, REPEAT_THRESHOLD_DAYS


class BrandSelector:
    def __init__(self):
        self.brands = self._load_brands()
        self.history = self._load_history()

    def _load_brands(self) -> List[Dict]:
        """Load brands from JSON file"""
        with open(BRANDS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data['brands']

    def _load_history(self) -> List[Dict]:
        """Load recommendation history"""
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data['recommendations']

    def _save_history(self):
        """Save recommendation history"""
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump({'recommendations': self.history}, f, indent=2)

    def _get_recently_recommended(self) -> set:
        """Get brand IDs recommended in the last N days"""
        cutoff_date = datetime.now() - timedelta(days=REPEAT_THRESHOLD_DAYS)
        recent_brands = set()

        for rec in self.history:
            rec_date = datetime.strptime(rec['date'], '%Y-%m-%d')
            if rec_date >= cutoff_date:
                recent_brands.update(rec['brands'])

        return recent_brands

    def _calculate_priority_score(self, brand: Dict, recent_brands: set) -> float:
        """Calculate priority score for a brand"""
        score = 0.0

        # Not recently recommended (highest priority)
        if brand['id'] not in recent_brands:
            score += 10.0

        # Never recommended before
        if brand['recommendation_count'] == 0:
            score += 5.0

        # Priority level
        priority_scores = {'high': 3.0, 'medium': 2.0, 'low': 1.0}
        score += priority_scores.get(brand.get('priority', 'medium'), 2.0)

        # Less frequently recommended brands get higher score
        score -= brand['recommendation_count'] * 0.5

        return max(score, 0.1)  # Ensure positive score

    def select_brands(self) -> List[Dict]:
        """Select 5 brands for today's recommendation"""
        recent_brands = self._get_recently_recommended()

        # Calculate scores for all brands
        brand_scores = []
        for brand in self.brands:
            score = self._calculate_priority_score(brand, recent_brands)
            brand_scores.append((brand, score))

        # Weighted random selection
        total_score = sum(score for _, score in brand_scores)
        probabilities = [score / total_score for _, score in brand_scores]

        # Select brands without replacement
        selected_brands = []
        remaining_brands = brand_scores.copy()

        for _ in range(min(DAILY_BRAND_COUNT, len(remaining_brands))):
            if not remaining_brands:
                break

            # Recalculate probabilities
            total = sum(score for _, score in remaining_brands)
            probs = [score / total for _, score in remaining_brands]

            # Select one brand
            selected_idx = random.choices(range(len(remaining_brands)), weights=probs)[0]
            selected_brand, _ = remaining_brands.pop(selected_idx)
            selected_brands.append(selected_brand)

        # Ensure category diversity
        selected_brands = self._ensure_diversity(selected_brands)

        return selected_brands

    def _ensure_diversity(self, brands: List[Dict]) -> List[Dict]:
        """Ensure category diversity in selection"""
        categories = {}
        diverse_brands = []
        remaining_brands = brands.copy()

        # First pass: one brand per category
        for brand in brands:
            category = brand['category']
            if category not in categories:
                categories[category] = True
                diverse_brands.append(brand)
                remaining_brands.remove(brand)

        # Second pass: fill remaining slots
        diverse_brands.extend(remaining_brands[:DAILY_BRAND_COUNT - len(diverse_brands)])

        return diverse_brands[:DAILY_BRAND_COUNT]

    def save_selection(self, selected_brands: List[Dict], date: str):
        """Save today's selection to history"""
        brand_ids = [brand['id'] for brand in selected_brands]

        # Add to history
        self.history.append({
            'date': date,
            'brands': brand_ids
        })

        # Update recommendation counts in brands.json
        for brand in self.brands:
            if brand['id'] in brand_ids:
                brand['recommendation_count'] += 1
                brand['last_recommended'] = date

        # Save both files
        self._save_history()
        self._save_brands()

    def _save_brands(self):
        """Save updated brands data"""
        with open(BRANDS_FILE, 'w', encoding='utf-8') as f:
            json.dump({'brands': self.brands}, f, indent=2)


if __name__ == '__main__':
    # Test the selector
    selector = BrandSelector()
    today = datetime.now().strftime('%Y-%m-%d')
    selected = selector.select_brands()

    print(f"Selected brands for {today}:")
    for i, brand in enumerate(selected, 1):
        print(f"{i}. {brand['name']} ({brand['category']}) - {brand['url']}")
