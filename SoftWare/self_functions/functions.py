# -*- coding: utf-8 -*-
import random
from math import isnan, isinf

import numpy as np
from scipy.linalg.misc import norm
from scipy.stats import ttest_ind
import scipy.io as sio
from Librarys.skfeature.function.similarity_based import fisher_score
from sklearn.preprocessing import MinMaxScaler

from Librarys.sklearn_lib import *


def load_mat(txtpath):
    data = sio.loadmat(txtpath)
    positive_data = data['positive']
    negative_data = data['negative']
    all_data = np.vstack((positive_data, negative_data))
    all_label = [1] * np.array(positive_data).shape[0] + [0] * np.array(negative_data).shape[0]
    all_label = np.array(all_label)

    temp_index = list(range(all_data.shape[0]))
    random.shuffle(temp_index)
    all_data = all_data[temp_index, :, :, :]
    all_label = all_label[temp_index]

    print('all_data', all_data.shape, 'all_label', all_label.shape)
    return all_data, all_label


def load_txt(txtpath):
    data = np.loadtxt(txtpath, dtype=float)
    return data


def div_label_feature(data, k=0):
    row, col = np.shape(data)

    features = data[:, 1:]

    labels = data[:, k]

    return features, labels


def div_train_test(features,labels,k=1/3):
    num = len(labels)

    indices = [i for i in range(num)]

    train_indices = random.sample(indices, 2 * num / 3)

    test_indices = list(set(indices).difference(set(train_indices)))

    train_data = features[train_indices, :]
    train_label = labels[train_indices]

    test_data = features[test_indices, :]
    test_label = labels[test_indices]

    return train_data,train_label,test_data,test_label


def get_result(test_labels, predict_labels, positive=1, negative=-1):
    print (test_labels)
    print (predict_labels)
    num = len(test_labels)
    right_num = 0
    true_p = 0
    true_n = 0
    false_p = 0
    false_n = 0

    for i in range(len(test_labels)):
        if test_labels[i] == positive and predict_labels[i] == positive:
            right_num += 1
            true_p += 1
        elif test_labels[i] == positive and predict_labels[i] == negative:
            false_n += 1
        elif test_labels[i] == negative and predict_labels[i] == positive:
            false_p += 1
        elif test_labels[i] == negative and predict_labels[i] == negative:
            right_num += 1
            true_n += 1

    accuracy = right_num / float(num)


    print('已得到性能度量')
    return accuracy, true_p, true_n, false_p, false_n


def TTest(data,p = 0.1):
    features, labels = div_label_feature(data)
    row, col = np.shape(features)
    l1 = []
    l2 = []
    index = []
    for i in range(len(labels)):
        if labels[i] == 1:
            l1.append(features[i, :])
        else:
            l2.append(features[i, :])

    for j in range(col):
        [S, p_value] = ttest_ind(np.array(l1).reshape((len(l1), col))[:, j], np.array(l2).reshape((len(l2), col))[:, j])
        if p_value < p:
            index.append(j)


    features = features[:, index]
    index = list(map(lambda x:x+1,index))
    # 这里对index里的每一个元素都加一，才是特征在原始矩阵中的列坐标，第0列是标签
    return np.hstack((labels.reshape(-1, 1), features)), index


def Fisher_score(data, p):
    features, labels = div_label_feature(data=data)
    scores = fisher_score.fisher_score(features, labels)
    scores = scores.tolist()
    f_index = []

    for i in range(len(features)):
        if scores[i] >= p:
            f_index.append(i)

    features = features[:, f_index]
    f_index = list(map(lambda x: x + 1, f_index))
    print(f_index)
    return np.hstack((labels.reshape(-1, 1), features)), f_index


def lasso(data, alpha, loop_num):
    model = Lasso(alpha=alpha)
    features, labels = div_label_feature(data=data)
    row, col = features.shape
    select_num = np.zeros(features.shape[1])
    print('准备进入循环')
    for i in range(loop_num):
        print('loop循环中')
        index = random.sample(list(range(row)), int(row / 3))
        print('index', index)
        model.fit(X=features[index], y=labels[index])
        cur_select = np.array([1 if item != 0 else 0 for item in model.coef_])
        select_num += cur_select

    print('select_num',select_num)

    f_index = []
    num_sort_index = select_num.argsort()[::-1]
    total = sum(select_num)
    threshold = total * 0.8

    p = 0
    cur_total_num = 0
    while p <= len(num_sort_index) and cur_total_num <= threshold:
        cur_total_num += select_num[num_sort_index[p]]
        f_index.append(num_sort_index[p])
        p += 1
    f_index = np.array(sorted(f_index))

    features = features[:, f_index]
    f_index = list(map(lambda x: x + 1, f_index))
    print(f_index)
    return np.hstack((labels.reshape(-1, 1), features)), f_index


def rf_select(data,n_trees,min_split,k_save):
    print('进入rf_select')
    features, labels = div_label_feature(data)

    rf = RandomForestClassifier(n_estimators=n_trees,min_samples_split=min_split)
    rf.fit(X=features,y=labels)

    weights = list(rf.feature_importances_)

    index = list(np.argsort(weights))
    index.reverse()
    # 这里的index中元素为坐标，weights中越大的元素的坐标在index中越靠前

    choose_index = index[:k_save]

    features = features[:, choose_index]

    print(choose_index)
    choose_index = list(map(lambda x: x + 1, choose_index))
    print(choose_index)

    return np.hstack((labels.reshape(-1, 1), features)), choose_index


def Norm(data):
    row, col = np.shape(data)
    for i in range(col):

        if i == 0:
            continue
        # 第一列是类别标签，不能归一化
        flag = False
        for item in data[:, i]:
            if np.isnan(item) or np.isinf(item):
                flag = True
        if flag:
            data[:, i] = float("nan")
        else:
            data[:, i] = data[:, i] / norm(data[:, i])

        return data


def Min_Max(data):
    labels, features = data[:, 1].reshape(-1, 1), data[:, 1:]
    min_max_scaler = MinMaxScaler()
    features = min_max_scaler.fit_transform(features)
    return np.hstack((labels, features))


def Norm_features(data):
    row, col = np.shape(data)
    for i in range(col):

        flag = False
        for item in data[:, i]:
            if np.isnan(item) or np.isinf(item):
                flag = True
        if flag:
            data[:, i] = float("nan")
        else:
            data[:, i] = data[:, i] / norm(data[:, i])

        return data


def replace_nan(data):
    hang, lie = data.shape
    for j in range(lie):
        sum = 0
        count = 0
        for i in range(hang):
            if isnan(data[i, j]) or isinf(data[i, j]):
                print('缺失值坐标', i, j)
            else:
                sum += data[i, j]
                count += 1
        mean = sum / count
        for i in range(hang):
            if isnan(data[i, j]) or isinf(data[i, j]):
                data[i, j] = mean
    return data



