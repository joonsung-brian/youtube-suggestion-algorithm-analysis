# youtube-suggestion-algorithm-analysis
The website was launched to study the impact of biased perception of media reports on fairness evaluation.       &lt;p>In particular, YouTube is one of the biggest media, with more than 2 billion users worldwide. Because of its huge influence on society, YouTube should also seriously consider the fact that it can favor users' decisions simply with algorithms to increase advertising exposure. This study began with these concerns.

#Preparing data
#Generating a dataset
#Learn the model1 (image)
#Learn models2 (Voice)

#Generating a dataset
After image labeling, Darknet framework prepares four files for training.
-labeled_data.data
-classes.names
-train.txt
-test.txt

When you run the Python program, you learn and create a file to test.
getting-full-pathPy
creating-train-and-test-txt-files.py
creating-files-data-and-names.py
Each file is routed and saved as a txt file

#Learn the model1 (image)
Install Darknet and check its operation.
Enter a command and recognize the image of the prepared video.
Basic image prediction is good.
Image recognition worked successfully but took a long time.
As a basic image detection for each frame, it shows the probability of the detection, or performance.

#Learn models2 (Voice)
I analyzed the image, but I also had to analyze the voice data on YouTube.
Found a technique for analyzing voice data.
I was able to download algorithm data to understand simple voice commands.

Kagle conducted a compilation to analyze and recognize voice data sets.
However, 3.5GB input data takes a lot of time to learn, so it's impossible.

Speech2Text Approach was available.
Trying to extract voice and use Google's STT technology (SOUND TO TEXT).
Alternative technology was needed due to high difficulty and increased time and cost.
In addition, there was no guarantee of analysis performance, so I tried to find an alternative technology, but I gave up.

YoutubeSpeech2Text in Google Cloud Platform was able to select and implement the project.
After checking the data, the participant's voice reading the sentences is saved, so you can learn with this.
But it takes a lot of time.

