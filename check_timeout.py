#!/usr/bin/env python3

import glob
import os
error_msg = "Connection timed out"
unwanted_log_file = ['/var/log/sssd/sssd.log',
                     '/var/log/sssd/ldap_child.log', '/var/log/sssd/sssd_implicit_files.log', '/var/log/sssd/sssd_nss.log', '/var/log/sssd/sssd_pam.log']
for sssd_log_file in glob.glob("/var/log/sssd/*"):
    if sssd_log_file not  in unwanted_log_file:
        # Open log_file for reading purpose
        fo = open(sssd_log_file)
        # Read the first line from the file
        line = fo.readline()
        # Initialize counter for line number
        line_no = 1
        # Loop until EOF
        while line != '' :
                #search for sdap_async_sys_connect request failed/Connection timed out
                index = line.find(error_msg)
                if ( index != -1) :
                    #print("[", line_no, ",", index, "] ", line, sep="")
                     print(line)
                #read the next line
                line = fo.readline()
                #increment line_counter
                line_no += 1
        #close the files
        fo.close()
