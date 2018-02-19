from . import stackoverflow

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--stdout", help="Print crawl data to stdout", action="store_true")
args = parser.parse_args()

if not args.stdout:
    import json
    import hashlib
    m = hashlib.md5()

def main():
    entries = stackoverflow.crawl()
    for entry in entries:
        title, tags = entry
        if args.stdout:
            print title
            print "--- {tags}".format(tags=",".join(tags))
        else:
            m = hashlib.md5()
            m.update(entry[0])
            entry_file = "/var/tmp/crawler/{entry_filename}.json".format(entry_filename=m.hexdigest())

            with open(entry_file, "w") as f:
                f.write(json.dumps(entry))
