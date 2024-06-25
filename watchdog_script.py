import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

print("Starting watchdog script...")  # Add this line

# Configuration
file_to_watch = os.environ.get('FILE_TO_WATCH', 'test.txt')
threshold = 100  # Example threshold value

# Debugging environment variable
print(f"Environment variable FILE_TO_WATCH: {file_to_watch}")

# Get absolute path of the file to watch
absolute_path_to_watch = os.path.abspath(file_to_watch)
print(f"File to watch: {absolute_path_to_watch}")

class WatchdogHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"Event detected: {event}")
        if event.src_path == absolute_path_to_watch:
            print(f"File modified: {event.src_path}")
            self.check_file()

    def check_file(self):
        try:
            with open(absolute_path_to_watch, 'r', encoding='utf-16') as file:
                content = file.read().strip()
                print(f"File content: {content}")
                value = float(content)
                if value > threshold:
                    self.send_alert(value)
        except ValueError:
            print("Error: The file content is not a valid number.")
        except FileNotFoundError:
            print(f"Error: The file was not found at {absolute_path_to_watch}.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def send_alert(self, value):
        print(f"Alert! The value {value} exceeds the threshold of {threshold}.")

if __name__ == "__main__":
    # Ensure the file exists before starting the observer
    if not os.path.exists(absolute_path_to_watch):
        with open(absolute_path_to_watch, 'w', encoding='utf-16') as file:
            file.write("0")

    event_handler = WatchdogHandler()
    observer = Observer()
    # Watch the directory containing the file
    observer.schedule(event_handler, path=os.path.dirname(absolute_path_to_watch), recursive=False)
    observer.start()
    print(f"Watching {absolute_path_to_watch}...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
