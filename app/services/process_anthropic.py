from typing import Optional
<<<<<<< HEAD

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))


from app.scrapers.anthropic import AnthropicScraper
from app.database.repository import Repository


def process_anthropic_markdown(limit: Optional[int] = None) -> dict:
    scraper = AnthropicScraper()
    repo = Repository()
    
    articles = repo.get_anthropic_articles_without_markdown(limit=limit)
    processed = 0
    failed = 0
    
    for article in articles:
        markdown = scraper.url_to_markdown(article.url)
        try:
            if markdown:
                repo.update_anthropic_article_markdown(article.guid, markdown)
                processed += 1
            else:
                failed += 1
        except Exception as e:
            failed += 1
            print(f"Error processing article {article.guid}: {e}")
            continue
    
    return {
        "total": len(articles),
        "processed": processed,
        "failed": failed
    }
=======
from app.scrapers.anthropic import AnthropicScraper
from app.database.repository import Repository
from .base import BaseProcessService


class AnthropicMarkdownProcessor(BaseProcessService):
    def __init__(self):
        super().__init__()
        self.scraper = AnthropicScraper()
        self.repo = Repository()

    def get_items_to_process(self, limit: Optional[int] = None) -> list:
        return self.repo.get_anthropic_articles_without_markdown(limit=limit)

    def process_item(self, item) -> Optional[str]:
        return self.scraper.url_to_markdown(item.url)

    def save_result(self, item, result: str) -> bool:
        return self.repo.update_anthropic_article_markdown(item.guid, result)


def process_anthropic_markdown(limit: Optional[int] = None) -> dict:
    processor = AnthropicMarkdownProcessor()
    return processor.process(limit=limit)
>>>>>>> ef3887c9d3ca5c255048389b17a5d655c67d7f8a


if __name__ == "__main__":
    result = process_anthropic_markdown()
    print(f"Total articles: {result['total']}")
    print(f"Processed: {result['processed']}")
    print(f"Failed: {result['failed']}")

