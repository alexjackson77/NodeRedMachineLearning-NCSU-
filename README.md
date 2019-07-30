# NodeRedMachineLearning-NCSU-
This repository shows the steps taken to begin the machine learning process in node red, as well as the flows used for HET Data collection.

The files contained in the master branch are all collected from the Arduino HET and were analyzed using the Matlab scripts provided in this branch.

The files contained in the "FLOWS" branch are the node red flows. These can be transferred to Node-Red by using the "Import --> Clipboard" option on any Node-Red server. Then just simply copy and paste the files into the clipboard.

HET flows: before using the HET flows, make sure you have mosquitto installed on your host device. Access the MQTT broker node and change the address to match that of your host device. Also, make sure the node red dashboard is installed in Node-Red. This can be done using the manage pallete option and searching "dashboard". Also, change any paths provided in the original flows to match your paths. 

A few of the node red flows provided allow for visualization of pre-recorded data on the node red dashboard. 

Machine Learning Flows: Follow instructions for downloading the machine learning package at https://flows.nodered.org/node/node-red-contrib-machine-learning.
