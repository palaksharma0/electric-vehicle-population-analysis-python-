⚡ Electric Vehicle Population Analysis Project
This project explores and analyzes a dataset of electric vehicle (EV) registrations using Python for data preprocessing, statistical analysis, and insightful visualizations. It aims to uncover trends, patterns, and growth metrics across various dimensions like time, location, and vehicle types.

📁 Dataset
Source: Public EV registration data (e.g., government or open data portals)
File: Electric_Vehicle_Population.csv

🔧 Technologies Used
Python (Pandas, NumPy)

Data Visualization: Matplotlib, SeaborN

✅ Project Objectives
🧹 Objective 0: Data Preprocessing & Cleaning
Convert date columns (e.g., Registration Date) to datetime objects.

Handle missing values:

Replace missing County or City with "Unknown".

Replace missing Electric Range or Vehicle Count with the mean of their respective columns.

Remove duplicates.

Print dataset info and preview the data.

📊 Objective 1: EV Statistics
Total EVs Registered: Sum of all vehicle entries.

Average Electric Range across vehicles.

Standard Deviation of Electric Range.

📦 Objective 2: EVs and Performance by State
Total number of EV models registered.

Total vehicle count.

State/Province with the highest number of registered EVs.

📈 Objective 3: EV Trends & Adoption Visualizations
Line Plot: EV registration trends over time.

Grouped Bar Chart: EV counts by State and Vehicle Type.

Histogram: Distribution of Electric Range and Vehicle Age.

Correlation Heatmap: Range, Model Year, and Battery Size relationships.

🚨 Objective 4: Outlier Detection
Detect outliers in:

Electric Range

Battery Size

Use Interquartile Range (IQR) method.

Visualize with Box Plots.

📊 Objective 5: Graphical Analysis
Pie Chart: EV distribution by vehicle make.

Heatmap: Correlation between numerical features.

Horizontal Bar Chart: EV counts by region.

Donut Chart: Proportion of EVs by vehicle type.

Scatter Plot: Electric Range vs. Battery Size.

📆 Objective 6: Seasonal Registration Trends
Line Chart: Monthly EV registration trends.

Area Chart: Year-over-year EV population growth.

📌 Insights & Benefits
This analysis helps to:

Understand which states and vehicle types are leading in EV adoption.

Identify seasonal trends in EV registration.

Detect data anomalies and outliers.

Visualize relationships between EV specifications and adoption patterns.

📎 Notes
Make sure the dataset Electric_Vehicle_Population.csv is in your working directory, and all required libraries are installed before running the script.

📬 Contact
For questions or feedback, feel free to reach out!

Happy Analyzing! ⚙️🔋
