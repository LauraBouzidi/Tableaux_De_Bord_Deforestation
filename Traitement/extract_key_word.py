# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 08:41:17 2019

@author: theca
"""

from rake_nltk import Rake
from nltk.corpus import stopwords 



text = ["Food is good and not too expensive. Serving is just right for adult. Ambient is nice too.",
           "Used to be good. Chicken soup was below average, bbq used to be good.",
           "Food was good, standouts were the spicy beef soup and seafood pancake! ",
           "Good office lunch or after work place to go to with a big group as they have a lot of private areas with large tables",
           "As a Korean person, it was very disappointing food quality and very pricey for what you get. I won't go back there again. ",
           "Not great quality food for the price. Average food at premium prices really.",
           "Fast service. Prices are reasonable and food is decent.",
           "Extremely long waiting time. Food is decent but definitely not worth the wait.",
           "Clean premises, tasty food. My family favourites are the clear Tom yum soup, stuffed chicken wings, chargrilled squid.",
           "really good and authentic Thai food! in particular, we loved their tom yup clear soup with sliced fish. it's so well balanced that we can have it just on its own. "
           ]



r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.Please note that "hello" is not included in the list of stopwords.



for i in range(len(text)):
    a=r.extract_keywords_from_text(text[i])
    b=r.get_ranked_phrases()
    c=r.get_ranked_phrases_with_scores()
    #print(b)
    print(c)
    

