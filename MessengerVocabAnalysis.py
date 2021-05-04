from Person import Person
import math
import numpy as np
import matplotlib.pyplot as plt

testData = {"John": {"one":2, "nice":4, "wow":6, "keyboard":1, "computer":1, "phone":5},
            "Zach":{"dang":4, "oh":5, "the":2, "of":1, "tech":1},
            "Matt":{"nice":10, "okay":2, "think":5, "yes":2, "what":2, "five":1, "one":1},
            "Bellamy":{"okay":2, "fine":2, "nope":2, "decent":1, "take":1},
            "Sarah":{"hola":1, "the":1, "a":1, "of":2, "which":13, "force":5},
            "Ally":{"hi":7, "good":5, "stats":4, "morning":2, "replace":1}}


# ------------------------------------------------------------
# Empty people list
# (Will contain Person objects)
# ------------------------------------------------------------
people = []


# ------------------------------------------------------------
# Parse the data
# ------------------------------------------------------------
for p in testData:
    person = Person(p)
    person.userDict = testData[p]
    people.append(person)
    


# ------------------------------------------------------------
# Process the data for plotting
# ------------------------------------------------------------

for p in people:
    p.doTotals()

labels = np.array([])
# Y Axis = Number of unique words
yLimit = people[0].uniqueWords
y = np.array([])
# X Axis = Total words
xLimit = people[0].totalWords    
x = np.array([])

for p in people:
    # labels.append(p.name)
    labels = np.append(labels, p.name)
    # y.append(p.uniqueWords)
    y = np.append(y, p.uniqueWords)
    # x.append(p.totalWords)
    x = np.append(x, p.totalWords)


# ------------------------------------------------------------
# Plot the scatter 
# ------------------------------------------------------------

for p in people:
    if p.uniqueWords > yLimit:
        yLimit = p.uniqueWords
    if p.totalWords > xLimit:
        xLimit = p.totalWords
        
# Create the figure and axes objects
fig, ax = plt.subplots(1, figsize=(10, 6))
fig.suptitle('Vocabulary distribution')

# Plot the scatter points
ax.scatter(x, y,
           color="blue",  # Color of the dots
           s=100,         # Size of the dots
           alpha=0.5,     # Alpha of the dots
           linewidths=1)  # Size of edge around the dots

# Add the participant names as text labels for each point
for x_pos, y_pos, label in zip(x, y, labels):
    ax.annotate(label,             # The label for this point
                xy=(x_pos, y_pos), # Position of the corresponding point
                xytext=(7, 0),     # Offset text by 7 points to the right
                textcoords='offset points', # tell it to use offset points
                ha='left',         # Horizontally aligned to the left
                va='center')       # Vertical alignment is centered
    ax.set_xlabel("Total Words")
    ax.set_ylabel("Unique Words")


# ------------------------------------------------------------
# Find the best fit line
# ------------------------------------------------------------

# plt.plot(x, np.poly1d(np.polyfit(x, y, 1))(x))
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b)

# Calculate the deltas
deltas = np.array([])
for p in range(len(labels)):
    y_true = y[p]
    y_predicted = m * x[p] + b
    # delta = mean_squared_error(y_true, y_predicted)
    delta = (y_true - y_predicted)
    deltas = np.append(deltas, delta)
    pass


# Softmax function to normalize deltas
softmax_sum = 0
for d in deltas:
    softmax_sum += math.exp(d)

# Calculate final variances
for d in range(len(deltas)):
    variance = math.exp(deltas[d])/softmax_sum
    if(deltas[d] >= 0):
        variance *= 100
    else:
        variance *= -100
    print("{} : {}".format(labels[d], variance))

# Show the plot
plt.show()