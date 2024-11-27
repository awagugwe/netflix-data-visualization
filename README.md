# Netflix Data Analysis Project

This project analyzes Netflix shows and movies data, creating visualizations for genre distribution and content ratings. The analysis is implemented in both Python and R.

## Setup Instructions

1. Clone this repository
2. Ensure you have Python 3.7+ installed
3. Install required Python packages:
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```
4. Place your Netflix data zip file in the project root directory
5. Run the Python script:
   ```bash
   python netflix_analysis.py
   ```

## Project Structure

- `netflix_analysis.py`: Main Python script for data analysis
- `netflix_data/`: Directory containing extracted and processed data
  - `genre_distribution.png`: Visualization of top genres
  - `ratings_distribution.png`: Visualization of content ratings
  - `netflix_shows_movies_cleaned.csv`: Cleaned dataset for R integration

## Features

1. **Data Preparation**
   - Renames dataset appropriately

2. **Data Cleaning**
   - Handles missing values in various columns
   - Standardizes date formats

3. **Data Exploration**
   - Provides basic statistics
   - Generates summary of numerical and categorical variables

4. **Visualizations**
   - Creates bar chart of most watched genres
   - Shows distribution of content ratings
   
5. **Integration of chart showing  most watched genres into R**
    -Load image generated from Python and display the chart showing the most watched genres on Netflix. 

## Output

The Python script generates:
1. Statistical summaries in the console
2. Two visualization files in the netflix_data directory
3. A cleaned CSV file for R integration

The R script generates:
1. The image of the chart showing most watched genres on Netflix.

## Notes

- Ensure the zip file contains a CSV file named 'netflix_titles.csv'
- The script creates a 'netflix_data' directory if it doesn't exist
- Visualizations are automatically saved in PNG format