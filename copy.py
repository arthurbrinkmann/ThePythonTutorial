import os
import shutil
from threading import Thread
from queue import Queue

def set_source(source):
    global source_directory
    source_directory = source

def set_destination(destination):
    global destination_directory
    destination_directory = destination

class CopyManager:
    def __init__(self):
        self.file_queue = Queue()
        self.total_size = 0
        self.copied_size = 0

    def get_size(self, file_path):
        return os.path.getsize(file_path)

    def preview_job(self):
        file_list = os.listdir(source_directory)
        self.total_size = sum(self.get_size(os.path.join(source_directory, file_name)) for file_name in file_list)
        return self.total_size

    def update_progress(self, copied_size):
        # Placeholder for progress update logic, you can implement this based on your GUI framework
        pass

    def thread_it(self):
        while not self.file_queue.empty():
            file_path = self.file_queue.get()
            with open(file_path, 'rb') as source_file, open(os.path.join(destination_directory, os.path.basename(file_path)), 'wb') as dest_file:
                shutil.copyfileobj(source_file, dest_file)
                self.copied_size += self.get_size(file_path)
                self.update_progress(self.copied_size)
            self.file_queue.task_done()

    def copy_job(self):
        file_list = os.listdir(source_directory)
        for file_name in file_list:
            file_path = os.path.join(source_directory, file_name)
            self.file_queue.put(file_path)

        num_threads = min(4, len(file_list))  # You can adjust the number of threads as needed
        threads = []
        for _ in range(num_threads):
            t = Thread(target=self.thread_it)
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        self.reset_gui()

    def reset_gui(self):
        # Placeholder for GUI reset logic
        pass

if __name__ == "__main__":
    set_source("/path/to/source")
    set_destination("/path/to/destination")

    manager = CopyManager()

    total_size = manager.preview_job()
    print(f"Total size of files to copy: {total_size} bytes")

    manager.copy_job()