import requests
import json


def get_json(url):
    headers = {'content-type': 'application/json'}
    r = requests.get(url, headers=headers)
    if r.text.strip()[-13:] == '{"error":404}':
        json_string = r.text.strip()[:-13]
    data = json.loads(json_string)
    return data


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


def get_osobe():
    data = get_json('http://otvoreniparlament.rs/osoba')
    content = data['osobe']
    for obj in content:
        print('id: ', obj['id'])
        print('ime: ', obj['ime'])
        print('prezime: ', obj['prezime'])
        print('datum rodjenja', obj['datum_rodjenja'])
        print('pol: ', obj['pol'])
        print('mesto rodjenja: ', obj['mesto_rodjenja'])
        print('profesija: ', obj['profesija'])
        print('biografija: ', obj['biografija'])
        print()
        print()


if __name__ == '__main__':
    get_osobe()
