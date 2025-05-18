############################
#Key Detection Python Script
#Author: Derek Wilson
#Date: 2025-05-17
############################

import librosa
import numpy as np
import matplotlib.pyplot as plt 

# FUNCTIONS -------------------

# cosine similarity function cos(theta) = dot(a,b) / (mag(a) * mag(b))
def cosine(a,b):
        return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

#finds key of inputed file
def find_key(filename, similar_list = False):
    # load file
    y, sr = librosa.load(filename) # y = audio information sr = sample rate

    chromagram = librosa.feature.chroma_stft(y=y,sr=sr) # take short-time fourier transform to determine chromagram 

    chroma_vector = np.mean(chromagram, axis=1) # find average chroma value through sample

    chroma_unit = chroma_vector / np.linalg.norm(chroma_vector) # Normalize the chroma vector

    keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    # Major and minor profiles for key of C - Krumhansl and Kessler
    major_key_profile = [6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88]
    minor_key_profile = [6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17]

    comparison_array = {}  

    # rotating the major key profile will change the key, the indexing corresponds to the keys array up above
    for i, tonic in enumerate(keys):
        # roll through keys
        major = np.roll(major_key_profile, i)
        minor = np.roll(minor_key_profile, i)

        # normalize
        major_unit = major / np.linalg.norm(major)
        minor_unit = minor / np.linalg.norm(minor)

        # compare to chroma vector using cosine similarity (dot product)
        major_similarity = cosine(major_unit, chroma_unit)
        minor_similarity = cosine(minor_unit, chroma_unit)

        # add to dictionary
        comparison_array[tonic + " " + "major"] = major_similarity
        comparison_array[tonic + " " + "minor"] = minor_similarity 

    # find max val from dictionary
    max_val = max(comparison_array, key=comparison_array.get)

    #print sorted keys based on similarity
    sorted_keys = sorted(comparison_array.items(), key=lambda x: x[1], reverse=True)

    plt.figure(figsize=(10, 4))
    librosa.display.specshow(chromagram, y_axis='chroma', x_axis='time', cmap='coolwarm')
    plt.colorbar()
    plt.title("Chroma Feature")
    plt.tight_layout()
    plt.show()

    if similar_list == True:
        return max_val, sorted_keys
    else:
        return max_val

# END FUNCTIONS ---------------

filename = "MOVING ON WAV.wav"

return_sort = True

if return_sort == True:
    key, sorted_keys = find_key(filename, return_sort)
    print(key)
    print("\n")
    for key, value in sorted_keys:
        print(f"{key}: {value:.3f}")
else:
    key = find_key
    print(key)

