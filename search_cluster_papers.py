"""search_cluster_papers.py: Search for papers with 'cluster' in their abstracts."""

import datetime
import pytz
import query_arxiv as qa

def search_cluster_papers(start_date: datetime.datetime, end_date: datetime.datetime, output_file: str):
    """Search for papers with 'cluster' in their abstracts.
    
    Args:
        start_date: Start date.
        end_date: End date.
        output_file: Output markdown file name.
    """
    categories = ['astro-ph.CO', 'astro-ph.GA']
    
    # Query arXiv for papers in the specified date range
    feed = qa.query_arxiv(categories, start_date, end_date, max_results=1000)
    
    # Filter papers with 'cluster' in their abstracts
    cluster_papers = []
    for entry in feed.entries:
        if 'cluster' in entry.summary.lower():
            cluster_papers.append(entry)
    
    # Save results to markdown file
    with open(output_file, 'w') as f:
        f.write(f"# Papers with 'cluster' in their abstracts\n\n")
        f.write(f"Date range: {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}\n")
        f.write(f"Categories: {', '.join(categories)}\n")
        f.write(f"Total papers found: {len(cluster_papers)}\n\n")
        f.write("---\n\n")
        
        for paper in cluster_papers:
            f.write(qa.make_markdown_entry(paper, include_abstract=True))
            f.write("\n---\n\n")
    
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    # Set timezone to UTC
    start_date = datetime.datetime(2024, 4, 1, tzinfo=pytz.UTC)
    end_date = datetime.datetime(2024, 5, 11, tzinfo=pytz.UTC)
    
    # Generate output filename based on date range
    output_file = f"cluster_papers_{start_date.strftime('%Y%m%d')}_{end_date.strftime('%Y%m%d')}.md"
    
    search_cluster_papers(start_date, end_date, output_file) 