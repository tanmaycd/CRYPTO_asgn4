
~$ nc socket.cryptohack.org 13379
Intercepted from Alice: {"supported": ["DH1536", "DH1024", "DH512", "DH256", "DH128", "DH64"]}

Send to Bob: {"supported": ["DH64"]}

Intercepted from Bob: {"chosen": "DH64"}

Send to Alice: {"chosen": "DH64"}

Intercepted from Alice: {"p": "0xde26ab651b92a129", "g": "0x2", "A": "0x71bd503db85c8a69"}
Intercepted from Bob: {"B": "0xcd0abfbbdf7db925"}
Intercepted from Alice: {"iv": "622269623bd6382fe4d7ac542951f944", "encrypted_flag": "5901469760c0ff6b578a77a56f848ca59d6c7015f9df1ce452fe71a2a8082fd7"}

#crypto{d0wn6r4d35_4r3_d4n63r0u5}