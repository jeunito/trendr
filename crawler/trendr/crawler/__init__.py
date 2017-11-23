from . import stackoverflow

def main():
    entries = stackoverflow.crawl()
    for entry in entries:
        title, _ = entry
        print title
