# -*- coding: utf-8 -*-
import os
import time
import wave
#import picamera
#import RPi.GPIO as GPIO
#import tweepy
#import pygame
from subprocess import call
from datetime import datetime
import sys
import contextlib
from array import *
#from tweepy import OAuthHandler
os.system('clear')
#GPIO.cleanup()
#GPIO.setwarnings(False)

sku_range = 3 # the first x ID values that relate to products
currency_name = "ZoinCoins" # name of your currency
currency_symbol = "Z" #Ƶ

ids = ["http://geek.zone/qr/001","http://geek.zone/qr/002","http://geek.zone/qr/003","http://geek.zone/qr/004","http://geek.zone/qr/005","http://geek.zone/qr/006"]#0
names = ["Coke","Muffin","Sandwich","Joe Bloggs","Fred Smith","Jane Deaux"]#1
coins = array('i',[5,6,7,23,33,42,])#2
descriptions = ["Coloured, flavoured, fizzy sugar water", "The bread of the Gods", "Cheese and Marmite", "GeekZone Member", "GeekZone Member", "GeekZone Member"]
#info = [ids, names, coins]

sku_range = sku_range - 1 #because arrays start at 0
transaction_item_count = 0 # counts the number of items in each transaction then is set back to 0 at the end of each transaction
transaction_item_ids = [] # list of IDs in each transaction. cleared at the end of each transaction
bill = 0

## main loop ##
while True:
        print("Hello and Welcome to the GeekZone Tuck Till\n\nA self service till that allows you to purchase\nitems with your wristband and " + currency_name + " aka " + currency_symbol + "\n\nScan your wristband to begin your transaction.\nScan a product to learn more about it")
        barcode = raw_input("Barcode: ")
        #print(ids.index(barcode))
        try:
                index = ids.index(barcode) #floating number that reflects the array position generated from barcode input
                #print("Index = " + str(index)) #debugging
                #print("SKU Range = " + str(sku_range)) #debugging
                barcode = None
        except ValueError:
                index = None
                barcode = None
                os.system('clear')
                print("Could not find that ID, please try again")
                time.sleep(3)
                os.system('clear')
        if index is not None:
                #os.system('clear')
                if index <= sku_range:
                        os.system('clear')
                        print(names[index] + "\n\n" + descriptions[index])
                        # Product Info Screen
                        raw_input("\n\nScan something to continue...")
                        os.system('clear')
                        barcode_input = None
                        index = None
                else:
                        human = index
                        index = None
                        os.system('clear')
                        print("Hello " + names[human] + "!")
                        if coins[human] < 1:
                                print("You have " + currency_symbol + "0 left to spend! Please talk to an event organiser!")
                        else:
                                print("You have " + str(coins[human]) + " " + currency_name + " available to spend\n\nPlease scan an item or scan your wristband again to finish")
                                
                                while True:
                                        try:
                                                barcode = raw_input("Barcode: ")
                                                index = ids.index(barcode)
                                                #barcode = None

                                                #print("Index = " + str(index)) #debugging
                                                #print("Human = " + str(human)) #debugging
                                                #print("SKU Range = " + str(sku_range)) #debugging
                                                
                                                if index <= sku_range:
                                                        os.system('clear')
                                                        print("You have " + str(coins[human]) + " " + currency_name + " available to spend\n\nPlease scan an item or scan your wristband again to finish\n\n")
                                                        transaction_item_ids.insert(transaction_item_count,ids[index])
                                                        print("Product added: " + names[index] + " costs " + str(coins[index]) + " " + currency_name + "\n\n")
                                                        print_count = 0
                                                        while transaction_item_count >= print_count:
                                                                print(str(names[ids.index(transaction_item_ids[print_count])]) + ": " + currency_symbol + str(coins[ids.index(transaction_item_ids[print_count])]))
                                                                print_count = print_count + 1
                                                        print_count = 0
                                                        bill = bill + coins[index]                                                        
                                                        print("\n\nBill is " + str(bill) + "\n\n")                                                        
                                                        transaction_item_count = transaction_item_count + 1
                                                elif index < human:
                                                        print("\n\nThat's not your wristband, please try again\n\n")
                                                        #time.sleep(3)
                                                        index = None
                                                elif index > human:
                                                        print("\n\nThat's not your wristband, please try again\n\n")
                                                        #time.sleep(3)
                                                        index = None
                                                elif index == human:
                                                        #print("Loop break")#debugging
                                                        break
                                                else:
                                                        print("You found the bug")#IFs should never get here
                                        except ValueError:
                                                print("Could not find that ID, please try again...")
                                                #time.sleep(3)
                                                #os.system('clear')
                                                
                                if bill <= coins[human]:
                                        os.system('clear')
                                        print("Thanks for your purchase " + names[human])
                                        coins[human] = coins[human] - bill
                                        print("\n\nYou spent " + currency_symbol + str(bill) + " and have " + currency_symbol + str(coins[human]) + " available")
                                        human = None
                                        index = None
                                        bill = 0
                                        transaction_item_count = 0
                                        transaction_item_ids = []
                                        
                                else:
                                        print("You don't have enough " + currency_name + " to make this purchase.\nPlease talk to an event organiser")
                                        human = None
                                        index = None
                                        bill = 0
                                        time.sleep(3)
                                
                                       
                        time.sleep(3)
                        os.system('clear')
        else:
                os.system('clear')
                index = None
        #print(customer_info[1][customer_position])
        #print(customer_position)
        #os.system('clear') # Linux Clear Screen
