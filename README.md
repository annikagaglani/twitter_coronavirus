# Coronavirus Twitter Analysis

## Project Description

This project analyzes geotagged tweets from 2020 to track trends in hashtags related to COVID-19. Using the MapReduce framework, the project processes large-scale Twitter datasets to extract relevant hashtags, aggregate their occurrences by language and country, and visualize the results. The analysis provides insights into how discussions around COVID-19 evolved across different regions and languages.

**Learning Objectives:**
1) Work with large-scale datasets
2) Work with multilingual text
3) Use the MapReduce divide-and-conquer paradigm to create parallel code

## Data

The dataset consists of geotagged Twitter data files from 2020, formatted as `geoTwitterYY-MM-DD.zip` for each day of the year. Inside each zip file is 24 text files for each hour of the day. These files contain counts of hashtags used in different countries and languages, extracted during the map and reduce phases. The processed data is stored as JSON files, which serve as inputs for visualization.

## Steps Taken

1) Map Phase (data preprocessing): `map.py`
   * Extract hashtags (coronavirus-related) and count occurrences by country and language.
   * Store intermediate results as JSON files.    
2) Reduce Phase (aggregation): `reduce.py`
   * Combine and sum hashtag counts across multiple data files.
   * Output final JSON files containing total counts for each hashtag by country and language.
3) Visualization
   * `visualize.py`: Generate bar plots for the most frequent hashtags by country and language.
   * `alternative_reduce.py`: Create a time-series analysis plot of hashtag trends over the course of the year.

## Results

**Top 10 Languages Using #coronavirus**

![lang json#coronavirus](https://github.com/user-attachments/assets/d78ed25e-6055-4cd6-ad89-0f979c0b0dc3)

**Top 10 Languages Using #코로나바이러스 (Korean coronavirus hashtag)**
![lang json#코로나바이러스](https://github.com/user-attachments/assets/805c70c3-46f6-4e27-b0d5-0affca8c4c3e)

**Top 10 Countries Using #coronavirus**

![country json#coronavirus](https://github.com/user-attachments/assets/c49d1615-c3c4-4dd6-8fb8-5a5de7ea243e)

**Top 10 Countries Using #코로나바이러스**

![country json#코로나바이러스](https://github.com/user-attachments/assets/c1f7051f-a9c2-4f8e-9ee6-22256e8a0912)

**Time-Series Trend of #coronavirus and #covid19**
![hashtag trends plot](graphs/hashtag_trends.png)

## How to Run the Analysis

1) Run the Mapper
```
./run_maps.sh
```

2) Run the Reducer for both Country and Language
```
python3 src/reduce.py --input_paths outputs/*.json --output_path outputs/country.json
python3 src/reduce.py --input_paths outputs/*.json --output_path outputs/lang.json
```

3) Generate the Bar Plots from `visualize.py`
   * For Language Data
     ```
     python3 src/visualize.py --input_path outputs/lang.json --key='#coronavirus'
     python3 src/visualize.py --input_path outputs/lang.json --key='#코로나바이러스'
     ```
   * For Country Data
     ```
     python3 src/visualize.py --input_path outputs/country.json --key='#coronavirus'
     python3 src/visualize.py --input_path outputs/country.json --key='#코로나바이러스'
     ```

4) Generate the Time-Series Analysis Plot from `alternative_reduce.py`
```
python3 src/alternative_reduce.py --hashtags '#coronavirus' '#covid19' --input_folder outputs/ --output_path graphs/trend_plot.png
```
