# Advanced-Deep-Learning-project

Pain expression detection from videos:

Processing steps undertaken:

1) Carefully select 18 Consecutive frames from videos distinctly showing the target expression (Pain and No pain).

2) Pass the video (18 frames) through 'frame.py' file to crop the faces from each frame. Note: The original image is lost after this operation.

3) Run the 'Deep Learning Project.py' file which converts the video file into a 5D tensor and feeds it to a 3D CNN model for classification.

4) Training and validation results are shown in 'Deep Learning Project.ipynb' file. (For demonstration purposes).

5) To test the results on a new testing dataset:

a) Make two folders and name them 'pain' and 'Nopain'. Make subfolders for each video (containing 18 frames) inside each category (pain and Nopain).

b) Add these two folders to your drive.

c) Go to: https://colab.research.google.com/drive/1CUof3vAM0kAkQ_uL5KKZBbY8I4UKQMNw

d) Make changes to 'filename' name variable to provide a path for each video file inside the two folders 'Pain' and 'Nopain'. This will employ face crop to your videos at the original destination itself.

e) Download the 3D CNN model with it's pre-trained weights from this github repository. Add the 'Pre-trained_model.h5' file to your google drive.

f) Go to: https://colab.research.google.com/drive/1iZGmZG_mF-5ZU7iR44iqsAga0BinH03e

g) Mount your Google drive in the above code.

h) Make changes to 'load_model' path accordingly.

i) Make changes to 'painpath' and 'Nopainpath' accordingly.

j) Run all the cells in the notebook to get the Confusion matrix for your testing videos.


















