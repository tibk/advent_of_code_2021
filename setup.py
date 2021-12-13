import codecs
import os.path
import re
import sys

import git

from setuptools import find_packages, setup


def load_dependencies(filename):
    if not os.path.exists(filename):
        return None, None
    install_requires = []
    dependency_links = []
    for line in codecs.open(filename, encoding="utf-8"):
        line = line.strip()
        m = re.match(r"http.+#egg=(?P<pkgname>.+)", line)
        if m:
            dependency_links.append(line)
            install_requires.append(m.groupdict()["pkgname"])
        else:
            install_requires.append(line)
    return install_requires, dependency_links


install_requires, dependency_links = load_dependencies("requirements.txt")


def lazy_find_packages(*args, **kwargs):
    if {"--name", "--version"} & set(sys.argv):
        return None
    return find_packages(*args, **kwargs)


def build_version(version_number):
    git_repo = git.repo.Repo(".", search_parent_directories=True)
    last_commit = [c for c in git_repo.iter_commits(max_count=1, paths=".")].pop()
    version = "{}+{}".format(version_number, last_commit.hexsha[:8])
    return version


setup(
    name="advent_of_code",
    version=build_version("1.0.0"),
    url="https://github.com/tibk/advent_of_code_2021",
    author="tibk",
    author_email="secret",
    packages=lazy_find_packages(exclude=["ez_setup", "vendors"]),
    include_package_data=True,
    zip_safe=False,
    platforms="any",
    install_requires=install_requires,
    classifiers=[
        "Development Status :: Release",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
