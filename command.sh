#!/bin/bash
Run tests for each app
python3 manage.py test admissions
if [ $? -ne 0 ]; then
echo "Tests failed for admissions app. Please fix the errors before committing."
exit 1
fi
python3 manage.py test campus_resources
if [ $? -ne 0 ]; then
echo "Tests failed for campus_resouces app. Please fix the errors before committing."
exit 1
fi
python3 manage.py test courses
if [ $? -ne 0 ]; then
echo "Tests failed for courses app. Please fix the errors before committing."
exit 1
fi
python3 manage.py test school_blog
if [ $? -ne 0 ]; then
echo "Tests failed for school_blog app. Please fix the errors before committing."
exit 1
fi
python3 manage.py test users
if [ $? -ne 0 ]; then
echo "Tests failed for users app. Please fix the errors before committing."
exit 1
fi
If all tests pass, proceed with committing and pushing the code
git add .
echo "Enter the commit message: "
read commitMsg
git commit -m "$commitMsg"
echo "Enter the name of the branch: "
read branch
git push -u origin $branch