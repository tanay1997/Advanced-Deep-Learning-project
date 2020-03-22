# Advanced-Deep-Learning-project

Pain expression detection from videos:

Processing steps:

1) Carefully select 18 Consecutive frames from videos distinctly showing the target expression (Pain and No pain).

2) Pass the video (18 frames) through 'frame.py' file to crop the faces from each frame. Note: The original image is lost after this operation.

3) Run the 'Deep Learning Project.py' file which converts the video file into a 5D tensor and feeds it to a 3D CNN model for classification.

4) Training and validation results are shown in 'Deep Learning Project.ipynb' file. (For demonstration purposes).

5) To run 'Face crop.py' and 'Deep Learning Project.py' directly from the google Colab platform find the shareable link below:

a) Face crop: https://colab.research.google.com/drive/1CUof3vAM0kAkQ_uL5KKZBbY8I4UKQMNw

b) Deep Learning Project: https://colab.research.google.com/drive/1ECR1r0ju2UjBAVsLp2OsUimyAxeQ1lR5













