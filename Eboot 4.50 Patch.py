#!/usr/bin/python3
# -*- coding: UTF-8 -*-

with open("eboot.bin", "rb") as input_file:
	content = input_file.read()
	if b"\x01\x80\x00\x05" in content:
		print("Found Reversed 50008001 SDK. Patching To 4.50 SDK")
	else:
		print("Already Patched, Reversed SDK is 04508001")
	if b"\x05\x00\x80\x01" in content:
		print("Found 50008001 SDK. Patching To 4.50 SDK")
	else:
		print("Already Patched, SDK is Now 04508001")
	content = content.replace(b"\x01\x80\x00\x05", b"\x01\x80\x50\x04")
	content = content.replace(b"\x05\x00\x80\x01", b"\x04\x50\x80\x01")
		
with open("eboot.bin", "wb") as output_file:
	output_file.write(content)

