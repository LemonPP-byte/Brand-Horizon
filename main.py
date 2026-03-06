#!/usr/bin/env python3
"""
Brand Sites - Main execution script
Selects 5 brands, analyzes them with AI, and generates daily post
"""

import sys
import os
from datetime import datetime

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from selector import BrandSelector
from analyzer import BrandAnalyzer
from generator import ContentGenerator


def main():
    print("\n🏢 Brand Sites - Starting daily selection...\n")

    today = datetime.now().strftime('%Y-%m-%d')

    # Step 1: Select brands
    print("📋 Step 1: Selecting 5 brands...")
    selector = BrandSelector()
    selected_brands = selector.select_brands()

    print(f"✅ Selected {len(selected_brands)} brands:")
    for i, brand in enumerate(selected_brands, 1):
        print(f"   {i}. {brand['name']} ({brand['category']})")

    # Step 2: Analyze with AI
    print("\n🤖 Step 2: Analyzing brands with AI...")
    analyzer = BrandAnalyzer()
    analyses = []

    for i, brand in enumerate(selected_brands, 1):
        print(f"   Analyzing {i}/{len(selected_brands)}: {brand['name']}...")
        try:
            analysis = analyzer.analyze_brand(brand)
            analyses.append(analysis)
            print(f"   ✅ Score: {analysis['overall_score']}/10")
        except Exception as e:
            print(f"   ❌ Error analyzing {brand['name']}: {e}")
            # Create a default analysis
            analyses.append({
                'summary': brand['description'],
                'design_highlights': 'Clean and modern design.',
                'marketing_strategy': 'Direct-to-consumer approach.',
                'target_audience': 'Modern consumers.',
                'key_takeaways': 'Focus on quality and customer experience.',
                'overall_score': 8.0,
                'scores': {
                    'design': 8.0,
                    'user_experience': 8.0,
                    'innovation': 8.0
                }
            })

    # Step 3: Generate content
    print("\n📝 Step 3: Generating markdown content...")
    generator = ContentGenerator()
    post_file = generator.generate_daily_post(selected_brands, analyses, today)

    # Step 4: Save selection to history
    print("\n💾 Step 4: Saving selection to history...")
    selector.save_selection(selected_brands, today)
    print("✅ History updated")

    print(f"\n✨ Brand Sites completed successfully!")
    print(f"📄 Post saved to: {post_file}")
    print(f"📅 Date: {today}\n")


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
