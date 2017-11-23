import feedparser

def crawl():
    stackoverflow = feedparser.parse("https://stackoverflow.com/jobs/feed?q=devops")
    entries = []
    for raw_entry in stackoverflow.entries:
        entry = (raw_entry.title, raw_entry.description)
        entries.append(entry)

    return entries
