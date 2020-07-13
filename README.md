# Detectron2_Training_Metric_Visualizations
This Repo contains a python script and jupyter notebook file that converts visualizes the loss curve training process. I needed this for my Internship project to determine if we should train for more iterations, and thought it would be useful for people to visualize how well their model is training. Visualizes data taken from Detectron2 metrics.json output file


## Instructions to Plot Loss Function:
1. Create an empty file with the .csv extension to write data to

2. Open jsonRead.py, and replace the file paths in the main function with first, the file to the metrics json that is output from detectron train package (Should be found in the output folder), and second to the path that is your empty CSV file. 

3. Run jsonRead.py on that file only once.

4. Check your csv file to ensure everything has been written correctly

5. Next open the CSVread.ipynb jupyter notebook and change your csv file 
path to your correct csv file path. Then run all of the cells and view
the plots. You can change the fit function as you wish. i have included 3 
functions there
