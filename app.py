#Not bu kod benim değil. Bi videoda gördüm. Yapay zeka çalışması. Örnek kalsın diye burada tutuyorum.
#Umarım bi ara bu kütüphaneyi öğrendiğim zamanlar gelecek.

import yfinance as yf 
import datetime
from datetime import date 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

def download_data(op,start_date,end_date):
    df = yf.download(op,start=start_date,end=end_date)
    return df

def model_engine(model,num):
    df  = data[['Close']]
    df['preds'] = df.Close.shift(-num) #bir tahmin sütunu oluşturuyor. Bir sonraki günü predictions sütununa aktarıyor. shift o işe yarıyor.

    # Eksen oluşturma
    x = df.drop(['preds'],axis=1).values
    x = scaler.fit_transform(x)
    x = x[:-num] #num gün öncesi kadar gibi bi anlamı var
    x_forecast = x[-num:] 
    y = df.preds.values
    y = y[:-num]

    #Modeli eğitme ve tahmin ettirme
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=7)
    model.fit(x_train,y_train)
    preds = model.predict(x_test)
    print(f'Tutarlılık oranı şu şekilde tahmin edildi: {r2_score(y_test,preds)}')

    #Tahmini söyletme
    forecasted_pred = model.predict(x_forecast)
    day = 1
    for i in forecasted_pred:
        print(f'{day}. gün için tahmini kapanış değeri: {i}')
        day += 1


stock = 'TUPRS.IS'
today = datetime.date.today() #Bugünü döndürüyor (2024-02-11)
duration = 3000
before = today - datetime.timedelta(days=duration) #yukarıda duration 3000 belirledik. bu kod today'den 3000 gün geri gidiyor.
start_date = before
end_date = today

data = download_data(stock,start_date,end_date)

num=3 #Kaç günlük tahmin yapacaksa
scaler = StandardScaler()
engine = LinearRegression()

model_engine(engine,num)
