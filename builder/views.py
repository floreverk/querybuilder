from django.shortcuts import render
from .forms import EndpointForm

# Create your views here.
def buildquery(request):
    if request.method == 'POST':
        form = EndpointForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['endpoints'] == True:
                endpoint = ''
            else:
                endpoint= ''
            if form.cleaned_data['dmg'] == True:
                dmg = 'FROM &lt;http://stad.gent/ldes/dmg&gt;'
            else:
                dmg= ''
            if form.cleaned_data['ag'] == True:
                ag = 'FROM &lt;http://stad.gent/ldes/archief&gt;'
            else:
                ag= ''
            if form.cleaned_data['hva'] == True:
                hva = 'FROM &lt;http://stad.gent/ldes/hva&gt;'
            else:
                hva= ''
            
            if form.cleaned_data['im'] == True:
                im = 'FROM &lt;http://stad.gent/ldes/industriemuseum&gt;'
            else:
                im= ''
            
            if form.cleaned_data['stam'] == True:
                stam = 'FROM &lt;http://stad.gent/ldes/stam&gt;'
            else:
                stam= ''
            
            if form.cleaned_data['limit'] == None:
                limit = ''
            else:
                limitnumber = str(form.cleaned_data['limit'])
                limit = 'LIMIT '+ limitnumber

            if form.cleaned_data['distinct'] == True:
                distinct = 'DISTINCT'
            else:
                distinct = ''

            if form.cleaned_data['count'] == True:
                count = 'COUNT ('
                closecount = ')'
            else:
                count = ''
                closecount = ''
            
            if form.cleaned_data['title'] == True:
                title = '?o cidoc:P102_has_title ?title.'
                variabletitle = '?title'
                if form.cleaned_data['titlefilter'] == '':
                    filtertitle = ''
                else:
                    titlefilter = form.cleaned_data['titlefilter']
                    filtertitle = 'FILTER (regex(?title, "'+titlefilter+'", "i"))'
            else:
                title= ''
                variabletitle = ''
                filtertitle = ''
            
            if form.cleaned_data['description'] == True:
                note = '?o cidoc:P3_has_note ?note.'
                variablenote = '?note'
                if form.cleaned_data['descriptionfilter'] == '':
                    filternote = ''
                else:
                    notefilter = form.cleaned_data['descriptionfilter']
                    filternote = 'FILTER (regex(?note, "'+notefilter+'", "i"))'
            else:
                note= ''
                variablenote = ''
                filternote = ''
            
            if form.cleaned_data['image'] == True:
                image = '?o cidoc:P129i_is_subject_of ?image.'
                variableimage = '?image'
            else:
                image= ''
                variableimage = ''
                   
            if form.cleaned_data['objectname'] == True:
                objectname = '''?o cidoc:P41i_was_classified_by ?classified.</br>
                ?classified cidoc:P42_assigned ?assigned.</br>
                ?assigned skos:prefLabel ?objectname.
                '''
                variableobjectname = '?objectname'
                if form.cleaned_data['objectnamefilter'] == '':
                    filterobjectname = ''
                else:
                    objectnamefilter = form.cleaned_data['objectnamefilter']
                    filterobjectname = 'FILTER (regex(?objectname, "'+objectnamefilter+'", "i"))'
            else:
                objectname = ''
                variableobjectname = ''
                filterobjectname = ''

            if form.cleaned_data['associatie'] == True:
                associatie = '''?o cidoc:P128_carries ?carries.</br>
                ?carries cidoc:P129_is_about ?about.</br>
                ?about cidoc:P2_has_type ?type.</br>
                ?type skos:prefLabel ?associatie.
                '''
                variableassociatie = '?associatie'
                if form.cleaned_data['associatiefilter'] == '':
                    filterassociatie = ''
                else:
                    associatiefilter = form.cleaned_data['associatiefilter']
                    filterassociatie = 'FILTER (regex(?associatie, "^'+associatiefilter+'$", "i"))'
            else:
                associatie = ''
                variableassociatie = ''
                filterassociatie = ''

            if form.cleaned_data['objectnumber'] == True:
                objectnumber = '''?o adms:identifier ?identifier.</br>
                ?identifier skos:notation ?objectnumber.
                '''
                variableobjectnumber = '?objectnumber'
                prefixadms = 'PREFIX adms:&lt;http://www.w3.org/ns/adms#&gt;'
                if form.cleaned_data['objectnumberfilter'] == '':
                    filterobjectnumber = ''
                else:
                    objectnumberfilter = form.cleaned_data['objectnumberfilter']
                    filterobjectnumber = 'FILTER (regex(?objectnumber, "^'+objectnumberfilter+'$", "i"))'
            else:
                objectnumber = ''
                variableobjectnumber = ''
                filterobjectnumber = ''
                prefixadms = ''

            if form.cleaned_data['vervaardiger'] == True:
                vervaardiger = '''?o cidoc:P108i_was_produced_by ?production.</br>
                ?production cidoc:P14_carried_out_by ?producer.</br>
                ?producer la:equivalent ?equivalent.</br>
                ?equivalent rdfs:label ?creator.
                '''
                variablevervaardiger = '?creator'
                prefixla = 'PREFIX la:&lt;https://linked.art/ns/terms/&gt;'
                if form.cleaned_data['vervaardigerfilter'] == '':
                    filtervervaardiger = ''
                else:
                    vervaardigerfilter = form.cleaned_data['vervaardigerfilter']
                    filtervervaardiger = 'FILTER (regex(?creator, "'+vervaardigerfilter+'", "i"))'
            else:
                vervaardiger = ''
                variablevervaardiger = ''
                filtervervaardiger = ''
                prefixla = ''
                        
            if form.cleaned_data['associatie'] or form.cleaned_data['objectname'] or form.cleaned_data['objectnumber']== True:
                prefix = 'PREFIX skos:&lt;http://www.w3.org/2004/02/skos/core#&gt;'
            else:
                prefix = ''

            if form.cleaned_data['datum'] == True:
                datum = '''?o cidoc:P108i_was_produced_by ?produced.</br>
                ?produced cidoc:P4_has_time-span ?timespan.</br>
                '''
                variabledatum = '?timespan'
                if form.cleaned_data['datumfilter'] == '':
                    filterdatum = ''
                else:
                    datumfilter = form.cleaned_data['datumfilter']
                    filterdatum = 'FILTER (regex(?timespan, "'+datumfilter+'", "i"))'
            else:
                datum = ''
                variabledatum = ''
                filterdatum = ''
           
            return render(request, 'query.html', {'endpoint': endpoint, 'hva': hva, 'dmg': dmg, 'im': im, 'ag': ag, 'stam': stam, 
            'limit': limit, 'distinct': distinct, 'count': count, 'closecount': closecount,
            'variabletitle': variabletitle, 'title': title, 'filtertitle': filtertitle, 
            'note': note, 'variablenote': variablenote, 'filternote': filternote, 
            'image': image, 'variableimage': variableimage, 
            'prefix': prefix, 'prefixadms': prefixadms, 'prefixla': prefixla,
            'objectname': objectname, 'variableobjectname': variableobjectname, 'filterobjectname': filterobjectname, 
            'associatie': associatie, 'variableassociatie': variableassociatie, 'filterassociatie': filterassociatie,
            'objectnumber': objectnumber, 'variableobjectnumber': variableobjectnumber, 'filterobjectnumber': filterobjectnumber,
            'vervaardiger': vervaardiger, 'variablevervaardiger': variablevervaardiger, 'filtervervaardiger': filtervervaardiger,
            'datum': datum, 'variabledatum': variabledatum, 'filterdatum': filterdatum})
            
    form = EndpointForm()
   
    return render(request, 'form.html', {'form':form})