<<<<<<< HEAD
from typing import List
from .config import YOUTUBE_CHANNELS
from .scrapers.youtube import YouTubeScraper, ChannelVideo
from .scrapers.openai import OpenAIScraper, OpenAIArticle
from .scrapers.anthropic import AnthropicScraper, AnthropicArticle
from .database.repository import Repository


def run_scrapers(hours: int = 24) -> dict:
    youtube_scraper = YouTubeScraper()
    openai_scraper = OpenAIScraper()
    anthropic_scraper = AnthropicScraper()
    repo = Repository()
    
    youtube_videos = []
    video_dicts = []
    for channel_id in YOUTUBE_CHANNELS:
        videos = youtube_scraper.get_latest_videos(channel_id, hours=hours)
        youtube_videos.extend(videos)
        video_dicts.extend([
            {
                "video_id": v.video_id,
                "title": v.title,
                "url": v.url,
                "channel_id": channel_id,
                "published_at": v.published_at,
                "description": v.description,
                "transcript": v.transcript
            }
            for v in videos
        ])
    
    openai_articles = openai_scraper.get_articles(hours=hours)
    anthropic_articles = anthropic_scraper.get_articles(hours=hours)
    
    if video_dicts:
        repo.bulk_create_youtube_videos(video_dicts)
    
    if openai_articles:
=======
from typing import List, Callable, Any
from .config import YOUTUBE_CHANNELS
from .scrapers.youtube import YouTubeScraper, ChannelVideo
from .scrapers.openai import OpenAIScraper
from .scrapers.anthropic import AnthropicScraper
from .database.repository import Repository


def _save_youtube_videos(
    scraper: YouTubeScraper, repo: Repository, hours: int
) -> List[ChannelVideo]:
    videos = []
    video_dicts = []
    for channel_id in YOUTUBE_CHANNELS:
        channel_videos = scraper.get_latest_videos(channel_id, hours=hours)
        videos.extend(channel_videos)
        video_dicts.extend(
            [
                {
                    "video_id": v.video_id,
                    "title": v.title,
                    "url": v.url,
                    "channel_id": channel_id,
                    "published_at": v.published_at,
                    "description": v.description,
                    "transcript": v.transcript,
                }
                for v in channel_videos
            ]
        )
    if video_dicts:
        repo.bulk_create_youtube_videos(video_dicts)
    return videos


def _save_rss_articles(
    scraper, repo: Repository, hours: int, save_func: Callable
) -> List[Any]:
    articles = scraper.get_articles(hours=hours)
    if articles:
>>>>>>> ef3887c9d3ca5c255048389b17a5d655c67d7f8a
        article_dicts = [
            {
                "guid": a.guid,
                "title": a.title,
                "url": a.url,
                "published_at": a.published_at,
                "description": a.description,
<<<<<<< HEAD
                "category": a.category
            }
            for a in openai_articles
        ]
        repo.bulk_create_openai_articles(article_dicts)
    
    if anthropic_articles:
        article_dicts = [
            {
                "guid": a.guid,
                "title": a.title,
                "url": a.url,
                "published_at": a.published_at,
                "description": a.description,
                "category": a.category
            }
            for a in anthropic_articles
        ]
        repo.bulk_create_anthropic_articles(article_dicts)
    
    return {
        "youtube": youtube_videos,
        "openai": openai_articles,
        "anthropic": anthropic_articles,
    }
=======
                "category": a.category,
            }
            for a in articles
        ]
        save_func(article_dicts)
    return articles


SCRAPER_REGISTRY = [
    ("youtube", YouTubeScraper(), _save_youtube_videos),
    (
        "openai",
        OpenAIScraper(),
        lambda s, r, h: _save_rss_articles(s, r, h, r.bulk_create_openai_articles),
    ),
    (
        "anthropic",
        AnthropicScraper(),
        lambda s, r, h: _save_rss_articles(s, r, h, r.bulk_create_anthropic_articles),
    ),
]


def run_scrapers(hours: int = 24) -> dict:
    repo = Repository()
    results = {}

    for name, scraper, save_func in SCRAPER_REGISTRY:
        try:
            items = save_func(scraper, repo, hours)
            results[name] = items
        except Exception:
            results[name] = []

    return results
>>>>>>> ef3887c9d3ca5c255048389b17a5d655c67d7f8a


if __name__ == "__main__":
    results = run_scrapers(hours=24)
    print(f"YouTube videos: {len(results['youtube'])}")
    print(f"OpenAI articles: {len(results['openai'])}")
    print(f"Anthropic articles: {len(results['anthropic'])}")
<<<<<<< HEAD

=======
>>>>>>> ef3887c9d3ca5c255048389b17a5d655c67d7f8a
