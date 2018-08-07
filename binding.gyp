{
  'targets': [
    {
      'target_name': 'binding',
      'conditions': [
        ['OS=="linux" or OS=="android" or OS=="freebsd"', {
          'sources': [
            'src/BluetoothHciSocket.cpp'
          ]
        }],['OS=="android"', {
              'cflags': [ '-fPIC' ]
            , 'ldflags': [ '-fPIC' ]
        }]
      ],
      "include_dirs" : [
            "<!(node -e \"require('nan')\")"
        ]
    },
    {
      'target_name': 'action_after_build',
      'type': 'none',
      'dependencies': [ '<(module_name)' ],
      'copies': [
        {
          'files': [ '<(PRODUCT_DIR)/<(module_name).node' ],
          'destination': '<(module_path)'
        }
      ]
    }
  ]
}
