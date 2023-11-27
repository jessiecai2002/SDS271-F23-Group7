## Project A
### Fit a curve and plot

Write a class that determines the relationship between altitude and temperature. It should:

1. automatically read in the csv when initializing
2. clean the data appropriately and return a new dataframe *Careful: be aware of units! You may need to create some new columns in your dataframe! Kelvin = Celsius + 273.15*
3. fit the data to the line $T = - r h + T_0$ where $h$ is Altitude in km and $T$ is temperature in Kelvin
  
  Special hint for this part **when you define your fit function inside the class, put ```@staticmethod``` above the function definition** -- this allows ```curve_fit``` to use the fit function without errors. You can read more about static methods [here](https://www.digitalocean.com/community/tutorials/python-static-method) and I'm happy to explain where those errors come from another time!
 
4. calculate (and return) the unknown parameter $r$ with error
4. calculate (and return) the unknown parameter $T_0$ with error
6. plot the data and the fit together on the same graph and label it appropriately


## Altitude Temperature Relationship

The `AltTemp_Relationship.py` file is a Python class that fits a linear relationship between altitude and temperature. It uses atmospheric data provided in the "atm_data.csv" CSV file to create a graph and the results are visualized with a plot/graph. 

## Overview

The script analyzes the atmospheric data and determines the relationship between altitude and temperature. The main functions of the script are as follow:

- Reads the atmospheric data from "atm_data.csv" file.
- Cleans the data by converting Temperature to Kelvin and dropping the missing values.
- Fits a linear model to the altitude-temperature relationship.
- Extracts and reports the fitted parameters and their errors.
- Plots the data along with the fitted curve.

## How to Use this script

1. Make sure that Python is installed in the system.
2. Import the necessary libraries in the Python script. 
3. Copy the Alt_Temp_Relationship class from Alt_Temp_Relationship.py into your project.
alt_temp_relation = AltTemp_Relationship("atm_data.csv")
4. Create an instance of the class by providing the path to your atmospheric data CSV file.
alt_temp_relation.clean_data()
alt_temp_relation.fit_data()
5. Clean the data and fit the altitude-temperature relationship.
alt_temp_relation.clean_data()
alt_temp_relation.fit_data()
6. Retrieve the fitted parameters. 
parameters = alt_temp_relation.get_parameters()
print(parameters)
7. Visualize the data and the fitted curve.
alt_temp_relation.plot_data()



