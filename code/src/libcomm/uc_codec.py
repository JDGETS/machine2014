# -*- coding: utf8 -*-

""" handles encoding/decoding data from the UC. """

from crc16 import crc16
from uc_messages import incoming_messages as messages
import struct
import sys

class Decoder :
	def __init__(self, cb):
		self.count_synchro = 0
		self.count_ignored = 0
		self.count_errors = 0
		self.callback = cb
		
		self.rawdata = ''
		self.id = 0
		self.btr = 0

	def run(self):
		pass


	def find_id(self, c):
		
		if ord(c) not in messages.keys():
			return False
		
		self.id = ord(c)
		self.format = str(messages[self.id]['format'])
		self.noms = messages[self.id]['noms']
		self.facteur = messages[self.id]['facteur']
		self.btr = struct.calcsize(self.format) + 2
		
		return True

	def decode(self, c):
		
		while True:
			# Recherche d'un identifiant
			if not self.btr:
				i = 0
				for cc in self.rawdata:
					i += 1
					if self.find_id(cc):
						self.rawdata = self.rawdata[i:]
						self.btr -= len(self.rawdata)
						break
					else:
						#print 'Identifiant de message inconnu (%s)' % repr(cc)
						pass
			
			if not self.btr:
				if not self.find_id(c):
					#print 'Identifiant de message inconnu (%s)' % repr(c)
					pass
				return
			
			# Lecture des donnees
			self.rawdata += c
			self.btr -= 1
			
			# Verification de la checksum
			if self.btr >= 1:
				return
			
			calcchecksum = crc16(chr(self.id)+self.rawdata[:struct.calcsize(self.format)])
			msgchecksum = struct.unpack('>H', self.rawdata[struct.calcsize(self.format):struct.calcsize(self.format)+2])[0]
			if msgchecksum != calcchecksum:
				print '\nEchec de la verification de la somme de controle ('+ repr(self.id) +')'+ \
					' calc:'+repr(hex(calcchecksum))+' msg:'+ repr(hex(msgchecksum))
				self.btr = 0
				return
			
			# Decodage des donnees
			a = struct.unpack(self.format, self.rawdata[0:struct.calcsize(self.format)])
			
			data = {}
			for i in xrange(len(a)):
				name = self.noms[i]
				value = a[i]*self.facteur[i]
				self.callback(name, value)
			
			#~ print 'Message recu'
			self.rawdata = self.rawdata[struct.calcsize(self.format)+2:]
			
			self.btr = 0
			return