import csv  , bs4, requests


words2 = ['Feral','Vehement','Ruefully','Wrathful','Furtive','Heathen','Squalid','Stolid','Duress','Demise','Radical','Irascible','Recluse','Purloined','Spurious','Pinioned','Turmoil','Blandly','Puncture','Perforated','Eluded','Rale']
words = ['Uncouth','Encumber','Subpoena','Champerty','Amicably','Klan','Succinct','Aggregation','Elucidate','Litigant','Corroborating','Dictum','Benign','Acrimonious','Exodus','Glean','Turbulent','Smugly','Tenet','Complacent','Discreet','Temerity','Volition','Expunge','Impudent','Contraband','Unmitigated','Cynical']
words_test = ['hi bye','hi','bye']

with open('wordFile.txt', 'w') as wordFile:
    for word in words:
        
        
        print('Finding definition: ' + word)
        
        word.replace(' ', '+')
        
        try:
            res = requests.get('http://google.com/search?q=define+' + word)
            res.raise_for_status()

            soup = bs4.BeautifulSoup(res.text)

            definition = soup.find(attrs={"data-hveid": "20"}).parent.parent.find("li").string
            definition = str(definition)

            wordFile.write(word + ': ' +  definition + '\n')
        except AttributeError:
            print("Couldn't find the definition for " + word)