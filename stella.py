# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import discord
import random
import asyncio
import re
import logging
import time
import threading
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)


'''
def reply(self, inpt):
	# chance of replying
	
		inpt.replace(f'<@{self.user.id}>', '')
				message.channel.send(f'<@{message.author.id}> ' + str(outpt))
				'''

class Bot(discord.Client):
	async def on_ready(self):
		self.chatbot = ChatBot(name='stella 2.1', read_only=False, logic_adapters=['chatterbot.logic.BestMatch'])
		self.trainer = ChatterBotCorpusTrainer(self.chatbot)
		#self.trainer.train("chatterbot.cor6pus.english")
		#self.chatbot.set_trainer(ChatterBotCorpusTrainer)
		#self.chatbot.train("chatterbot.corpus.english")

	async def on_message(self, message):
		# don't respond to ourselves
		if message.author == self.user:
			return
	
		inpt = str(message.content)

		outpt = ''
		try:
                        outpt = self.chatbot.get_response(re.sub('<@[-+]?[1-9]\d*>', '', inpt))
		except Exception as e:
			outpt = str(e)
			#self.chatbot = ChatBot(name='stella 2.1', read_only=False, logic_adapters=['chatterbot.logic.BestMatch'])
			
		print(f'{message.channel.name}: {str(message.author.name).encode("utf-8")}: {inpt.encode("utf-8")}')    
		if random.randint(0, 1000) < 2 or f'<@{self.user.id}>' in inpt or self.user.name in inpt:
			inpt.replace(f'<@{self.user.id}>', '')
			await message.channel.send(f'<@{message.author.id}> ' + str(outpt))

client = Bot()
client.run('', bot=False)

# stella.walker.0@protonmail.com

			

