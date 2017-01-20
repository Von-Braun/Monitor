Commands
--------
* read: display sector

* write <string>: write string to sector and zero the remaining bytes

* select <sector#>: select sector to work with

* randomize: fill sector with random data

* info: display drive info

* writeo <hex offset> <string>: write string starting at offset

* append <hexoffset> <string>: write starting at offset, without zeroing the remaining bytes

* q: quit progam

* help: display help menu

Arguments
--------
w: enable write

mount_drive
-----------

```
possible_drives = [r"\\.\PhysicalDrive1",r"\\.\PhysicalDrive2",r"\\.\PhysicalDrive3"]
for drive in possible_drives:
    disk = file(drive,'rb+')
```

unmount_drive
-------------

```
disk.close()
```

# Functions And Their Arguments

* write_to_sector(disk,provided_data='',selected_sector=0,sector_size = 512):

* read_sector(disk,selected_sector=0,sector_size = 512,return_list=False):

* get_disk_info(disk,drive,selected_sector=0,sector_size = 512):

* writeo(disk,offset,provided_data,selected_sector=0,sector_size = 512): 

* append_command(disk,offset,provided_data,selected_sector=0,sector_size = 512):

* randomize(disk,selected_sector=0,sector_size = 512):

# Example Output

```
INFO: You are in read-only mode
DRIVE: \\.\PhysicalDrive1
Sector Count: 125042680
Byte Count: 64021852160

SECTOR:0>  select 5324342

SECTOR:5324342>  read

a27c6c00L  01 aa 24 3f 01 5d d5 28  26 c0 f3 35 be f4 85 3b  |..$?.].(&..5...;|
a27c6c10L  9f e1 0c 37 44 93 46 d5  b5 c7 d3 2a 5e af d9 84  |...7D.F....*^...|
a27c6c20L  a1 64 b3 2a d7 5d 16 56  86 2e 82 4d 2a e5 84 14  |.d.*.].V...M*...|
a27c6c30L  a6 9c b7 a2 be 66 af fa  98 ed 6c aa f7 78 0a cb  |.....f....l..x..|
a27c6c40L  88 b8 e6 51 80 a9 50 b5  9a 74 18 e4 31 71 cb 2d  |...Q..P..t..1q.-|
a27c6c50L  20 a1 fb c2 b6 1c 95 69  51 72 32 c1 01 2b 57 9c  |.......iQr2..+W.|
a27c6c60L  bc ac 7a de 05 8d 4b c5  6c b7 8f a7 8e 48 1b 41  |..z...K.l....H.A|
a27c6c70L  28 59 71 25 1a 84 c7 14  10 0f e0 07 d9 c3 77 bb  |(Yq%..........w.|
a27c6c80L  3b 8a 5a aa c3 68 88 cc  f9 2b f8 c7 be 94 1d f1  |;.Z..h...+......|
a27c6c90L  67 62 8a 17 00 4c cb 60  a8 e1 ef 96 77 6e a1 0b  |gb...L.`....wn..|
a27c6ca0L  5e b3 f2 d1 9f 6d 69 99  e0 d2 55 a9 12 2f c7 97  |^....mi...U../..|
a27c6cb0L  01 53 55 3d 48 af 2e 46  ad 93 e4 23 01 c6 85 7a  |.SU=H..F...#...z|
a27c6cc0L  6e 41 01 17 15 6b 98 2a  a1 c3 56 2d ad 62 58 fe  |nA...k.*..V-.bX.|
a27c6cd0L  a6 56 8e 04 82 d0 e6 37  d3 0c 51 d1 dc be f2 63  |.V.....7..Q....c|
a27c6ce0L  2a 90 f7 2e f1 d3 f8 c8  5b f6 59 2b 1e 9f 28 23  |*.......[.Y+..(#|
a27c6cf0L  ec f7 3a 0b a3 03 11 90  ea 22 32 cf 17 05 5e 19  |..:......"2...^.|
a27c6d00L  ff ed 65 a7 c6 1f f5 12  92 aa be f5 6f e4 c2 7c  |..e.........o..||
a27c6d10L  e6 55 58 03 f4 de cb 68  7d 1e a4 91 7f 72 be 3f  |.UX....h}....r.?|
a27c6d20L  90 b7 9c 78 6e 78 af a1  59 fd d7 35 b7 80 ca 96  |...xnx..Y..5....|
a27c6d30L  51 d7 ed 98 b9 2b 6d 3d  29 9a 0d dc 8a b1 a5 2b  |Q....+m=)......+|
a27c6d40L  1b 67 13 ff a8 03 d6 1e  0e b8 e7 b6 a0 8c 09 93  |.g..............|
a27c6d50L  27 67 90 da 71 a8 65 f8  05 c4 d5 54 c6 6f 73 15  |'g..q.e....T.os.|
a27c6d60L  df ea 3c ac dc e4 f5 cb  c2 5b a2 c9 91 b7 d2 00  |..<......[......|
a27c6d70L  89 5c 6a 65 0b 72 0a b0  ad 63 23 da 9f ad 0f 28  |.\je.r...c#....(|
a27c6d80L  77 84 8b 8a f6 ce 66 e1  35 ca e0 d6 ba b6 4a e2  |w.....f.5.....J.|
a27c6d90L  c4 be 27 d5 e4 70 e3 2c  6f 80 a9 f5 d5 d7 e6 0d  |..'..p.,o.......|
a27c6da0L  50 8d 46 82 0b 5b 19 7b  af 45 69 98 59 30 69 dc  |P.F..[.{.Ei.Y0i.|
a27c6db0L  db ca 7c aa 3b f2 e7 b3  61 d2 75 43 c5 8f 5a 2c  |..|.;...a.uC..Z,|
a27c6dc0L  d3 f6 13 5a 07 9f ab 92  4e 59 97 04 dc 8a 55 09  |...Z....NY....U.|
a27c6dd0L  8e f0 b0 15 77 b9 5b d7  91 97 00 32 4f 77 57 86  |....w.[....2OwW.|
a27c6de0L  55 8e 29 69 c7 ce 3e aa  f7 56 0f bb d5 c4 ee 84  |U.)i..>..V......|
a27c6df0L  55 53 ee c3 c1 be e8 32  60 21 1c 4a b6 ff ff ff  |US.....2`!.J....|

SECTOR:5324342>
```
