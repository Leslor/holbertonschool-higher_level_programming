#!/usr/bin/python3
"""function that creates an Object from a “JSON file"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

size = len(sys.argv)
lista = []
for i in range(1, size):
    lista.append(sys.argv[i])

save_to_json_file(lista, 'add_item.json')
