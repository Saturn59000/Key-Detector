############################
#File: keydetect.py
#Function: detects key for an inputted file
#Author: Derek Wilson
#Date: 2025-05-17
############################

import librosa
import numpy as np
import matplotlib.pyplot as plt 

# cosine similarity function cos(theta) = dot(a,b) / (mag(a) * mag(b))
def cosine(a,b):
        return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

#finds key of inputed file
def find_data(filename):
    # load file
    y, sr = librosa.load(filename) # y = audio information sr = sample rate
    
    bpm, beat_frames = librosa.beat.beat_track(y=y,sr=sr)

    chromagram = librosa.feature.chroma_stft(y=y,sr=sr) # take short-time fourier transform to determine chromagram [2][1]

    chroma_vector = np.mean(chromagram, axis=1) # find average chroma value through sample [2]

    chroma_unit = chroma_vector / np.linalg.norm(chroma_vector) # Normalize the chroma vector

    keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    # Major and minor profiles for key of C - Krumhansl and Kessler - [3]
    major_key_profile = [6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88]
    minor_key_profile = [6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17]

    comparison_array = {}  

    """ rotating the major key profile will change the key, the indexing corresponds to the keys array up above - Idea proposed by Chatgpt
        Instead fo comparing against each individual key profile
    """
    for i, tonic in enumerate(keys):
        # roll through keys
        major = np.roll(major_key_profile, i)
        minor = np.roll(minor_key_profile, i)

        # normalize major and minor profile vectors
        major_unit = major / np.linalg.norm(major)
        minor_unit = minor / np.linalg.norm(minor)

        # compare to chroma vector using cosine similarity (dot product method)
        major_similarity = cosine(major_unit, chroma_unit)
        minor_similarity = cosine(minor_unit, chroma_unit)

        # add to dictionary
        comparison_array[tonic + " " + "major"] = major_similarity
        comparison_array[tonic + " " + "minor"] = minor_similarity 

    # find max val from dictionary
    max_val = max(comparison_array, key=comparison_array.get)

    #print sorted keys based on similarity
    sorted_keys = sorted(comparison_array.items(), key=lambda x: x[1], reverse=True)

    return max_val, sorted_keys, float(bpm)



