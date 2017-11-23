from setuptools import setup, find_packages

setup(
    name="trendr-crawler",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "feedparser"
    ],
    entry_points={
        "console_scripts": [
            "crawl = trendr.crawler:main"
        ]
    }
)
