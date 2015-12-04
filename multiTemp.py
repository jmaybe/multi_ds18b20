import subprocess
import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir1 = '/sys/bus/w1/devices/'
device_folder1 = glob.glob(base_dir1 + '28-############')[0] # you need to add each sensor's address manually to these lines
device_file1 = device_folder1 + '/w1_slave'

def read_temp_raw1():
        catdata = subprocess.Popen(['cat',device_file1], stdout = subprocess.PIPE, stderr=subprocess.PIPE)
        out,err = catdata.communicate()
        out_decode = out.decode('utf-8')
        lines = out_decode.split('\n')
        return lines

def read_temp1():
        lines = read_temp_raw1()
        while lines[0].strip()[-3:] != 'YES':
                time.sleep(10.0)
                lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
                temp_string = lines[1][equals_pos+2:]
                temp_c = float(temp_string) / 1000.0
                temp_f = temp_c * 9.0 / 5.0 + 32.0
                return temp_c, temp_f

base_dir2 = '/sys/bus/w1/devices/'
device_folder2 = glob.glob(base_dir2 + '28-############')[0] # you need to add each sensor's address manually to these lines
device_file2 = device_folder2 + '/w1_slave'

def read_temp_raw2():
        catdata = subprocess.Popen(['cat',device_file2], stdout = subprocess.PIPE, stderr=subprocess.PIPE)
        out,err = catdata.communicate()
        out_decode = out.decode('utf-8')
        lines = out_decode.split('\n')
        return lines

def read_temp2():
        lines = read_temp_raw2()
        while lines[0].strip()[-3:] != 'YES':
                time.sleep(10.0)
                lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
                temp_string = lines[1][equals_pos+2:]
                temp_c = float(temp_string) / 1000.0
                temp_f = temp_c * 9.0 / 5.0 + 32.0
                return temp_c, temp_f

# repeat adding above sections for each additional sensor

#base_dir3 = '/sys/bus/w1/devices/'
#device_folder3 = glob.glob(base_dir3 + '28-############')[0] # you need to add each sensor's address manually to these lines
#device_file3 = device_folder3 + '/w1_slave'

#def read_temp_raw3():
#        catdata = subprocess.Popen(['cat',device_file3], stdout = subprocess.PIPE, stderr=subprocess.PIPE)
#        out,err = catdata.communicate()
#        out_decode = out.decode('utf-8')
#        lines = out_decode.split('\n')
#        return lines

#def read_temp3():
#        lines = read_temp_raw3()
#        while lines[0].strip()[-3:] != 'YES':
#                time.sleep(10.0)
#                lines = read_temp_raw()
#        equals_pos = lines[1].find('t=')
#        if equals_pos != -1:
#                temp_string = lines[1][equals_pos+2:]
#                temp_c = float(temp_string) / 1000.0
#                temp_f = temp_c * 9.0 / 5.0 + 32.0
#                return temp_c, temp_f

# etc, etc...

while True:
        print('A', read_temp1())
        print('B', read_temp2())
        #print('C', read_temp3()) # add additional sensors to final output
        #etc
        time.sleep(30.0)

