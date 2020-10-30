# youtube-suggestion-algorithm-analysis
The website was launched to study the impact of biased perception of media reports on fairness evaluation. In particular, YouTube is one of the biggest media, with more than 2 billion users worldwide. Because of its huge influence on society, YouTube should also seriously consider the fact that it can favor users' decisions simply with algorithms to increase advertising exposure. This study began with these concerns.
<br>
<br>
#Preparing data<br>
#Generating a dataset<br>
#Learn the model1 (image)<br>
#Learn models2 (Voice)<br>
<br>
<br>
#Preparing data<br>
To analyze YouTube videos, FFmpeg program to extract images is installed in a virtual environment and images are extracted.<br>
Runs a labeling program to label all extracted images.<br>
Download github.com/AlexeyAB/darknet for post-analysis of image recognition algorithms.<br>
<br>
<br>
#Generating a dataset<br>
After image labeling, Darknet framework prepares four files for training.<br>
-labeled_data.data<br>
-classes.names<br>
-train.txt<br>
-test.txt<br>

When you run the Python program, you learn and create a file to test.<br>
getting-full-pathPy<br>
creating-train-and-test-txt-files.py<br>
creating-files-data-and-names.py<br>
Each file is routed and saved as a txt file<br>
<br>
<br>
#Learn the model1 (image)<br>
Install Darknet and check its operation.<br>
Enter a command and recognize the image of the prepared video.<br>
Basic image prediction is good.<br>
Image recognition worked successfully but took a long time.<br>
As a basic image detection for each frame, it shows the probability of the detection, or performance.<br>
<br>
<br>
#Learn models2 (Voice)<br>
I analyzed the image, but I also had to analyze the voice data on YouTube.<br>
Found a technique for analyzing voice data.<br>
I was able to download algorithm data to understand simple voice commands.<br>

Kaggle conducted a compilation to analyze and recognize voice data sets.<br>
However, 3.5GB input data takes a lot of time to learn, so it's impossible.<br>

Speech2Text Approach was available.<br>
Trying to extract voice and use Google's STT technology (SOUND TO TEXT).<br>
Alternative technology was needed due to high difficulty and increased time and cost.<br>
In addition, there was no guarantee of analysis performance, so I tried to find an alternative technology, but I gave up.<br>

YoutubeSpeech2Text in Google Cloud Platform was able to select and implement the project.<br>
After checking the data, the participant's voice reading the sentences is saved, so you can learn with this.<br>
But it takes a lot of time.<br>

