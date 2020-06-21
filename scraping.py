#!/usr/bin/python3.6

import requests, json
from bs4 import BeautifulSoup
import constants as cte

class Scraping:
    def nationalPanorama(self):
        url = 'https://xx9p7hp1p7.execute-api.us-east-1.amazonaws.com/prod/PortalSintese'
        response = json.loads(requests.get(url).content)
        response = response[0]
        
        return {
            'date': response['data'][-2:] + '/' + response['data'][5:-3]+ '/' + response['data'][:4],
            'cases': int(response['casosAcumulado']),
            'deaths': int(response['obitosAcumulado']),
            'recovered': int(response['Recuperadosnovos']),
            'percentageInfected': round((float(response['casosAcumulado']) / float(response['populacaoTCU2019'])) * 100, 2),
            'states': self.statePanorama(),
            'source': 'Ministério da Saude, 2020 (https://covid.saude.gov.br/).'
        }
    
    def statePanorama(self):         
        url = 'https://xx9p7hp1p7.execute-api.us-east-1.amazonaws.com/prod/PortalEstado'
        response = json.loads(requests.get(url).content)
        data = []
        
        for state in response:            
            data.append({
                'name': cte.stateName[state['nome']],
                'flag': cte.stateFlag[state['nome']],
                'cases': int(state['casosAcumulado']),
                'deaths': int(state['obitosAcumulado']),
                'percentageInfected': round((float(state['casosAcumulado']) / float(state['populacaoTCU2019'])) * 100, 2)
            })
        
         
        return sorted(data, key=lambda name: name['name'])        
   
    def worldPanorama(self):
        URL = 'https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data#covid19-container'
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        dataTable = soup.find_all('table', class_ = 'wikitable plainrowheaders sortable')
        dataTable = dataTable[0]
        self.totalCases = soup.find_all('tr', class_ = 'sorttop')
        self.totalCases = self.totalCases[0].find_all('th')[2:-1]
        print(self.totalCases)
        key = ['cases', 'deaths']
        rows = [row for row in dataTable.find_all('tr')[2:]]
        locations = [row.find('a').text for row in rows[:-1]]
        countryFlag = [row.find('img').get('srcset') for row in rows[:-2]]
        print(len(countryFlag))
        data = [ { key[i] : int(value.text[:-1].replace(',', '')) for i, value in enumerate(row.find_all('td')[:-2])} for row in rows]
        totalPopulation = self.totalPopulation()
        result = []  
        

        for i in range(len(countryFlag)): 
            if i < cte.NUMBER_COUNTRIES:
                    name = ''
                    for country in cte.countryName:
                        if country['name'] == locations[i]:
                            data[i]['name'] = country['translation']
                            name = country['translation']
                        for value in totalPopulation:
                            if value['name'] == name:
                                data[i]['percentageInfected'] = round((float(data[i]['cases']) / float(value['totalPopulation'].replace(' ', ''))) * 100, 2)
                    data[i]['flag'] = 'https:' + countryFlag[i].rsplit(' ', 3)[0]
                    result.append(data[i])

        return {
            'cases': int(self.totalCases[0].text[:-1].replace(',', '')),
            'deaths': int(self.totalCases[1].text[:-1].replace(',', '')),
            'recovered': int(self.totalCases[2].text[:-1].replace(',', '')),
            'percentageInfected': round((float(self.totalCases[0].text.replace(',', '')) / float(7790000000)) * 100, 2),
            'states': result
        }    

    def totalPopulation(self):
        URL = 'https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_popula%C3%A7%C3%A3o'
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        dataTable = soup.find_all('table', class_ = 'wikitable sortable')
        dataTable = dataTable[0]
        key = ['name', 'totalPopulation']
        rows = [row for row in dataTable.find_all('tr')[1:]]   
        data =  [ { key[i] : value.text[:-1].replace(',', '') for i, value in enumerate(row.find_all('td')[1:3])} for row in rows]
        for country in data:
            if country['name'][0] == '\xa0':
                country['name'] = country['name'][1:]
        return data

    
