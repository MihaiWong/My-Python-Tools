# -*- coding: utf-8 -*-
import csv
import numpy as np
import os
import pandas as pd
import re

"""
1.遍历读取文件夹
2.读取Excel， 分为两类，汇总
日期，时间，数据
"""


def read_dir(path):
    """
    文件路径获取
    :return:
    """
    dir_list = []
    # 文件夹目录
    # path = r'C:\Users\MC\Desktop\sampleData'
    # 文件夹下所有文件名称
    for root, dirs, files in os.walk(path):
        for i, file in enumerate(files):
            temp = os.path.join(root, file)
            if '2017' in temp or '2016' in temp:
                dir_list.append(temp)
    return dir_list


def get_date_time(lista, listb):
    new_list = []
    for i in range(0, len(lista)):
        temp = str(lista[i]) + ' ' + str(listb[i])
        new_list.append(temp)
    return new_list


# 获取表头
def get_csv_head(path):

    with open(path, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
    return headers


# 数据装配
def data_assembly(sampling_date, sampling_time, sampling_data, sampling_coding,
                  sampling_name, production_system_name):
    sampling_date_time = get_date_time(sampling_date, sampling_time)  # 日期时间

    # sampling_data = ''  # 数据 可为空值
    # sampling_coding = ''  # 编码 可为空值
    # sampling_name = ''  # 名称 可为空值
    # production_system_name = ''  # 系统名称
    new_df = {'日期': sampling_date,
              '时间': sampling_time,
              '日期时间': sampling_date_time,
              '数据': sampling_data,
              '编码': sampling_coding,
              '名称': sampling_name,
              '系统名称': production_system_name
              }
    return new_df


def opera_csv(path):
    head = get_csv_head(path)
    print(len(head))
    index = 0
    name = ''
    sampling_date = ''
    sampling_time = ''
    with open(path) as fp:
        obj = pd.read_csv(fp)
        numpy_matrix = obj.as_matrix()
    for i in range(0, len(head) - 1):
        if i % 4 == 0:
            name = numpy_matrix[:, i][0]
            sampling_dates = numpy_matrix[:, i][1:]
            for j, sam in enumerate(sampling_dates):
                if '2015/12' not in sam:
                    print(j, sam)
                    index = j
                    break
            sampling_date = numpy_matrix[:, i][index + 1:]
        if i % 4 == 1:
            sampling_time = numpy_matrix[:, i][index + 1:]
        if i % 4 == 3:
            sampling_data = numpy_matrix[:, i][index + 1:]
            sampling_coding = [head[i - 3]] * len(sampling_date)
            sampling_name = [name] * len(sampling_date)
            if '高' in path:
                production_system_name = ['高'] * len(sampling_date)
            else:
                production_system_name = ['低'] * len(sampling_date)
            data = data_assembly(sampling_date, sampling_time, sampling_data,
                                 sampling_coding, sampling_name, production_system_name)

            df_temp = pd.DataFrame(data)

            # columns = ['日期', '时间', '日期时间', '数据', '编码', '名称', '系统名称']
            df_temp.to_csv('test.csv', mode='a', encoding='utf_8_sig', header=True)
            df = pd.read_csv('test.csv')

            df_end = df[(df_temp['日期'].notnull())]

            # 将赋值清空
            index = ''
            name = ''
            sampling_date = ''
            sampling_time = ''
            # 固定列顺序
            columns = ['日期', '时间', '日期时间', '数据', '编码', '名称', '系统名称']
            df_end.to_csv('data.csv', mode='a', encoding='utf_8_sig', header=True, columns=columns)

            os.remove('test.csv')
    return 'ok'


def dispatch(path):
    """
    运行程序，在程序目录下生成 text.csv
    :param path: 文件夾所在目錄
    :return: ok
    """
    path_list = read_dir(path)
    for plist in path_list:
        status = opera_csv(plist)
        if status == 'ok':
            continue
        else:
            return 'error'
    return 'ok'


if __name__ == '__main__':
    # x = read_dir()
    # for s in x:
    #     print(s)
    # 输入文件夹地址
    dispatch('C:/Users/MC/Desktop/sampleData')
