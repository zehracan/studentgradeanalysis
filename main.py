import pandas as pd

cols =['no','isim','soyisim','vize','final']
df=pd.DataFrame(columns=cols)
keep="y"

while keep == "y":
        print("Kayıt giriniz:")
        data = input().split(' ')
        for i in range (0,len(data),5):
            df = df.append(pd.Series(data[i:i+5], index=cols),ignore_index=True)
        print("yeni kayıt girmek istiyor musunuz?(y/n)")
        keep=input()
        df['ortalama'] = (df['vize'].astype(str).astype(float)+df['final'].astype(str).astype(float))/2

def letter_grading(col):
    if col < 50:
        harf_notu =  'F'
    elif col < 60:
        harf_notu =  'D'
    elif col < 70:
        harf_notu = 'C'
    elif col < 80:
        harf_notu = 'B'
    elif col < 90:
        harf_notu = 'A'
    else:
        harf_notu = 'A+'
    return harf_notu

def pass_lesson(harf_notu):
    if harf_notu == 'D' or harf_notu == 'F':
        return "kaldı"
    else:
        return "geçti"

df["harf_notu"] = df['ortalama'].apply(letter_grading)
df["durum"] = df["harf_notu"].apply(pass_lesson)

print(df.head())

df.to_excel(r'C:\Users\asus\Desktop\studentgrade.xlsx',index=False)

