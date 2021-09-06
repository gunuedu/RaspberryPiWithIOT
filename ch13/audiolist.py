import pyaudio
p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    temp = p.get_device_info_by_index(i)
    if temp['defaultLowInputLatency'] > 0:
        print( "Index : %d, Name : %s, Rate : %d" % (temp['index'], temp['name'], temp['defaultSampleRate']))
