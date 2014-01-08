# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'targets': [
    {
      'target_name': 'zookeeper',
      'type': 'static_library',
      'sources': [
        'config.h',
        'src/zookeeper.c',
        'include/zookeeper.h',
        'include/zookeeper_version.h',
        'include/zookeeper_log.h',
        'src/recordio.c',
        'include/recordio.h',
        'include/proto.h',
        'src/zk_adaptor.h',
        'generated/zookeeper.jute.h',
        'generated/zookeeper.jute.c',
        'src/zk_log.c',
        'src/zk_hashtable.h',
        'src/zk_hashtable.c',
        'src/hashtable/hashtable.h',
        'src/hashtable/hashtable_itr.h',
        'src/hashtable/hashtable.c',
        'src/hashtable/hashtable_itr.c',
        'src/hashtable/hashtable_private.h',
        'src/mt_adaptor.c',
        'include/winconfig.h',
        'include/winstdint.h',
        'src/winport.c',
        'src/winport.h',
      ],
      'defines': [
        'THREADED',
      ],
      'include_dirs': [
        '.',
        'include',
        'generated',
        'src/hashtable',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
        'include',
        'generated',
        ],
        'defines': [
          'THREADED',
         ],
      },
      'conditions': [
        ['OS!="win"', {
          'sources!':[
            'include/winconfig.h',
            'include/winstdint.h',
            'src/winport.c',
            'src/winport.h',
          ],
          'defines': [
            '_GNU_SOURCE',
            'HAVE_CONFIG_H',
          ],
          'cflags': [ '-std=gnu99' ]
        }, {
          'sources!': [
            'config.h'
          ],
          'defines': [
            'USE_STATIC_LIB',
          ],
          'direct_dependent_settings': {
            'defines': [
              'USE_STATIC_LIB',
            ],
          },
          'msvs_settings': {
            'VCCLCompilerTool': {
              'WarningLevel': '4',
              'WarnAsError': 'false',
              'AdditionalOptions': [ '/WX-' ],
            }
          }
        }],
        ['OS=="mac"', {
          'xcode_settings': {
            'GCC_C_LANGUAGE_STANDARD': 'gnu99',
          }
        }],
      ],
    },
    {
      'target_name': 'zkcli',
      'type': 'executable',
      'sources': [
        'src/cli.c'
      ],
      'dependencies': [
        'zookeeper',
      ],
    },
  ],
}
