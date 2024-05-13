#!/bin/bash
git add .
echo "Enter a commit message: "
read commitMsg
git commit -m "$commitMsg"
eacho "What branch should be pushed to: "
rech branch
git push -u origin "$branch"