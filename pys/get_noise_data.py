#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 10:43:02 2020

@author: sydneydybing
"""

from obspy.core import Stream, UTCDateTime
from obspy.clients.fdsn import Client
import numpy as np
import pandas as pd

# Naming the client where the data will be coming from. Googling obspy fdsn will
# list other options.

client = Client('IRIS')

# Reading in my info files - earthquakes is a list of the events I want to get data for,
# which includes locations and origin times, and then stas is the list of stations I want
# to pull data from. Chans is then the four strainmeter channels for these instruments.

earthquakes = pd.read_csv('/Users/sydneydybing/IRIS_pbo_data/Data_noise/earthquakes_sel4.csv', dtype=str)
stas = np.genfromtxt('/Users/sydneydybing/IRIS_pbo_data/Data_noise/stations_sel4.txt', dtype=str)
chans = ['BS1', 'BS2', 'BS3', 'BS4']

print(earthquakes)
print(stas)

# This method of reading in data from IRIS uses origin times in the UTCDateTime format.
# To get the origin times from my earthquakes file in this format, since in the CSV each
# time unit is a separate column, I pulled each time unit out into its own variable.

eqnum = earthquakes.eqnum.values
ot_yr = earthquakes.year.values
ot_mo = earthquakes.mo.values
ot_day = earthquakes.dy.values
ot_hr = earthquakes.hr.values
ot_min = earthquakes.mi.values
ot_sec = earthquakes.sec.values
mag = earthquakes.Mw.values

# I then started looping through my list of earthquakes, and putting together the origin
# times for each one as the variable 'ot' in UTCDateTime format. stime and etime are the 
# start and end times of the data I want to pull from IRIS, so I made my stimes the origin
# times of the earthquakes, and the etimes five minutes after the origin.

for idx in range(len(earthquakes)):
    ot = str(ot_yr[idx]) + '-' + str(ot_mo[idx]) + '-' + str(ot_day[idx]) + 'T' + str(ot_hr[idx]) + ':' + str(ot_min[idx]) + ':' + str(ot_sec[idx])
    stime = UTCDateTime(ot) - 2.*60.
    etime = UTCDateTime(ot) - 1.*60.
    print(stime)
    print(etime)
    
    # I then looped through my stations. All of the stations I want are in the 'PB' network,
    # and the data has the location 'T0'. This information you'll probably have to look up on
    # the IRIS Metadata Aggregator website. 
    
    for sta in stas:
        net = 'PB'
        sta = sta
        loc = 'T0'
        
        st = Stream()
        
        # My final loop was through my four channels so I could write individual miniSEED data
        # files for each channel.
        
        for chan in chans:
            chan = chan
            
            # I used this try-except condition so I didn't get errors if a station didn't have 
            # data for the time window I was looking at.
            
            try:
                
                # I use the function get_waveforms to get the data from the client (IRIS), and
                # read it into an obpsy stream object using the network, stations, etc. info
                # that I collected earlier. I printed some stats to make sure things were working.
                # Then I wrote the stream into a miniSEED data file and saved it onto my laptop.
                
                st = client.get_waveforms(net, sta, loc, chan, stime, etime)
                st.write('/Users/sydneydybing/IRIS_pbo_data/Data_noise/' + eqnum[idx] + '_' + ot_yr[idx] + '_' + mag[idx] + '/' + sta + '_' + chan +'.mseed', format='MSEED')
            
            # If that didn't work, my code prints out the station name and the earthquake number
            # (a piece of information in the original earthquakes CSV that just identifies the
            # event), and the phrase "not found" so I could tell what didn't work.
            
            except:
                print(sta, eqnum[idx], "not found")