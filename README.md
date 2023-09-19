# PDS

As part of the collaboration between New College of Florida and Harvard. We worked on a project that brings New College, NASA, Harvard, and the Smithsonian together to study solar flares and build machine-learning models that will detect different class solar flares. 


Data Source: 
https://www.ngdc.noaa.gov/stp/satellite/goes-r.html 

Which specific data? 
EXIS (Extreme Ultraviolet and X-ray Sensors)

What are we doing with it? 
The website shows 3 telescopes GOES-16, GOES-17, GOES-18. 
We will start with the most recent 1-minute averages of XRS measurements from the GOES-16 telescope.

These are nc (netCDF) files, you’ll have to pip install netCDF4 to open them in Python. We will also be using Sunpy to work on the solar data (https://sunpy.org/). 

