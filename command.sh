#!/bin/bash

git add . 
echo "Enter the comit message: "
read commitMsh
git commit -m "$commitMsg"
echo "Enter the name of the branch: "
read branch
git push -u origin $branch
