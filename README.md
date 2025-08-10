# cookiecutter-python-cmdline-package

This cookiecutter template constructs a new python [click](https://click.palletsprojects.com/en/stable/) + [rich](https://rich.readthedocs.io/en/stable/introduction.html) command line package suitable for publishing to PyPI,  and for publishing documentation to readthedocs.org.

## Features of projects produced with this cookiecutter

* Python 3.11+ ready
* __Modern package configuration__: `pyproject.toml` provided, with default sets of packages (`click`, `rich` and `pydantic`, `pydantic-settings`), `ruff` configuration, python build configuration
* __Package management__: `uv` for package management
* __Autoenv__: [autoenv](https://github.com/hyperupcall/autoenv) ready for activating and deactivating your virtualenv when you move in and out of the project.
* __Versioning__ Uses `bumpversion` to handle versioning.
* __Settings management__: Built in configuration management system

    * A `pydantic-settings` `Settings` object with a default set of fields.
    * Cascacding TOML based config files: in `/etc/`, in the user's home directory, in the current directory, and finally via command line options
    * Environment variables work also to configure your command line tool's settings

* Two default commands:

    * `version`: print the version number, as well as the versions of major important packages
    * `settings`: print all the settings after dealing with defaults, config files and environment variables

* __Licensing__: MIT licensed by default, though, of course, you can change that.
* __Documentation__: Comes with a full skeleton for a set of Sphinx documentation ready for you to expand (in `doc`), including a "How to contribute" page. Plus a reasonable `.readthedocs.yaml` ready for use.
* __Github hooks__: Comes with one hook, which generates a new `requirements.txt` from `uv.lock` every time you push to master.  This is important for readthedocs.org, which can't work with `uv` yet.
* __Helper scripts__: `Makefile` with useful targets, plus `bin/release.sh` which will check that everything has been committed to git, check that the last commit was a `bumpversion` commit, push your code up to `origin` and release to PyPI via `twine`

## Usage

In the below instructions:

* Any time you see the string "`my_project`", replace it with the
  `project_python_name` you enter at the cookiecutter prompts, below.

### Install and run cookiecutter to create the project folder

```bash
> uv tool install cookiecutter
> cookiecutter https://github.com/cmalek/cookiecutter-python-cmdline-package
```

**NOTES**:

### Create a python virtual environment for your new project and activate it

After building the project with cookiecutter, ``cd`` into ``my_project`` and run:

```bash
uv venv -p 3.13
```

If 3.13 is not a choice, you need to run:

```bash
uv python install 3.13
```

You will also need `autoenv`:

``` bash
curl -#fLo- 'https://raw.githubusercontent.com/hyperupcall/autoenv/main/scripts/install.sh' | sh
```

Once the venv is installed in `my_project/.venv/` and you have installed
`autoenv`, you can activate it by ``cd``ing out of the ``my_project`` folder,
which will trigger bash to ask if you want to run the ``.autoenv.leave`` script
(say yes), and then ``cd``ing back in, which will ask if you want to run the
`.autoenv` script (say yes). Your venv will now be automatically activated
whenever you're in the ``my_project`` folder, and your bash prompt will change
to indicate as much.

## Bootstrapping your project

### Install your dependencies

```bash
cd my_project
uv sync --dev
```

### Set up git and gihub

Go to github.com, login to your organization (probably just your own account),
and create a new project named for the project name you chose.

In your new

```bash
git init
git add -A
git commit -am 'initial commit'
git tag 0.1.0
git remote add origin git@github.com:your-org/my_project.git
git push --tags -u origin master
```

## Fix the documentation

Once you have the app working, put some effort into making the Sphinx
docs build cleanly and have some initial descriptions and whatnot.

At the least, edit `doc/source/index.rst` and fill in the appropriate sections,
and go through all the heading under/overlines in all the `.rst` files in
`doc/source` and below to have exactly the same the number of characters in the
heading text.

Then build the docs and look at them:

```bash
make docs
```

This will build the HTML docs and open them in your default browser (if you're on MacOS; I don't know how to do it for other OSes).

### ReadTheDocs

Now go to your <https://readthedocs.org> account, login and create a new ReadTheDOcs project to which to publish your documentation.  Follow the directions there to link it to the github repository.

## Releasing to PyPI

Commit all your changes to git.

You will need ``twine`` and ``bumpversion`` installed, and properly configured to publish to PyPI.

If you don't have ``twine`` installed:

```bash
uv tool install twine bumpversion
```

Now:

```bash
bumpversion <major|minor|version>
make release
```

This should:

* Bump the version of your package in these files:

    * `my_project/__init__.py`
    * `Makefile`
    * `pyproject.toml`
    * `doc/source/conf.py`
    * `doc/source/index.rst`
    * `doc/srouce/overview/configuration.rst`
    * `my_project/settings.py`

* Tag the current revision in git with the new version number
* Build the sdist and wheel distributions for your package
* Upload them to PyPI
