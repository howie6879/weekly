#!/bin/sh
# echo "> Building HTML by mddocs..."
# mkdocs build

echo "> Push code to git"
read -p "> Please input commit info: " commit_info
git add *
git commit -m "$commit_info"
git push
mkdocs gh-deploy --clean
echo "> Done!"