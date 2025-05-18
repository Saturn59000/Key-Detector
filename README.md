# Key-Detector

Background:
This is a musical key and audio detector for BCIT's ELEX 4653 term project. It uses the librosa library for audio processing, specifically in extracting chroma data from the audio sample. This can be used to generate a Chromogram, which is similar to a spectogram, but is based on pitch information instead of frequency. The chromogram is represented as a 12 dimensional vector, which can be compared to known key profiles, such as those experimentally determined by Carol L. Krumhansl and Mark A. Schmuckler [3]. Using linear algebra to compute the similarity between the vectors determines the most likely key of the sample.

References:

[1] 	S. B. F. Z. Meinard Müller, "Audio-Processing-Uni-Projects," April 2020. [Online]. Available: https://github.com/StefanRinger/Audio-Processing-Uni-Projects/blob/main/1%20STFT/stft_and_chroma_features.ipynb.

[2] 	D. Oluyale, "Detecting Musical Key from Audio Using Chroma Feature in Python," 24 September 2023. [Online]. Available: https://medium.com/@oluyaled/detecting-musical-key-from-audio-using-chroma-feature-in-python-72850c0ae4b1.

[3] 	D. Temperley, "What's Key for Key? The Krumhansl-Schmuckler Key-Finding algorithm reconsidered," Music Perception, vol. 17, no. 1, pp. 65-100, 1999. 

[4] 	S. Cambell, "Automatic Key Detection of Musical Excerpts from Audio," McGill University, Montreal, 2010.

[5] 	T. Schimansky, "CustomTkinter," [Online]. Available: https://github.com/TomSchimansky/CustomTkinter/tree/master. [Accessed 17 May 2025].


