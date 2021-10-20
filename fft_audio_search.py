import scipy
from scipy.io.wavfile import read
from scipy.signal import hann
from scipy.fftpack import rfft
import matplotlib.pyplot as plt


def fftfromwav(audio, t_hold):
# read audio samples
	sample_mat = []
	temp_list = []
	count = 0
#	bigger = 5
	
	for i in audio:
		count += 1
		nextpoint = count + 300
		lastval = audio[count:nextpoint]
		for j in lastval:
			if j > 0:
				bigger = 5
			else:
				bigger = 0
#		bigger = max(lastval)
		
		if i > 0:
			temp_list.append(i)
		else:
			if bigger == 0:
				sample_mat.append(temp_list)
				temp_list = []
			else:
				temp_list.append(i)
			
		
	print len(sample_mat)
		
		
#			temp_list.append(i)
			
#		elif i == 0:

#		else:
#			if lastval > 0:
#				sample_mat.append(temp_list)
#			temp_list = []
			
#	print sample_mat		
#	for i in sample_mat:
#		length = len(i)
#		window = hann(length)
#		peakaudio = i * window
#		mags = abs(rfft(peakaudio))

#	1111111window = hann(3254)

#1111111	audio = audio[0:3254] * window
# fft
#111111	mags = abs(rfft(audio))
# convert to dB
#	1111111mags = 20 * scipy.log10(mags)
# normalise to 0 dB max
	#mags -= max(mags)

	#print input_data
#	plt.plot(mags)
# label the axes
	plt.ylabel("Magnitude (dB)")
	plt.xlabel("Frequency Bin")
# set the title
	plt.title("Gunshot Spectrum")
#	plt.show()



from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import scipy
import math	
	
def magvtime(sndfile):
	# initializations
	peak_audio = []
	count = 0
	audio2 = []
	# read audio samples
	#input_data = read("test3.wav")
	input_data = read(sndfile)
	audio = input_data[1]
	for j in audio:
		k = math.fabs(j)
		audio2.append(k)
	# convert to magnitude
	#audio = 20 * scipy.log10(audio)
	
	minimum = min(audio2)
	maximum = max(audio2)
	average = sum(audio2)/len(audio2)
	threshold = average + (maximum-average)/2
#	threshold = minimum + ((maximum - minimum)/2)
#	print threshold
#	print minimum
#	print maximum
#	print average
	
	for i in audio2:
		count = count +1
		if i > threshold:
			peak_audio.append(i)
		elif i < threshold: 
			peak_audio.append(0)
	thold = threshold		
	
	
	return peak_audio, thold
	#return peak_audio
#	plt.plot(audio[0:640000])
#	plt.plot(audio)
#	plt.plot(peak_audio[0:640000])
#	plt.plot(peak_audio)
#	plt.plot(peak_audio)
	# label the axes
#	plt.ylabel("Amplitude")
#	plt.xlabel("Time (samples)")
  # set the title
#	plt.title("Shot Sample")
	# display the plot
#	plt.show()



if __name__ =="__main__":
	
	sound_file = raw_input("What is the name of the file you want to analyze? ")
	peaks = magvtime(sound_file)
	#ftfromwav()
	thold = peaks[1]
	peak_audio = peaks[0]
	shots = fftfromwav(peak_audio, thold)
	
	
	
	
	
	
