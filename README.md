# Advanced-Deep-Learning-project

Pain expression detection from videos:

Processing steps:

1) Carefully select 18 frames from videos distinctly showing the target expression (Pain and No pain).

2) Pass the video (18 frames) through 'frame.py' file to crop the faces from each frame. Note: The original image is lost after this operation.

3) Run the 'Deep Learning Project.py' file which converts the video file into a 5D tensor and feeds it to a 3D CNN model for classification.

4) Training and validation results are shown in 'Deep Learning Project.ipynb' file. (For demonstration purposes).











