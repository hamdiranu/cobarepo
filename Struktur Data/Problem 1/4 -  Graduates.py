import pprint

def graduates(student):
    outgabungan={'foxes' :[],'wolves' :[],'tigers' :[]}
    for i in range(len(student)):
        if student[i]['score'] > 75 :
            calon = {}
            calon['name']=student[i]['name']
            calon['score']=student[i]['score']
            if student[i]['class'] == 'foxes' :
                outgabungan['foxes'].append(calon)
            elif student[i]['class'] == 'wolves' :
                outgabungan['wolves'].append(calon)
            elif student[i]['class'] == 'tigers' :
                outgabungan['tigers'].append(calon)

    if outgabungan['foxes'] == []:
        del outgabungan['foxes']
    elif outgabungan['wolves'] == []:
        del outgabungan['wolves']
    elif outgabungan['tigers'] == []:
        del outgabungan['tigers']
    
    return outgabungan

print(" ")
pprint.pprint(graduates([
 {
   'name': 'Dimitri',
   'score': 90,
   'class': 'foxes'
 },
 {
   'name': 'Alexei',
   'score': 85,
   'class': 'wolves'
 },
 {
   'name': 'Sergei',
   'score': 74,
   'class': 'foxes'
 },
 {
   'name': 'Anastasia',
   'score': 78,
   'class': 'wolves'
 }
]))
print(" ")

pprint.pprint(graduates([
 {
   'name': 'Alexander',
   'score': 100,
   'class': 'foxes'
 },
 {
   'name': 'Alisa',
   'score': 76,
   'class': 'wolves'
 },
 {
   'name': 'Vladimir',
   'score': 92,
   'class': 'foxes'
 },
 {
   'name': 'Albert',
   'score': 71,
   'class': 'wolves'
 },
 {
   'name': 'Viktor',
   'score': 80,
   'class': 'tigers'
 }
]))

print(" ")
            