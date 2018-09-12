#!/usr/bin/python3
# -*- coding: UTF-8 -*-

with open("eboot.bin", "rb") as input_file:
	content = input_file.read()
	if b"\x01\x80\x00\x05" in content:
		print("Found Reversed 50008001 SDK")
	content = content.replace(b"\x01\x80\x00\x05", b"\x01\x80\x50\x04")
	if b"\x01\x80\x50\x04" in content:
		print("Patched With 04508001 SDK")
	if b"\x01\x80\x00\x05" not in content:
		print("Already Patched")
	
		
with open("eboot.bin", "wb") as output_file:
	output_file.write(content)
		
with open("eboot.bin", "rb") as input_file:
	content = input_file.read()
	if b"\x05\x00\x80\x01" in content:
		print("Found 50008001 SDK")
	content = content.replace(b"\x05\x00\x80\x01", b"\x04\x50\x80\x01")
	if b"\x04\x50\x80\x01" in content:
		print("Patched With 04508001 SDK")
	if b"\x01\x80\x00\x05" not in content:
		print("Already Patched")

	with open("eboot.bin", "wb") as output_file:
		output_file.write(content)