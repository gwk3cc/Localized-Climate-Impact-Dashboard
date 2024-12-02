Climate Data Analysis for US Counties

Abstract:
This project aims to present and analyze climate risk data across U.S. counties and make them more accessible and actionable, enabling local governments, researchers, 
and the public to better understand the distribution and implications of climate-related risks in different regions. The data used is based on climate indicators along 
with a prediction of temperature variation and status quo of air quality. The project is built using an interactive dashboard with Plotly Dash. Utilizing information from
the web-scraped ProPublica Climate Risk Table1 and the Open-Meteo API2,3 for historical climate and live air quality data, the information is condensed and made usable 
in the form of interactive visualizations. It employed GeoPandas for spatial data integration, enabling geographic mapping of counties with climate risk levels across 
the U.S using the shapefile based on 2020 census boundaries4 , filtered by user selection. The Open-Meteo API is integrated with the help of OpenMeteo Requests, Requests 
Cache, and Retry Requests libraries to fetch and cache real-time climate data via API calls. SciPy is applied for mathematical operations, including percentile calculations
to rank counties by risk levels. It also uses the Sci-kit learn library for creating a Multiple Linear Regression model to predict the Mean Temperature for the next 5 years
(this prediction is specific to the selected county). All insights are then presented through a web application-based interface using a Jupyter Notebook.


User Instructions:

Our project dashboard was developed and optimized for Jupyter Notebook. Below are the steps for setting up Jupyter Notebook, installing required packages, 
and running the dashboard for an optimal experience.

Step 1: Install Jupyter Notebook
If you don’t already have Jupyter installed, you can install it via pip or conda:

Step 2: Clone Repository

This repository uses Git Large File Storage (Git LFS) to manage large files. 

To clone this repository and properly download the large files:
1. Ensure you have [Git LFS](https://git-lfs.com/) installed.
   - On macOS: `brew install git-lfs`
   - On Windows: Use the [Git LFS installer](https://git-lfs.com/).

2. Initialize Git LFS:
   ```bash
   git lfs install
   
Open the repository gwk3cc/Localized-Climate-Impact-Dashboard
Click the green "CODE" button and hit "Open with GitHub Desktop"
Note: Do NOT download the repository as a zip file. Because of the Git LFS, csv files will not download correctly in a zip file.

Step 2: Install Project Dependencies
Our project requires certain Python packages, which are listed below. Refer to library or Python documentation for instructions on installing each library.

Step 3: Run the Dashboard Script in Jupyter
1.	In the Jupyter Notebook interface, navigate to the directory containing your project files (in the folder "Dashboard").
2.	Open the Script: Locate the main dashboard file, "Climate Dashboard.ipynb", and open it in a Jupyter notebook.
3.	Run the Dashboard: Execute the cells containing the dashboard code by selecting each cell and clicking “Run” or by pressing Shift + Enter.


Libraries Used
Pandas: Pandas is a powerful Python library for data manipulation and analysis. In this project, it is used to read the CSV file, modify the data, clean the data, perform groupings, 
and manipulate string columns like extracting county and state information, and creating new columns such as 'Score' and 'Risk' based on conditions.
Pandas is often pre-installed in most environments, but if it's not, you can install it by running: 
!conda install pandas -y

Numpy: NumPy is a fundamental library for numerical computations in Python, offering support for large, multi-dimensional arrays and matrices. 
In this code, NumPy’s “Select” function is used to classify counties into risk categories based on the 'Score' column, allowing the program to 
assign different labels according to specified conditions. 
To install it:
!conda install numpy -y

Dash: Dash is a framework for building web applications, often used for creating interactive data visualizations. In this project, its inclusion’s goal  is to build a 
dashboard where users can interact with visual representations of the climate risk data.
Dash can be installed via pip: !pip install dash

Plotly: Plotly is a graphing library that allows for creating interactive visualizations in Python. It is imported to visualize the climate risk data, for interactive maps and 
charts based on the processed DataFrame. 
Install it by running: !pip install plotly

GeoPandas: GeoPandas is used to extend Pandas to work with geospatial data. It allows us to manipulate geometric shapes and join spatial data with tabular data, its inclusion indicates
mapping geographic areas (counties), such as using shapefiles or GeoJSONs for visualization.
How to run GeoPandas Library?
You can install GeoPandas using either pip or conda, After installation, import GeoPandas in your Python script or Jupyter Notebook. GeoPandas supports various file formats for geospatial data, including Shapefiles, GeoJSON, KML, and others. Use the read_file function to load a spatial dataset. Once your data is in a GeoDataFrame, you can manipulate it just like a pandas DataFrame.
GeoPandas has dependencies that are best handled by conda, so if you’re using Anaconda or Miniconda, use:
!conda install -c conda-forge geopandas -y

Requests Cache: This library is used to cache HTTP requests, reducing redundant API calls by storing responses and reusing them for a set time period. In this project, it helps optimize 
the repeated calls to the Open-Meteo API for air quality data.
To cache HTTP requests, use: !pip install requests-cache

Retry Requests: This library is used to handle API request failures by retrying the request a specified number of times if it encounters errors. Here, it ensures robust API communication 
by retrying failed Open-Meteo requests up to 5 times with exponential backoff.
Install retry requests for handling retries in HTTP requests with:
!pip install retry 

Matplotlib: A comprehensive library for creating static, animated, and interactive visualizations in Python. In this project, it is used to generate line plots for daily average, along 
with annotations and visual enhancements like labels and safe-level thresholds.
Matplotlib is a common library for plotting and is often pre-installed. To install it: !pip install matplotlib

OpenMeteo Requests: This custom Python client library is used to interact with the Open-Meteo API. In this project, it simplifies the process of retrieving and structuring the data from 
the API for analysis. 
For the OpenMeteo API: !pip install openmeteo_requests
Py. Files Used

Air Quality Index.py: This script utilizes various libraries like ‘pandas’  for data handling and OpenMeteo Requests for accessing air quality data. It processes air quality metrics and levels
for a specific county by querying the Open-Meteo API. The results are then visualized with matplotlib to display daily averages over time, allowing users to assess particulate matter levels.

Risk Distribution.py: This script focuses on analyzing climate risk data. Using pandas, it processes climate risk scores across counties and assigns risk levels based on the score. It also visualizes
the distribution of risk levels using matplotlib and marks where the chosen county stands in terms of overall climate risk. 

Climate risk webscrape.py: This script automates the process of scraping climate risk data. It sets up a web browser, navigates to the climate risk page, extracts data from an HTML table, and saves 
the scraped information into a CSV file. This file is then used in other scripts, like "Risk distribution.py", for further analysis and visualization. 

Functionality: 

Using the Dashboard

1.State Selection:
At the top of the dashboard, select a state from the dropdown menu. The county dropdown will update automatically, displaying the counties in that selected state.

2. County Selection:
After selecting a state, you can choose a county from the updated dropdown. This will update the bar chart and choropleth map to show the selected county's risk score compared to other counties
in the state.

4. Visualizations:
•	Risk Score Bar Chart: This chart displays the risk scores of all counties in the selected state. The selected county is highlighted in a darker color. National and state-level mean scores are
shown as dashed lines for comparison.
•	Choropleth Map: The map displays the spatial distribution of risk scores for the selected state. The selected county is outlined with a thicker border and highlighted with its specific risk score.
•	Interactive Elements: The interface uses a bunch of interactive elements for the maps such as Zoom (In and Out), Download feature, 
Key Features:
•	Interactive: Changing the state or county selection dynamically updates the bar chart and map.
•	Risk Score Levels: The risk score of each county is categorized into risk level by light to dark shades of red in the legend.
•	Spatial Map: The choropleth map visually shows how different counties within a state rank in terms of climate risk scores.



References 
Timothy Akohler, T. M. (2020). Future of the human climate niche. PNAS.
Shaw, A., Lustgarten, A., ProPublica, & Goldsmith, J. W. (2020, September 15). New Climate
Pachauri, R. K., Allen, M. R., Barros, V. R., Broome, J., Cramer, W., Christ, R., ... & van Ypserle, J. P. (2014). Climate change 2014: synthesis report. Contribution of Working Groups I, II and III to the fifth assessment report of the Intergovernmental Panel on Climate Change (p. 151). Ipcc.
OpenAI. (2024). [Large language model]: 
https://chat.openai.com/chat
Shapefile download link: 
https://catalog.data.gov/dataset/2020-cartographic-boundary-file-kml-current-county-and-equivalent-for-united-states-1-500000/resource/13d546be-47ce-4670-8e9f-c1647bc56342
Latitude and Longitude csv file download link: https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/us-county-boundaries/exports/csv?lang=en&timezone=America%2FNew_York&use_labels=true&delimiter=%3B
Climate risk indicators: 
https://projects.propublica.org/climate-migration/ (table at the end, data source analysed from https://www.pnas.org/doi/10.1073/pnas.1910114117)
Open-Meteo Historical Data API: 
https://open-meteo.com/en/docs/historical-weather-api
Open-Meteo AQI Data API: 
https://open-meteo.com/en/docs/air-quality-api
https://simplemaps.com/data/us-counties
https://projects.propublica.org/climate





