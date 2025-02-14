import pandas as pd
import csv
import datetime as dt
import matplotlib.pyplot as plt

# Reading hacker_news_data.csv into a list of lists
file_path = 'data/hacker_news_data.csv'
file = open(file_path)
hn = list(csv.reader(file))

# Displaying the first five rows from the file
print("First five rows:\n")
for row in hn[:5]:
    print(row)

# Extracting the first row from the data, assigning it to a variable
headers = hn[0]
# Removing the first row from hn
hn = hn[1:]

# Displaying the first five rows again
print("\nFirst five rows after removing headers:\n")
for row in hn[:5]:
    print(row)

# Creating empty lists for ask_posts, show_posts, and other_posts
ask_posts = []
show_posts = []
other_posts = []

# Filtering posts from hn to the relevant lists using for loop
for post in hn:
    title = post[1]
    if title.lower().startswith("ask hn"):
        ask_posts.append(post)
    elif title.lower().startswith("show hn"):
        show_posts.append(post)
    else:
        other_posts.append(post)

# Checking number of posts in each list
print("\nNumber of posts:\n")
print(f"Ask Posts: {len(ask_posts)}")
print(f"Show Posts: {len(show_posts)}")
print(f"Other Posts: {len(other_posts)}")

# Finding the total number of comments in ask posts
total_ask_comments = 0
for post in ask_posts:
    total_ask_comments += int(post[4])
avg_ask_comments = total_ask_comments / len(ask_posts)
print(f"\nAverage Ask Comments: {avg_ask_comments:.2f}")

# Finding the total number of comments in show posts
total_show_comments = 0
for row in show_posts:
    total_show_comments += int(row[4])
avg_show_comments = total_show_comments / len(show_posts)
print(f"\nAverage Show Comments: {avg_show_comments:.2f}")

# Iterating over ask posts to find amount of ask posts created in each hour and the number of comments received
result_list = []
for row in ask_posts:
    created_at = row[6]
    num_comments = row[4]
    result_list.append([created_at, int(num_comments)])

counts_by_hour = {}
comments_by_hour = {}

# Changing the date format
date_format = "%m/%d/%Y %H:%M"
for row in result_list:
    post_date = row[0]
    comments = row[1]
    date = dt.datetime.strptime(post_date, date_format)
    hour = dt.datetime.strftime(date, "%H")

    # Creating frequency table
    if hour not in counts_by_hour:
        counts_by_hour[hour] = 1
        comments_by_hour[hour] = comments
    else:
        counts_by_hour[hour] += 1
        comments_by_hour[hour] += comments

# Calculating average number of comments ask posts received per hour created
avg_by_hour = []
for comment in comments_by_hour:
    avg_by_hour.append([comment, comments_by_hour[comment] / counts_by_hour[comment]])
print("\nAverage comments by hour:\n")
print(avg_by_hour)

# Swapping columns for sorting
swap_avg_by_hour = []
for row in avg_by_hour:
    swap_avg_by_hour.append([row[1], row[0]])

# Sorting by the average number of comments
sorted_swap = sorted(swap_avg_by_hour, reverse=True)
print("\nTop hours for Ask Posts comments:\n")
for avg, hr in sorted_swap[:5]:
    print(f"{dt.datetime.strptime(hr, '%H').strftime('%H:%M')}: {avg:.2f} average comments per post")

# Visualizing Data with Matplotlib
# Example: Visualizing the number of comments per hour for Ask HN posts
# This is an extended analysis you can perform later in the project
counts_by_hour = {}
comments_by_hour = {}

for post in ask_posts:
    created_at = post[6]
    num_comments = int(post[4])
    hour = created_at.split()[1].split(':')[0]

    if hour not in counts_by_hour:
        counts_by_hour[hour] = 1
        comments_by_hour[hour] = num_comments
    else:
        counts_by_hour[hour] += 1
        comments_by_hour[hour] += num_comments

# Calculating the average number of comments per hour
avg_by_hour = []
for hour in comments_by_hour:
    avg_by_hour.append([hour, comments_by_hour[hour] / counts_by_hour[hour]])

# Sorting the list
avg_by_hour.sort(key=lambda x: x[1], reverse=True)

# Plotting the results
hours = [x[0] for x in avg_by_hour]
avg_comments = [x[1] for x in avg_by_hour]

plt.plot(hours, avg_comments)
plt.xlabel('Hour of the Day')
plt.ylabel('Average Number of Comments')
plt.title('Average Number of Comments by Hour of the Day')
plt.show()
