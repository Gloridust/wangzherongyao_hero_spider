import requests
import os

def download_wzry():
    url = "https://pvp.qq.com/web201605/js/herolist.json"
    hero_list = requests.get(url)
    hero_list_json = hero_list.json()
    
    hero_name = [hero['cname'] for hero in hero_list_json]
    hero_number = [hero['ename'] for hero in hero_list_json]

    for i, j in enumerate(hero_number):
        # 创建文件夹
        os.makedirs(f"./wzry/{hero_name[i]}", exist_ok=True)

        for k in range(10):
            # 拼接URL
            one_hero_link = f"http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{j}/{j}-bigskin-{k}.jpg"
            # 请求URL
            im = requests.get(one_hero_link)
            if im.status_code == 200:
                # 写入文件
                open(f"./wzry/{hero_name[i]}/{hero_name[i]}{k}.jpg", 'wb').write(im.content)
                print(f">>{hero_name[i]}/{hero_name[i]}{k}.jpg Saved")


if __name__ == "__main__":
    download_wzry()