
# Task 1 - Data Collection # 

For the Data Collection part, several sources were seeded out to use Data from. An excel sheet was compiled to review the features and the usability of the data from the different sources. A beginning approach was to gather high quality .tiff (High Resolution) photos and then divide the image into even patches after some processing is done but this was discarded due to the reason of not having an optimal angle for the photos to be used, Data was also taken from sources of ISRO's MangalYaan and NASA's Reconnaissance but the amount of Negative Data required for training was very minimum. 

An idea was floated to use two parallel data sources for better accuracy - one data source from the satellite view and the other with a perpendicular angle to the surface for double validation. An API was also tested for getting the data but due to lack of time and resources it was not ventured into further. In the end it was decided to go with Mars orbital image (HiRISE) labeled data set version 3. 

This data set contains a total of 73,031 landmarks. 10,433 landmarks were detected and extracted from 180 HiRISE browse images, and 62,598 landmarks were augmented from 10,433 original landmarks. For each original landmark, we cropped a square bounding box that includes the full extent of the landmark plus a 30-pixel margin to left, right, top and bottom. Each cropped landmark was resized to 227x227 pixels, and then was augmented to generate 6 additional landmarks using the following methods:

1. 90 degrees clockwise rotation
2. 180 degrees clockwise rotation
3. 270 degrees clockwise rotation
4. Horizontal flip
5. Vertical flip
6. Random brightness adjustment



