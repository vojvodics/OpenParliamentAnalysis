import requests
import json


def get_json(url, page=1):
    headers = {'content-type': 'application/json'}
    params = {'page': page}
    r = requests.get(url, headers=headers, params=params)
    json_string = r.text.strip().replace('{"error":404}', '')
    data = json.loads(json_string)
    return data


"""
    Get entity functions.
"""


def get_osobe():
    data = get_json('http://otvoreniparlament.rs/osoba')
    content = data['osobe']
    for obj in content:
        _print_osoba(obj)


def get_poslanicki_klub():
    data = get_json('http://otvoreniparlament.rs/poslanicki-klub')
    content = data['poslanickiKlub']
    for obj in content:
        _print_poslanicki_klub(obj)


def get_politicke_partije():
    data = get_json('http://otvoreniparlament.rs/politicka-partija')
    content = data['politickePartije']
    for obj in content:
        _print_partija(obj)


def get_poslanike():
    data = get_json('http://otvoreniparlament.rs/poslanik')
    for posl_grupa in data:
        for item in data[posl_grupa]:
            print('poslanik_id:', item['id'])
            _print_osoba(item['osoba'])


# get_poslanik ??
def get_poslanik_by_id(poslanik_id):
    data = get_json('http://otvoreniparlament.rs/poslanik/{}'.format(poslanik_id))
    # vraca objekat {'poslanik': {}}
    _print_poslanik(data['poslanik'])


def get_aktuelno():
    data = get_json('http://otvoreniparlament.rs/aktuelno')
    num_pages = data['vesti']['last_page']
    for i in range(1, num_pages + 1):
        # r = requests.get('http://otvoreniparlament.rs/aktuelno', headers={'content-type': 'application/json'},
        #                  params={'page': i})
        # json_string = r.text.strip().replace('{"error":404}', '')
        # data = json.loads(json_string)
        data = get_json(url='http://otvoreniparlament.rs/aktuelno', page=i)
        content = data['vesti']['data']
        for obj in content:
            print('id: ', obj['id'])
            print('naslov: ', obj['naslov'])
            print('datum ', obj['datum'])
            opis = obj['opis'].replace('<p>', '').replace('</p>', '').replace('<br />', '').replace('&scaron;', 'š') \
                .replace('<em>', '').replace('</em>', '')
            print('opis: ', opis)
            print()


def get_govor_by_poslanik(poslanik_id):
    data = get_json('http://otvoreniparlament.rs/poslanik/{}/govori'.format(poslanik_id))
    # data keys: dict_keys(['tipGovora', 'tipGovoraParam', 'poslanik', 'rod', 'govori', 'stranka'])
    num_pages = data['govori']['last_page']
    for i in range(1, num_pages + 1):
        data = get_json(url='http://otvoreniparlament.rs/poslanik/{}/govori'.format(poslanik_id), page=i)
        content = data['govori']['data']
        for obj in content:
            # obj keys: dict_keys(['tezina', 'osoba_id', 'govor', 'predsedavajuci', 'id', 'transkript_id', 'vrsta_govora', 'osoba'])
            print(obj['govor'])


"""
    Print entity functions.
"""


def _print_osoba(obj):
    print('id: ', obj['id'])
    print('ime: ', obj['ime'])
    print('prezime: ', obj['prezime'])
    print('datum rodjenja', obj['datum_rodjenja'])
    print('pol: ', obj['pol'])
    print('mesto rodjenja: ', obj['mesto_rodjenja'])
    print('profesija: ', obj['profesija'])
    print('biografija: ', obj['biografija'])
    print('\n')


def _print_poslanicki_klub(obj):
    print('id: ', obj['id'])
    print('naziv: ', obj['naziv'])
    print('opis: ', obj['opis'])
    print('last_update', obj['updated_at'])
    print('saziv id', obj['saziv_id'])
    print('\n')


def _print_partija(obj):
    print('id: ', obj['id'])
    print('naziv: ', obj['naziv'])
    print('\n')


def _print_poslanik(obj):
    print('poslanik_id:', obj['id'])
    _print_osoba(obj['osoba'])


"""
    Task specific functions.
"""


def akt_naslov_list():
    lst = []
    data = get_json('http://otvoreniparlament.rs/akt')
    num_pages = data['paginator']['last_page']
    for i in range(num_pages + 1):
        page = get_json(url='http://otvoreniparlament.rs/akt', page=i)
        content = page['akta']
        for obj in content:
            lst.append(obj['naslov'])
    return lst


if __name__ == '__main__':
    print(akt_naslov_list())
