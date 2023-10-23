git add .

commit_message=$(git log --oneline -1 --pretty=%B)
git commit -m "$commit_message"

@REM git remote add origin git@github.com:evanhollier/BG3_Mods.git

git push -u origin master