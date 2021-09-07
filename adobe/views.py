import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
import xml.etree.ElementTree as ET
import xmltodict


BASE_URL = 'https://class.r-ayandehsazan.ir/api/xml?'


def get_cookies(username, password):
    try:
        response = requests.get(
            f'{BASE_URL}action=login&login={username}&password={password}')
        print(response.headers)
        BREEZESESSION = response.headers.get(
            'Set-Cookie').split(';')[0].split('=')[1]

    except:
        print('not good')
    return BREEZESESSION

@api_view(['GET', 'POST'])
def adobe_login(request):
    try:
        username = request.GET.get('username')
        password = request.GET.get('password')
        print('username : '+username)
        print('password : '+password)
        BREEZESESSION = get_cookies(username, password)
        response = requests.get(
            f'{BASE_URL}action=login&login={username}&password={password}&session={BREEZESESSION}')
        obj = xmltodict.parse(response.text)
    except:
        print('not good')
    return Response(obj)

@api_view(['GET', 'POST'])
def common_info(request):
    try:
        username = request.GET.get('username')
        password = str(request.GET.get('password'))
        print('username : '+username)
        print('password : '+password)
        BREEZESESSION = get_cookies(username, password)
        response = requests.get(
            f'{BASE_URL}action=common-info&session={BREEZESESSION}')
        common_info = xmltodict.parse(response.content)
    except:
        print('not good')
    return Response(common_info)


@api_view(['GET'])
def get_principal_list(request):
    try:
        username = request.GET.get('username')
        password = request.GET.get('password')
        print('username : '+username)
        print('password : '+password)
        BREEZESESSION = get_cookies(username, password)
        response = requests.get(
            f'{BASE_URL}action=principal-list&session={BREEZESESSION}')
        principal_list = xmltodict.parse(response.content)
    except:
        print('not good')
    return Response(principal_list)


@api_view(['GET'])
def report_my_meetings(request):
    try:
        username = request.GET.get('username')
        password = request.GET.get('password')
        print('username : '+username)
        print('password : '+password)
        BREEZESESSION = get_cookies(username, password)
        response = requests.get(
            f'{BASE_URL}action=report-my-meetings&session={BREEZESESSION}')
        my_meetings = xmltodict.parse(response.content)
    except:
        print('not good')
    return Response(my_meetings)


def create_adobe_user(request):
    try:
        first_name = request.GET.get('firstname')
        last_name = request.GET.get('lastname')
        login = request.GET.get('login')
        password = request.GET.get('password')
        email = request.GET.get('email')
        print('first_name : '+first_name +
              'last_name : '+last_name +
              'login : '+login +
              'email : '+email
              )
        response = requests.get(
            f'{BASE_URL}action=principal-update&first-name={first_name}&last-name={last_name}&login={login}&password={password}&type=user&send-email=true&has-children=0&email={email}')
        obj = xmltodict.parse(response.content)
    except:
        print('not good')
    return Response(obj)

@api_view(['GET'])
def create_adobe_group():
    pass



@api_view(['GET'])
def report_bulk_users():
    pass


@api_view(['POST'])
def principals_of_manager():
    pass
