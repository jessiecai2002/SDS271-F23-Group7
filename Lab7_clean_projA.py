{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "2cf6a5b3-c44f-4dfb-9433-b4717c072272",
   "metadata": {
    "tags": []
   },
   "source": [
    "# Lab 7 - Collaboration Lab"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "19027ccd-36de-4044-ba9f-a28b35efae89",
   "metadata": {},
   "source": [
    "This lab is going to be quite different from the previous ones. \n",
    "\n",
    "You will work in teams of two to create a python mini-package. Details on what that package must accomplish and how it must be organized will be included. Consider these a set of requirements given to you by a client that you must satisfy.\n",
    "\n",
    "This package will have a few parts to it, and you must divide up the work so that both members of the team contribute functions to the package. You must document the package in detail with both comments and a README that describes how to use it.\n",
    "\n",
    "Once you are finished with this package, you will turn in the following things in the following way:\n",
    "\n",
    "1. You will turn in on GitHub a shared Jupyter notebook (.ipynb) and Python file (.py). The Python file will contain your package (with code and comments) and the Jupyter notebook will import your package and document how it works.\n",
    "\n",
    "2. You will also turn in via GitHub a version of the package (just the .py file) where you have deleted *all the code you wrote* leaving only the comments. **You may leave function definitions, but none of the code below them.**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "22605f0c-f4d5-4be1-8457-3da533fa2d0b",
   "metadata": {},
   "source": [
    "## But first, GitHub"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "96c905e6-c6a3-4e2d-bbe4-b312912ab616",
   "metadata": {},
   "source": [
    "You will be working collaboratively on this project, so you should use version control.\n",
    "\n",
    "<div class=\"alert alert-info\"> Exercise 1:\n",
    "\n",
    "If you have not yet created a [GitHub account](https://github.com/), do so now. \n",
    "\n",
    "Once every member of your team has a GitHub account, one member of the team should create a *private* repo for the project. Come up with a team name and name the repo \"SDS271-F23-[your-team-name]\"\n",
    "    \n",
    "Next, [add every member of the team to the repo](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository).\n",
    "    \n",
    "Add Casey to your repo -- this is how you will turn in this assignment. Casey's GitHub username is @caseyberger\n",
    "\n",
    "Now, you're ready for the project.\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "db424a37-de4d-4f73-858a-f643a20f8190",
   "metadata": {},
   "source": [
    "## Project A"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "29dca1b8-6731-4202-8bf0-91115aba2590",
   "metadata": {},
   "source": [
    "### Fit a curve and plot\n",
    "\n",
    "Now write a class that determines the relationship between altitude and temperature. It should:\n",
    "\n",
    "1. automatically read in the csv when initializing\n",
    "2. clean the data appropriately and return a new dataframe *Careful: be aware of units! You may need to create some new columns in your dataframe! Kelvin = Celsius + 273.15*\n",
    "3. fit the data to the line $T = - r h + T_0$ where $h$ is Altitude in km and $T$ is temperature in Kelvin\n",
    "  \n",
    "  Special hint for this part **when you define your fit function inside the class, put ```@staticmethod``` above the function definition** -- this allows ```curve_fit``` to use the fit function without errors. You can read more about static methods [here](https://www.digitalocean.com/community/tutorials/python-static-method) and I'm happy to explain where those errors come from another time!\n",
    " \n",
    "4. calculate (and return) the unknown parameter $r$ with error\n",
    "4. calculate (and return) the unknown parameter $T_0$ with error\n",
    "6. plot the data and the fit together on the same graph and label it appropriately"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "07b9b717-61ab-47f4-ad5f-02dca7bc098b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from scipy.optimize import curve_fit\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "class Alt_Temp_Relationship:\n",
    "\n",
    "    def __init__(self, atm_data): # Initialize the class\n",
    "        self.data = pd.read_csv(atm_data) # Reads the csv when initializing\n",
    "        self.clean_data() # Cleans the data\n",
    "        self.params=None\n",
    "        self.cov=None\n",
    "\n",
    "    @staticmethod  # Static method defining the fit function\n",
    "    def fit_function(h, r, T0):\n",
    "        return -r * h + T0\n",
    "\n",
    "    def clean_data(self): #Cleans the data\n",
    "        self.data['Temperature (K)'] = self.data['Temperature (C)'] + 273.15 # Cleans the data by converting Temperature to Kelvin\n",
    "        self.data=self.data.dropna() #Drops any NaN values\n",
    "\n",
    "    def fit_data(self):\n",
    "         # Fits the data using the curve_fit function from scipy\n",
    "        self.params, self.cov = curve_fit(self.fit_function,\n",
    "                                         self.data['Altitude (km)'],\n",
    "                                         self.data['Temperature (K)'])\n",
    "        self.r, self.T0 = self.params  # Extracts fitted parameters and their errors\n",
    "        self.r_error, self.T0_error = np.sqrt(np.diag(self.cov))\n",
    "\n",
    "    def get_parameters(self):   # Returns a dictionary of fitted parameters and their errors\n",
    "        return {'r': self.r, 'r_error': self.r_error, 'T0': self.T0, 'T0_error': self.T0_error}\n",
    "\n",
    "    def plot_data(self):\n",
    "        # Plost the original data and the fitted curve\n",
    "        plt.scatter(self.data['Altitude (km)'], self.data['Temperature (K)'], label='Data')\n",
    "        alt_values = np.linspace(self.data['Altitude (km)'].min(), self.data['Altitude (km)'].max(), 100)\n",
    "        plt.plot(alt_values, self.fit_function(alt_values, *self.params), label='Fit', color='red')\n",
    "        plt.xlabel('Altitude (km)')\n",
    "        plt.ylabel('Temperature (K)')\n",
    "        plt.title('Altitude vs Temperature')\n",
    "        plt.legend()\n",
    "        plt.show()\n",
    "\n",
    "alt_temp_relation=Alt_Temp_Relationship(\"atm_data.csv\")\n",
    "alt_temp_relation.clean_data()\n",
    "alt_temp_relation.fit_data()\n",
    "alt_temp_relation.get_parameters()\n",
    "alt_temp_relation.plot_data()\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5455e6d9-d395-475e-a3c5-152b68998fa3",
   "metadata": {},
   "source": [
    "# Post-Lab: Production and Reflection"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d40d4ca5-7ecc-4c91-adb1-de6c53bda4bd",
   "metadata": {},
   "source": [
    "**Note: the instructions for this lab are different, so read carefully**\n",
    "\n",
    "When you are done with this lab, make sure your team has in its GitHub one JupyterNotebook, a README, and at least one.py file that contains the class you've written. The Jupyter Notebook should import your .py file(s) and walk through how you solved the problem given to you. The README should provide a brief overview of what is in the .py file(s) and how to use it(them). It should also include the problem prompt! Finally, the .py file(s) should be adequately commented.\n",
    "\n",
    "During class today, Casey will have added you to the SDS-271-F23 organization on GitHub and will have assigned your team a secret number and created a public repo for you in the organization. \n",
    "\n",
    "In this public repo, upload your README only. Then, make a copy of your .py files and **delete all the code, leaving only the comments. You may leave function definitions, but none of the code below them.** Upload this comments-only version of your .py file(s) to the public repo and add Casey to it.\n",
    "\n",
    "In addition, don't forget to fill out the <a href=\"https://forms.gle/nAJeHRedav8kPyCi8\"> post-lab reflection form</a>. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "395908e4-3c83-49b7-82f0-c5c2a36d521a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
