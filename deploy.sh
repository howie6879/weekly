#!/bin/sh
echo "> Building HTML by mddocs..."
mkdocs build

echo "> Push code to git"
read -p "> please input commit info: " commit_info
git add *
git commit -m "Auto push: $commit_info"
git push
# mkdocs gh-deploy --clean
echo "> Done!"