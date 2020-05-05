#!/usr/bin/env bash

for f in $(find /home/grant/Projects/amari/tortuga/dump/upneat -type f); do
  curl -H "Content-Type: application/json" -X POST http://localhost:5000/api/v1/cocktails/ -d "$(cat $f | yq -j '.[0]')" -f -s >/dev/null
  if [[ "$?" != "0" ]]; then
    echo $f
  fi
done
