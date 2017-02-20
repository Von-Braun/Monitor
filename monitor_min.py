import os,sys,monitor_lib,subprocess,traceback

def get_cmd_output(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return proc.communicate() #out, error

os.system('cls')
possible_drives_logical = get_cmd_output('wmic logicaldisk get caption')[0].strip('Caption').strip().replace('       \r\r\n','').split(':')[:-1]
possible_drives_physical = get_cmd_output('wmic diskdrive get name')[0].strip('Name').strip().split()
print get_cmd_output('wmic logicaldisk get caption,description,size,volumename')[0],
print get_cmd_output('wmic diskdrive get caption,name,interfaceType,size,TotalSectors')[0],

choice='!'
while True:
    if choice.isdigit() and choice in ''.join(possible_drives_physical):
        drive=possible_drives_physical[int(choice)]
        break
    elif choice.upper() in possible_drives_logical:
        drive = r"\\.\%s:" %choice.upper() #\\.\X:
        break
    elif choice=='quit':
        sys.exit(0)
    choice = raw_input('Drive:')

selected_sector=0
command='select 0'
os.system('cls')
if len(sys.argv)>1:
    if sys.argv[1]=='w':
        print '+------------------------------------------+\n| WARNING WARNING: WRITE HAS BEEN ENABLED! |\n| PROCEED WITH CAUTION!                    |\n+------------------------------------------+'
        write_enabled=True
else:
    write_enabled=False
    print 'INFO: You are in read-only mode'

while True:
    try:

        disk = file(drive,'rb+')
        if command=='':
            print 'Invalid Command!'

        elif command.split()[0]=='read':
            monitor_lib.read_sector(disk,selected_sector=selected_sector)
        elif command.split()[0]=='write':
            if write_enabled:
                monitor_lib.write_to_sector(disk,' '.join(command.split()[2:]),False,command.split()[1],selected_sector=selected_sector)
            else:
                print 'ACCESS DENIED: WRITE NOT ENABLED!'
        elif command.split()[0]=='writehex':
            if write_enabled:
                monitor_lib.write_to_sector(disk,' '.join(command.split()[2:]),True,command.split()[1],selected_sector=selected_sector)
            else:
                print 'ACCESS DENIED: WRITE NOT ENABLED!'
        elif command.split()[0]=='select':
            selected_sector=int(command.split()[1])
        elif command.split()[0]=='randomize':
            if write_enabled:
                monitor_lib.randomize(disk,selected_sector=selected_sector)
            else:
                print 'ACCESS DENIED: WRITE NOT ENABLED!'
        elif command.split()[0]=='clear':
            if write_enabled:
                monitor_lib.clear(disk,selected_sector=selected_sector)
            else:
                print 'ACCESS DENIED: WRITE NOT ENABLED!'
        elif command.split()[0]=='info':
            if choice.isdigit():
                monitor_lib.get_disk_info(disk,drive,selected_sector=selected_sector)
            else:
                print 'Drive:',drive
                print 'Info is for physical drives only!'
        elif command.split()[0]=='q':
            sys.exit(0)
        elif command.split()[0]=='help':
            print '\nCommands\n--------\nread: display sector\nwrite <offset> <string>: write string to sector and zero the remaining bytes'
            print 'select <sector#>: select sector to work with\nrandomize: fill sector with random data\ninfo: display drive info'
            print 'clear: fill sector with zero data\nwritehex <offset> <hex>: write hex to sector and zero the remaining bytes'
            print 'q: quit progam\nhelp: display help menu\n\nArguments\n--------\nw: enable write\n'
        command=raw_input('SECTOR:'+str(selected_sector)+'>')
        disk.close()
    except Exception, e:
        print 'Error:',e
        traceback.print_exc()
        command=''
