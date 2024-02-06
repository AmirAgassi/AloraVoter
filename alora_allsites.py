import requests, time, random, json, re, threading, csv, traceback, sys
from twocaptcha import TwoCaptcha
solver = TwoCaptcha('your-api-key-here')
global request

def doVotes(mutex,proxy,responsedict):
    global request
    request = requests.session()
    request.trust_env = False

    request.proxies = proxy
    class alora:

        def getVotedSites():
            url = "https://www.alora.io/vote_includes/load.php?id=vote_data"

            payload={}
            headers = {
              'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
              'Accept': 'application/json, text/javascript, */*; q=0.01',
              'X-Requested-With': 'XMLHttpRequest',
              'sec-ch-ua-mobile': '?0',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
              'sec-ch-ua-platform': '"Windows"',
              'Sec-Fetch-Site': 'same-origin',
              'Sec-Fetch-Mode': 'cors',
              'Sec-Fetch-Dest': 'empty',
              'host': 'www.alora.io'
            }

            response = json.loads(request.request("POST", url, headers=headers, data=payload).text)
            voted_sites = {'runelocus':False,'rspslist':False,'moparscape':False,'runelist':False}

            if response['data']['1']:
                voted_sites['runelocus'] = True

            if response['data']['4']:
                voted_sites['rspslist'] = True

            if response['data']['7']:
                voted_sites['moparscape'] = True

            if response['data']['9']:
                voted_sites['runelist'] = True

            return voted_sites


        def getUIDs():
            global request
            request.request("GET","https://www.alora.io/vote")

            url = "https://www.alora.io/vote_includes/load.php?id=stage1"

            payload={}
            headers = {
              'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
              'Accept': 'text/html, */*; q=0.01',
              'X-Requested-With': 'XMLHttpRequest',
              'sec-ch-ua-mobile': '?0',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
              'sec-ch-ua-platform': '"Windows"',
              'Sec-Fetch-Site': 'same-origin',
              'Sec-Fetch-Mode': 'cors',
              'Sec-Fetch-Dest': 'empty'
            }

            response = request.request("GET", url, headers=headers, data=payload).text
            regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
            url = re.findall(regex,response)      
            links = [x[0] for x in url]
            if links:
                links[0] = links[0].split("?id2=")[1]
                links[1] = links[1].split(";id=")[1]
                links[2] = links[2].split("?name=")[1]
                links[3] = links[3].split("/vote/")[1]

                links = {'runelocus':links[0],'rspslist':links[1],'moparscape':links[2],'runelist':links[3]}

                return links
            else:
                return "votecode"



        def getVoteCode():
            return request.request("GET","https://www.alora.io/vote_includes/load.php?id=stage1").text.split('notice-text">')[1].split("</div>")[0]




    class runelocus:

        def submitVote(uid,captcha_answer):
            url = "https://www.runelocus.com/top-rsps-list/alora/vote?callback=" + uid

            payload='callback=' + uid + '&countanswer=' + captcha_answer + '&rf=K3M2S1RkdmRick9aM2R4K0RHbzNLUT09&thedfp=4d02d582637a3c23886d820940c12eec&ua=TGpLdEZxa0JNVlFTbHAwR2Rlc1g0ZllyaUkzTEV3dFQzZlZwb3dZZnU4QStYY3J0QldvdkRlTWVLOGNyVzJWZk1uSmFQOUNMbUN4b3FBTi9CU3QySnVybEc5RDk3STlWN3hVYVhESVNkMmV2VE9tNkdEVjBJRGdtK0N2aERYTDErUUhjNzRyUC9wL0hHOFVkWmMyL01nPT0%3D&vote=Vote%20now&wd=2'
            headers = {
              'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
              'sec-ch-ua-mobile': '?0',
              'sec-ch-ua-platform': '"Windows"',
              'Upgrade-Insecure-Requests': '1',
              'Content-Type': 'application/x-www-form-urlencoded',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
              'Sec-Fetch-Site': 'same-origin',
              'Sec-Fetch-Mode': 'navigate',
              'Sec-Fetch-User': '?1',
              'Sec-Fetch-Dest': 'document',
              'Cookie': 'PHPSESSID=asm1m78ev2pgg71qof6g8mbv1f; helpful_user=abf38d241cef2120d5400707a7d3e444'
            }

            response = request.request("POST", url, headers=headers, data=payload)
            return response.text

        def requestCaptcha():
            url = "https://www.runelocus.com/vote-captcha.php?rnd=" + str(random.randrange(111111, 999999, 6))
            payload={}
            headers = {
              'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
              'sec-ch-ua-mobile': '?0',
              'sec-ch-ua-platform': '"Windows"',
              'Upgrade-Insecure-Requests': '1',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
              'Sec-Fetch-Site': 'none',
              'Sec-Fetch-Mode': 'navigate',
              'Sec-Fetch-User': '?1',
              'Sec-Fetch-Dest': 'document',
              'Cookie': 'PHPSESSID=asm1m78ev2pgg71qof6g8mbv1f; helpful_user=abf38d241cef2120d5400707a7d3e444'
            }

            response = request.request("GET", url, headers=headers, data=payload)
            #with open("C:/Users/Admin/Desktop/captcha" + str(random.randint(1,999999)) + ".jpg", 'wb') as f:
            #    f.write(response.content)


        def voteRunelocus():
            runelocus_uid = alora.getUIDs()['runelocus']

            runelocus.requestCaptcha()

            inc = 1
            good = False
            while True:
                responsedict[mutex] = "runelocus 3/3 [" + str(inc) + "]"
                if inc > 5:
                    pass
                resp = runelocus.submitVote(runelocus_uid,str(inc))
                if "incorrect" in resp.lower():
                    pass
                    inc+=1
                elif "you have already voted for this server in the past 12 hours." in resp.lower():
                    pass
                    break
                else:
                    pass
                    good = True
                    break
            if good:
                pass
                '''
                time.sleep(3)
                if alora.getVotedSites()['runelocus']:
                    print("Vote completed.")
                else:
                    print("Vote didn't register? ")'''



    class rspslist:
        global request
        def getUID():
            rspslist_uid = alora.getUIDs()['rspslist']
            pass
            return rspslist_uid
        def getRecaptchaPage(rspslist_uid):
            global request

            while True:
                pass
                url = "https://www.rsps-list.com/index.php?a=in&u=alora&id=" + rspslist_uid

                payload={}
                headers = {
                  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                  'accept-encoding': 'gzip, deflate, br',
                  'accept-language': 'en-US,en;q=0.9',
                  'cache-control': 'max-age=0',
                  'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
                  'sec-ch-ua-mobile': '?0',
                  'sec-ch-ua-platform': '"Windows"',
                  'sec-fetch-dest': 'document',
                  'sec-fetch-mode': 'navigate',
                  'sec-fetch-site': 'none',
                  'sec-fetch-user': '?1',
                  'upgrade-insecure-requests': '1',
                  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
                }
                response = request.request("GET", url, headers=headers, data=payload)

                if '"g-recaptcha d-inline-block mx-auto" data-sitekey="6LeUNQsUAAAAAMptmCCMmLVNQCm5Ll7PvSD4Qw-k"' in response.text:
                    pass
                    return response.text.split('<input type="hidden" name="sid" value="')[1].split('">')[0], response.cookies
                    break
                time.sleep(0.5)
        def getCaptchaPage(rspslist_uid):

            while True:
                url = "https://www.rsps-list.com/index.php?a=in&u=alora&id=" + rspslist_uid

                payload={}
                headers = {
                  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                  'accept-encoding': 'gzip, deflate, br',
                  'accept-language': 'en-US,en;q=0.9',
                  'cache-control': 'max-age=0',
                  'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
                  'sec-ch-ua-mobile': '?0',
                  'sec-ch-ua-platform': '"Windows"',
                  'sec-fetch-dest': 'document',
                  'sec-fetch-mode': 'navigate',
                  'sec-fetch-site': 'none',
                  'sec-fetch-user': '?1',
                  'upgrade-insecure-requests': '1',
                  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
                }

                response = request.request("GET", url, headers=headers, data=payload).text
                if 'id="captcha-image"' in response.r:
                    pass
                    return response.split('<input type="hidden" name="sid" value="')[1].split('">')[0]
                    break

        def downloadCaptcha(rspslist_uid):
            url = "https://www.rsps-list.com/captcha.php?sid=" + rspslist_uid

            payload={}
            headers = {
              'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
              'accept-encoding': 'gzip, deflate, br',
              'accept-language': 'en-US,en;q=0.9',
              'referer': 'https://www.rsps-list.com/index.php?a=in&u=alora&id=' + rspslist_uid,
              'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
              'sec-ch-ua-mobile': '?0',
              'sec-ch-ua-platform': '"Windows"',
              'sec-fetch-dest': 'image',
              'sec-fetch-mode': 'no-cors',
              'sec-fetch-site': 'same-origin',
              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
            }

            response = request.request("GET", url, headers=headers, data=payload)
            with open("C:/Users/Admin/Desktop/captcha" + str(random.randint(1,999999)) + ".jpg", 'wb') as f:
                f.write(response.content)


        def submitVote(rspslist_uid,sid,captcha_response):
            url = "https://www.rsps-list.com/index.php?a=in&u=alora&id=" + rspslist_uid

            payload='captcha=' + captcha_response + '&sid=' + sid
            headers = {
              'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
              'sec-ch-ua-mobile': '?0',
              'sec-ch-ua-platform': '"Windows"',
              'Upgrade-Insecure-Requests': '1',
              'Content-Type': 'application/x-www-form-urlencoded',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
              'Sec-Fetch-Site': 'same-origin',
              'Sec-Fetch-Mode': 'navigate',
              'Sec-Fetch-User': '?1',
              'Sec-Fetch-Dest': 'document'
            }

            response = request.request("POST", url, headers=headers, data=payload)

            return response


        def submitRecaptchaVote(rspslist_uid,sid,cookies,captcha_response):
            global request
            url = "https://www.rsps-list.com/index.php?a=in&u=alora&id=" + rspslist_uid

            payload='g-recaptcha-response=' + captcha_response + '&sid=' + sid
            headers = {
              'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
              'sec-ch-ua-mobile': '?0',
              'sec-ch-ua-platform': '"Windows"',
              'Upgrade-Insecure-Requests': '1',
              'Content-Type': 'application/x-www-form-urlencoded',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
              'Sec-Fetch-Site': 'same-origin',
              'Sec-Fetch-Mode': 'navigate',
              'Sec-Fetch-User': '?1',
              'Sec-Fetch-Dest': 'document'
            }

            response = request.request("POST", url, headers=headers, cookies=cookies, data=payload)

            return response

        def voteRspslist():
            global request
            rspslist_uid = rspslist.getUID()
            sid,cookies = rspslist.getRecaptchaPage(rspslist_uid)

            if not 1==1:
                pass
            else:
                result = solver.recaptcha(
                        sitekey='6LeUNQsUAAAAAMptmCCMmLVNQCm5Ll7PvSD4Qw-k',
                        url="https://www.rsps-list.com/index.php",
                    )

                code = result['code']
                resp = rspslist.submitRecaptchaVote(rspslist_uid,sid,cookies,code)
                if resp.status_code == 200:
                    pass
                    '''
                    voted=False
                    for i in range(6):
                        if alora.getVotedSites()['rspslist']:
                            print("Vote Confirmed.")
                            voted = True
                            break
                        time.sleep(1)
                    if not voted:
                        print("Unable to confirm vote?")'''
                else:
                    responsedict[mutex] = "maybe f-a-iled (rspslist)"



    class moparscape:
        global request

        def getToken(uid):
            global request
            url = "https://www.moparscape.org/rsps-list/server/Alora?name=" + uid

            payload={}
            headers = {
              'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
              'sec-ch-ua-mobile': '?0',
              'sec-ch-ua-platform': '"Windows"',
              'Upgrade-Insecure-Requests': '1',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
              'Sec-Fetch-Site': 'none',
              'Sec-Fetch-Mode': 'navigate',
              'Sec-Fetch-User': '?1',
              'Sec-Fetch-Dest': 'document'
            }

            response = request.request("GET", url, headers=headers, data=payload)

            return response.text.split('<meta name="csrf-token" content="')[1].split('" />')[0], response.cookies


        def submitVote(uid,token,cookies,captcha):
            global request
            url = "https://www.moparscape.org/server/vote/Alora"

            payload='_token=' + token + '&g-recaptcha-response=' + captcha + '&username=' + uid
            headers = {
              'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
              'sec-ch-ua-mobile': '?0',
              'sec-ch-ua-platform': '"Windows"',
              'Upgrade-Insecure-Requests': '1',
              'Content-Type': 'application/x-www-form-urlencoded',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
              'Sec-Fetch-Site': 'same-origin',
              'Sec-Fetch-Mode': 'navigate',
              'Sec-Fetch-User': '?1',
              'Sec-Fetch-Dest': 'document'
            }

            response = request.request("POST", url, headers=headers, cookies=cookies, data=payload)

            return response

        def voteMoparscape():
            global request
            moparscape_uid = alora.getUIDs()['moparscape']
            token,cookies = moparscape.getToken(moparscape_uid)

            result = solver.recaptcha(
                    sitekey='6LclzxMUAAAAAJkbpofiE95kkDC3xgNRJHPPRi32',
                    url="https://www.moparscape.org/rsps-list/server/Alora",
                )

            code = result['code']
            resp = moparscape.submitVote(moparscape_uid,token,cookies,code)
            if "Your vote has been saved!" in resp.text:
                voted=False
                '''
                for i in range(6):
                    if alora.getVotedSites()['moparscape']:
                        print("Vote Confirmed.")
                        voted = True
                        break
                    time.sleep(1)
                if not voted:
                    print("Unable to confirm vote?")'''
            else:
                pass




    class runelist:
        global request

        def getKeys(uid):

            url = "https://runelist.io/toplist/server/197/vote/" + uid

            payload={}
            headers = {
              'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
              'sec-ch-ua-mobile': '?0',
              'sec-ch-ua-platform': '"Windows"',
              'Upgrade-Insecure-Requests': '1',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
              'Sec-Fetch-Site': 'cross-site',
              'Sec-Fetch-Mode': 'navigate',
              'Sec-Fetch-User': '?1',
              'Sec-Fetch-Dest': 'document'
            }


            response = request.request("GET", url, headers=headers, data=payload)
            cookies = response.cookies

            formsubmitted = response.text.split('<input type="hidden" name="form_197_submitted" value="')[1].split('">')[0]
            csrfkey = response.text.split('<input type="hidden" name="csrfKey" value="')[1].split('">')[0]
            captchafield = response.text.split('<input type="hidden" name="captcha_field" value="')[1].split('">')[0]
            incentive = response.text.split('<input type="hidden" name="incentive" value="')[1].split('">')[0]
            maxfilesize = response.text.split('<input type="hidden" name="MAX_FILE_SIZE" value="')[1].split('">')[0]
            plupload = response.text.split('<input type="hidden" name="plupload" value="')[1].split('">')[0]


            return formsubmitted, csrfkey, captchafield, incentive, maxfilesize, plupload, cookies





        def submitVote(moparscape_uid,formsubmitted, csrfkey, captchafield, incentive, maxfilesize, plupload, cookies, code):
            global request
            url = "https://runelist.io/toplist/server/197/vote/" + moparscape_uid
            data = """------WebKitFormBoundaryg5VNeIECAvsyIDTk
Content-Disposition: form-data; name="form_197_submitted"

1
------WebKitFormBoundaryg5VNeIECAvsyIDTk
Content-Disposition: form-data; name="csrfKey"

""" + csrfkey + """
------WebKitFormBoundaryg5VNeIECAvsyIDTk
Content-Disposition: form-data; name="captcha_field"

1
------WebKitFormBoundaryg5VNeIECAvsyIDTk
Content-Disposition: form-data; name="incentive"

""" + moparscape_uid + """
------WebKitFormBoundaryg5VNeIECAvsyIDTk
Content-Disposition: form-data; name="MAX_FILE_SIZE"

7340032
------WebKitFormBoundaryg5VNeIECAvsyIDTk
Content-Disposition: form-data; name="plupload"

""" + plupload + """
------WebKitFormBoundaryg5VNeIECAvsyIDTk
Content-Disposition: form-data; name="g-recaptcha-response"

""" + code + """
------WebKitFormBoundaryg5VNeIECAvsyIDTk
Content-Disposition: form-data; name="h-captcha-response"

""" + code + """
------WebKitFormBoundaryg5VNeIECAvsyIDTk--"""


            files=[

            ]
            headers = {
                'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
                  'sec-ch-ua-mobile': '?0',
                  'sec-ch-ua-platform': '"Windows"',
                  'Upgrade-Insecure-Requests': '1',
                  'Accept-Language': 'en-US,en;q=0.9',
                  'Cache-Control': 'max-age=0',
                  'Origin': 'https://runelist.io',
                  'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryg5VNeIECAvsyIDTk',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
                  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                  'Sec-Fetch-Site': 'same-origin',
                  'Sec-Fetch-Mode': 'navigate',
                  'Sec-Fetch-User': '?1',
                  'Sec-Fetch-Dest': 'document',
                  "Referer": "https://runelist.io/toplist/server/197/vote/" + moparscape_uid,
                  'Cookie': 'rlforum_IPSSessionFront=' + cookies
            }

            response = request.request("POST", url, headers=headers, data=data)
            return response.text


        def voteRunelist():
            runelist_uid = alora.getUIDs()
            if runelist_uid == "votecode":
                print("Banned IP")
                responsedict[mutex] = "bannedip"
                sys.exit()
            else:
                runelist_uid = runelist_uid['runelist']
            if "votecode" not in runelist_uid:
                formsubmitted, csrfkey, captchafield, incentive, maxfilesize, plupload, cookies = runelist.getKeys(runelist_uid)
                cookies = cookies['rlforum_IPSSessionFront']
                result = solver.hcaptcha(
                        sitekey='3c899147-81d3-4ea9-8b5d-b925c7182965',
                        url="https://runelist.io/toplist/server/197/vote/" + runelist_uid,
                    )
                #result = {'code':'1'}
                code = result['code']
                time.sleep(10)
                resp = runelist.submitVote(runelist_uid, formsubmitted, csrfkey, captchafield, incentive, maxfilesize, plupload, cookies, code)
                if "has been added" in resp:#if "did not pass the security" not in resp:

                    '''
                    voted=False
                    for i in range(6):
                        if alora.getVotedSites()['runelist']:
                            print("Vote Confirmed.")
                            voted = True
                            break
                        time.sleep(1)
                    if not voted:
                        print("Unable to confirm vote?")
                        '''
                else:
                    pass
            else:
                pass
    try:
        print(proxy)
        print("Voted sites:",alora.getVotedSites())
        responsedict[mutex] = "runelist 1/3"
        runelist.voteRunelist()
        responsedict[mutex] = "moparscape 2/3"
        #rspslist.voteRspslist()
        moparscape.voteMoparscape()
        responsedict[mutex] = "runelocus 3/3"
        runelocus.voteRunelocus()
        time.sleep(1)
        votecode = alora.getVoteCode()
        responsedict[mutex] = "done " + votecode
        print("Voted sites (after finish):",alora.getVotedSites())
        return votecode
    except Exception as e:
        print("ERROR:",e)
        print(traceback.format_exc())
        print("Voted sites (after fail):",alora.getVotedSites())
        print("Voted code:",alora.getVoteCode())
        responsedict[mutex] = "failed"
        return

with open("C:/Users/Admin/Desktop/proxies.txt") as f:
    proxies_full = f.read().splitlines() 
proxies = proxies_full.copy()
threads = 20
responsedict = {}
threadslist = []
for i in range(threads):
    responsedict[i] = "waiting"
    if len(proxies) > 0:
        ex = proxies.pop()
    else:
        proxies = proxies.copy()
        ex = proxies.pop()
    proxy = {
    "http": "http://" + ex,
    "https": "http://" + ex
    }
    print(ex)
    threadslist.append(threading.Thread(target=doVotes, args=(i,proxy,responsedict)))
    threadslist[i].start()
#test.start()
stats = [0,0,0]
while True:
    time.sleep(1)
    print(responsedict,"    ",stats)
    for i in range(threads):
        if "done" in responsedict[i]:
            print("Done")
            code = responsedict[i].split()[1]
            with open('alora_authcodes.csv', 'a', newline="") as f_object:
                writer_object = csv.writer(f_object)
                writer_object.writerow([code])
                f_object.close()
            if len(proxies) > 0:
                ex = proxies.pop()
            else:
                proxies = proxies.copy()
                ex = proxies.pop()
            proxy = {
            "http": "http://" + ex,
            "https": "http://" + ex
            }
            responsedict[i] = "waiting"
            threadslist[i] = threading.Thread(target=doVotes, args=(i,proxy,responsedict))
            threadslist[i].start()
            stats[0]+=1
        elif "failed" in responsedict[i]:
            responsedict[i] = "waiting"
            print("Failed")
            if len(proxies) > 0:
                ex = proxies.pop()
            else:
                proxies = proxies.copy()
                ex = proxies.pop()
            proxy = {
            "http": "http://" + ex,
            "https": "http://" + ex
            }
            threadslist[i] = threading.Thread(target=doVotes, args=(i,proxy,responsedict))
            #=threadslist[i].start()
            stats[1]+=1
        elif "bannedip" in responsedict[i]:
            responsedict[i] = "waiting"
            print("Banned IP")
            if len(proxies) > 0:
                ex = proxies.pop()
            else:
                proxies = proxies.copy()
                ex = proxies.pop()
            proxy = {
            "http": "http://" + ex,
            "https": "http://" + ex
            }
            threadslist[i] = threading.Thread(target=doVotes, args=(i,proxy,responsedict))
            threadslist[i].start()
            stats[2]+=1
#doVotes(proxy,proxy)