<<<<<<< HEAD
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

=======
>>>>>>> ef3887c9d3ca5c255048389b17a5d655c67d7f8a
from app.database.models import Base
from app.database.connection import engine

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Tables created successfully")

