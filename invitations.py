# Gist for Invitation problem

# Copyright (c) 2024 Neurosync

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sys

# Initialize lists to store the names of people and their friendships
names = []
friendships = []

# Read all input lines
data = sys.stdin.readlines()

# Process each line to extract names and friendships
for line in data:
    line = line.strip()

    # If line starts with "Group:", extract names
    if line.startswith("Group:"):
        names = line.split(":")[1].strip().split(", ")
    # Otherwise, add friendship pair to the list
    elif line:
        friendships.append(line)
    else:
        print("Invalid input")
        exit(0)

# Ensure there are enough friendships to distribute tickets
if len(friendships) < 3:
    print("Not enough friends to distribute tickets")
    exit(0)

# Create a dictionary to store each person's friends
friend_map = {name: [] for name in names}

# Populate the dictionary with friendships
for friendship in friendships:
    try:
        friend1, friend2 = friendship.split(' - ')
        friend_map[friend1].append(friend2)
        friend_map[friend2].append(friend1)
    except ValueError:
        print("Invalid input")
        exit(0)

print(friend_map)

# Count the number of friends for each person
friend_counts = {}
for name, friends in friend_map.items():
    friend_counts[name] = len(friends)  # Count friends for each person

print(friend_counts)

# Sort people by the number of friends and get the top 3
# Step 1: Convert the dictionary to a list of tuples
sorted_friends = list(friend_counts.items())

# Step 2: Sort the list by the number of friends in descending order
sorted_friends.sort(key=lambda item: item[1], reverse=True)

# Step 3: Take the top 3 people with the most friends
top_3_friends = sorted_friends[:3]

# Display the top 3 people with their friend counts
for name, count in top_3_friends:
    print(f"{name} ({count})")