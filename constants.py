# -*- coding: utf-8 -*-

#!/usr/bin/python3.6

NUMBER_COUNTRIES = 20  # Max 200.

stateName = {
    'SP': 'São Paulo',
    'RJ': 'Rio de Janeiro',
    'CE': 'Ceará',
    'AM': 'Amazonas',
    'PA': 'Pará',
    'MA': 'Maranhão',
    'PE': 'Pernambuco',
    'BA': 'Bahia',
    'ES': 'Espirito Santo',
    'PB': 'Paraíba',
    'AL': 'Alagoas',
    'DF': 'Distrito Federal',
    'MG': 'Minas Gerais',
    'AP': 'Amapá',
    'RS': 'Rio Grande do Sul',
    'SC': 'Santa Catarina',
    'RN': 'Rio Grande do Norte',
    'SE': 'Sergipe',
    'AC': 'Acre',
    'PI': 'Piauí',
    'RO': 'Rondônia',
    'PR': 'Paraná',
    'TO': 'Tocantins',
    'GO': 'Goiás',
    'RR': 'Roraima',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul' 
}
stateFlag = {
  'SP': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Bandeira_do_estado_de_S%C3%A3o_Paulo.svg/1280px-Bandeira_do_estado_de_S%C3%A3o_Paulo.svg.png',
  'RJ': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Bandeira_do_estado_do_Rio_de_Janeiro.svg/1280px-Bandeira_do_estado_do_Rio_de_Janeiro.svg.png',
  'CE': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Bandeira_do_Cear%C3%A1.svg/1280px-Bandeira_do_Cear%C3%A1.svg.png',
  'AM': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Bandeira_do_Amazonas.svg/1280px-Bandeira_do_Amazonas.svg.png',
  'PA': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Bandeira_do_Par%C3%A1.svg/1280px-Bandeira_do_Par%C3%A1.svg.png',
  'MA': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Bandeira_do_Maranh%C3%A3o.svg/1280px-Bandeira_do_Maranh%C3%A3o.svg.png',
  'PE': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Bandeira_de_Pernambuco.svg/1280px-Bandeira_de_Pernambuco.svg.png',
  'BA': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Bandeira_da_Bahia.svg/1280px-Bandeira_da_Bahia.svg.png',
  'ES': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Bandeira_do_Esp%C3%ADrito_Santo.svg/1280px-Bandeira_do_Esp%C3%ADrito_Santo.svg.png',
  'PB': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Bandeira_da_Para%C3%ADba.svg/1280px-Bandeira_da_Para%C3%ADba.svg.png',
  'AL': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Bandeira_de_Alagoas.svg/1280px-Bandeira_de_Alagoas.svg.png',
  'DF': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Bandeira_do_Distrito_Federal_%28Brasil%29.svg/1280px-Bandeira_do_Distrito_Federal_%28Brasil%29.svg.png',
  'MG': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Bandeira_de_Minas_Gerais.svg/1280px-Bandeira_de_Minas_Gerais.svg.png',
  'AP': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Bandeira_do_Amap%C3%A1.svg/1280px-Bandeira_do_Amap%C3%A1.svg.png',
  'RS': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Bandeira_do_Rio_Grande_do_Sul.svg/1280px-Bandeira_do_Rio_Grande_do_Sul.svg.png',
  'SC': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Bandeira_de_Santa_Catarina.svg/1280px-Bandeira_de_Santa_Catarina.svg.png',
  'RN': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Bandeira_do_Rio_Grande_do_Norte.svg/1280px-Bandeira_do_Rio_Grande_do_Norte.svg.png',
  'SE': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Bandeira_de_Sergipe.svg/1280px-Bandeira_de_Sergipe.svg.png',
  'AC': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Bandeira_do_Acre.svg/1280px-Bandeira_do_Acre.svg.png',
  'PI': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Bandeira_do_Piau%C3%AD.svg/1280px-Bandeira_do_Piau%C3%AD.svg.png',
  'RO': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Bandeira_de_Rond%C3%B4nia.svg/1280px-Bandeira_de_Rond%C3%B4nia.svg.png',
  'PR': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Bandeira_do_Paran%C3%A1.svg/1280px-Bandeira_do_Paran%C3%A1.svg.png',
  'TO': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Bandeira_do_Tocantins.svg/1280px-Bandeira_do_Tocantins.svg.png',
  'GO': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Flag_of_Goi%C3%A1s.svg/1280px-Flag_of_Goi%C3%A1s.svg.png',
  'RR': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Bandeira_de_Roraima.svg/1280px-Bandeira_de_Roraima.svg.png',
  'MT': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Bandeira_de_Mato_Grosso.svg/1280px-Bandeira_de_Mato_Grosso.svg.png',
  'MS': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Bandeira_de_Mato_Grosso_do_Sul.svg/1280px-Bandeira_de_Mato_Grosso_do_Sul.svg.png'
}
countryName = [
{
  'name': 'United States',
  'translation': 'Estados Unidos'
},
{
  'name': 'Brazil',
  'translation': 'Brasil'
},
{
  'name': 'Russia',
  'translation': 'Rússia'
},
{
  'name': 'India',
  'translation': 'Índia'
},
{
  'name': 'United Kingdom',
  'translation': 'Reino Unido'
},
{
  'name': 'Spain',
  'translation': 'Espanha'
},
{
  'name': 'Italy',
  'translation': 'Itália'
},
{
  'name': 'Peru',
  'translation': 'Peru'
},
{
  'name': 'Germany',
  'translation': 'Alemanha'
},
{
  'name': 'Iran',
  'translation': 'Irã'
},
{
  'name': 'Turkey',
  'translation': 'Turquia'
},
{
  'name': 'Chile',
  'translation': 'Chile'
},
{
  'name': 'France',
  'translation': 'França'
},
{
  'name': 'Mexico',
  'translation': 'México'
},
{
  'name': 'Pakistan',
  'translation': 'Paquistão'
},
{
  'name': 'Saudi Arabia',
  'translation': 'Arábia Saudita'
},
{
  'name': 'Canada',
  'translation': 'Canadá'
},
{
  'name': 'China',
  'translation': 'China'
},
{
  'name': 'Bangladesh',
  'translation': 'Bangladesh'
},
{
  'name': 'Qatar',
  'translation': 'Catar'
},
{
  'name': 'Belgium',
  'translation': 'Bélgica'
},
{
  'name': 'South Africa',
  'translation': 'África do Sul'
},
{
  'name': 'Belarus',
  'translation': 'Belarus'
},
{
  'name': 'Sweden',
  'translation': 'Suécia'
},
{
  'name': 'Colombia',
  'translation': 'Colômbia'
},
{
  'name': 'Ecuador',
  'translation': 'Equador'
},
{
  'name': 'United Arab Emirates',
  'translation': 'Emirados Árabes Unidos'
},
{
  'name': 'Netherlands',
  'translation': 'Holanda'
},
{
  'name': 'Singapore',
  'translation': 'Singapura'
},
{
  'name': 'Egypt',
  'translation': 'Egíto'
},
{
  'name': 'Indonesia',
  'translation': 'Indonésia'
},
{
  'name': 'Portugal',
  'translation': 'Portugal'
},
{
  'name': 'Kuwait',
  'translation': 'Kuwait'
},
{
  'name': 'Switzerland',
  'translation': 'Suíça'
},
{
  'name': 'Ukraine',
  'translation': 'Ucrânia'
},
{
  'name': 'Poland',
  'translation': 'Polônia'
},
{
  'name': 'Argentina',
  'translation': 'Argentina'
},
{
  'name': 'Ireland',
  'translation': 'Irlanda'
},
{
  'name': 'Philippines',
  'translation': 'Filipinas'
},
{
  'name': 'Afghanistan',
  'translation': 'Afeganistão'
},
{
  'name': 'Dominican Republic',
  'translation': 'República Dominicana'
},
{
  'name': 'Romania',
  'translation': 'Romênia'
},
{
  'name': 'Oman',
  'translation': 'Omã'
},
{
  'name': 'Israel',
  'translation': 'Israel'
},
{
  'name': 'Panama',
  'translation': 'Panamá'
},
{
  'name': 'Iraq',
  'translation': 'Iraque'
},
{
  'name': 'Japan',
  'translation': 'Japão'
},
{
  'name': 'Austria',
  'translation': 'Áustria'
},
{
  'name': 'Bahrain',
  'translation': 'Bahrein'
},
{
  'name': 'Bolivia',
  'translation': 'Bolívia'
},
{
  'name': 'Armenia',
  'translation': 'Armênia'
},
{
  'name': 'Nigeria',
  'translation': 'Nigéria'
},
{
  'name': 'Kazakhstan',
  'translation': 'Cazaquistão'
},
{
  'name': 'Serbia',
  'translation': 'Sérvia'
},
{
  'name': 'Denmark',
  'translation': 'Dinamarca'
},
{
  'name': 'South Korea',
  'translation': 'Coréia do Sul'
},
{
  'name': 'Moldova',
  'translation': 'Moldávia'
},
{
  'name': 'Algeria',
  'translation': 'Argélia'
},
{
  'name': 'Ghana',
  'translation': 'Gana'
},
{
  'name': 'Czech Republic',
  'translation': 'República Tcheca'
},
{
  'name': 'Azerbaijan',
  'translation': 'Azerbaijão'
},
{
  'name': 'Cameroon',
  'translation': 'Camarões'
},
{
  'name': 'Norway',
  'translation': 'Noruega'
},
{
  'name': 'Guatemala',
  'translation': 'Guatemala'
},
{
  'name': 'Malaysia',
  'translation': 'Malásia'
},
{
  'name': 'Honduras',
  'translation': 'Honduras'
},
{
  'name': 'Australia',
  'translation': 'Austrália'
},
{
  'name': 'Finland',
  'translation': 'Finlândia'
},
{
  'name': 'Sudan',
  'translation': 'Sudão'
},
{
  'name': 'Tajikistan',
  'translation': 'Tajiquistão'
},
{
  'name': 'Uzbekistan',
  'translation': 'Uzbequistão'
},
{
  'name': 'Senegal',
  'translation': 'Senegal'
},
{
  'name': 'DR Congo',
  'translation': 'Rep. Dem. do Congo'
},
{
  'name': 'Nepal',
  'translation': 'Nepal'
},
{
  'name': 'Ivory Coast',
  'translation': 'Costa do Marfim'
},
{
  'name': 'Djibouti',
  'translation': 'Djibuti'
},
{
  'name': 'Guinea',
  'translation': 'Guiné'
},
{
  'name': 'Luxembourg',
  'translation': 'Luxemburgo'
},
{
  'name': 'Hungary',
  'translation': 'Hungria'
}]
