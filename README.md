# soundpadrc

test111

## todo

- always tag and push to test.pypi.org
- force pr, disallow main commit?
- semver to tag after commit?
- run action only on tag and not commit?
- if release generate changelog + push to pypi?

## example:

```python
from soundpadrc import Soundpad

sp = Soundpad()

print(sp.categories())

```

## soundpad links

https://github.com/Ilya-Kokhanovsky/soundpad.py  
https://www.leppsoft.com/soundpad/files/rc/SoundpadRemoteControl.java  
https://www.leppsoft.com/soundpad/en/rc/

## python packaging

https://packaging.python.org/en/latest/tutorials/packaging-projects/  
https://github.com/pypa/sampleproject  
https://python-semantic-release.readthedocs.io/en/latest/  
https://python-semantic-release.readthedocs.io/en/latest/automatic-releases/github-actions.html  
https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/
