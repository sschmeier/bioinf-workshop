# bioinf-workshop
Facilitated through [MDwiki](https://dynalon.github.io/mdwiki/#!index.md). Based on version [0.6.2](https://github.com/Dynalon/mdwiki/releases/download/0.6.2/mdwiki-0.6.2.zip).

## Publish on github pages (http://sschmeier.github.io/bioinf-workshop)
To publish this tutorial on the github pages one needs to push the origin to gh-pages.

  - Make changes in the master branch
  - Once changes are good to go to gh-pages change branch to gh-pages 
  - merge changes from master to gh-pages
  - commit changes
  - push gh-pages
  - return to master branch

```bash
git checkout gh-pages
git merge master
#git commit -m "Merged changes from master to gh-pages"
git push origin gh-pages
git checkout master
```




