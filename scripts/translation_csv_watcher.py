import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from django.core.management import call_command
from django.conf import settings

class FileModifiedHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == settings.CSV_FILE_PATH:
            print(f"{event.src_path} has been modified. Importing translations...")
            call_command('import_translation', settings.CSV_FILE_PATH)

if __name__ == "__main__":
    path_to_watch = os.path.dirname(settings.CSV_FILE_PATH)
    event_handler = FileModifiedHandler()
    observer = Observer()
    observer.schedule(event_handler, path_to_watch, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()