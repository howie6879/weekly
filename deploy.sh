#!/bin/sh
# echo "> Building HTML by mddocs..."
# mkdocs build

echo "> Gen mkdocs config"
pipenv run python main.py 
echo "> Push code to git"
read -p "> Please input commit info: " commit_info
git add *
git commit -m "$commit_info"
git push
echo "> Push code to gh-deploy"
mkdocs gh-deploy --clean
echo "> Done!"