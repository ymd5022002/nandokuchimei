import datetime

#設定
read_filename = 'nandoku.txt'       #読み込むファイル名を指定
pref = '青森県'                      #県名
url_text ='東北地方の難読地名一覧'      #wikiのURLのあとの日本語

#出典URLの取得
url1 ='https://ja.wikipedia.org/wiki/'
url2 = str(url_text.encode('utf-8')).replace("b'","").replace("'","").replace("\\x","%").upper()
url3 = str(pref.encode('utf-8')).replace("b'","").replace("'","").replace("\\x","%").upper()

url = url1 + url2 + '#' + url3

#日付の取得
today1= datetime.date.today()
today2= "{0:%Y/%m/%d}".format(today1)

#データ整形
print(f'{read_filename}から読み込み！')
text = open(read_filename,'r')

s = ''

for tt in text:
    t = tt.replace(" ","").replace("　","")
    mojisuu = len(t)       #文字数
    pos_bra = t.find('（')  #'（'の位置
    pos_ket = t.find('）')  #'）'の位置
    pos_hifen = t.find('-') #'-'の位置 

    # 難読地名の切り出し
    nandoku_chimei = t[0: pos_bra]

    #よみ の切り出し
    yomi = t[pos_bra+1: pos_ket]

    #地名の切り出し
    chimei = pref + t[pos_hifen + 1: mojisuu-1] + nandoku_chimei

    #データ生成
    s += f'{nandoku_chimei},{yomi},{chimei},,{url},{today2},{pref}\n'

# ファイル生成・データの書き込み
write_filename = f'nandoku_{pref}.csv'
f = open(write_filename, 'w')
n = f.write(s)
print(s)
print(f'{write_filename} に書き込み！')
f.close()

