@echo off
git init
git add .
git commit -m "Adding positive and negative tests"
git remote add origin https://github.com/Garfild63/smo.git
git pull origin master
git push origin master
pause
