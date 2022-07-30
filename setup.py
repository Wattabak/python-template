from pathlib import Path

import toml
from setuptools import find_packages, setup

PACKAGE_ROOT = Path(__file__).resolve().parent


def load_python_version(default: str,
                        version_file_path: Path = PACKAGE_ROOT / '.python-version',
                        ) -> str:
    '''Retrieves the current project python version from the .python-version file

    returns default value if the version file does not exist or the path is wrong, or the file is empty
    '''
    if not isinstance(version_file_path, Path):
        version_file_path = Path(version_file_path)
    if not version_file_path.exists():
        return default
    version = version_file_path.read_text().strip()
    if not version:
        return default
    return '>=' + version


def read_requirements(requirements_path: Path):
    return PACKAGE_ROOT.joinpath(requirements_path).read_text().strip()


def read_long_description(readme_path: Path):
    return readme_path.read_text().strip()


poetry_settings = toml.loads(PACKAGE_ROOT.joinpath('pyproject.toml').read_text())

author, email = poetry_settings['tool']['poetry']['authors'].rsplit(' ', 1)

setup(
    name=poetry_settings['tool']['poetry']['name'],
    description=poetry_settings['tool']['poetry']['description'],
    version=load_python_version(default='3.8'),
    author=author,
    email=email,
    long_description=read_long_description(readme_path=PACKAGE_ROOT / 'README.md'),
    long_description_content_type="text/markdown",
    packages=find_packages(
        where=str(PACKAGE_ROOT.absolute()),
        include="parser_gibdd",
        exclude="./tests"
    ),
    include_package_data=True,
    install_requires=read_requirements(PACKAGE_ROOT / "requirements.txt"),
    extras_require={
        "dev": read_requirements(PACKAGE_ROOT / "requirements-dev.txt"),
    },
    entry_points={
        'console_scripts': [
            'cli_script = package_name.services.cli_1:main'
        ]
    },
    python_requires=load_python_version(
        default=poetry_settings['tool']['poetry']['dependencies']['python'],
        version_file_path=PACKAGE_ROOT / '.python-version'
    ),
    # sets up the version of the package to be imported from the git tag
    setuptools_git_versioning={
        "enabled": True,
    },
    setup_requires=["setuptools-git-versioning"],
)
