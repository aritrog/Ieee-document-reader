import tkinter  as tk
import ieeehack as ih

class guiapt:

	def __init__(self):

		self.l1=[]
		self.l2=[]
		self.t=0

		self.dc=ih.datacollecter()
		self.m=tk.Tk()

		self.lb=tk.Label(self.m,text="Enter your search below",bg="#332828",fg="white")
		self.lb.pack(fill=tk.X,expand=True)

		self.hold1=tk.Frame(self.m,padx=5,pady=5,bg="#332828")
		self.hold1.pack(fill=tk.X,expand=True)

		self.m.title('IEEE RIPPER')

		self.ent= tk.Entry(self.hold1, width=40,fg="white",bg="#665c5c")
		self.ent.pack(side='left')

		self.btn=tk.Button(self.hold1,text='search',fg='white',height=1,width=10,command=self.clearer,bg="#332828")

		self.btn.pack(side='left')


		self.fr2=tk.Frame(self.m,padx=5,pady=5,bg="#332828")
		self.fr2.pack(side=tk.LEFT)



		self.ent.bind('<Return>',self.clearer)

		self.m.mainloop()


	def clearer(self,p=1):
		key=self.ent.get()
		key="ieee "+ key
		self.lb.config(text="Getting your results")
		self.l1,self.l2=self.dc.t_searcher(key)
		print(self.l2)
		self.displayer()


	def displayer(self):
		i=0
		p=1
		for f in self.l2:
			i=i+1
			tk.Radiobutton(self.fr2,text=str(f),variable=p,value=i,bg="#332828").pack()	
		self.btn.config(text="open",command=self.choice(p))


	def choice(self,p):
		print(self.t,p)
		self.dc.p_searcher(self.l1[self.t-1])	
	

ga=guiapt()
