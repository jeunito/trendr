import vcr
import unittest
from trendr.crawler import stackoverflow

class StackOverFlowCrawlerTestCase(unittest.TestCase):
    def test_crawl(self):
        with vcr.use_cassette("fixtures/vcr/trendr/crawler/stackoverflow.yaml"):
            items = stackoverflow.crawl()
            for item in items:
                self.assertTrue(type(item) == tuple)
                self.assertEqual(len(item), 2)
