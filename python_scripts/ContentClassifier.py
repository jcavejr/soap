import argparse
import io
import json
import os

from google.cloud import language
import numpy
import six

profanity = 0
discrimination = 0

def classify(text, verbose=True):
    language_client = language.LanguageServiceClient()

    document = language.types.Document(
        content=text,
        type=language.enums.Document.Type.PLAIN_TEXT)
    response = language_client.classify_text(document)
    categories = response.categories

    result = {}

    for category in categories:
        # Turn the categories into a dictionary of the form:
        # {category.name: category.confidence}, so that they can
        # be treated as a sparse vector.
        result[category.name] = category.confidence

    if verbose:
        print(text)
        for category in categories:
            print(u'=' * 20)
            print(u'{:<16}: {}'.format('category', category.name))
            print(u'{:<16}: {}'.format('confidence', category.confidence))

    return result

with open("C:\Users\samvi\Desktop\outputone.txt","r") as o:
	r=o.readlines()

i=0
while i<200:
	with open("C:\Users\samvi\Desktop\lastoutput.txt","a+") as w:
		text1 = str(r[i])
		text=str(r[i])
		while len(text.split(" "))<200:
			text = text+text1
		
		try:
			analysis = classify(text)
			for key in analysis:
				w.write("category: "+key+" ")
				w.write("confidence: "+str(analysis[key]))
				w.write("\n")
				if key=="/Sensitive Subjects" or "/Adult":
					profanity+=1 
					
				elif key=="/People & Society/Social Issues & Advocacy/Discrimination & Identity Relations" or "/People & Society/Social Issues & Advocacy":
					discrimination+=1 
			
				else:
					pass
				
		except:
			w.write("\n")
		
		
	i+=1
	
print profanity
print discrimination

with open("C:\Users\samvi\Desktop\outputlast.txt","a+") as w2:
	w2.write("Profanity percentage: "+str((float(profanity/200))*100))
	w2.write("\nDiscrimination percentage: "+str((float(discrimination/200))*100))