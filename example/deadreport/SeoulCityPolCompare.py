# -*- coding: utf-8 -*- 
# 서울시 대기오염별 관계 그래프
import numpy as np
import matplotlib.pyplot as plt
from operator import eq
import csv

def analyzePollutionCompare():

    nInputPol1 = 3;
    nInputPol2 = 4;
    
    if (nInputPol1 < 1 or nInputPol1 > 6) or (nInputPol2 < 1 or nInputPol2 > 6) :
        print "비교할 입력 변수는 1~6까지 입니다."
        return 0

    # 2016년 대기오염 평균 csv 파일 읽어오기
    # 연도, 이산화질소농도(ppm), 오존농도(ppm), 일산화탄소농도(ppm), 아황산가스(ppm), 미세먼지(㎍/㎥), 초미세먼지(㎍/㎥)
    pollutionData = [[0 for col in range(0)] for row in range(7)]
    polltutionDatafile = '.\\csv\\SeoulAirpollution.csv'
    with open(polltutionDatafile, 'rt') as f :
        rowData = csv.reader(f, delimiter = ',')
        for colIdx2, data in enumerate(rowData):
            for colIdx1, d in enumerate(data):
               pollutionData[colIdx1].insert(colIdx2, d)
     
    # X축 월별 배열 정보 선언
    month = ['1','2','3','4','5','6','7','8','9','10','11','12']
    
    # 그래프 메인 타이틀 설정
    plt.title('Seoul City and Air Pollution')
    
    # 2016년 대기오염 정보 plot 설정
    plt.plot(month, pollutionData[nInputPol1], 'b-o', label="pollution1")
    plt.xlabel('Month')
    plt.ylabel('Pollution1 Count')
    plt.legend()
    
    ax2 = plt.twinx()
    plt.plot(month, pollutionData[nInputPol2], 'r-s', label="pollution2")
    plt.ylabel('Pollution2 Count')
    plt.legend()
    ax2.yaxis.tick_right()
   
    # 그래프 노출
    plt.show()

if __name__== '__main__':
    analyzePollutionCompare()
