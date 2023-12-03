from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QInputDialog
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import *
import sys
from random import randint
import datetime
from data import Save, Load


class Towers(QWidget):
	def __init__(self, n=6, t1=[], t2=[], t3=[]):
		super().__init__()
		self.InitUi()
		self.first = False
		self.second = False
		self.free_block = None
		self.score = 0
		# n is the number of blocks and will be added in future
		self.n = n
		# creating blocks and towers
		self.blocks = {}
		self.tower1 = t1
		self.tower2 = t2
		self.tower3 = t3
		self.example = ["block1", "block2", "block3", "block4", "block5",
		                "block6", "block7", "block8", "block9", "block10",
		                "block11", "block12", "block13", "block14", "block15"]
		self.k = int(400 / self.n)
		# 60 - 210
		for i in range(1, self.n + 1):
			self.blocks["block" + str(i)] = [
				(60 + (10 * i), self.k), randint(0, 255), randint(0, 255), randint(0, 255)
				]
			# adding blocks to towers
			if len(self.tower1) + len(self.tower2) + len(self.tower3) < self.n:
				if i % 3 == 1:
					self.tower1.append("block" + str(i))
				elif i % 3 == 2:
					self.tower2.append("block" + str(i))
				elif i % 3 == 0:
					self.tower3.append("block" + str(i))
		self.tower1 = list(set(self.tower1))
		self.tower2 = list(set(self.tower2))
		self.tower3 = list(set(self.tower3))
		self.paint = True

	def InitUi(self):
		# creating a main window
		self.setWindowTitle("Hanoi Tower")
		self.setGeometry(300, 300, 1000, 800)
		
		# creating a label
		self.label_score = QLabel("Score: 0", self)
		self.label_score.move(50, 20)

		# creating a buttons
		self.button1 = QPushButton("1", self)
		self.button2 = QPushButton("2", self)
		self.button3 = QPushButton("3", self)
		self.btn_save = QPushButton("Save", self)
		self.btn_load = QPushButton("Load", self)
		self.btn_col = QPushButton("Change color", self)
		self.button1.resize(50, 50)
		self.button2.resize(50, 50)
		self.button3.resize(50, 50)
		self.btn_save.resize(50, 50)
		self.btn_load.resize(50, 50)
		self.btn_col.resize(100, 50)
		self.button1.move(200, 150)
		self.button2.move(450, 150)
		self.button3.move(700, 150)
		self.btn_save.move(900, 720)
		self.btn_load.move(840, 720)
		self.btn_col.move(50, 720)
		self.button1.clicked.connect(self.action)
		self.button2.clicked.connect(self.action)
		self.button3.clicked.connect(self.action)
		self.btn_save.clicked.connect(self.save)
		self.btn_load.clicked.connect(self.load)
		self.btn_col.clicked.connect(self.col)
	
	def col(self):
		self.k = int(400 / self.n)
		for i in range(1, self.n + 1):
			self.blocks["block" + str(i)] = [
				(60 + (10 * i), self.k), randint(0, 255), randint(0, 255), randint(0, 255)
				]
		self.redrawing()

	def action(self):
		if not self.first:
			self.first = True
		else:
			self.first = False
			self.second = True

		if self.first:
			if self.sender().text() == "1" and self.tower1 != []:
				self.free_block = self.tower1.pop(-1)
			elif self.sender().text() == "2" and self.tower2 != []:
				self.free_block = self.tower2.pop(-1)
			elif self.sender().text() == "3" and self.tower3 != []:
				self.free_block = self.tower3.pop(-1)
			else:
				self.first = False
				self.message("You can't put a block from empty tower!")
			self.redrawing()
		else:
			if self.sender().text() == "1":
				self.tower1.append(self.free_block)
				self.free_block = None
			elif self.sender().text() == "2":
				self.tower2.append(self.free_block)
				self.free_block = None
			else:
				self.tower3.append(self.free_block)
				self.free_block = None
			self.score += 1
			self.label_score.setText("Score: " + str(self.score))
			self.redrawing()
			if self.tower1[::-1] == self.example[:self.n]:
				self.message("You win!")
				self.close()
			elif self.tower2[::-1] == self.example[:self.n]:
				self.message("You win!")
				self.close()
			elif self.tower3[::-1] == self.example[:self.n]:
				self.message("You win! Your score: " + str(self.score))
				self.close()
	
	def paintEvent(self, event):
		if self.paint:
			qp = QPainter()
			qp.begin(self)
			self.draw(qp)
			qp.end()
		self.paint = False

	def draw(self, qp):
		qp.setBrush(QColor(255, 255, 255))
		qp.drawRect(0, 0, 1000, 800)
		qp.setBrush(QColor(90, 0, 0))
		qp.drawRect(200, 250, 50, 400)
		qp.drawRect(450, 250, 50, 400)
		qp.drawRect(700, 250, 50, 400)
		height = 0
		# draw blocks at tower1
		for i in self.tower1:
			qp.setBrush(QColor(self.blocks[i][1], self.blocks[i][2], self.blocks[i][3]))
			qp.drawRect(
				225 - int(0.5 * self.blocks[i][0][0]),
				600 - (int(0.6 * self.k)) - height, self.blocks[i][0][0], self.blocks[i][0][1]
				)
			height += self.k
		height = 0
		# draw blocks at tower2
		for i in self.tower2:
			qp.setBrush(QColor(self.blocks[i][1], self.blocks[i][2], self.blocks[i][3]))
			qp.drawRect(
				475 - int(0.5 * self.blocks[i][0][0]),
				600 - (int(0.6 * self.k)) - height, self.blocks[i][0][0], self.blocks[i][0][1]
				)
			height += self.k
		height = 0
		# draw blocks at tower3
		for i in self.tower3:
			qp.setBrush(QColor(self.blocks[i][1], self.blocks[i][2], self.blocks[i][3]))
			qp.drawRect(
				725 - int(0.5 * self.blocks[i][0][0]),
			   600 - (int(0.6 * self.k)) - height, self.blocks[i][0][0], self.blocks[i][0][1]
			   )
			height += self.k
		if self.free_block is not None:
			qp.setBrush(QColor(
				self.blocks[self.free_block][1],
				self.blocks[self.free_block][2], self.blocks[self.free_block][3]
				))
			qp.drawRect(800, 50, self.blocks[self.free_block][0][0], self.blocks[self.free_block][0][1])
	
	def message(self, text="Warning!"):
		msg = QMessageBox()
		if text == "You win!":
			msg.setIcon(QMessageBox.Information)
			msg.setText(text)
			msg.setWindowTitle("Congratulations!")
		else:
			msg.setIcon(QMessageBox.Warning)
			msg.setText(text)
			msg.setWindowTitle("Warning!")
		msg.exec_()
	
	def save(self):
		name, ok_pressed = QInputDialog.getText(self, "Save", "Write save name")
		dt = datetime.datetime.now().date()
		start = str(dt)
		score = self.score
		t1 = []
		t2 = []
		t3 = []
		for i in self.tower1:
			t1.append(i[-1])
		for i in self.tower2:
			t2.append(i[-1])
		for i in self.tower3:
			t3.append(i[-1])
		n = self.n
		Save(name, start, score, ", ".join(t1), ", ".join(t2), ", ".join(t3), n)
	
	def load(self):
		self.clear()
		n, ok_pressed = QInputDialog.getText(self, "Load", "Write save name")
		dat = Load(n)
		self.score = dat[0]
		self.n = dat[-1]
		for i in dat[1].split(", "):
			if i != "":
				self.tower1.append("block" + i)
		for i in dat[2].split(", "):
			if i != "":
				self.tower2.append("block" + i)
		for i in dat[3].split(", "):
			if i != "":
				self.tower3.append("block" + i)
		self.k = int(400 / self.n)
		for i in range(1, self.n + 1):
			self.blocks["block" + str(i)] = [
				(60 + (10 * i), self.k), randint(0, 255), randint(0, 255), randint(0, 255)
				]
		# print(self.tower1, self.tower2, self.tower3)
		self.redrawing()

	def redrawing(self):
		self.paint = True
		self.update()
	
	def clear(self):
		self.tower1 = []
		self.tower2 = []
		self.tower3 = []
		self.blocks = {}
		self.free_block = None
		self.score = 0
		self.redrawing()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Towers()
	window.show()
	sys.exit(app.exec())
