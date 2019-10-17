from tkinter import *




def main():
    master = Tk()
    Calculator(master)
    master.mainloop()

    
class Calculator:
    def __init__(self,master):
        self.master=master

        self.master.geometry("300x530+800+150")
        self.master.resizable(0, 0)
        self.master.title("WAEC CALCULATOR")
        self.expression = ""
        self.input_text = StringVar()
        self.input_sys = StringVar()

        self.entryscreen = Frame(self.master)
        self.entryscreen.pack()
        self.screen = Frame(self.master, width = 312, height = 80, bd = 0)
        self.screen.pack()

        self.screen_input = Entry(self.entryscreen, font = ("Book antique",20,"bold"), width = 50, textvariable = self.input_text, bd = 0, justify = "left")
        self.screen_input.grid(row = 0, column = 0)



        self.screen_input2 = Entry(self.screen, font = ("Book antique",20,"bold"),textvariable = self.input_sys, width = 20, bd = 0, justify = "center")
        self.screen_input2.grid(row = 1, column = 0)

        self.btn = Frame(self.master, width = 312, height = 470, bd = 2, bg = "lightblue")
        self.btn.pack()

        self.rnd = Label(self.btn, text = "SHIFT", bd = 0, bg = "lightblue").place(x = 10, y = 5)
        self.shift = Button(self.btn, text = "", width = 7, height = 1, fg = "black", bg = "grey", bd = 2, cursor = "hand2", command = lambda: self.btn_click("SHIFT"))
        self.shift.place(x = 0, y = 20)

        self.rnd = Label(self.btn, text = "MODE", bd = 0, fg = "red", bg = "lightblue").place(x = 200, y = 5)
        self.mode = Button(self.btn, text = "", width = 4, height = 1, fg = "black", bg = "grey", bd = 2, cursor = "hand2", command = lambda: self.btn_click("MODE"))
        self.mode.place(x = 200, y = 20)

        #self.rnd = Label(self.btn, text = "CLR", bd = 0, bg = "lightblue").place(x = 240, y = 5)
        self.rnd = Label(self.btn, text = "ON", bd = 0, fg = "red", bg = "lightblue").place(x = 260, y = 5)
        self.on = Button(self.btn, text = "", width = 4, height = 1, fg = "black", bg = "grey", bd = 2, cursor = "hand2", command = lambda: self.btn_click("ON"))
        self.on.place(x = 250, y = 20)

        self.photo7 = PhotoImage(file ="sup..png")
        self.xz = Label(self.btn, image = self.photo7).place(x = 10, y = 53)
        self.photox = PhotoImage(file ="x2.png")
        self.x = Button(self.btn, image = self.photox, width = 32, height = 20, fg = "black", bg = "white", bd = 2, cursor = "hand2", command = lambda: self.btn_click("X-1"))
        self.x.place(x = 0, y = 70)

        self.npr = Label(self.btn, text = "nPr", bd = 0, bg = "lightblue").place(x = 60, y = 50)
        self.nCr = Button(self.btn, text = "nCr", width = 4, height = 1, fg = "black", bg = "white", bd = 2, cursor = "hand2", command = lambda: self.btn_click("nCr"))
        self.nCr.place(x = 50, y =70)

        self.rec = Label(self.btn, text = "Rec(", bd = 0, bg = "lightblue").place(x = 200, y = 50)
        self.pol = Button(self.btn, text = "Pol(", width = 4, height = 1, fg = "black", bg = "white", bd = 2, cursor = "hand2", command = lambda: self.btn_click("Pol("))
        self.pol.place(x = 200, y = 70)

        self.photo1 = PhotoImage(file = "sq.png")
        self.sq = Label(self.btn, image = self.photo1).place(x = 260, y = 55)
        self.photr = PhotoImage(file = "myy.png")
        self.x3 = Button(self.btn, image = self.photr, width = 32, height = 20, fg = "black", bg = "white", bd = 2, cursor = "hand2", command = lambda: self.btn_click("X-3"))
        self.x3.place(x = 250, y = 70)

        self.dc = Label(self.btn, text = "d/c", bd = 0, bg = "lightblue").place(x = 10, y = 100)
        self.abc = Button(self.btn, text = "ab/c", width = 4, height = 1, fg = "black", bg = "white", bd = 2, cursor = "hand2", command = lambda: self.btn_click("ab/c"))
        self.abc.place(x = 0, y = 120)

        self.phi = PhotoImage(file = "sqrt1.png")
        self.sqrt = Button(self.btn, image = self.phi, width = 39, height = 20, fg = "black", bg = "white", bd = 2, cursor = "hand2", command = lambda: self.btn_click("X-3"))
        self.sqrt.place(x = 50, y = 120)

        self.pp = PhotoImage(file = "myx.png")
        self.x2 = Button(self.btn, image = self.pp, width = 32, height = 20, fg = "black", bg = "white", bd = 2, cursor = "hand2", command = lambda: self.btn_click("X-2"))
        self.x2.place(x = 100, y = 120)

        self.photo = PhotoImage(file ="sxx.png")
        
        self.xs = Label(self.btn, image = self.photo).place(x = 155, y = 100)
        
        self.up = Button(self.btn, text = "^", width = 4, height = 1, fg = "black", bg = "white", bd = 2, cursor = "hand2", command = lambda: self.btn_click("^"))
        self.up.place(x = 150, y = 120)

        self.im = PhotoImage(file="ten.png")
        self.ten = Label(self.btn, image=self.im, bd = 0, bg = "lightblue").place(x = 210, y = 105)
        self.log = Button(self.btn, text = "log", width = 4, height = 1, fg = "black", bg = "white", bd = 2, cursor = "hand2", command = lambda: self.btn_click("log"))
        self.log.place(x = 200, y = 120)

        self.ss = PhotoImage(file = "ee.png")
        self.e = Label(self.btn, image = self.ss, bd = 0, bg = "lightblue").place(x = 260, y = 107)
        self.inn = Button(self.btn, text = "In", width = 4, height = 1, fg = "black", bg = "white", bd = 2, cursor = "hand2", command = lambda: self.btn_click("In"))
        self.inn.place(x = 250, y = 120)

        self.ab = Button(self.btn, text = "(-)", width = 4, height = 1, fg = "black", bg = "white", bd = 2, cursor = "hand2", command = lambda: self.btn_click("(-)"))
        self.ab.place(x = 0, y = 170)

        self.photo2 = PhotoImage(file ="arrow.png")
        self.arrow = Label(self.btn, image = self.photo2, bd = 0, bg = "lightblue").place(x = 60, y = 155)
        self.pho = PhotoImage(file ="do.png")
        self.dot = Button(self.btn, image = self.pho, width = 39, height = 20, fg = "black", bg = "white", bd = 2, cursor = "hand2", command = lambda: self.btn_click(".,,,"))
        self.dot.place(x = 50, y = 170)

        self.hyp = Button(self.btn, text = "hyp", width = 4, height = 1, fg = "black", bg = "white", bd = 2, cursor = "hand2", command = lambda: self.btn_click("hyp"))
        self.hyp.place(x = 100, y = 170)

        self.imge = PhotoImage(file = "sin.png")
        self.sinn = Label(self.btn, image = self.imge).place(x = 155, y = 154)
        self.sin = Button(self.btn, text = "sin", width = 4, height = 1, fg = "black", bg = "white", bd = 2, cursor = "hand2", command = lambda: self.btn_click("sin"))
        self.sin.place(x = 150, y = 170)

        self.ig = PhotoImage(file = "cos.png")
        self.coss = Label(self.btn, image = self.ig).place(x = 205, y = 154)
        self.cos = Button(self.btn, text = "cos", width = 4, height = 1, fg = "black", bg = "white", bd = 2, cursor = "hand2", command = lambda: self.btn_click("cos"))
        self.cos.place(x = 200, y = 170)

        self.imgg = PhotoImage(file = "tan.png")
        self.tann = self.sinn = Label(self.btn, image = self.imgg).place(x = 255, y = 154)
        self.tan = Button(self.btn, text = "tan", width = 4, height = 1, fg = "black", bg = "white", bd = 2, cursor = "hand2", command = lambda: self.btn_click("tan"))
        self.tan.place(x = 250, y = 170)

        self.sto = Label(self.btn, text = "STO", bd = 0, bg = "lightblue").place(x = 10, y = 200)
        self.rcl = Button(self.btn, text = "RCL", width = 4, height = 1, fg = "black", bg = "white", bd = 2, cursor = "hand2", command = lambda: self.btn_click("RCL"))
        self.rcl.place(x = 0, y = 220)

        self.photo3 = PhotoImage(file ="arrow.png")
        self.sto = Label(self.btn, image = self.photo3).place(x = 60, y = 205)
        self.eng = Button(self.btn, text = "ENG", width = 4, height = 1, fg = "black", bg = "white", bd = 2, cursor = "hand2", command = lambda: self.btn_click("ENG"))
        self.eng.place(x = 50, y = 220)

        self.bra1 = Button(self.btn, text = "(", width = 4, height = 1, fg = "black", bg = "white", bd = 2, cursor = "hand2", command = lambda: self.btn_click("("))
        self.bra1.place(x = 100, y = 220)

        self.bra2 = Button(self.btn, text = ")", width = 4, height = 1, fg = "black", bg = "white", bd = 2, cursor = "hand2", command = lambda: self.btn_click(")"))
        self.bra2.place(x = 150, y = 220)

        self.img = PhotoImage(file = "dot.png")
        self.sto = Label(self.btn, image = self.img).place(x = 220, y = 200)
        self.comma = Button(self.btn, text = ",", width = 4, height = 1, fg = "black", bg = "white", bd = 2, cursor = "hand2", command = lambda: self.btn_click(","))
        self.comma.place(x = 200, y = 220)

        self.sto = Label(self.btn, text = "M-", bd = 0, bg = "lightblue").place(x = 260, y = 200)
        self.minn = Button(self.btn, text = "M", width = 4, height = 1, fg = "black", bg = "white", bd = 2, cursor = "hand2", command = lambda: self.btn_click("M"))
        self.minn.place(x = 250, y = 220)

        self.seven = Button(self.btn, text = "7", width = 5, height = 1, fg = "white", bg = "black", bd = 2, cursor = "hand2", command = lambda: self.btn_click("7"))
        self.seven.place(x = 0, y = 270)

        self.eight = Button(self.btn, text = "8", width = 5, height = 1, fg = "white", bg = "black", bd = 2, cursor = "hand2", command = lambda: self.btn_click("8"))
        self.eight.place(x = 60, y = 270)

        self.nine = Button(self.btn, text = "9", width = 5, height = 1, fg = "white", bg = "black", bd = 2, cursor = "hand2", command = lambda: self.btn_click("9"))
        self.nine.place(x = 120, y = 270)

        self.sto = Label(self.btn, text = "INS", bd = 0, bg = "lightblue").place(x = 190, y = 250)        
        self.dell = Button(self.btn, text = "DEL", width = 5, height = 1, fg = "white", bg = "red", bd = 2, cursor = "hand2", command = lambda: self.btn_clear())
        self.dell.place(x = 180, y = 270)

        self.sto = Label(self.btn, text = "OFF", bd = 0, bg = "lightblue").place(x = 250, y = 250)  
        self.ac = Button(self.btn, text = "AC", width = 5, height = 1, fg = "white", bg = "red", bd = 2, cursor = "hand2", command = lambda: self.btn_click("AC"))
        self.ac.place(x = 240, y = 270)

        self.four = Button(self.btn, text = "4", width = 5, height = 1, fg = "white", bg = "black", bd = 2, cursor = "hand2", command = lambda: self.btn_click("4"))
        self.four.place(x = 0, y = 320)

        self.five = Button(self.btn, text = "5", width = 5, height = 1, fg = "white", bg = "black", bd = 2, cursor = "hand2", command = lambda: self.btn_click("5"))
        self.five.place(x = 60, y = 320)

        self.six = Button(self.btn, text = "6", width = 5, height = 1, fg = "white", bg = "black", bd = 2, cursor = "hand2", command = lambda: self.btn_click("6"))
        self.six.place(x = 120, y = 320)

        self.mult = Button(self.btn, text = "x", width = 5, height = 1, fg = "white", bg = "black", bd = 2, cursor = "hand2", command = lambda: self.btn_click("*"))
        self.mult.place(x = 180, y = 320)

        self.imm = PhotoImage(file = "div.png")
        self.div = Button(self.btn, image = self.imm, width = 39, height = 20,fg = "white", bg = "black", bd = 2, cursor = "hand2", command = lambda: self.btn_click("/"))
        self.div.place(x = 240, y = 320)

        self.ssum = Label(self.btn, text = "S-SUM", bd = 0, bg = "lightblue").place(x = 5, y = 350)  
        self.one = Button(self.btn, text = "1", width = 5, height = 1, fg = "white", bg = "black", bd = 2, cursor = "hand2", command = lambda: self.btn_click("1"))
        self.one.place(x = 0, y = 370)

        self.svar = Label(self.btn, text = "S-VAR", bd = 0, bg = "lightblue").place(x = 65, y = 350)  
        self.two = Button(self.btn, text = "2", width = 5, height = 1, fg = "white", bg = "black", bd = 2, cursor = "hand2", command = lambda: self.btn_click("2"))
        self.two.place(x = 60, y = 370)

        self.three = Button(self.btn, text = "3", width = 5, height = 1, fg = "white", bg = "black", bd = 2, cursor = "hand2", command = lambda: self.btn_click("3"))
        self.three.place(x = 120, y = 370)

        self.add = Button(self.btn, text = "+", width = 5, height = 1, fg = "white", bg = "black", bd = 2, cursor = "hand2", command = lambda: self.btn_click("+"))
        self.add.place(x = 180, y = 370)

        self.minus = Button(self.btn, text = "-", width = 5, height = 1, fg = "white", bg = "black", bd = 2, cursor = "hand2", command = lambda: self.btn_click("-"))
        self.minus.place(x = 240, y = 370)

        self.rnd = Label(self.btn, text = "Rnd", bd = 0, bg = "lightblue").place(x = 10, y = 400)  
        self.zero = Button(self.btn, text = "0", width = 5, height = 1, fg = "white", bg = "black", bd = 2, cursor = "hand2", command = lambda: self.btn_click("0"))
        self.zero.place(x = 0, y = 420)

        self.rndn = Label(self.btn, text = "Rnd#", bd = 0, bg = "lightblue").place(x = 70, y = 400)
        self.dot1 = Button(self.btn, text = ".", width = 5, height = 1, fg = "white", bg = "black", bd = 2, cursor = "hand2", command = lambda: self.btn_click("."))
        self.dot1.place(x = 60, y = 420)

        self.phott = PhotoImage(file = "par.png")
        self.par = Label(self.btn, image = self.phott, bd = 0, bg = "lightblue").place(x = 140, y = 400)
        self.exp = Button(self.btn, text = "EXP", width = 5, height = 1, fg = "white", bg = "black", bd = 2, cursor = "hand2", command = lambda: self.btn_click("EXP"))
        self.exp.place(x = 120, y = 420)

        self.phot4 = PhotoImage(file = "arr.png")
        self.att = Label(self.btn, image = self.phot4).place(x = 200, y = 400)
        self.drg = Label(self.btn, text = "DRG", bd = 0, bg = "lightblue").place(x = 180, y = 400)
        self.ans = Button(self.btn, text = "Ans", width = 5, height = 1, fg = "white", bg = "black", bd = 2, cursor = "hand2", command = lambda: self.btn_click("Ans"))
        self.ans.place(x = 180, y = 420)

        self.per = Label(self.btn, text = "%", bd = 0, bg = "lightblue").place(x = 250, y = 400)
        self.equal = Button(self.btn, text = "=", width = 5, height = 1, fg = "white", bg = "black", bd = 2, cursor = "hand2", command = lambda: self.btn_equals())
        self.equal.place(x = 240, y = 420)

        
    def btn_click(self,item):
        self.expression = self.expression + str(item)
        self.input_text.set(self.expression)

    def btn_clear(self):
        self.expression = " "
        self.input_text.set("")

    def btn_equals(self):
        result = str(eval(self.expression))
        self.input_text.set(result)
        self.expression = ""



if __name__=='__main__':
    main()
