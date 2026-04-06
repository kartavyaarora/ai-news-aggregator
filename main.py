from app.daily_runner import run_daily_pipeline


def main(hours: int = 24, top_n: int = 10):
    return run_daily_pipeline(hours=hours, top_n=top_n)


if __name__ == "__main__":
    import sys
<<<<<<< HEAD
    
    hours = 24
    top_n = 10
    
=======

    hours = 24
    top_n = 10

>>>>>>> ef3887c9d3ca5c255048389b17a5d655c67d7f8a
    if len(sys.argv) > 1:
        hours = int(sys.argv[1])
    if len(sys.argv) > 2:
        top_n = int(sys.argv[2])
<<<<<<< HEAD
    
    result = main(hours=hours, top_n=top_n)
    exit(0 if result["success"] else 1)

=======

    result = main(hours=hours, top_n=top_n)
    exit(0 if result["success"] else 1)
>>>>>>> ef3887c9d3ca5c255048389b17a5d655c67d7f8a
