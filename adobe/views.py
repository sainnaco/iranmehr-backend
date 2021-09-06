import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
import xml.etree.ElementTree as ET
import xmltodict
import json
# action
#     'principal-list'
#     'common-info'
# xml. etree. ElementTree. tostring(element, encoding="unicode")

BASE_URL = 'https://class.r-ayandehsazan.ir/api/xml?'
# 'https://class.r-ayandehsazan.ir/api/'

base_url = 'https://class.r-ayandehsazan.ir/'

# 'https://class.r-ayandehsazan.ir/api/xml?action=principal-list&filter-email=rezataghipour1999@gmail.com/'
BASE_AUTH_URL = 'https://class.r-ayandehsazan.ir/account-id=7&principal-id=31016&showNotif=true&OWASP_CSRFTOKEN=fdc96e761f6bc41b0b0f3c6aea6bb6534c08cc05d5676a783acad23bd15b1926/'

@api_view(['GET','POST'])
def adobe_login(request):    
    username = request.GET.get('username')
    password = request.GET.get('password')
   
    try :
        response = requests.get(f'{BASE_URL}action=login&login={username}&password={password}')
        print(response.headers.get('Set-Cookie'))
        # h_obj = json.dumps(response.headers)

        obj = response.headers.get('Set-Cookie').split(';')[0].split('=')[1]
        # headers = xmltodict.parse(response.headers)
        # header_obj = json.dumps(headers)
        # print(header_obj)
    
    except:
        print('not good')
    return Response(obj)
    


@api_view(['GET','POST'])
def get_common_info(request):

    BREEZESESSION = request.GET.get('BREEZESESSION')
    print('B :'+BREEZESESSION)

    data = {}
    querystring = {"action":"common-info"}
    payload = ""
    headers = {"Cookie": f"BREEZESESSION={BREEZESESSION};"}

    try:
        response = requests.request("GET", 'https://class.r-iranmehr.ir/api/xml', data=payload, headers=headers, params=querystring)
        print(response.text)
        # tree = ET.fromstring(response.content)
        # user = (tree.find('common')).find('user')
        # data['name'] = (user.find('name')).text
        # data['login'] = (user.find('login')).text
        obj = xmltodict.parse(response.text)

    except:
        data['error'] = None
    return Response(obj)

    # try:
    #     response = requests.get(f'{BASE_URL}action=common-info&session={BREEZESESSION}')
    #     print('okkkkkkkkkk')
    #     # print(response.)
    #     # print('s :'+response.status)
    #     # print('h :'+response.headers)
    #     # print('c :'+response.content)

    #     obj = xmltodict.parse(response.text)

    # except:
    #     print('not good')



@api_view(['GET'])
def get_principal_list(request):

    email = request.GET.get('email')
    url = f'{BASE_URL}xml?action=principal-list&filter-email={email}'
    adobe_response = requests.get(url)
    obj = xmltodict.parse(adobe_response.text)
    j_obj = json.dumps(obj)
    print(j_obj)

    return Response(obj)



@api_view(['GET'])
def report_bulk_users():

    url =f'{BASE_URL}xml?action=report-bulk-users/'
    adobe_response = requests.get(url)
    obj = xmltodict.parse(adobe_response.text)

    return Response(obj)    

@api_view(['POST'])
def principals_of_manager(request):
    manager_id = request.GET.get('manager-id')
    url =f'{BASE_URL}xml?action=principal-list&filter-manager-id={manager_id}'
    adobe_response = requests.get(url)
    obj = xmltodict.parse(adobe_response.text)

    return Response(obj)     
