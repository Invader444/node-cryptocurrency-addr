{
    "targets": [
        {
            "target_name": "cryptocurrencyaddr",
            "sources": [
                "cryptocurrencyaddr.cc"
            ],
            'conditions': [
                ['OS=="linux"',
                  {
                    'link_settings': {
                      'libraries': [
                        '-lgmp'
                      ]
                    }
                  }
                ],
                ['OS=="mac"',
                  {
                    'link_settings': {
                      'libraries': [
                        '-lgmp'
                      ]
                    }
                  }
                ],
                ['OS=="win"',
                  {
                    'link_settings': {
                      'libraries': [
                        '-lgmp.lib'
                      ],
                    }
                  }
                ]
              ],
            "cflags_cc": [
                "-std=c++0x"
            ],
        }
    ]
}
