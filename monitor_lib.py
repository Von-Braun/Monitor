from random import randint

def write_to_sector(disk,provided_data='',selected_sector=0,sector_size = 512):
    data=[]
    for character in list(provided_data):
        data.append(character)
    empty_space=sector_size-len(data)
    for i in range(0,empty_space):
        data.append(chr(0))
    disk.seek(selected_sector*sector_size)
    disk.write(bytearray(data))

def read_sector(disk,selected_sector=0,sector_size = 512,return_list=False):
    disk.seek(selected_sector*sector_size)
    hex_data = ("{:02x}".format(ord(c)) for c in disk.read(sector_size)) #list of 512 hex bytes
    if not return_list:
        ascii_data=''
        new_line_counter=0
        address=selected_sector*sector_size
        for i in hex_data:
            if new_line_counter==0:
                print str(hex(address)[2:].zfill(8))+' ',
            print i,
            new_line_counter+=1
            address+=1
            if chr(int(i,16)).isalnum() or chr(int(i,16)) in '!@#$%^&*()_-+={}[]|\\:;?/><,.~`\'\"':
                ascii_data=ascii_data+chr(int(i,16))
            else:
                ascii_data=ascii_data+'.'
            if new_line_counter==8:
                print '',
            if new_line_counter==16:
                new_line_counter=0
                print ' |'+ascii_data+'|' #ascii of line
                ascii_data=''
    else:
        return list(hex_data)

def get_disk_info(disk,drive,selected_sector=0,sector_size = 512):
    #count in a large amount until you overshoot the filesize, then go back by one increment and count in a smaller ammount.
    #repeat until the increment is by 1. This is a faster way of getting its size.
    print 'DRIVE:',drive
    count=0
    increment_amount=1000000
    while True:
        try:
            while True:
                disk.seek(count*sector_size)
                disk.read(sector_size)
                count+=increment_amount
        except:
            if increment_amount==1:
                count=count-1
                print 'Sector Count:',count
                print 'Byte Count:',count*sector_size
                break
            count=count-increment_amount
            increment_amount=increment_amount/10


def writeo(disk,offset,provided_data,selected_sector=0,sector_size = 512): #offset = start position
    hex_list=read_sector(disk,selected_sector,sector_size,return_list=True)
    actual_offset=int(offset,16)%sector_size
    data=[]
    for i in hex_list[:actual_offset]:
        data.append(chr(int(i,16)))
    for character in list(provided_data):
        data.append(character)
    empty_space=sector_size-len(data)
    for i in range(0,empty_space):
        data.append(chr(0))
    disk.seek(selected_sector*sector_size)
    disk.write(bytearray(data))

def append_command(disk,offset,provided_data,selected_sector=0,sector_size = 512): #offset = start position
    hex_list=read_sector(disk,selected_sector,sector_size,return_list=True)
    actual_offset=int(offset,16)%sector_size
    data=[]
    for i in hex_list[:actual_offset]:
        data.append(chr(int(i,16)))
    for character in list(provided_data):
        data.append(character)
    empty_space=sector_size-len(data)
    for i in hex_list[-empty_space:]:
        data.append(chr(int(i,16)))
    disk.seek(selected_sector*sector_size)
    disk.write(bytearray(data))

def randomize(disk,selected_sector=0,sector_size = 512):
    random_string=[]
    for i in range(0,sector_size):
        random_string.append(chr(randint(0,255)))
    write_to_sector(disk,''.join(random_string),selected_sector,sector_size)