import requests
dwurl = 'https://officecdn-microsoft-com.akamaized.net/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Office_16.39.20071300_Installer.pkg'
r = requests.get(url=dwurl)
with open('office.pkg', "wb") as f:
    # 这样才能保存到本地
    f.write(r.content)
f.close()