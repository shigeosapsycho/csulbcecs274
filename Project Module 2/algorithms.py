"""Implementations of some sorting"""
import random


def merge(a0, a1, a):
    i = j = k = 0
    while i < len(a0) and j < len(a1):
        if a0[i] < a1[j]:
            a[k] = a0[i]
            i += 1
        else:
            a[k] = a1[j]
            j += 1
        k += 1
    while i < len(a0):
        a[k] = a0[i]
        i += 1
        k += 1
    while j < len(a1):
        a[k] = a1[j]
        j += 1
        k += 1

def merge_sort(a):
    if len(a) <= 1:
        return
    mid = len(a) // 2
    a0 = a[:mid]
    a1 = a[mid:]
    merge_sort(a0)
    merge_sort(a1)
    merge(a0, a1, a)

def _quick_sort(a, i, n):
    if n <= 1:
        return
    pivot = a[i]
    l = i
    r = i + n - 1
    while l <= r:
        while l <= r and a[l] < pivot:
            l += 1
        while l <= r and a[r] > pivot:
            r -= 1
        if l <= r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1
    _quick_sort(a, i, r - i + 1)
    _quick_sort(a, l, n - (l - i))

def quick_sort(a):
    _quick_sort(a, 0, len(a))
    
