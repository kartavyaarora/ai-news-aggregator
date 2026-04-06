from typing import Optional
<<<<<<< HEAD

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from app.scrapers.youtube import YouTubeScraper
from app.database.repository import Repository
=======
from app.scrapers.youtube import YouTubeScraper
from app.database.repository import Repository
from .base import BaseProcessService
>>>>>>> ef3887c9d3ca5c255048389b17a5d655c67d7f8a


TRANSCRIPT_UNAVAILABLE_MARKER = "__UNAVAILABLE__"


<<<<<<< HEAD
def process_youtube_transcripts(limit: Optional[int] = None) -> dict:
    scraper = YouTubeScraper()
    repo = Repository()
    
    videos = repo.get_youtube_videos_without_transcript(limit=limit)
    processed = 0
    unavailable = 0
    failed = 0
    
    for video in videos:
        try:
            transcript_result = scraper.get_transcript(video.video_id)
            if transcript_result:
                repo.update_youtube_video_transcript(video.video_id, transcript_result.text)
                processed += 1
            else:
                repo.update_youtube_video_transcript(video.video_id, TRANSCRIPT_UNAVAILABLE_MARKER)
                unavailable += 1
        except Exception as e:
            repo.update_youtube_video_transcript(video.video_id, TRANSCRIPT_UNAVAILABLE_MARKER)
            unavailable += 1
            print(f"Error processing video {video.video_id}: {e}")
    
    return {
        "total": len(videos),
        "processed": processed,
        "unavailable": unavailable,
        "failed": failed
    }
=======
class YouTubeTranscriptProcessor(BaseProcessService):
    def __init__(self):
        super().__init__()
        self.scraper = YouTubeScraper()
        self.repo = Repository()
        self.unavailable = 0

    def get_items_to_process(self, limit: Optional[int] = None) -> list:
        return self.repo.get_youtube_videos_without_transcript(limit=limit)

    def process_item(self, item) -> Optional[str]:
        try:
            transcript_result = self.scraper.get_transcript(item.video_id)
            return transcript_result.text if transcript_result else TRANSCRIPT_UNAVAILABLE_MARKER
        except Exception:
            return TRANSCRIPT_UNAVAILABLE_MARKER

    def save_result(self, item, result: str) -> bool:
        success = self.repo.update_youtube_video_transcript(item.video_id, result)
        if result == TRANSCRIPT_UNAVAILABLE_MARKER:
            self.unavailable += 1
        return success

    def process(self, limit: Optional[int] = None) -> dict:
        result = super().process(limit=limit)
        result["unavailable"] = self.unavailable
        return result


def process_youtube_transcripts(limit: Optional[int] = None) -> dict:
    processor = YouTubeTranscriptProcessor()
    return processor.process(limit=limit)
>>>>>>> ef3887c9d3ca5c255048389b17a5d655c67d7f8a


if __name__ == "__main__":
    result = process_youtube_transcripts()
    print(f"Total videos: {result['total']}")
    print(f"Processed: {result['processed']}")
    print(f"Unavailable: {result['unavailable']}")
    print(f"Failed: {result['failed']}")

