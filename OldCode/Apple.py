import requests
import time
import random

Phone = 1
n = 0
while Phone == 1:
    url = 'https://www.apple.com.cn/shop/pickup-message-recommendations?mt=compact&searchNearby=true&store=R705&product=MLHC3CH/A'
    header = {
        "cookie": "dssf=1; dssid2=d75fafa6-130e-4b36-8d98-220e9816872f; as_sfa=Mnxjbnxjbnx8emhfQ058Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; as_uct=2; "
                  "rtsid=%7BCN%3D%7Bt%3Da%3Bi%3DR705%3B%7D%3B%7D; "
                  "as_loc=dbc3164bb04ad69b5174b98c19dcefd4c2309f4c76e5cc64c475e64d8d8ec1c0f3ae1e3be778d60c541744b2b8e786f7d631a3061465e9adc4e987d2bdbca9ccdeb6fe0acb73aa1a8dfac9e003a6ea20024c08aec39f1a68df8e8192368635c554f79c96b17b75761feeb1465c6fc6d786ee37fdfd19bf7798bfe0c220c4f5d5; "
                  "geo=CN; at_check=true; s_cc=true; "
                  "as_pcts=SwHGZG9mibvzF:+ypU+rhVe5eoqt7f48WXFAC1PzDk77DWVM7L-YSTXC0NTY98CAeby9IiVsPdroebXR4qDnZsgjBRxJKX-vJpi2Ofu3HLSem3vYZ0xU:6Iq9e9; "
                  "dslang=CN-ZH; site=CHN; as_cn=~dexExQtLmAda6gCGPZPJaJstLZFkWUikyN8n4nikHZU=; as_dc=nc; "
                  "acn01=5PqtDNGTRL5gcIEfboIbhb5/gmyy40AmdFPMc1ezwXpPigAHdPJatWlX; "
                  "as_disa=AAAjAAABMfIPJN70lS-ae8rzLLR3gyI1bE6_I7hBVY8weiezWLEAAgGXTJBo5cmact2egDs8ardFgiEdb1Y1sBa1goepZOoyXQ==; "
                  "as_rec=f80c6675e6ba4c57b096f7a6fb35da21b9931f3760b45d892baa6d2c50a8dd52ad7b90e9f42b86f068381e6b9a8721a8f960ecdb4e5c822417952d654fc1501bfe4baa68ea085d8e8be5d0b2cf3eca0f; "
                  "as_ltn_cn=AAQEAMCVfG-aLLSg3WwHkmqV3M6w4qkji_HmQSdIiSGc7tR-VUe4c26VeuELC7Pkmeiq31BT6JSR_iSAZvLBXfm7qZ549MinjkA; s_fid=24FAE4D4C706E28C-0ADA4C90A290AA50; "
                  "s_sq=appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Diphone%252520-%252520index%25252Ftab%252520%252528cn%252529%2526link%253Dbuy%252520iphone%25252013%252520pro%252520-%252520%25252Fcn%25252Fshop%25252Fgoto%25252Fbuy_iphone%25252Fiphone_13_pro%252520-%252520hero%252520-%252520iphone%25252013%252520pro%2526region%253Dhero%252520-%252520iphone%25252013%252520pro%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Diphone%252520-%252520index%25252Ftab%252520%252528cn%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com.cn%25252Fcn%25252Fshop%25252Fgoto%25252Fbuy_iphone%25252Fiphone_13_pro%2526ot%253DA; as_atb=1.0|MjAyMS0wOS0yNSAwOTowMTo0MA|05fc3aa7f73336978a80659056d5cce9ec905c61; mbox=session#2fca11d21e724c2188f6393c555c658b#1632630736|PC#2fca11d21e724c2188f6393c555c658b.32_0#1632630705"
    }
    r = requests.get(url=url, headers=header)

    text = r.json()['body']['PickupMessage']['notAvailableNearby']
    texts = str(text)
    text1 = texts[0:5]
    text2 = texts[10:]
    num = (r.json()['body']['PickupMessage']['storesCount'])
    nums = str(num)
    numss = nums[0:2]
    text3 = texts[14:18]
    n = n +1

    if text3 == '今日无货':

        timetext = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print(text1 + numss + text2 + timetext)

    else:

        Phone = 2
        requests.post(url=' https://maker.ifttt.com/trigger/iphone13/with/key/cNJnZXBLjJK_fneljUa4vP')
        print('有货啦!!!!!')

    sleeptime = random.choice(range(20))

    print(f'这是第{n}次尝试')

    print('本次休息了'+str(sleeptime)+'秒~~')

    time.sleep(sleeptime)

    # print(r.json()['body']['noSimilarModelsText'])