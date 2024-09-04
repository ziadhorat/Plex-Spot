import logging

def setup_logging():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    return logging.getLogger(__name__)

def format_time(seconds):
    mins, secs = divmod(seconds, 60)
    hrs, mins = divmod(mins, 60)
    return f"{int(hrs)}h {int(mins)}m {int(secs)}s"

