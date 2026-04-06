from typing import Optional
import logging
<<<<<<< HEAD
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from app.agent.digest_agent import DigestAgent
from app.database.repository import Repository
=======
from app.agent.digest_agent import DigestAgent, DigestOutput
from app.database.repository import Repository
from .base import BaseProcessService
>>>>>>> ef3887c9d3ca5c255048389b17a5d655c67d7f8a

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
<<<<<<< HEAD
logger = logging.getLogger(__name__)


def process_digests(limit: Optional[int] = None) -> dict:
    agent = DigestAgent()
    repo = Repository()
    
    articles = repo.get_articles_without_digest(limit=limit)
    total = len(articles)
    processed = 0
    failed = 0
    
    logger.info(f"Starting digest processing for {total} articles")
    
    for idx, article in enumerate(articles, 1):
        article_type = article["type"]
        article_id = article["id"]
        article_title = article["title"][:60] + "..." if len(article["title"]) > 60 else article["title"]
        
        logger.info(f"[{idx}/{total}] Processing {article_type}: {article_title} (ID: {article_id})")
        
        try:
            digest_result = agent.generate_digest(
                title=article["title"],
                content=article["content"],
                article_type=article_type
            )
            
            if digest_result:
                repo.create_digest(
                    article_type=article_type,
                    article_id=article_id,
                    url=article["url"],
                    title=digest_result.title,
                    summary=digest_result.summary,
                    published_at=article.get("published_at")
                )
                processed += 1
                logger.info(f"✓ Successfully created digest for {article_type} {article_id}")
            else:
                failed += 1
                logger.warning(f"✗ Failed to generate digest for {article_type} {article_id}")
        except Exception as e:
            failed += 1
            logger.error(f"✗ Error processing {article_type} {article_id}: {e}")
    
    logger.info(f"Processing complete: {processed} processed, {failed} failed out of {total} total")
    
    return {
        "total": total,
        "processed": processed,
        "failed": failed
    }
=======


class DigestProcessor(BaseProcessService):
    def __init__(self):
        super().__init__()
        self.agent = DigestAgent()
        self.repo = Repository()

    def get_items_to_process(self, limit: Optional[int] = None) -> list:
        return self.repo.get_articles_without_digest(limit=limit)

    def process_item(self, item: dict) -> Optional[DigestOutput]:
        return self.agent.generate_digest(
            title=item["title"],
            content=item["content"],
            article_type=item["type"]
        )

    def save_result(self, item: dict, result: DigestOutput) -> bool:
        try:
            self.repo.create_digest(
                article_type=item["type"],
                article_id=item["id"],
                url=item["url"],
                title=result.title,
                summary=result.summary,
                published_at=item.get("published_at")
            )
            return True
        except Exception:
            return False

    def _get_item_id(self, item: dict) -> str:
        return f"{item['type']}:{item['id']}"

    def _get_item_title(self, item: dict) -> str:
        return item["title"]


def process_digests(limit: Optional[int] = None) -> dict:
    processor = DigestProcessor()
    return processor.process(limit=limit)
>>>>>>> ef3887c9d3ca5c255048389b17a5d655c67d7f8a


if __name__ == "__main__":
    result = process_digests()
    print(f"Total articles: {result['total']}")
    print(f"Processed: {result['processed']}")
    print(f"Failed: {result['failed']}")

