#!/usr/bin/python3

import gpxpy as mod_gpxpy
import sys as mod_sys
import matplotlib.pyplot as plt

lats=[]
longs=[]
elevats=[]

def run(gpx_files):
    print(gpx_files)
     
    if not gpx_files:
        print('No GPX files given')
        mod_sys.exit(1)
    for gpx_file in gpx_files:
        gpx = mod_gpxpy.parse(open(gpx_file))
 
        print(gpx)
        for track_no, track in enumerate(gpx.tracks):
            for segment_no, segment in enumerate(track.segments):
                print('    Track #%s, Segment #%s' % (track_no, segment_no))
                for point in (segment.points):
                    lats.append(point.latitude)
                    longs.append(point.longitude)
                    elevats.append(point.elevation)

    
    plt.figure(1)
    plt.subplot(311)
    plt.plot(lats)
    
    plt.subplot(312)
    plt.plot(longs)
    
    plt.subplot(313)
    plt.plot(elevats)
    
    
    
#     for lat in lats:
#         print(bin(round(lat*3600000))+" "+hex(round(lat*3600000)) +"   "+bin(round(lat*1000000))+" "+hex(round(lat*1000000)))
        
    plt.show()
    
if __name__ == '__main__':
    run(mod_sys.argv[1:])




    