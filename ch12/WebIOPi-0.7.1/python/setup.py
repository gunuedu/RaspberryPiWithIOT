from distutils.core import setup, Extension

classifiers = ['Development Status :: 3 - Alpha',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.6',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: Home Automation',
               'Topic :: System :: Hardware']

setup(name             = 'WebIOPi',
      version          = '0.7.1',
      author           = 'Eric PTAK',
      author_email     = 'trouch@trouch.com',
      description      = 'A package to control Raspberry Pi GPIO from the web',
      long_description = open('../doc/README').read(),
      license          = 'MIT',
      keywords         = 'RaspberryPi GPIO Python REST',
      url              = 'http://code.google.com/p/webiopi/',
      classifiers      = classifiers,
      packages         = ["webiopi",
                          "webiopi.utils",
                          "webiopi.clients",
                          "webiopi.protocols",
                          "webiopi.server",
                          "webiopi.decorators",
                          "webiopi.devices",
                          "webiopi.devices.digital",
                          "webiopi.devices.analog",
                          "webiopi.devices.sensor",
                          "webiopi.devices.shield"
                          ],
      ext_modules      = [Extension('webiopi.GPIO', ['native/bridge.c', 'native/gpio.c', 'native/cpuinfo.c'])],
      )
