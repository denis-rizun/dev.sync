export const GEN_CODE = `denis-rizun@onlinegame-14-121: ~/.ssh$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/denis-rizun/.ssh/id_rsa): id_rsa_forwebhook
id_rsa_forwebhook already exists.
Overwrite (y/n)? y
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in id_rsa_forwebhook.
Your public key has been saved in id_rsa_forwebhook.pub.
The key fingerprint is:
27:04:9f:0b:21:73:a7:2a:cd:4e:9e:43:2a:45:c2:29 denis-rizun@onlinegame-14-121
The key's randomart image is:
+--[ RSA 2048]----+
|    o + .        |
|. .  + * .       |
|Eo.   o +        |
|.o o . o .       |
|  o *   S .      |
| . B .   o       |
|. .              |
| .   .           |
|                 |
+-----------------+`;

export const ADD_KEY_CMD = `[denis-rizun@host ~]$ cd ~/.ssh
[denis-rizun@host .ssh]$ cat id_rsa_forwebhook.pub >> authorized_keys`;
