#  Energy Consumption Pattern Clustering Web App

A Flask-based machine learning web application that performs **Hierarchical Clustering** to group households based on their energy consumption behavior.

---

##  Project Overview

This web app allows users to upload a CSV file containing household electricity usage data and clusters them based on patterns like daily usage, night usage, weekend consumption, and peak hours. Results are visualized with a cluster plot and detailed data table.

---

##  Features

-  Upload your own `.csv` energy dataset
-  Select the number of clusters
-  Uses Agglomerative (Hierarchical) Clustering
-  Displays clustered results in a styled table
-  Visualizes clusters using a scatter plot
-  Clean, modern, and responsive user interface

---

##  Machine Learning Details

- **Clustering Algorithm**: Agglomerative Clustering (`ward` linkage, `euclidean` metric)
- **Preprocessing**: Standardization using `StandardScaler`
- **Libraries Used**:
  - `scikit-learn`
  - `pandas`
  - `matplotlib`
  - `seaborn`

---

##  File Structure
```
energy_cluster_app/
│
├── app.py # Flask app
├── model.py # Clustering logic
├── utils.py # Plotting helper
├── requirements.txt # Python dependencies
├── sample_energy.csv # Sample dataset
│
├── static/
│ └── style.css # Custom CSS styling
│
├── templates/
│ ├── index.html # Upload form page
│ └── result.html # Result display page

```

---

##  Sample Input Format

Your `.csv` file should include at least the following columns:

```
HouseholdID,AvgDailyUsage(kWh),PeakHourUsage(kWh),NightUsage(kWh),WeekendUsage(kWh)
1,12.3,3.1,2.2,5.5
2,7.8,1.5,4.3,3.8

```

## Getting Started
 Installation

        Clone the repository:

        git clone https://github.com/Deepakprasath10/Hierarchical.git

        cd energy-clustering-app

        Install dependencies:

        pip install -r requirements.txt

        Run the Flask app:

        python app.py

        Open your browser and visit:

        http://127.0.0.1:5000


## Output Example    
![alt text](<Screenshot 2025-08-01 160816.png>)
  ![alt text](<Screenshot 2025-08-01 160830.png>)
    ![alt text](<Screenshot 2025-08-01 160843.png>)
    ![alt text](<Screenshot 2025-08-01 160903.png>)
    
## Future Enhancements
    Add interactive dendrograms

    Downloadable clustered dataset (.csv)

    Add login and user history tracking

    Use real-time smart meter data streams
