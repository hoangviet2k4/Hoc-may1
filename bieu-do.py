import pandas as pd
import matplotlib.pyplot as plt

excel_file = r"D:\Học máy\austin_weather.xlsx"
df = pd.read_excel(excel_file)
print(df)


thang1_2014 = df.head(30)
print(thang1_2014)


#### Biểu đồ cột
plt.figure(figsize=(10, 6))
plt.bar(thang1_2014['Date'], thang1_2014['TempHighF'], label='TemHighF', color='red')
plt.bar(thang1_2014['Date'], thang1_2014['TempLowF'], label='TempLowF', color='blue')
plt.xlabel('Ngay Thang Nam')
plt.ylabel('Nhiet Do (°F)')
plt.title('Biểu đồ nhiệt độ tháng 1/2014')
plt.legend()
plt.show()


####Biểu đồ đường
plt.figure(figsize=(10, 6))
plt.plot(thang1_2014['Date'], thang1_2014['DewPointHighF'], label='DewPointHighF', color='red')
plt.plot(thang1_2014['Date'], thang1_2014['DewPointAvgF'], label='DewPointAvgF', color='green')
plt.plot(thang1_2014['Date'], thang1_2014['DewPointLowF'], label='DewPointLowF', color='orange')
plt.xlabel('Thời gian')
plt.ylabel('Diem Suong độ F')
plt.title('Biên động điểm sương tháng 1/2014')
plt.legend()
plt.show()



