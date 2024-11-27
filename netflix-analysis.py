import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

# 1. Data Preparation
def load_and_prepare_data(file_path):
    """
    Load the Netflix dataset and perform initial preparation
    """
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully with shape:", df.shape)
    return df

# 2. Data Cleaning
def clean_data(df):
    """
    Clean the dataset by handling missing values
    """
    # Check missing values
    missing_values = df.isnull().sum()
    print("\nMissing values before cleaning:\n", missing_values)
    
    # Handle missing values
    df['director'].fillna('Unknown Director', inplace=True)
    df['cast'].fillna('Unknown Cast', inplace=True)
    df['country'].fillna('Unknown Country', inplace=True)
    df['rating'].fillna('Not Rated', inplace=True)
    
    print("\nMissing values after cleaning:\n", df.isnull().sum())
    return df

# 3. Data Exploration
def explore_data(df):
    """
    Perform exploratory data analysis
    """
    # Basic statistics
    print("\nDataset Overview:")
    print(df.describe())
    
    # Content type distribution
    print("\nContent Type Distribution:")
    print(df['type'].value_counts())
    
    # Release year distribution
    print("\nRelease Year Statistics:")
    print(df['release_year'].describe())
    
    return df

# 4. Data Visualization
def create_visualizations(df):
    """
    Create visualizations for genres and ratings
    """
    # Most watched genres visualization
    plt.figure(figsize=(15, 8))
    # Split the listed_in column and count genre frequencies
    genres = df['listed_in'].str.split(',').explode().str.strip()
    genre_counts = genres.value_counts().head(10)
    
    sns.barplot(x=genre_counts.values, y=genre_counts.index)
    plt.title('Top 10 Most Common Genres on Netflix')
    plt.xlabel('Count')
    plt.ylabel('Genre')
    plt.tight_layout()
    plt.savefig('genres_distribution.png')
    plt.close()
    
    # Ratings distribution visualization
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, y='rating', order=df['rating'].value_counts().index)
    plt.title('Distribution of Content Ratings on Netflix')
    plt.xlabel('Count')
    plt.ylabel('Rating')
    plt.tight_layout()
    plt.savefig('ratings_distribution.png')
    plt.close()

# Main execution function
def main(file_path):
    """
    Main function to execute the analysis pipeline
    """
    # 1. Load data
    df = load_and_prepare_data(file_path)
    
    # 2. Clean data
    df = clean_data(df)
    
    # 3. Explore data
    df = explore_data(df)
    
    # 4. Create visualizations
    create_visualizations(df)
    
    return df

# Example usage
if __name__ == "__main__":
    file_path = "Netflix_shows_movies.csv"  # Update with your file path
    df = main(file_path)