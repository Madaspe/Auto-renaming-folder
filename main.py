import os, sys, time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler



class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if event.event_type == 'created' and event.is_directory:
            old_folder_name = '/'.join(event.src_path.split('/')[:-1])
            new_folder_name = old_folder_name.replace(get_only_digit(old_folder_name), str(int(get_only_digit(old_folder_name)) + 1))
            rename_folder(old_folder_name, new_folder_name)

    def on_deleted(self, event):
        if event.event_type == 'deleted' and event.is_directory:
            old_folder_name = '/'.join(event.src_path.split('/')[:-1])
            new_folder_name = old_folder_name.replace(get_only_digit(old_folder_name), str(int(get_only_digit(old_folder_name)) - 1))
            rename_folder(old_folder_name, new_folder_name)

    

def get_only_digit(string: str) -> str:
    result = ''
    for simbol in string:
        if simbol.isdigit():
            result += simbol
    return result


def rename_folder(src: str, dist: str):
    os.rename(src, dist)


def main():
    observer = Observer()
    observer.schedule(Handler(), path='/home/madaspe/HDD_MOUNT_POINT/Projects/', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        observer.stop()

if __name__ == "__main__":
    main()