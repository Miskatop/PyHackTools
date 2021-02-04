# PyHackTools - scripts For Attack in python

## DDOS - ddos.py is console based utility for ddoas attacks from one computer usign fake ip
### Usage\`
```bash
python3 ddos.py [ARGUMENS]
# For Help use -h or --help flags
```
## CLIPBOARD - clipboard.py is a mini utility for handle clipboard changes
### Usage\`
```python

from clipboard import on_change

def changed(data):
  print('clipboard is changed - ', data)

on_change(changed)
```
