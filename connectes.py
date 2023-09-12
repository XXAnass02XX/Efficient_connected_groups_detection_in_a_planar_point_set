#!/usr/bin/env python3
"""
compute sizes of all connected components.
sort and display.
"""

from math import sqrt
from sys import argv
from point import Point
from quadrant import Quadrant
from math import floor
def load_instance(filename):
    """
    loads .pts file.
    returns distance limit and points.
    """
    with open(filename, "r") as instance_file:
        lines = iter(instance_file)
        distance = float(next(lines))
        points = [Point([float(f) for f in l.split(",")]) for l in lines]

    return distance, points


def print_components_sizes(distance, points):
    """
    affichage des tailles triees de chaque composante
    """
    print(methode2(distance,points))


def methode2(distance, points):
    d = dict()
    cote=distance/sqrt(2)
    for pt in points :
        key = (floor(pt.coordinates[0]/cote),floor(pt.coordinates[1]/cote))
        if key in d:
            d[key].append(pt)
        else:
            d[key] = [pt]
    together=list()
    visited= set()
    for key in d.keys():
        if key in visited :
            continue
        visited.add(key)
        file=list()
        l=[key]
        for i in range(-2,3):
            for j in range(-2,3):
                if (i==0 and j==0 )or (abs(i)==2 and abs(j)==2):
                    continue
                flag=0
                q=(key[0]+i, key[1]+j)
                if q in visited:
                    continue
                if q in d.keys():
                    for p1 in d[key]:
                        for p2 in d[q]:
                            if p1.distance_to(p2)<=distance:
                                file.append(q)
                                visited.add(q)
                                l.append(q)
                                flag=1
                                break
                        if flag==1:
                            break
        k = 0
        while k<len(file):
            q=file[k]
            for i in range(-2,3):
                for j in range(-2,3):
                    if (i==0 and j==0)or (abs(i)==2 and abs(j)==2):
                        continue
                    flag=0
                    vois=(q[0]+i, q[1]+j)
                    if vois in visited:
                        continue
                    if vois in d.keys():
                        for p1 in d[vois]:
                            for p2 in d[q]:
                                if p1.distance_to(p2)<=distance:
                                    file.append(vois)
                                    visited.add(vois)
                                    l.append(vois)
                                    flag=1
                                    break
                            if flag==1:
                                break
            k+=1
        together.append(l)
    res=list()
    for composante in together:
        sum=0
        for q in composante:
            sum+=len(d[q])
        res.append(sum)
    res.sort(reverse=True)
    return res



def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        print_components_sizes(distance, points)


main()
