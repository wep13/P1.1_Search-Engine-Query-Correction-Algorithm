#!/usr/bin/env python
# coding: utf-8

# In[1]:


def Levenshtein_distance(str_1, str_2):
    
    """
    Calculates the Levenshtein distance between two strings.

    The distance represents the minimum number of insertions, deletions, and substitutions 
    required to transform str_1 into str_2.

    Args:
        str_1 (str): First string.
        str_2 (str): Second string.

    Returns:
        int: Levenshtein distance between the two strings.
    """

    matrix = []

    # Create an empty matrix

    for i in range(len(str_1) + 1):
        matrix.append([])

        for j in range(len(str_2) + 1):
            matrix[i].append(0)

    # Adding numbers to the first row and first column

    for i in range(len(str_1) + 1):
        matrix[i][0] = i

    for j in range(len(str_2) + 1):
        matrix[0][j] = j

    # Calculating the distances for each element in the matrix

    for i in range(1, len(str_1) + 1):
        for j in range(1, len(str_2) + 1):

            if str_1[i-1] == str_2[j-1]:

                matrix[i][j] = min(
                    matrix[i-1][j] + 1,    # Upper element
                    matrix[i][j-1] + 1,    # Left element
                    matrix[i-1][j-1]       # Diagonal element without weight
                )

            else:

                matrix[i][j] = min(
                    matrix[i-1][j] + 1,     # Upper element
                    matrix[i][j-1] + 1,     # Left element
                    matrix[i-1][j-1] + 1    # Diagonal element with weight
                )

    return matrix[-1][-1]


# In[2]:


def suggest_correction(query, dictionary):

    # Tokenize the query                              
    query_tokenized = query.lower().split(" ")  

    # Initialize the lists that will contain the modified query,
    # the minimum Levenshtein distances, and the indexes of the replacement words
    query_tokenized_modified = [] 
    distance_list_min = []
    distance_list_min_index = []

    # Calculate the Levenshtein distance between each word in the query
    # and every word in the searchify_words list.
    # If all words have a minimum distance of 0, the query is correct.
    # If at least one word has a distance greater than 3, the query cannot be modified.
    # Otherwise, replace the incorrect words with the closest words in the dictionary.

    for word in query_tokenized:
    
        distance_list = []

        for i in range(len(dictionary)):
    
            distance_list.append(Levenshtein_distance(word, dictionary[i]))
    
        distance_list_min.append(min(distance_list))
        distance_list_min_index.append(distance_list.index(min(distance_list)))
    
    # Case 1: the query is already correct
    if sum(distance_list_min) == 0:
        print(f'Initial query: {query}')
        print("The query is correct")
    
    # Case 2: at least one word is too distant from the dictionary
    elif max(distance_list_min)>2:
        for index, distance in enumerate(distance_list_min):
            if distance > 2 :
                word = query_tokenized[index]
                print(f'Initial query: {query}')
                print(f'The word {word} is too distant from the one in the dictionary and i am not able to modify the query')
                break
                
    # Case 3: modify the incorrect words
    else:
    
        for index in range(len(query_tokenized)):
            if distance_list_min[index] == 0:
                query_tokenized_modified.append(query_tokenized[index])
            else:
                query_tokenized_modified.append(searchify_words[distance_list_min_index[index]])
            
            
        query_modified = " ".join(query_tokenized_modified)    
        print(f'Initial query: {query}')
        print(f'Did you mean to search: {query_modified}')


# In[3]:


# Define the dictionary of included words
# We created the dictionary with 50 words relevant to the company's scope (searchify_words).
# We also included commonly used Italian prepositions, articles, and conjunctions.


conjunctions = ["e", "ed", "che", "se"]
articles = ["il", "lo", "la", "i", "gli", "le", "un", "uno", "una"]
prepositions = ["di", "a", "da", "in", "con", "su", "per", "tra", "fra", 
                "del", "dello", "della", "dei", "degli", "delle", "al", "allo", 
                "alla", "ai", "agli", "alle", "dal", "dallo", "dalla", "dai", "dagli", 
                "dalle", "nel", "nello", "nella", "nei", "negli", "nelle", "col", 
                "coi", "sul", "sullo", "sulla", "sui", "sugli", "sulle"]

searchify_words = ["ricerca", "motore", "documenti", "archivi", "intranet", 
                   "gestionale", "repository", "aziendale", "informazioni", "parole", "chiave", 
                   "risorse", "report", "saas", "licenza", "piattaforma", "integrazione", 
                   "software", "startup", "tecnologia", "algoritmo", "algoritmica", 
                   "sviluppo", "esperienza", "semplicità", "utilizzo", "utenti", 
                   "azienda", "manifattura", "servizi", "professionale", "clienti", 
                   "rilascio", "sviluppatori", "customer", "success", "formazione", "informazione", 
                   "accesso", "recupero", "condivisione", "database", "interna", "digitale", "produttività", 
                   "efficienza", "autonomia", "qualità", "rapporto", "vendite"]

searchify_words_dictionary = searchify_words + conjunctions + articles + prepositions



# In[4]:


query_list = [
    "motore ricerca aziendale",
    "motor ricerca aziendale",
    "motoree ricerca aziendale",
    "motore ricerac aziendale",
    "motore ricerca azlendale",
    "ricerca documeti aziendale",
    "ricerca documentti aziendale",
    "ricerca documetni aziendale",
    "piattaforma saaS aziendale",
    "motore documenti ricerca",
    "ciao sono michele"
]


# In[5]:


for query in query_list:
    suggest_correction(query, searchify_words_dictionary)

