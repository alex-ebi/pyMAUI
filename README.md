# ShootingPiDemo

[![pipeline status](https://git.uibk.ac.at/csaq1985/shootingpidemo/badges/master/pipeline.svg)](https://git.uibk.ac.at/csaq1985/shootingpidemo/commits/master)
[![coverage report](https://git.uibk.ac.at/csaq1985/shootingpidemo/badges/master/coverage.svg)](https://git.uibk.ac.at/csaq1985/shootingpidemo/commits/master)


Demonstrate and test GitLab funtionality with example python project.

## Python Template
Using [Scientific Python Cookiecutter](https://nsls-ii.github.io/scientific-python-cookiecutter/philosophy.html) 
as template with minor changes for university GitLab.

## GitLab Settings
Sensible settings to ensure code quality:

### Protect Master Branch
Settings > Repository > Protected Branches

"Nobody should be able to push straight to master"

### Merge Checks
Settings > General > Merge Requests > Merge Checks

"Pipelines should be okay and all discussions resolved"

### Repository Status and Reports
Settings > CI / CD > General pipelines

Pipeline status and coverage report

Requires test coverage parsing (with `^TOTAL.+?(\d+\%)$`)

## Demonstration
- [x] SSH keys
- [ ] Rebasing (example: dev branch to master)
- [ ] Create merge request
- [ ] Code review
- [ ] Updating pipeline (example: add pycodestyle)

## Unused Python Developer Tools 
* Pylint: code analysis tool which helps to enforce coding standards
* Bandit: analyzes code to find common security issues
* Black: formats Python code without compromise
* isort: formats imports by sorting alphabetically and separating into sections
* pip-tools: command line tools for managing packages and requirements
* tqdm: easy to use progress bar

[Even more dev tools](https://reposhub.com/python/learning-tutorial/ml-tooling-best-of-python-dev.html)
