inotifywait -e close_write,moved_to,create -m . |
while read -r directory events filename; do
  if [ "$filename" = "repos.yaml" ]; then
    sudo python controller.py
  fi
done
