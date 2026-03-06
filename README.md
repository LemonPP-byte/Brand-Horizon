# Brand Sites - Daily DTC Brand Recommendations

AI-curated daily digest of 5 exceptional Direct-to-Consumer (DTC) brand websites from the US and Europe.

## 🎯 What is This?

Every day, this system automatically:
- Selects 5 outstanding DTC brand websites
- Analyzes their design, UX, and marketing strategies using AI
- Generates detailed insights and scores
- Publishes to a beautiful GitHub Pages website

## 🚀 Features

- **Smart Selection Algorithm**: Ensures variety and avoids repetition
- **AI-Powered Analysis**: Deep insights into design, UX, and innovation
- **Category Diversity**: Fashion, Beauty, Home, Health, Travel, and more
- **Automated Publishing**: Daily updates via cron job
- **Clean Design**: Minimalist Jekyll-based website

## 📁 Project Structure

```
BrandSites/
├── data/
│   ├── brands.json          # Brand database
│   ├── history.json         # Recommendation history
│   └── summaries/           # Generated summaries
├── docs/
│   ├── _posts/              # Jekyll posts
│   ├── _layouts/            # Page layouts
│   ├── assets/              # CSS/JS
│   └── index.md             # Homepage
├── src/
│   ├── selector.py          # Brand selection logic
│   ├── analyzer.py          # AI analysis
│   ├── generator.py         # Markdown generation
│   └── config.py            # Configuration
├── main.py                  # Main execution script
├── run-brand-sites.sh       # Automation script
└── README.md
```

## 🛠️ Setup

### 1. Install Dependencies

```bash
pip install openai anthropic
```

### 2. Set API Keys

```bash
export OPENAI_API_KEY="your-key-here"
# or
export ANTHROPIC_API_KEY="your-key-here"
```

### 3. Run Manually

```bash
cd /Users/admin/BrandSites
python3 main.py
```

### 4. Setup Automation (Optional)

Add to crontab:
```bash
crontab -e
```

Add this line:
```
0 8 * * * /Users/admin/BrandSites/run-brand-sites.sh >> /Users/admin/BrandSites/logs/cron.log 2>> /Users/admin/BrandSites/logs/cron-error.log
```

## 📊 Brand Database

The `data/brands.json` file contains:
- Brand name and URL
- Category and subcategory
- Region and founding year
- Tags (DTC, Sustainable, etc.)
- Recommendation history

### Adding New Brands

Edit `data/brands.json`:

```json
{
  "id": "brand-slug",
  "name": "Brand Name",
  "url": "https://www.example.com",
  "category": "Fashion",
  "subcategory": "Apparel",
  "region": "US",
  "founded": 2020,
  "tags": ["DTC", "Sustainable"],
  "description": "Brief description",
  "last_recommended": null,
  "recommendation_count": 0,
  "priority": "high"
}
```

## 🤖 AI Analysis

Each brand receives:
- **Summary**: What makes it unique
- **Design Highlights**: UI/UX standout features
- **Marketing Strategy**: Positioning and USP
- **Target Audience**: Ideal customer profile
- **Key Takeaways**: Actionable insights
- **Scores**: Design, UX, Innovation (1-10)

## 🌐 Website

The generated content is published to GitHub Pages with:
- Daily digest view
- Archive by date
- Category filtering
- Responsive design

## 📝 Configuration

Edit `src/config.py` to customize:
- AI provider (OpenAI or Anthropic)
- Daily brand count
- Repeat threshold
- Scoring weights
- Categories and regions

## 🔄 How It Works

1. **Selection**: Algorithm picks 5 brands based on:
   - Not recently recommended (30 days)
   - Category diversity
   - Priority level
   - Recommendation frequency

2. **Analysis**: AI analyzes each brand's:
   - Design and aesthetics
   - User experience
   - Innovation and uniqueness

3. **Generation**: Creates markdown with:
   - Structured content
   - Scores and ratings
   - Tags and metadata

4. **Publishing**: Commits to Git and pushes to GitHub Pages

## 📈 Future Enhancements

- [ ] Add traffic data via SimilarWeb API
- [ ] Include tech stack analysis (BuiltWith)
- [ ] Social media metrics
- [ ] User voting system
- [ ] Email newsletter
- [ ] Mobile app

## 📄 License

MIT License

## 🤝 Contributing

Feel free to add more brands to the database or improve the analysis prompts!

---

**Powered by AI** | Built with Python & Jekyll
