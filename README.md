reimagined-winner
---


### Local run
```
$ git clone git@github.com:esemi/reimagined-winner.git
$ cd reimagined-winner
$ export PYTHONPATH="${PYTHONPATH}:`pwd`"
$ python3.9 -m venv venv
$ source venv/bin/activate
$ pip install poetry
$ poetry config virtualenvs.create false --local
$ poetry install
```

### Todo
- mvp of UI test
- action for run tests
- action for flake8