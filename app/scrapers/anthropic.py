<<<<<<< HEAD
from datetime import datetime, timedelta, timezone
from typing import List, Optional
import feedparser
from docling.document_converter import DocumentConverter
from pydantic import BaseModel


class AnthropicArticle(BaseModel):
    title: str
    description: str
    url: str
    guid: str
    published_at: datetime
    category: Optional[str] = None


class AnthropicScraper:
    def __init__(self):
        self.rss_urls = [
=======
from typing import List, Optional
import requests
from html_to_markdown import convert
from .base import BaseScraper, Article


class AnthropicArticle(Article):
    pass


class AnthropicScraper(BaseScraper):
    @property
    def rss_urls(self) -> List[str]:
        return [
>>>>>>> ef3887c9d3ca5c255048389b17a5d655c67d7f8a
            "https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_anthropic_news.xml",
            "https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_anthropic_research.xml",
            "https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_anthropic_engineering.xml",
        ]
<<<<<<< HEAD
        self.converter = DocumentConverter()

    def get_articles(self, hours: int = 24) -> List[AnthropicArticle]:
        now = datetime.now(timezone.utc)
        cutoff_time = now - timedelta(hours=hours)
        articles = []
        seen_guids = set()
        
        for rss_url in self.rss_urls:
            feed = feedparser.parse(rss_url)
            if not feed.entries:
                continue
            
            for entry in feed.entries:
                published_parsed = getattr(entry, "published_parsed", None)
                if not published_parsed:
                    continue
                
                published_time = datetime(*published_parsed[:6], tzinfo=timezone.utc)
                if published_time >= cutoff_time:
                    guid = entry.get("id", entry.get("link", ""))
                    if guid not in seen_guids:
                        seen_guids.add(guid)
                        articles.append(AnthropicArticle(
                            title=entry.get("title", ""),
                            description=entry.get("description", ""),
                            url=entry.get("link", ""),
                            guid=guid,
                            published_at=published_time,
                            category=entry.get("tags", [{}])[0].get("term") if entry.get("tags") else None
                        ))
        
        return articles

    def url_to_markdown(self, url: str) -> Optional[str]:
        try:
            result = self.converter.convert(url)
            return result.document.export_to_markdown()
        except Exception:
            return None

=======

    def get_articles(self, hours: int = 24) -> List[AnthropicArticle]:
        return [
            AnthropicArticle(**article.model_dump())
            for article in super().get_articles(hours)
        ]

    def url_to_markdown(self, url: str) -> Optional[str]:
        try:
            response = requests.get(
                url, headers={"User-Agent": "Mozilla/5.0"}, timeout=30
            )
            response.raise_for_status()
            html = response.text
            markdown = convert(html)
            return markdown
        except Exception:
            return None


>>>>>>> ef3887c9d3ca5c255048389b17a5d655c67d7f8a
if __name__ == "__main__":
    scraper = AnthropicScraper()
    articles: List[AnthropicArticle] = scraper.get_articles(hours=100)
    markdown: str = scraper.url_to_markdown(articles[1].url)
<<<<<<< HEAD
    print(markdown)
=======
    print(markdown)
>>>>>>> ef3887c9d3ca5c255048389b17a5d655c67d7f8a
