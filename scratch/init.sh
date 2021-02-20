#!/usr/bin/env zsh

set -ex

london setup

# https://opensource.com/article/18/5/you-dont-know-bash-intro-bash-arrays
RESOURCES=('construction' 'glassware' 'ingredient' 'recipe' 'inventory' 'lists')

for resource in "${RESOURCES[@]}"; do
  london ${resource} recreate all
done