#library json
#untuk parse/memanggil data dari file json 
import json
#library flask
#untuk membuat web service gateway interface
from flask import Flask, render_template, request
#library xml
#untuk membaca atau membuat file xml
import xml.etree.ElementTree as xml
#import time Digunakan untuk meng-import modul time
from datetime import datetime


#untuk membuat Flask instance.
app = Flask(__name__)

#sintak untuk membaca file json
with open('databook.json') as b:
	data = json.load(b)

#meload json dengan nama data seperti diatas
#lalu pada['book'] memaggil nama dict pada json
buku = data['book']

#sintak di bawah untuk sorting
temp = sorted(buku, key=lambda x: (x['judul']))



#list
allbook = []
allpenerbit = []
bukuaraska = []
bukutransidea = []
bukuzahara = []
bukugavamedia = []
bukuindoliterasi = []
bukudivapress = []
bukulaksana = []
bukuliterindo = []
bukustarbooks = []
bukugalangpress = []
bukunoktah = []
bukuscritto = []
bukujavalitera = []
bukukaktus = []
bukusaufa = []
bukuglobalpustaka = []
bukukompas = []
bukutabiyamedia = []
bukumitrapelajar = []
bukubasabasi = []
bukuceklist = []
bukuandioffsite = []
bukumizzan = []
buy=[]

# perulangan untuk mengambil data judul dan penerbit
# data judul akan di simpan pada list allbook
# data penerbit akan disimpan pada list allpenerbit
for x in buku:
	allbook.append(x['judul'])
	allpenerbit.append(x['penerbit'])

#map digunakan untuk menampilkan jumlah total buku secara keseluruhan
mapping = map(lambda x: x, allbook)
ttl = len(list(mapping))

# perulangan untuk mengambil judul buku berdasarkan penerbit
for i in buku:
	a = i['penerbit']
	if a == 'Araska':
		bukuaraska.append(i['judul'])
	elif a == 'Trans Idea':
		bukutransidea.append(i['judul'])
	elif a == 'Zahara':
		bukuzahara.append(i['judul'])
	elif a == 'Gava Media':
		bukugavamedia.append(i['judul'])
	elif a == 'Indoliterasi':
		bukuindoliterasi.append(i['judul'])
	elif a == 'Diva Press':
		bukudivapress.append(i['judul'])
	elif a == 'Laksana':
		bukulaksana.append(i['judul'])
	elif a == 'Literindo':
		bukuliterindo.append(i['judul'])
	elif a == 'Star Books':
		bukustarbooks.append(i['judul'])
	elif a == 'Galang Press':
		bukugalangpress.append(i['judul'])
	elif a == 'Noktah':
		bukunoktah.append(i['judul'])
	elif a == 'Scritto':
		bukuscritto.append(i['judul'])
	elif a == 'Javalitera':
		bukujavalitera.append(i['judul'])
	elif a == 'Kaktus':
		bukukaktus.append(i['judul'])
	elif a == 'Saufa':
		bukusaufa.append(i['judul'])
	elif a == 'Global Pustaka':
		bukuglobalpustaka.append(i['judul'])
	elif a == 'Kompas':
		bukukompas.append(i['judul'])
	elif a == 'Tabiya Media':
		bukutabiyamedia.append(i['judul'])
	elif a == 'Mitra Pelajar':
		bukumitrapelajar.append(i['judul'])
	elif a == 'Basa Basi':
		bukubasabasi.append(i['judul'])
	elif a == 'Ceklist':
		bukuceklist.append(i['judul'])
	elif a == 'Andi Offsite':
		bukuandioffsite.append(i['judul'])
	elif a == 'Mizzan':
		bukumizzan.append(i['judul'])

#fungsi untuk mengfilter judul berdasarkan penerbit
def araska(jdl):
	#mendeklarasi list bukuaraska dengan variabel d
	d  = bukuaraska
	#lalu dicek apakah jdl ada di variabel d
	if(jdl in d):
		# jika jdl ada pada list maka akan bernilai true dan bisa dipanggil pada fungsi filter
		return True
	else:
		# jika tidak ada maka tidak akan dipanggil pada fungsi filter
		return False

def transidea(jdl):
	d  = bukutransidea
	if(jdl in d):
		return True
	else:
		return False

def zahara(jdl):
	d  = bukuzahara
	if(jdl in d):
		return True
	else:
		return False

def gavamedia(jdl):
	d  = bukugavamedia
	if(jdl in d):
		return True
	else:
		return False

def indoliterasi(jdl):
	d  = bukuindoliterasi
	if(jdl in d):
		return True
	else:
		return False

def divapress(jdl):
	d  = bukudivapress
	if(jdl in d):
		return True
	else:
		return False

def laksana(jdl):
	d  = bukulaksana
	if(jdl in d):
		return True
	else:
		return False

def literindo(jdl):
	d  = bukuliterindo
	if(jdl in d):
		return True
	else:
		return False

def starbooks(jdl):
	d  = bukustarbooks
	if(jdl in d):
		return True
	else:
		return False

def galangpress(jdl):
	d  = bukugalangpress
	if(jdl in d):
		return True
	else:
		return False

def noktah(jdl):
	d  = bukunoktah
	if(jdl in d):
		return True
	else:
		return False

def scritto(jdl):
	d  = bukuscritto
	if(jdl in d):
		return True
	else:
		return False

def javalitera(jdl):
	d  = bukujavalitera
	if(jdl in d):
		return True
	else:
		return False

def kaktus(jdl):
	d  = bukukaktus
	if(jdl in d):
		return True
	else:
		return False

def saufa(jdl):
	d  = bukusaufa
	if(jdl in d):
		return True
	else:
		return False

def globalpustaka(jdl):
	d  = bukuglobalpustaka
	if(jdl in d):
		return True
	else:
		return False

def kompas(jdl):
	d  = bukukompas
	if(jdl in d):
		return True
	else:
		return False

def tabiyamedia(jdl):
	d  = bukutabiyamedia
	if(jdl in d):
		return True
	else:
		return False

def mitrapelajar(jdl):
	d  = bukumitrapelajar
	if(jdl in d):
		return True
	else:
		return False

def basabasi(jdl):
	d  = bukubasabasi
	if(jdl in d):
		return True
	else:
		return False

def ceklist(jdl):
	d  = bukuceklist
	if(jdl in d):
		return True
	else:
		return False

def andioffsite(jdl):
	d  = bukuandioffsite
	if(jdl in d):
		return True
	else:
		return False

def mizzan(jdl):
	d  = bukumizzan
	if(jdl in d):
		return True
	else:
		return False

# app route digunakan untuk memberi alamat website
# pada flask ini default hostnya adalah 127.0.0.1 dengan port 5000 atau bisa ditulis 127.0.0.1:5000
# app route di bawah kita bisa menggunakan dua alamat yaitu 127.0.0.1:5000 dan 127.0.0.1:5000/index.html
@app.route("/")
@app.route("/index.html")
def home(): #fungsi untuk index.html
	# jika kita mengakses alamat diatas maka program akan memanggil file index.html pada browser
	# render_template digunakan untuk memanggil file yang berformat html
	# didalalm render_template ada sebuah variabel bernama bk
	# dimana bk itu mendeklarasikan temp yang terdapat pada baris ke 26 dan akan dipanggil pada index.html
	return render_template("index.html", bk = temp, ttl=ttl)

# app route di bawah memiliki alamat 127.0.0.1:5000/filter.html
# pada app route filter ini menggunakan method POST dan GET
@app.route("/filter.html", methods=["POST", "GET"])
def filtering():

	# jdlfilter digunakan untuk memanggil request form pada html yang bernama penerbit
	jdlfilter = request.form.get('penerbit')

	# deklarasi filter judul buku berdasarkan penerbit
	listaraska = filter(araska, allbook)
	listtransidea = filter(transidea, allbook)
	listzahara = filter(zahara, allbook)
	listgavamedia = filter(gavamedia, allbook)
	listindoliterasi = filter(indoliterasi, allbook)
	listdivapress = filter(divapress, allbook)
	listlaksana = filter(laksana, allbook)
	listliterindo = filter(literindo, allbook)
	liststarbooks = filter(starbooks, allbook)
	listgalangpress = filter(galangpress, allbook)
	listnoktah = filter(noktah, allbook)
	listscritto = filter(scritto, allbook)
	listjavalitera = filter(javalitera, allbook)
	listkaktus = filter(kaktus, allbook)
	listsaufa = filter(saufa, allbook)
	listglobalpustaka = filter(globalpustaka, allbook)
	listkompas = filter(kompas, allbook)
	listtabiyamedia = filter(tabiyamedia, allbook)
	listmitrapelajar = filter(mitrapelajar, allbook)
	listbasabasi = filter(basabasi, allbook)
	listceklist = filter(ceklist, allbook)
	listandioffsite = filter(andioffsite, allbook)
	listmizzan = filter(mizzan, allbook)

	# render_template digunakan untuk memanggil file yang bernama filter.html 
	# didalalm render_template terdapat beberapa variabel baru yang memuat variabel deklarasi filter (seperti pada baris ke 306-328)
	# variabel baru pada render_template digunakan untuk dipanggil di htmlnya
	return render_template("filter.html",allp=allpenerbit, 
		t=jdlfilter, lar=listaraska, lti=listtransidea, lz=listzahara, 
		lgm=listgavamedia, lil=listindoliterasi, ldp=listdivapress, 
		lla=listlaksana, llo=listliterindo, lsb=liststarbooks, 
		lgp=listgalangpress, ln=listnoktah, ls=listscritto, 
		ljl=listjavalitera, lk=listkaktus, lsf=listsaufa, 
		lgpa=listglobalpustaka, lkm=listkompas, ltm=listtabiyamedia, 
		lmp=listmitrapelajar, lbb=listbasabasi, lc=listceklist, 
		lao=listandioffsite, lmz=listmizzan)

# app route di bawah memiliki alamat 127.0.0.1:5000/buy.html
# pada app route filter ini menggunakan method POST dan GET
@app.route("/buy.html", methods=["POST","GET"])
def buy():

	# sintak di bawah digunakan untuk
	waktu = datetime.now()
	date = waktu.strftime("%d-%b-%Y, %X")

	# jdeklarasi dibawah digunakan untuk memanggil request form pada html yang bernama idbook, judul, harga, jumlah, total, tunai, kembalian
	idb = request.form.get('idbook')
	getjudul = request.form.get('judul')
	getharga = request.form.get('harga')
	getjumlah = request.form.get('jumlah')
	gettotal = request.form.get('total')
	gettunai = request.form.get('tunai')
	getkembalian = request.form.get('kembalian')

	# sintak dibawah digunakan untuk membuat file xml
	root = xml.Element('starbooks')
	transaksi = xml.Element('transaksi')
	root.append(transaksi)

	subtgl = xml.SubElement(transaksi, "tanggal")
	subtgl.text = date
	subjdl = xml.SubElement(transaksi, "judul")
	subjdl.text = getjudul
	subhrg = xml.SubElement(transaksi, "harga")
	subhrg.text = getharga
	subjml = xml.SubElement(transaksi, "jumlah")
	subjml.text = getjumlah
	subttl = xml.SubElement(transaksi, "total")
	subttl.text = gettotal
	subtni = xml.SubElement(transaksi, "tunai")
	subtni.text = gettunai
	subkbl = xml.SubElement(transaksi, "kembalian")
	subkbl.text = getkembalian

	tree = xml.ElementTree(root)
	# program dibawah digunakan untuk membuat file yang bernama bukti.xml
	with open("bukti.xml","wb") as file:
		tree.write(file)

	# render_template digunakan untuk memanggil file yang bernama buy.html
	# didalam render_template ada sebuah variabel bernama t dan bk dimana t dan bk itu variabel baru 
	# t ini untuk mengambil varibel idb diatas pada baris 353
	# t ini untuk mengambil varibel idb diatas pada baris 26
	return render_template("buy.html", t=idb, bk = temp)

# app route digunakan untuk memberi alamat website 
# pada flask ini default hostnya adalah 127.0.0.1:5000/transaksi.html
@app.route("/transaksi.html") #127.0.0.1:5000/transaksi.html
def transaksi():

	# varibel tree dibawah di gunakan untuk membaca dan memilah isi file bukti.xml
	tree = xml.parse("bukti.xml")
	root = tree.getroot()

	# menampilkan isi data xml menggunakan perulangang
	for y in root.findall("transaksi"):
		tanggal = y.find('tanggal').text
		judul = y.find('judul').text
		harga = y.find('harga').text
		jumlah = y.find('jumlah').text
		total = y.find('total').text
		tunai = y.find('tunai').text
		kembalian = y.find('kembalian').text

	# render_template digunakan untuk memanggil file yang bernama transaksi.html
	# didalam render_template ada beberapa variabel baru bernama tgl, jdl, hrg, jml, ttl, tni, kmbl
	# dimana variabel baru tersebut digunakan untuk mendeklarasikan variabel pada baris 402 sampai 408
	# dan variabel baru tersebut akan dipanggil oleh transaksi.html
	return render_template("transaksi.html", tgl=tanggal, jdl=judul, hrg=harga,
		jml=jumlah, ttl=total, tni=tunai, kmbl=kembalian)

# app roucutte di bawah memiliki alamat 127.0.0.1:5000/tentang.html
@app.route("/tentang.html")
def tentang():
	# render_template digunakan untuk memanggil file yang bernama tentang.html
	return render_template("tentang.html")

if __name__ == "__main__":
	# app run dibawah digunakan untuk menjalankan flasknya dengan mengaktifkan debug
	app.run(debug = True)