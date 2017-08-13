# -*- coding: utf-8 -*- 
# 서울시 대기오염별 관계 그래프 (연속으로 노출하기)
import numpy as np
import math  as mt
from matplotlib import pyplot as plt, font_manager, rc

from operator import eq
import csv
import sys

def analyzeProc():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)

    # 연도별 대기오염 평균 csv 파일 읽어오기
    # 연도, 이산화질소농도(ppm), 오존농도(ppm), 일산화탄소농도(ppm), 아황산가스(ppm), 미세먼지(㎍/㎥)
    bf_date = ''
    yearIdx = 0
    monthIdx = 0
    pollutionData = [[[0 for col in range(0)] for row in range(5)] for row in range(10)]
    polltutionDataFile = 'csv/Airpollution_tot.csv'
    with open(polltutionDataFile, 'rt') as f :
        rowData = csv.reader(f, delimiter = ',')
        for colIdx2, data in enumerate(rowData):
            for colIdx1, value in enumerate(data):
                if colIdx1 == 0 :
                    if eq(bf_date, '') == True :
                        bf_date = value[:4]
                    elif eq(bf_date, value[:4]) == False : # 연도별로 데이터 담기
                        bf_date = value[:4]
                        yearIdx += 1
                        monthIdx = 0
                    continue
                
                # [연도별][오염종류별][오염수치]
                pollutionData[yearIdx][colIdx1-1].insert(monthIdx, float(value))
                
            monthIdx += 1
                
    # 정규화 처리
    # 공식 : (X - min(X') / (max(X') - min(X'))
    for idx1, yearData in enumerate(pollutionData) :
        for idx2, polData in enumerate(yearData):
                minVal = min(polData)
                maxVal = max(polData)
                for idx3, val in enumerate(polData):
                   rangeVal = (maxVal - minVal)
                   pollutionData[idx1][idx2][idx3] = (pollutionData[idx1][idx2][idx3] - minVal) / rangeVal
    
    # 연도별 사망자 csv 파일 읽어오기
    bf_date = ''
    yearIdx = 0
    monthIdx = 0
    deadData = [[0 for col in range(0)] for row in range(10)] 
    deadDataFile = 'csv/DeadData.csv'
    with open(deadDataFile, 'rt') as f :
        rowData = csv.reader(f, delimiter = ',')
        for colIdx2, data in enumerate(rowData):
            for colIdx1, value in enumerate(data):
                if colIdx1 == 0 :
                    if eq(bf_date, '') == True :
                        bf_date = value[:4]
                    elif eq(bf_date, value[:4]) == False : # 연도별로 데이터 담기
                        bf_date = value[:4]
                        yearIdx += 1
                        monthIdx = 0
                    continue
                
                # [연도별][오염종류별][오염수치]
                deadData[yearIdx].insert(monthIdx, float(value))
                
            monthIdx += 1
    
    # 정규화 처리
    # 공식 : (X - min(X') / (max(X') - min(X'))
    for idx1, data in enumerate(deadData):
        minVal = min(data)
        maxVal = max(data)
        for idx2, val in enumerate(data):
           rangeVal = (maxVal - minVal)
           deadData[idx1][idx2] = (deadData[idx1][idx2] - minVal) / rangeVal
    
    
    # 오염 제목 리스트
    polName = ["이산화질소", "오존", "일산화탄소", "아황산가스", "미세먼지"]
       
    # X축 월별 배열 정보 선언
    month = ['1','2','3','4','5','6','7','8','9','10','11','12']
    
    # 그래프 수치 년도
    year = ['2007','2008','2009','2010','2011','2012','2013','2014','2015','2016']
    
    # 대기오염 정보 plot 설정
    f, axarr = plt.subplots(4, 3)

    # 오염 종류 및 연도별 노출
    xIdx = 2
    plotX = 0
    plotY = 0
    for yearIdx in range(0, 10):
        axarr[plotX, plotY].set_title(year[yearIdx])
        axarr[plotX, plotY].plot(month, pollutionData[yearIdx][xIdx], '-o', label=polName[xIdx], color='b')
        axarr[plotX, plotY].plot(month, deadData[yearIdx], 'r-s', label='사망자', color='r')
        axarr[plotX, plotY].set_ylabel("오염도 ")
        axarr[plotX, plotY].legend()

        plotY += 1 

        if (plotY > 2) :
            plotX += 1
            plotY = 0
                 
    # 그래프 노출
    plt.show()

if __name__== '__main__':
    analyzeProc()
