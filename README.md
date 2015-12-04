# multi_ds18b20
Read from multiple DS18B20 sensors (can be expanded) on a Raspberry Pi

I started with the 'basic' python file for pulling data from the DS18B20 and tweaked it to allow for multiple sensors. I haven't tried attaching more than 10 sensors to same pin (usually gpio 4) on the Pi. However, it does work with up to that many from my experience.

My ultimate plan is to make another program that allows for one to add sensors more easily. 
