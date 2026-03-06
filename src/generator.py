"""
Content Generator - Generates Markdown files for Jekyll
"""

import os
from datetime import datetime
from typing import List, Dict
from config import POSTS_DIR, SUMMARIES_DIR


class ContentGenerator:
    def __init__(self):
        os.makedirs(POSTS_DIR, exist_ok=True)
        os.makedirs(SUMMARIES_DIR, exist_ok=True)

    def generate_daily_post(self, brands: List[Dict], analyses: List[Dict], date: str):
        """Generate daily markdown post"""
        content = self._create_markdown(brands, analyses, date)

        # Save to summaries
        summary_file = os.path.join(SUMMARIES_DIR, f"brands-{date}.md")
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write(content)

        # Save to Jekyll posts
        post_file = os.path.join(POSTS_DIR, f"{date}-brand-sites.md")
        with open(post_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✅ Generated post: {post_file}")
        return post_file

    def _create_markdown(self, brands: List[Dict], analyses: List[Dict], date: str) -> str:
        """Create markdown content"""
        # Header
        content = f"""---
layout: default
title: "Brand Sites Digest: {date}"
date: {date}
---

> 5 curated DTC brand websites selected from our database

---

"""

        # Table of contents
        for i, (brand, analysis) in enumerate(zip(brands, analyses), 1):
            score = analysis['overall_score']
            content += f"{i}. [{brand['name']}](#brand-{i}) ⭐️ {score}/10\n"

        content += "\n---\n\n"

        # Brand details
        for i, (brand, analysis) in enumerate(zip(brands, analyses), 1):
            content += self._create_brand_section(brand, analysis, i)

        return content

    def _create_brand_section(self, brand: Dict, analysis: Dict, index: int) -> str:
        """Create markdown section for a single brand"""
        score = analysis['overall_score']

        section = f"""<a id="brand-{index}"></a>
## [{brand['name']}]({brand['url']}) ⭐️ {score}/10

{analysis['summary']}

**Category**: {brand['category']} - {brand['subcategory']} | **Region**: {brand['region']} | **Founded**: {brand['founded']}

### Design Highlights
{analysis['design_highlights']}

### Marketing Strategy
{analysis['marketing_strategy']}

### Target Audience
{analysis['target_audience']}

### Key Takeaways
{analysis['key_takeaways']}

### Scores
- **Design**: {analysis['scores']['design']}/10
- **User Experience**: {analysis['scores']['user_experience']}/10
- **Innovation**: {analysis['scores']['innovation']}/10

**Tags**: {', '.join([f'`#{tag}`' for tag in brand['tags']])}

---

"""
        return section


if __name__ == '__main__':
    # Test the generator
    test_brands = [
        {
            'name': 'Allbirds',
            'url': 'https://www.allbirds.com',
            'category': 'Fashion',
            'subcategory': 'Footwear',
            'region': 'US',
            'founded': 2016,
            'tags': ['DTC', 'Sustainable', 'Minimalist']
        }
    ]

    test_analyses = [
        {
            'summary': 'Allbirds revolutionized sustainable footwear with natural materials.',
            'design_highlights': 'Clean, minimalist design with focus on product photography.',
            'marketing_strategy': 'Emphasizes sustainability and comfort.',
            'target_audience': 'Environmentally conscious millennials.',
            'key_takeaways': 'Focus on a single product category and do it exceptionally well.',
            'overall_score': 8.5,
            'scores': {
                'design': 9.0,
                'user_experience': 8.5,
                'innovation': 8.0
            }
        }
    ]

    generator = ContentGenerator()
    today = datetime.now().strftime('%Y-%m-%d')
    generator.generate_daily_post(test_brands, test_analyses, today)
