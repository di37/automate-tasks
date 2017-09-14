#! /usr/bin/python3

import webbrowser, sys, pyperclip

starting_point = input("Enter starting_point: ")
destination = input("Enter destination: ")

webbrowser.open('https://www.google.ae/maps/dir/'+ starting_point + '/' + destination)


