#!/usr/bin/env python3
#  Copyright 2024 Direkt Embedded Pty Ltd
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


"""
A module used to package a version of the python package as defined by setup.py which should be in the same
directory as this file.
git describe --dirty is used to check that the VERSION content is the same, to ensure a packages isn't created
which does not match the git tag. It also does not allow for a package to be created if the git tree is dirty.
"""


def get_git_version():
    import subprocess
    return subprocess.check_output(["git", "describe", "--dirty"]).strip().decode()


def is_version_clean(git_version):
    return not ('dirty' in git_version)


def package():
    from build.__main__ import main
    print("VERSION file matches git version, running setup to package")
    main(["--sdist", "--wheel"])


def get_package_version(path):
    import sys
    sys.path.insert(0, path)
    from testdirektor import __version__
    return __version__


if __name__ == "__main__":
    import os

    return_code = -1
    current_path = os.path.dirname(os.path.abspath(__file__))
    package_path = os.path.join(current_path, 'src')
    git_version = get_git_version()
    if is_version_clean(git_version):
        package_version = get_package_version(os.path.join(package_path))
        if package_version != git_version:
            print(f"Package version ({package_version}) not same as git version ({git_version})\n"
                  "Please update, commit, tag and re-run this script")
        else:
            package()
            return_code = 0
    else:
        print(f"Git version ({git_version}) not clean, not packaging\n"
              "git tree must be clean and tag must match VERSION file")

    exit(return_code)
