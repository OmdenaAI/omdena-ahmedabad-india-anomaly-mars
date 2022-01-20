
# Task 2 - Preprocessing # 

For the Preprocessing task, we had worked on with the thought in mind as to which classes can be taken into consideration as anomalies classes based on it. The Anomalies are geomorphic in nature.

The classes taken in are as follows - 
Crater
Dark Dunes
Slope Streak
Bright Dunes
Impact Ejecta
Swiss Cheese
Spider

The Dataset of Mars Orbital Image (HiRISE) labeled data set version 3 was used had a total of 73,031 landmarks. Various pre-processsing methods were used for the detection model like - 

Clustering - K means    k means clustering as it gave better output but we not able to contour from the output due to some channel error. 
![image](https://user-images.githubusercontent.com/72397412/150272717-0651123c-77d3-4082-8d21-79efb825a6bc.png)

DBSCAN
![image](https://user-images.githubusercontent.com/72397412/150272877-5ca10fbd-0fc6-4310-9e8c-5ae0fdec8cdd.png)
 
Grad CAM - Not able to produce activation maps
![image](https://user-images.githubusercontent.com/72397412/150272981-80f684ee-1b9c-422b-8422-e08c5d83ff96.png)


We tried the above methods but was not able to get the satisfactory results from it hence we decide to move ahead with annotation of the images where each class was meant to have a minimum of 100 annotations but due to reduced number images for impact ejecta where we had only 68 images. For the purpose of annotation we decide to go ahead with VGG annotator instead of LabellImg because in LabellImg we have only one shape for annotating the images which was rectangle/square but for few of our classes we needed proper shape fitted bounding box hence the choice. Also VGG annotator gives us masked layer over the region of annotation which could be stored in various format which gave us the flexibility to training on n number models.

Snips showing showing the interface of VGG Annotator -
![image](https://user-images.githubusercontent.com/72397412/150272016-cfbfc778-7934-4486-86e3-94006504d259.png)
![image](https://user-images.githubusercontent.com/72397412/150272227-2e16e626-b951-4f14-aaf6-33cc4b1c589b.png)

The various option available for making the annotation is a big plus while using VGG Annotator  also we can name attribute and give class a number and it stores the information which can be used to prepare multiple images for annotation along with a one lines description of the class.
