import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt


df = pd.read_csv('word.csv')
words = df['word'].tolist()

# Convert the list of words to a single string
word_data = ' '.join(words)

# Create the WordCloud
wordcloud = WordCloud(width=800, height=800, background_color='black').generate(word_data)

# Plot the WordCloud
plt.figure(figsize=(8, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# Save the WordCloud as an image
wordcloud.to_file('mental_health_wordcloud_dark.png')

# Show the WordCloud (optional)
plt.show()