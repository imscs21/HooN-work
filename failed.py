from tkinter import *

class App(Frame) :
	def __init__(self, master) :
		super().__init__(master)
		self.pack(padx=30, pady=20)
		self.create_widgets()

	def create_widgets(self) :
		Label(self, text="게임에서 패배하셨습니다.").grid(row=0, column=0)
		Label(self, text="계속하시겠습니까?").grid(row=1, column=0)
		Button(self, text="O", command=self.proceed).grid(row=2, column=0)
		Button(self, text="X", command=self.quit).grid(row=2, column=1)

	def proceed(self) :
		return True


root = Tk()
root.title("Failed")
root.geometry("280x180")
App(root)
root.mainloop()
