import random

#people that can't be matched with each other
al = ['ed', 'maria']
alena = ['emerson']
mands = ['arvi', 'yana', 'aren']
aren = ['arvi', 'yana', 'mands']
yana = ['arvi', 'mands', 'aren']
arvi = ['robin', 'mands', 'yana', 'aren']
brett = ['tin', 'roxie', 'ellie']
brian = ['ate']
te = ['jas', 'gabe', 'dana_te']
dana_te = ['te']
drew = ['mands']
ed = ['al']
ellie = ['brett', 'tin', 'roxie']
emerson = ['ate', 'alena']
gabe = ['jas', 'te']
jas = ['gabe', 'te']
jes = ['domo']
maria = ['al']
robin = ['arvi']
roxie = ['brett', 'tin', 'ellie']
tin = ['ellie']
ate = ['brian', 'kim']
domo = ['jess']
leni = []

#combine unmatch list into dictionary
santas = {'al': al, 'alena': alena, 'mands': mands, 'aren':aren, 'yana':yana, 'arvi':arvi, 'brett':brett, \
          'brian': brian, 'te': te, 'dana_te': dana_te, 'drew': drew, 'ed': ed, 'ellie': ellie, 'emerson':emerson, \
          'gabe': gabe, 'jas': jas, 'jes': jes, 'maria': maria, 'robin': robin, 'roxie': roxie, \
          'tin': tin, 'ate': ate, 'domo': domo, 'leni': leni}



#checks if the person being matched has any possible matches from remaining unmatched pool
def is_matchable(person, pos_matches):
    result = False
    
    for possible_match in pos_matches:
        if possible_match != person and possible_match not in santas[person]:
            result = True
    return result

#creates secret santa list from list of possible santas
#returns match list if possible, None if not
def make_secret_santa_list(santas_list):
    unmatched = santas_list.keys()
    matches = {}
    
    for person in santas_list:
        not_matched = True
        finished = True
    
        if  not is_matchable(person, unmatched):
            print("run again")
            not_matched = False
            finished = False
    
        while not_matched:
            i = random.randint(0, len(unmatched)-1)
            if person != unmatched[i] and unmatched[i] not in santas_list[person]:
                matches[person] = unmatched[i]
                unmatched.pop(i)
                not_matched = False
                
    if finished:
        return matches
    else:
        return None

secret_santa_list = make_secret_santa_list(santas)
        
while not secret_santa_list:
    secret_santa_list = make_secret_santa_list(santas)
    
for key, value in secret_santa_list.iteritems():
        print("{} -> {}".format(key, value))