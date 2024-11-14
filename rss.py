import feedparser

def fetch_rss_feed(url):
    # Parse the RSS feed from the given URL
    feed = feedparser.parse(url)
    
    # Check if the feed was successfully parsed
    if feed.bozo:
        print("Failed to parse the feed.")
        return
    
    # Display feed title and link
    print(f"Feed Title: {feed.feed.title}")
    print(f"Feed Link: {feed.feed.link}")
    print("-" * 50)
    
    # Loop through the feed entries and display the title and summary
    for entry in feed.entries:
        print(f"Title: {entry.title}")
        print(f"Link: {entry.link}")
        print(f"Published: {entry.published}")
        print(f"Summary: {entry.summary}")
        print("-" * 50)

# Main function to run the program
def main():
    # RSS feed URL (you can replace this with any RSS feed URL)
    rss_url = "https://rss.cnn.com/rss/cnn_topstories.rss"
    
    print("Fetching RSS feed...")
    fetch_rss_feed(rss_url)

if _name_ == "_main_":
    main()
