#!/bin/python
# module
try:
  import os,sys,time,requests,bs4
  from bs4 import BeatifulSoup
  from time import sleep
  from os import system
except:
  system("pip install requests bs4")
# tampilan
def jalan():
  tampil = """
=======================================
Author : MR.T1T4N_CYBER_HOOD
Team : Mafia Teknologi Indonesia
======================================="""
  system("clear")
  sleep(1)
  system("figlet GOOGLE")
  print(tampil)
  # isi data
  file = input ("MASUKAN PENCARIAN: ")
  url =f"https://google.com/search?&q={file}"
  r = requests.get(url)
  cari = BeatifulSoup(r.text,"html.perser")
  a = cari.find("dive",class_="BNeawe").text
  # hasi pencarian
  print("HASIL => ",a)
jalan ()
