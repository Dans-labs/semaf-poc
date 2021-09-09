from rdflib import Graph, URIRef, Literal, BNode, plugin
from rdflib.serializer import Serializer
import json
from collections import defaultdict, OrderedDict
import re

def jsontograph(context, DEBUG):
    g = Graph().parse(data=json.dumps(context), format='json-ld')
    DEBUG = True
    if DEBUG:
        for subj, pred, obj in g:
            #print("%s %s %s" % (subj, pred, obj))
            if re.search('keyword#Term', pred):
                guid = subj
                gupred = pred
            if re.search('citation/Keyword', pred):
                keyguid = obj
                k1 = subj
                k2 = pred

    #g.add(subj, 'https://dataverse.org/schema/citation/keyword#Vocabulary', 'http://danbri.livejournal.com/data/foaf')
    subjurl = URIRef(guid)
    gupredurl = URIRef('https://dataverse.org/schema/citation/keyword#Vocabulary')
    # Found and set new field
    g.set((guid, gupred, Literal('Utest'))) 
    g.add((guid, gupredurl, Literal('https://www.wikidata.org/wiki/Q1935049')))
    # Add new node
    k = "https://dataverse.org/schema/citation/Keyword"
    for i in range(0,7):
        staID = BNode(k2)
        staID = BNode()
        varlit = "%s%s" % ('News', str(i))
        varurl = "%s%s" % ('https://www.wikidata.org/wiki/Q1935050', str(i))
        g.add((staID, gupred, Literal(varlit)))
        g.add((staID, gupredurl, Literal(varurl)))
        g.add((k1, k2, staID))
    
    v = g.serialize(format='json-ld')
    data = json.loads(v, object_pairs_hook=OrderedDict)
    o = data
    items = {}
    for i in range(0, len(o)):
        item = o[i]
        thiskey = o[i]['@id']
        del item['@id']
        items[thiskey] = item
    records = defaultdict(list)

    for i in range(0, len(o)):
        item = o[i]
        if re.search('terms\/title', str(item)):
            #print("%s %s" % (i, item))
            indexblock = i
    #print(o)
    #return 
    if '@id' in o[indexblock]:
        del o[indexblock]['@id']
    #del o[indexblock]['@type']

    for ikey in o[indexblock]:
        #print("%s %s [%s]" % (ikey, type(o[0][ikey]), len(o[0][ikey])))
        for element in o[indexblock][ikey]:
            fullrecord = ''
            #print("%s %s" % (ikey, element))
            if '@id' in element:
                fullrecord = items[element['@id']]

            #print(fullrecord)
            if fullrecord:
                if ikey in records:
                    #print(type(records[ikey]))
                    if not type(records[ikey]) is list:
                        thisrecord = [ records[ikey] ]
                    else:
                        thisrecord = records[ikey] 
                    thisrecord.append(fullrecord)
                    records[ikey] = thisrecord 
                    #records[ikey] = fullrecord
                else:
                    records[ikey] = fullrecord  
            else:
                if ikey in records:
                    #print("Check %s" % type(records[ikey]))
                    if not type(records[ikey]) is list: 
                        thisrecord = [ element ] 
                        records[ikey] = thisrecord
                    else:
                        thisrecord = element
                    #print(records[ikey])
                    #print(thisrecord)
                    thisrecord.append(fullrecord)
                    records[ikey] = thisrecord
                    records[ikey] = element
                else:
                    records[ikey] = element
    #if '@id' in records:
    #    del records['@id']
    v = g.serialize(destination='harvard.nt', format='n3')
    return records
        
datafile = 'new-dataset-template.jsonld'
#datafile = 'new-template.json'
datafile = 'harvard'
#datafile = 'harvard3'
#with open(datafile) as json_file:
#    context = json.load(json_file)
with open(datafile, encoding='utf-8') as fh:
    context = json.load(fh)
#print(context)
print(json.dumps(jsontograph(context, False)))
