[Functional testing](https://esemi.github.io/reimagined-winner/) for web-application.
---
[![wemake-python](https://github.com/esemi/reimagined-winner/actions/workflows/linters.yml/badge.svg?branch=master)](https://github.com/esemi/reimagined-winner/actions/workflows/linters.yml)
[![Pytest](https://github.com/esemi/reimagined-winner/actions/workflows/tests.yml/badge.svg?branch=master)](https://github.com/esemi/reimagined-winner/actions/workflows/tests.yml)


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
$ pytest
```

### Todo
- [x] mvp of UI test
- [x] action for run tests
- [x] action for flake8
- [x] enable allure
- [ ] real app-hostname
- [ ] determine priority happy-paths cases
- [ ] tests for happy-paths
- [ ] determine priority error cases
- [ ] tests for error cases
