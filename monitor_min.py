import os, sys, monitor_lib
possible_drives = [r"\\.\PhysicalDrive1",r"\\.\PhysicalDrive2",r"\\.\PhysicalDrive3"]
selected_sector=0
command='info'
os.system('cls')
if len(sys.argv)>1:
    if sys.argv[1]=='w':
        print '+------------------------------------------+\n| WARNING WARNING: WRITE HAS BEEN ENABLED! |\n| PROCEED WITH CAUTION!                    |\n+------------------------------------------+'
        write_enabled=True
else:
    write_enabled=False
    print 'INFO: You are in read-only mode'
for drive in possible_drives:
    while True:
        try:
            disk = file(drive,'rb+')
            if command.split()[0]=='read':
                monitor_lib.read_sector(disk,selected_sector=selected_sector)
            elif command.split()[0]=='write':
                if write_enabled:
                    monitor_lib.write_to_sector(disk,' '.join(command.split()[1:]),selected_sector=selected_sector)
                else:
                    print 'ACCESS DENIED: WRITE NOT ENABLED!'
            elif command.split()[0]=='select':
                selected_sector=int(command.split()[1])
            elif command.split()[0]=='randomize':
                if write_enabled:
                    monitor_lib.randomize(disk,selected_sector=selected_sector)
                else:
                    print 'ACCESS DENIED: WRITE NOT ENABLED!'
            elif command.split()[0]=='info':
                monitor_lib.get_disk_info(disk,drive,selected_sector=selected_sector)
            elif command.split()[0]=='q':
                sys.exit(0)
            elif command.split()[0]=='writeo':
                if write_enabled:
                    monitor_lib.writeo(disk,command.split()[1],' '.join(command.split()[2:]),selected_sector=selected_sector)
                else:
                    print 'ACCESS DENIED: WRITE NOT ENABLED!'
            elif command.split()[0]=='append':
                if write_enabled:
                    monitor_lib.append_command(disk,command.split()[1],' '.join(command.split()[2:]),selected_sector=selected_sector)
                else:
                    print 'ACCESS DENIED: WRITE NOT ENABLED!'
            elif command.split()[0]=='help':
                print 'Commands\n--------\nread: display sector\nwrite <string>: write string to sector and zero the remaining bytes'
                print 'select <sector#>: select sector to work with\nrandomize: fill sector with random data\ninfo: display drive info'
                print 'writeo <hex offset> <string>: write string starting at offset\nappend <hexoffset> <string>: write starting at offset, without zeroing the remaining bytes'
                print 'q: quit progam\nhelp: display help menu\nArguments\n--------\nw: enable write'
            command=raw_input('SECTOR:'+str(selected_sector)+'>')
            disk.close()
        except Exception, e:
            print e