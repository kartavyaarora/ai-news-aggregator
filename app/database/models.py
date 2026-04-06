from datetime import datetime
<<<<<<< HEAD
from typing import Optional
=======
>>>>>>> ef3887c9d3ca5c255048389b17a5d655c67d7f8a
from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class YouTubeVideo(Base):
    __tablename__ = "youtube_videos"
<<<<<<< HEAD
    
=======

>>>>>>> ef3887c9d3ca5c255048389b17a5d655c67d7f8a
    video_id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    url = Column(String, nullable=False)
    channel_id = Column(String, nullable=False)
    published_at = Column(DateTime, nullable=False)
    description = Column(Text)
    transcript = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class OpenAIArticle(Base):
    __tablename__ = "openai_articles"
<<<<<<< HEAD
    
=======

>>>>>>> ef3887c9d3ca5c255048389b17a5d655c67d7f8a
    guid = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    url = Column(String, nullable=False)
    description = Column(Text)
    published_at = Column(DateTime, nullable=False)
    category = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class AnthropicArticle(Base):
    __tablename__ = "anthropic_articles"
<<<<<<< HEAD
    
=======

>>>>>>> ef3887c9d3ca5c255048389b17a5d655c67d7f8a
    guid = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    url = Column(String, nullable=False)
    description = Column(Text)
    published_at = Column(DateTime, nullable=False)
    category = Column(String, nullable=True)
    markdown = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class Digest(Base):
    __tablename__ = "digests"
<<<<<<< HEAD
    
=======

>>>>>>> ef3887c9d3ca5c255048389b17a5d655c67d7f8a
    id = Column(String, primary_key=True)
    article_type = Column(String, nullable=False)
    article_id = Column(String, nullable=False)
    url = Column(String, nullable=False)
    title = Column(String, nullable=False)
    summary = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
<<<<<<< HEAD

=======
    sent_at = Column(DateTime, nullable=True)
>>>>>>> ef3887c9d3ca5c255048389b17a5d655c67d7f8a
