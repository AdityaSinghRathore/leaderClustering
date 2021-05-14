"""
Implementation of Leader Clustering inspired by https://sigir-ecom.github.io/ecom2018/ecom18Papers/paper8.pdf
Creatred By: adipunchh, sjeet-lab
"""

from nlp_utils.distances import lev, dmeta

def _find_leaders(data: list, threshold: int = 3) -> list:
    # p = data
    ldrpat = []
    ldrpat.append(data[0])
    no_of_leaders = 1

    for i in range(len(data)-1):
        nldr = no_of_leaders
        for j in range(no_of_leaders):
            # TODO: Define lev distance and dmeta
            if (lev.get_raw_score(data[i],ldrpat[j]) > threshold) & \
                (dmeta.phonetics(data[i])[0]!=dmeta.phonetics(ldrpat[j])[0]):
                
                no_of_leaders += 1
                ldrpat.append(data[i])
                break

            else:
                continue
    
    return ldrpat

def _cluster_criterion(leader: str, data: list, threshold: int = 3) -> list:
    cluster = list()
    for data_point in data:
        if (lev.get_raw_score(data_point, leader) < threshold) & \
            (dmeta.phonetics(data_point)[0]==dmeta.phonetics(leader)):
            cluster.append()

    return cluster


def leader_cluster(data: list, threshold: int = 3) -> dict:
    clusters = {}

    leaders = _find_leaders(data, threshold)
    for i in leaders:
        clusters[i] = _cluster_criterion(i, data, threshold)

    return clusters
