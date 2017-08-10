import requests
import json


# todo /grad (/akt /radno_telo /saziv /oblasti /) /radno_telo /sednica_odbrora /javno_slusanje /glasanje{akt} /istrazivanje

def get_json(url):
    headers = {'content-type': 'application/json'}
    r = requests.get(url, headers=headers)
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


def get_politicke_partije(url='http://otvoreniparlament.rs/politicka-partija'):
    data = get_json()
    content = data['politickePartije']
    for obj in content:
        _print_partija(obj)


def get_aktuelno():
    data = get_json('http://otvoreniparlament.rs/aktuelno')
    num_pages = data['vesti']['last_page']
    for i in range(1, num_pages + 1):
        r = requests.get('http://otvoreniparlament.rs/aktuelno', headers={'content-type': 'application/json'},
                         params={'page': i})
        if r.text.strip()[-13:] == '{"error":404}':
            json_string = r.text.strip()[:-13]
        data = json.loads(json_string)
        content = data['vesti']['data']
        for obj in content:
            print('id: ', obj['id'])
            print('naslov: ', obj['naslov'])
            print('datum ', obj['datum'])
            opis = obj['opis'].replace('<p>', '').replace('</p>', '').replace('<br />', '').replace('&scaron;', 'š') \
                .replace('<em>', '').replace('</em>', '')
            print('opis: ', opis)
            print()


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


"""
    Task specific functions.
"""


def akt_naslov_list():
    lst = []
    data = get_json('http://otvoreniparlament.rs/akt')
    content = data['akta']
    for obj in content:
        lst.append(obj['naslov'])
    return lst


if __name__ == '__main__':
    pass
