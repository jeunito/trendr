import feedparser

def crawl():
    stackoverflow = feedparser.parse("https://stackoverflow.com/jobs/feed?q=devops")
    entries = []
    for raw_entry in stackoverflow.entries:
        entry = (raw_entry.title, map(lambda i: str(i["term"]), raw_entry.tags))
        entries.append(entry)

    return entries
