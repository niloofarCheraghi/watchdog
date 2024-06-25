#!/bin/sh

echo "Starting entrypoint script..."
echo "Environment variable FILE_TO_WATCH: $FILE_TO_WATCH"

# Ensure the file exists
if [ ! -f "$FILE_TO_WATCH" ]; then
  echo "Creating file $FILE_TO_WATCH..."
  echo "0" > "$FILE_TO_WATCH"
fi

# Print the file to watch
echo "Watching file: $FILE_TO_WATCH"

# Run the watchdog script
exec python watchdog_script.py
