my_answers/voting contains the following files:
--- data (a folder containing all the necessary data)
--- images_docs (containing all the images and docs)
--- biclustering.pdf (containing biclustering images)
--- polarization.pdf (containing polarization plot)
--- voting_(a) (ipython notebook for question a)
--- voting_(b)(c)(d) (ipython notebook for question bcd)
--- README.txt

For polarization, by using fisher discriminant analysis method,
I define polarization as:
	   (mu1 - mu2)^2 / (s1^2 + s2^2)
Where 
mu1 is a 2D vector containing the mean value of democratic x and y coordinates
mu2 is a 2D vector containing the mean value of republic x and y coordinates  
s1^2 is a 2D vector containing the variance value of democratic x and y coordinates
s2^2 is a 2D vector containing the variance value of republic x and y coordinates

This is a reasonable formula:
When two classes have larger disparity of mu (two classes have larger distance between each other
on biclustering map), and smaller variance within each class (each class clusters in more limited area), then it indicates a larger disparity between two classes.