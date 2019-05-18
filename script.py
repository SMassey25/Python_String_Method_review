highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# print(highlighted_poems)
# print('\n')

#Splits the highlighted_poems at the commas and saves it in a new list. 
highlighted_poems_list = highlighted_poems.split(',')
# print(highlighted_poems_list)
# print('\n')

#Removes the white space in the highlighted_poems_list and stores it in the highlighted_poems_stripped
highlighted_poems_stripped = []
for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())
# print(highlighted_poems_stripped)
# print('\n')

#Splits the stripped highlighted_poems to get the details of each poem. The delimiter that seprates the details in a colon. 
highlighted_poems_details = []
for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(':'))
  
titles = []
poets = []
dates = []

#Creates lists of the titles of the poems, poets and tha year the peoms were published in 
for poem in highlighted_poems_details:
  titles.append(poem[0])
  poets.append(poem[1])
  dates.append(poem[2])
  
#Prints the result for each poem. 
range_check = range(0,len(highlighted_poems_details))  
for i in range_check:
    print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))
