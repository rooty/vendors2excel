#!/usr/bin/python
# Copyright (c) 2010-2012 OpenStack, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages


name = 'swift'


with open('tools/pip-requires', 'r') as f:
    requires = [x.strip() for x in f if x.strip()]


setup(
    name=name,
    version="1.0",
    description='Swift',
    license='Apache License (2.0)',
    author='OpenStack, LLC.',
    author_email='openstack-admins@lists.launchpad.net',
    url='https://launchpad.net/swift',
    packages=find_packages(exclude=['test', 'bin']),
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6',
        'Environment :: No Input/Output (Daemon)',
        'Environment :: OpenStack',
    ],
    install_requires=requires,
    scripts=[
        '',
    ],
    entry_points={
        'paste.app_factory': [
            'proxy=swift.proxy.server:app_factory',
            'object=swift.obj.server:app_factory',
            'container=swift.container.server:app_factory',
            'account=swift.account.server:app_factory',
        ],
        'paste.filter_factory': [
            'healthcheck=swift.common.middleware.healthcheck:filter_factory',
            'memcache=swift.common.middleware.memcache:filter_factory',
            'ratelimit=swift.common.middleware.ratelimit:filter_factory',
            'cname_lookup=swift.common.middleware.cname_lookup:filter_factory',
            'catch_errors=swift.common.middleware.catch_errors:filter_factory',
            'domain_remap=swift.common.middleware.domain_remap:filter_factory',
            'staticweb=swift.common.middleware.staticweb:filter_factory',
            'tempauth=swift.common.middleware.tempauth:filter_factory',
            'keystoneauth=swift.common.middleware.keystoneauth:filter_factory',
            'recon=swift.common.middleware.recon:filter_factory',
            'tempurl=swift.common.middleware.tempurl:filter_factory',
            'formpost=swift.common.middleware.formpost:filter_factory',
            'name_check=swift.common.middleware.name_check:filter_factory',
            'proxy_logging=swift.common.middleware.proxy_logging:'
            'filter_factory',
        ],
    },
)