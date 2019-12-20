import pprint
def highestScore(students):
    output={}
    for i in range(len(students)):
        inp={}
        inp['name']=students[i]['name']
        inp['score']=students[i]['score']
        if students[i]['class'] not in output:
            output[students[i]['class']]=inp
        else :
            if students[i]['score']>output[students[i]['class']]['score']:
                output[students[i]['class']]=inp
    return output



print(highestScore([])) # {}

pprint.pprint(highestScore([
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
   'score': 100,
   'class': 'foxes'
 },
 {
   'name': 'Anastasia',
   'score': 78,
   'class': 'wolves'
 }
]))


'''
{
 'foxes': {'name': 'Sergei', 'score': 100},
 'wolves': {'name': 'Alexei', 'score': 85}
}
'''

pprint.pprint(highestScore([
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

'''
{
 foxes: { 'name': 'Alexander', 'score': 100 },
 wolves: { 'name': 'Alisa', 'score': 76 },
 tigers: { 'name': 'Viktor', 'score': 80 }
}
'''