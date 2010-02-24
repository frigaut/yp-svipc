#!/usr/bin/env python
# setenv DISTUTILS_DEBUG

#from distutils.core import setup, Extension
from numpy.distutils.core import setup, Extension
from os import environ as env

version = '0.4'                   # module version

#
# power users may want to play with these options
#

undef_macros=[
#   'PYTHON_SVIPC_NODEBUG',             # compile without debug
   ]
   
define_macros=[
   ('PYTHON_SVIPC_VERSION',          '\\\"%s\\\"' % version),
   ('SVIPC_NOSEGFUNC',               None),
   ]

extra_compile_args=[
   #'-g3',
   #'-ggdb3'
]

setup(name='python-svipc',
      version=version,
      description='System V IPC for Python',
      long_description='A python plugin to System V IPC.',
      author='Matthieu Bec',
      author_email='mbec@gemini.edu',
      url='http://myst.cl.gemini.edu/gemini/repo',
      license='GNU General Public License',
      ext_modules=[
         Extension(
            name='svipc',
            sources = [
               '../common/svipc.c',
               'svipc_module.c',
              ],
            include_dirs=['../common'],
            define_macros=define_macros,
            #undef_macros=undef_macros,
            #library_dirs=[],
            #libraries = [],
            #runtime_library_dirs = [],
            #extra_objects = [string],
            #extra_compile_args = extra_compile_args,
            #extra_link_args = ['string'],
            #export_symbols = [string],
            #depends = [string],
            #language = string,
            )
         ],
      #py_modules=[],
      #data_files=[('share/python-ca', ['glade/ca_admin.glade']),
      #    #('config', ['cfg/data.cfg']),
      #    #('/etc/init.d', ['init-script'])
      #   ],
      )
     
