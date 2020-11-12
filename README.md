# PyMultical
  
This script is developed for reading out Kamstrup Multical 402 & 403 (city heating used in NL)
  
Dependency:
 * Software: linux, python3 and python3-serial  
 * Hardware: IR Optical Probe IEC1107 IEC61107  
  
Syntax:  `pymultical.py <DEVICE> <IDX>,<IDX>:,...`
Example: `pymultical.py /dev/ttyUSB2 60`
  

You must atleast execute this script once every 30 minutes or else the IR port on the Kamstrup will be disabled until you press a physical button on the device itself.    

`*/20 *  * * *   root    /usr/bin/python3 /usr/local/sbin/pymultical.py /dev/ttyUSB2 60`
