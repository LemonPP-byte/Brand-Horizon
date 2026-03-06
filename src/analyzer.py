"""
AI Analyzer - Analyzes brand websites using AI
"""

import os
from typing import Dict
from openai import OpenAI
from config import AI_PROVIDER, OPENAI_API_KEY, ANTHROPIC_API_KEY, DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL


class BrandAnalyzer:
    def __init__(self):
        if AI_PROVIDER == "openai":
            self.client = OpenAI(api_key=OPENAI_API_KEY)
            self.model = "gpt-4o"
        elif AI_PROVIDER == "anthropic":
            import anthropic
            self.client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
            self.model = "claude-3-5-sonnet-20241022"
        elif AI_PROVIDER == "deepseek":
            self.client = OpenAI(
                api_key=DEEPSEEK_API_KEY,
                base_url=DEEPSEEK_BASE_URL
            )
            self.model = "deepseek-chat"

    def analyze_brand(self, brand: Dict) -> Dict:
        """Analyze a brand and generate content"""
        prompt = self._create_prompt(brand)

        if AI_PROVIDER in ["openai", "deepseek"]:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an expert in e-commerce, brand strategy, and web design. Analyze DTC brands and provide insightful commentary."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            analysis_text = response.choices[0].message.content
        else:  # anthropic
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1500,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            analysis_text = response.content[0].text

        # Parse the analysis
        analysis = self._parse_analysis(analysis_text, brand)
        return analysis

    def _create_prompt(self, brand: Dict) -> str:
        """Create analysis prompt for AI"""
        return f"""Analyze this DTC brand website:

Brand: {brand['name']}
URL: {brand['url']}
Category: {brand['category']} - {brand['subcategory']}
Region: {brand['region']}
Founded: {brand['founded']}
Tags: {', '.join(brand['tags'])}
Description: {brand['description']}

Please provide a detailed analysis in the following format:

**Brief Summary** (2-3 sentences about what makes this brand unique)

**Design Highlights** (3-4 key design elements that stand out - UI, color scheme, typography, layout, imagery)

**Marketing Strategy** (2-3 sentences about their unique selling proposition and how they position themselves)

**Target Audience** (1-2 sentences describing their ideal customer)

**Key Takeaways** (2-3 actionable insights for someone building their own brand)

**Scores** (Rate 1-10):
- Design: X/10
- User Experience: X/10
- Innovation: X/10

Keep the tone professional but engaging. Focus on what makes this brand worth studying."""

    def _parse_analysis(self, analysis_text: str, brand: Dict) -> Dict:
        """Parse AI response into structured data"""
        # Extract sections from the analysis
        sections = {
            'summary': '',
            'design_highlights': '',
            'marketing_strategy': '',
            'target_audience': '',
            'key_takeaways': '',
            'scores': {
                'design': 8.0,
                'user_experience': 8.0,
                'innovation': 8.0
            }
        }

        # Simple parsing (you can make this more robust)
        lines = analysis_text.split('\n')
        current_section = None

        for line in lines:
            line = line.strip()
            if not line:
                continue

            if '**Brief Summary**' in line or 'Brief Summary' in line:
                current_section = 'summary'
            elif '**Design Highlights**' in line or 'Design Highlights' in line:
                current_section = 'design_highlights'
            elif '**Marketing Strategy**' in line or 'Marketing Strategy' in line:
                current_section = 'marketing_strategy'
            elif '**Target Audience**' in line or 'Target Audience' in line:
                current_section = 'target_audience'
            elif '**Key Takeaways**' in line or 'Key Takeaways' in line:
                current_section = 'key_takeaways'
            elif '**Scores**' in line or 'Scores' in line:
                current_section = 'scores'
            elif current_section == 'scores':
                # Parse scores
                if 'Design:' in line:
                    try:
                        score = float(line.split(':')[1].split('/')[0].strip())
                        sections['scores']['design'] = score
                    except:
                        pass
                elif 'User Experience:' in line:
                    try:
                        score = float(line.split(':')[1].split('/')[0].strip())
                        sections['scores']['user_experience'] = score
                    except:
                        pass
                elif 'Innovation:' in line:
                    try:
                        score = float(line.split(':')[1].split('/')[0].strip())
                        sections['scores']['innovation'] = score
                    except:
                        pass
            elif current_section and current_section != 'scores':
                # Append to current section
                if sections[current_section]:
                    sections[current_section] += ' ' + line
                else:
                    sections[current_section] = line

        # Calculate overall score
        scores = sections['scores']
        overall_score = (scores['design'] * 0.4 +
                        scores['user_experience'] * 0.3 +
                        scores['innovation'] * 0.3)
        sections['overall_score'] = round(overall_score, 1)

        return sections


if __name__ == '__main__':
    # Test the analyzer
    test_brand = {
        'name': 'Allbirds',
        'url': 'https://www.allbirds.com',
        'category': 'Fashion',
        'subcategory': 'Footwear',
        'region': 'US',
        'founded': 2016,
        'tags': ['DTC', 'Sustainable', 'Minimalist'],
        'description': 'Sustainable footwear brand using natural materials'
    }

    analyzer = BrandAnalyzer()
    analysis = analyzer.analyze_brand(test_brand)
    print(f"Analysis for {test_brand['name']}:")
    print(f"Overall Score: {analysis['overall_score']}/10")
    print(f"\nSummary: {analysis['summary']}")
