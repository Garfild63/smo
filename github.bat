@echo off
git init
git add .
git commit -m "Adding file github.bat"
git remote add origin https://github.com/Garfild63/smo.git
git pull origin master
git push origin master
pause
