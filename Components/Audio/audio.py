#it need pyaudio library
import pyaudio
import wave
import sys
import time
class AudioFile:
    chunk = 1024

    def __init__(self, file):
        """ Init audio stream """ 
        self.wf = wave.open(file, 'rb')
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format = self.p.get_format_from_width(self.wf.getsampwidth()),
            channels = self.wf.getnchannels(),
            rate = self.wf.getframerate(),
            output = True
        )
        #self.lenght = self.duration()
    def duration(self):
        i = 1
        data = self.wf.readframes(self.chunk)
        while data != '':
            data = self.wf.readframes(self.chunk)
            i += 1
        n_secs = 1.93492984772
        n = 88
        secs = (n_secs * i)/n
        return secs
    def play(self):
        """ Play entire file """
        data = self.wf.readframes(self.chunk)
        while data != '':
            self.stream.write(data)
            data = self.wf.readframes(self.chunk)
    def playf(self,secs):
        data = self.wf.readframes(self.chunk)
        stop = 0
        t1 = time.time()
        while data != '':
            self.stream.write(data)
            data = self.wf.readframes(self.chunk)
            t2 = time.time()
            stop = int(t2 - t1)
            if stop == int(secs): break
    def close(self):
        """ Graceful shutdown """ 
        self.stream.close()
        self.p.terminate()

# Usage example for pyaudio
if __name__ == "__main__":
    a = AudioFile("sine.wav")
    a.playf(1) #play for 1 sec
    a.close()
