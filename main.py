#This is the converter start point.

from celsiusandfahrenheit import celiusandfahrenheit
from milesandkm import milesandkm
from acres import acres
from volume import volume
from percentage import percentage
from squaremeter import squaremeter
from poundsandkg import poundsandkg
from inchtocm import inchtocm
from timeconvertor import timeconvertor

response=input("For Celsius and Fahrenheit conversion type '1'\n"
               "For Miles and Kilometers conversion type '2'\n"
                "For Acres and Square meters cnversion type '3'\n"
                "For Volume calculation type '4'\n"
                "For Percentage calculations type '5'\n"
                "For Square meters conversion type '6'\n"
                "For Pounds and Kilograns conversions type '7'\n"
                "For Inch and Centimeters conversion type '8'\n"
                "For Time convertor type '9'\n")
             
if response =='1':
    celiusandfahrenheit()
if response=='2':
    milesandkm()
if response=='3':
    acres()
if response=='4':
    volume()
if response=='5':
    percentage()
if response=='6':
    squaremeter()
if response=='7':
    poundsandkg()
if response=='8':
    inchtocm()
if response=='9':
    timeconvertor()

