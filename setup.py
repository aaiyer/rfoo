"""
    setup.py

    Setup script for rfoo

    Copyright (c) 2010 Nir Aides <nir@winpdb.org> and individual contributors.
    All rights reserved.

    Redistribution and use in source and binary forms, with or without modification,
    are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice,
    this list of conditions and the following disclaimer.

    2. Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.

    3. Neither the name of Nir Aides nor the names of other contributors may
    be used to endorse or promote products derived from this software without
    specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
    ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
    WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
    ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
    (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
    LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
    ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
    SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""


import sys

from distutils.core import setup
from distutils.extension import Extension
from distutils.command.build_ext import build_ext

if 'bdist_egg' in sys.argv:
    sys.stderr.write("""===========================================================
rfoo can not be installed by easy_install due to conflict
between easy_install and Cython:
http://mail.python.org/pipermail/distutils-sig/2007-September/008205.html

To install rfoo, download the source archive, extract it
and install with:
    sudo python setup.py install
===========================================================\n""")
    sys.exit(1)


ext_modules = [Extension("rfoo.marsh", ["rfoo/marsh.pyx"])]


setup(
    name = 'rfoo',
    version = '1.3.1',
    description = 'Fast RPC client/server module.',
    author = 'Nir Aides',
    url = 'https://github.com/aaiyer/rfoo',
    license = 'BSD',
    packages = ['rfoo', 'rfoo.utils'],
    scripts = ['scripts/rconsole'],
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
