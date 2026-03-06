#!/usr/bin/env python3
"""
Test script to verify Brand Sites system
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

print("🧪 Testing Brand Sites System...\n")

# Test 1: Configuration
print("1️⃣ Testing Configuration...")
try:
    from config import AI_PROVIDER, DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL
    print(f"   ✅ AI Provider: {AI_PROVIDER}")
    print(f"   ✅ API Key configured: {DEEPSEEK_API_KEY[:20]}...")
    print(f"   ✅ Base URL: {DEEPSEEK_BASE_URL}")
except Exception as e:
    print(f"   ❌ Configuration error: {e}")
    sys.exit(1)

# Test 2: Brand Selector
print("\n2️⃣ Testing Brand Selector...")
try:
    from selector import BrandSelector
    selector = BrandSelector()
    brands = selector.select_brands()
    print(f"   ✅ Selected {len(brands)} brands:")
    for i, brand in enumerate(brands, 1):
        print(f"      {i}. {brand['name']} ({brand['category']})")
except Exception as e:
    print(f"   ❌ Selector error: {e}")
    sys.exit(1)

# Test 3: AI Analyzer (single brand test)
print("\n3️⃣ Testing AI Analyzer...")
try:
    from analyzer import BrandAnalyzer
    analyzer = BrandAnalyzer()

    test_brand = brands[0]  # Test with first selected brand
    print(f"   Analyzing: {test_brand['name']}...")

    analysis = analyzer.analyze_brand(test_brand)
    print(f"   ✅ Analysis completed!")
    print(f"   ✅ Overall Score: {analysis['overall_score']}/10")
    print(f"   ✅ Summary: {analysis['summary'][:100]}...")
except Exception as e:
    print(f"   ❌ Analyzer error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 4: Content Generator
print("\n4️⃣ Testing Content Generator...")
try:
    from generator import ContentGenerator
    from datetime import datetime

    generator = ContentGenerator()
    today = datetime.now().strftime('%Y-%m-%d')

    # Generate with just one brand for testing
    test_analyses = [analysis]
    test_brands = [test_brand]

    post_file = generator.generate_daily_post(test_brands, test_analyses, f"{today}-test")
    print(f"   ✅ Test post generated: {post_file}")
except Exception as e:
    print(f"   ❌ Generator error: {e}")
    sys.exit(1)

print("\n✨ All tests passed! System is ready to use.")
print("\n📝 Next steps:")
print("   1. Run: python3 main.py")
print("   2. Check: docs/_posts/ for generated content")
print("   3. Setup GitHub repo and enable Pages")
