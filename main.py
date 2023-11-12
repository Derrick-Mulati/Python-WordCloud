from wordcloud import WordCloud, STOPWORDS
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image



text = open('pythontext.txt', 'r').read()

python_mask = np.array(PIL.Image.open("pyhonlogo.png"))

wc = WordCloud(stopwords=STOPWORDS,
               mask=python_mask,
               background_color="white").generate(text)


plt.imshow(wc)
plt.axis("off")
plt.show()