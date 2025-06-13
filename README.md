# Query arXiv

A Python package for querying and analyzing arXiv submissions, with a focus on astronomy and astrophysics papers.

## Features

- Query arXiv submissions with flexible date ranges and category filters
- Support for daily arXiv updates (considering business days)
- Built-in functions for searching specific topics in paper abstracts
- Export results to markdown format with customizable output options
- Timezone-aware date handling


## Usage

### Basic Query

#### From Simple Command

```bash
python3 -m query_arxiv 2025-05-21
```

```bash
python3 -m query_arxiv 2025-05-21 --include-abstract
```


#### From Python

```python
import datetime
import pytz
import query_arxiv as qa

# Set up date range
start_date = datetime.datetime(2024, 4, 1, tzinfo=pytz.UTC)
end_date = datetime.datetime(2024, 5, 1, tzinfo=pytz.UTC)

# Define categories to search
categories = ['astro-ph.CO', 'astro-ph.GA']

# Query arXiv
feed = qa.query_arxiv(categories, start_date, end_date)

# Print titles
qa.print_titles(feed)

# Save results to markdown file
qa.save_feed(feed, 'papers.md', include_abstract=True)
```

### Daily Updates

```python
import datetime
import pytz
import query_arxiv as qa

# Get today's date
today = datetime.datetime.now(pytz.UTC)

# Query arXiv for daily updates
feed = qa.query_arxiv_daily(['astro-ph.CO'], today)

# Save results
qa.save_feed(feed, 'daily_papers.md')
```


## Available Categories

The package supports all arXiv categories. Some common astronomy-related categories include:

- `astro-ph.CO`: Cosmology and Nongalactic Astrophysics
- `astro-ph.GA`: Astrophysics of Galaxies
- `astro-ph.SR`: Solar and Stellar Astrophysics
- `astro-ph.HE`: High Energy Astrophysical Phenomena
- `astro-ph.EP`: Earth and Planetary Astrophysics
