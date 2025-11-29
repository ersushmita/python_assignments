from mimetypes import inited

git config --global user.name "ersushmita"
git config --global user.email "ersushmita@gmail.com"
git config --global color.ui auto
git init
git remote add origin https://github.com/ersushmita/python_assignments.git
git pull origin main
git status

git add .
git status
git commit -m "commit message"
git push