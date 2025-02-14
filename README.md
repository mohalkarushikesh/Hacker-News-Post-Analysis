# Hacker-News-Post-Analysis

## Overview

This project analyzes a dataset of submissions to the Hacker News website over the last 12 months (up to September 26, 2016). The analysis focuses on posts whose titles begin with "Ask HN" or "Show HN" and aims to answer the following questions:
1. Do "Ask HN" or "Show HN" posts receive more comments on average?
2. Do posts created at a certain time receive more comments on average?

## Dataset

The dataset includes the following columns:
- `id`: The unique identifier of the post
- `title`: The title of the post
- `url`: The URL of the item being linked to
- `num_points`: The number of upvotes the post received
- `num_comments`: The number of comments the post received
- `author`: The name of the account that made the post
- `created_at`: The date and time the post was made (in Eastern Time, US)

The dataset can be downloaded from [here](https://dataquest.io/data/hacker_news.csv).

## Cloning and Running the Project

### Prerequisites

- Python 3.x
- `pip` package manager
- `git` for cloning the repository

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/hacker-news-posts.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd hacker-news-posts
   ```

3. **Create a Virtual Environment:**

   ```bash
   python -m venv env
   ```

4. **Activate the Virtual Environment:**

   - On Windows:
     ```bash
     env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

5. **Install the Required Packages:**

   ```bash
   pip install -r requirements.txt
   ```

### Running the Analysis

1. **Run the Analysis Script:**

   ```bash
   python analysis_script.py
   ```

   This script will load the dataset, perform data cleaning, analysis, and visualization as described in the project steps.

### Deactivating the Virtual Environment

After completing your work, you can deactivate the virtual environment:

```bash
deactivate
```

## Project Steps

### 1. Data Loading
Load the dataset using the `csv` module and display the first few rows to understand its structure.

### 2. Data Cleaning
- Extract and remove the headers.
- Clean the dataset by handling missing values and duplicates if any.

### 3. Data Exploration
- Explore the dataset to find the number of "Ask HN" and "Show HN" posts.
- Calculate the average number of comments for each type of post.

### 4. Data Analysis
- Analyze the number of comments received by posts created at different times of the day.
- Identify the best time to post to get the most comments.

### 5. Data Visualization
- Use libraries like Matplotlib to create visual representations of the findings.

## Key Findings

1. **Average Comments for "Ask HN" and "Show HN" Posts**:
   - "Ask HN" posts receive more comments on average compared to "Show HN" posts.

2. **Best Time to Post**:
   - Posts created at certain times of the day receive more comments on average, with specific hours showing significantly higher engagement.

## Code Example

Here's a snippet of the code used to analyze the dataset:

```python
import csv
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'data/hacker_news_data.csv'
with open(file_path, mode='r', newline='') as file:
    hn = list(csv.reader(file))

# Extract and remove headers
headers = hn[0]
hn = hn[1:]

# Filter and categorize posts
ask_posts = [post for post in hn if post[1].lower().startswith("ask hn")]
show_posts = [post for post in hn if post[1].lower().startswith("show hn")]
other_posts = [post for post in hn if not (post[1].lower().startswith("ask hn") or post[1].lower().startswith("show hn"))]

# Calculate average comments
avg_ask_comments = sum(int(post[4]) for post in ask_posts) / len(ask_posts)
avg_show_comments = sum(int(post[4]) for post in show_posts) / len(show_posts)

# Analyze comments by hour
result_list = [[post[6], int(post[4])] for post in ask_posts]
date_format = "%m/%d/%Y %H:%M"
counts_by_hour = {}
comments_by_hour = {}

for row in result_list:
    date = dt.datetime.strptime(row[0], date_format)
    hour = date.strftime("%H")
    if hour not in counts_by_hour:
        counts_by_hour[hour] = 1
        comments_by_hour[hour] = row[1]
    else:
        counts_by_hour[hour] += 1
        comments_by_hour[hour] += row[1]

avg_by_hour = [[hour, comments_by_hour[hour] / counts_by_hour[hour]] for hour in comments_by_hour]

# Display results
print(f"Average Ask Comments: {avg_ask_comments:.2f}")
print(f"Average Show Comments: {avg_show_comments:.2f}")

avg_by_hour.sort(key=lambda x: x[1], reverse=True)
for avg, hour in avg_by_hour:
    print(f"{hour}: {avg:.2f} average comments per post")

# Visualization
hours = [x[0] for x in avg_by_hour]
avg_comments = [x[1] for x in avg_by_hour]

plt.plot(hours, avg_comments)
plt.xlabel('Hour of the Day')
plt.ylabel('Average Number of Comments')
plt.title('Average Number of Comments by Hour of the Day')
plt.show()
```

## Conclusion

This project provides valuable insights into the engagement patterns on Hacker News. By understanding which types of posts and posting times receive more comments, users can optimize their submissions for better visibility and interaction.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Dataquest](https://www.dataquest.io/) for providing the dataset and the guided project.
