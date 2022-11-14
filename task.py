import requests
token = ''
hero = {}
#HERO
def smart_hero(*name_hero):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    resp = requests.get(url)
    count = 0
    for i in resp.json():
        if i['name'] in name_hero:
            hero[i['name']] = i['powerstats']['intelligence']
            count += 1
    smart_guy = max(hero, key=hero.get)
    print(f"Самый умный герой {smart_guy}, у него {hero[smart_guy]} интелекта!!!")
    return
#YANDEX
def get_headers():
    return{
        'Content-Type':'application/json',
        'Authorization':f'OAuth {token}'
    }
def get_link(disk_file_path: str):
    upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
    headers = get_headers()
    params = {"path": disk_file_path, "overwrite": "true"}
    response = requests.get(upload_url, headers=headers, params=params)
    print (response.json())
    return response.json()    
def upload(file_path: str, filename:str):
    href = get_link(disk_file_path=file_path).get("href", "")
    response = requests.put(href, data=open(filename, 'rb'))
    if response.status_code == 201:
        print("УСПЕХ!")
   
if __name__ == '__main__':
    smart_hero('Hulk', 'Captain America', 'Thanos')

    file_puth = input("Введите путь до файла(включая имя файла и расширение): ")
    name_file = file_puth.split('/')
    upload(f"/{name_file[-1]}", file_puth)