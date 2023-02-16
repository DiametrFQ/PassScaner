from ast import For
from email.mime import image
import tkinter as tk
import sqlite3
import pytesseract
from tkinter import *
from turtle import title
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import cv2
import numpy as np
import time

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file='add.gif')
        btn_open_dialog = tk.Button(toolbar, text='Добавить позицию', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file='update.gif')
        btn_edit_dialog = tk.Button(toolbar, text='Редактировать', bg='#d7d8e0', bd=0, image=self.update_img,
                                    compound=tk.TOP, command=self.open_update_dialog)
        btn_edit_dialog.pack(side=tk.RIGHT)

        self.delete_img = tk.PhotoImage(file='delete.gif')
        btn_delete = tk.Button(toolbar, text='Удалить позицию', bg='#d7d8e0', bd=0, image=self.delete_img,
                               compound=tk.TOP, command= self.delete_records)
        btn_delete.pack(side=tk.RIGHT)

        self.search_img = tk.PhotoImage(file='search.gif')
        btn_search = tk.Button(toolbar, text='Поиск', bg='#d7d8e0', bd=0, image=self.search_img,
                               compound=tk.TOP, command=self.open_search_dialog)
        btn_search.pack(side=tk.RIGHT)

        self.refresh_img = tk.PhotoImage(file='refresh.gif')
        btn_refresh = tk.Button(toolbar, text='Обновить', bg='#d7d8e0', bd=0, image=self.refresh_img,
                                compound=tk.TOP, command=self.view_records)
        btn_refresh.pack(side=tk.RIGHT)


        pasInfo = tk.Frame(bg='#d7d8e0', bd=2)
        pasInfo.pack(side=tk.TOP)

        self.label_f = tk.Label(pasInfo, text='                                                                                                                                          ')
        self.label_f.pack(side=tk.LEFT)
        self.label_f = tk.Label(pasInfo, text='                                                                                                                                          ')
        self.label_f.pack(side=tk.RIGHT)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)



        self.canvas= Canvas(pasInfo, width=190, height= 285)
        self.canvas.place(x=1, y=10)

        self.img1= ImageTk.PhotoImage(file="images/pas2.png")

        self.image_container = self.canvas.create_image(0,0, anchor="nw",image=self.img1)
        self.canvas.itemconfig(self.image_container,image=self.img1)

        X1 = 200
        X2 = 330
        X3 = 450
        Y = 20
        self.label_f = tk.Label(pasInfo, text='Фамилия:')
        self.label_f.place(x=X1, y=0)
        self.value_lastName = tk.Label(pasInfo, text='ФАМИЛИЯ')
        self.value_lastName.place(x=X2, y=Y*0)

        self.label_f2 = tk.Label(pasInfo, text='Имя:')
        self.label_f2.place(x=X1, y=Y*1)
        self.value_name = tk.Label(pasInfo, text='ИМЯ')
        self.value_name.place(x=X2, y=Y*1)

        self.label_f3 = tk.Label(pasInfo, text='Отчество:')
        self.label_f3.place(x=X1, y=Y*2)
        self.value_midleName = tk.Label(pasInfo, text='Отчество')
        self.value_midleName.place(x=X2, y=Y*2)

        self.label_f4 = tk.Label(pasInfo, text='Дата рождения:')
        self.label_f4.place(x=X1, y=Y*3)
        self.value_birth = tk.Label(pasInfo, text='00.00.0000')
        self.value_birth.place(x=X2, y=Y*3)

        self.label_f5 = tk.Label(pasInfo, text='Место рождения:')
        self.label_f5.place(x=X1, y=Y*4)
        self.value_placeBirth = tk.Label(pasInfo, text='МЕСТО РОЖДЕНИЯ')
        self.value_placeBirth.place(x=X2, y=Y*4)

        self.label_f6 = tk.Label(pasInfo, text='Серийный номер:')
        self.label_f6.place(x=X1, y=Y*6)
        self.value_Namber = tk.Label(pasInfo, text='00 00 000000')
        self.value_Namber.place(x=X2, y=Y*6)

        self.label_f7 = tk.Label(pasInfo, text='Дата выдачи:')
        self.label_f7.place(x=X1, y=Y*7)
        self.value_dateGet = tk.Label(pasInfo, text='00.00.0000')
        self.value_dateGet.place(x=X2, y=Y*7)

        self.label_f3 = tk.Label(pasInfo, text='Паспорт выдан:')
        self.label_f3.place(x=X1, y=Y*8)
        self.value_whoGet  = tk.Label(pasInfo, text='ПАСПОРТ ВЫДАН')
        self.value_whoGet.place(x=X2, y=Y*8)

        self.label_f4 = tk.Label(pasInfo, text='Код подразделения:')
        self.label_f4.place(x=X1, y=Y*10)
        self.value_codeWho = tk.Label(pasInfo, text='000-000')
        self.value_codeWho.place(x=X2, y=Y*10)



        self.label_f5 = tk.Label(pasInfo, text='Адрес регистрации:')
        self.label_f5.place(x=X3, y=0)
        self.value_adresReg = tk.Label(pasInfo, text='Адрес регистрации')
        self.value_adresReg.place(x=X3+200, y=20*0)

        self.label_f6 = tk.Label(pasInfo, text='СНИЛС:')
        self.label_f6.place(x=X3, y=20*3)
        self.value_snils = tk.Label(pasInfo, text='Сведетельство выдано')
        self.value_snils.place(x=X3+200, y=20*3)

        self.label_f7 = tk.Label(pasInfo, text='ИНН:')
        self.label_f7.place(x=X3, y=20*4)
        self.value_tax = tk.Label(pasInfo, text='Сведетельство выдано')
        self.value_tax.place(x=X3+200, y=20*4)

        self.label_f3 = tk.Label(pasInfo, text='Номер сведетельства:')
        self.label_f3.place(x=X3, y=20*5)
        self.value_certNum = tk.Label(pasInfo, text='Номер сведетельства')
        self.value_certNum.place(x=X3+200, y=20*5)

        self.label_f = tk.Label(pasInfo, text='Сведетельство выдано')
        self.label_f.place(x=X3, y=20*6)
        self.value_certPlace = tk.Label(pasInfo, text='Сведетельство выдано:')
        self.value_certPlace.place(x=X3+200, y=20*6)

        self.label_f5 = tk.Label(pasInfo, text='ФИО отца:')
        self.label_f5.place(x=X3, y=20*11)
        self.value_LNMFather = tk.Label(pasInfo, text='ФИО отца')
        self.value_LNMFather.place(x=X3+200, y=20*11)

        self.label_f6 = tk.Label(pasInfo, text='ФИО матери:')
        self.label_f6.place(x=X3, y=20*13)
        self.value_LNMMather = tk.Label(pasInfo, text='ФИО матери')
        self.value_LNMMather.place(x=X3+200, y=20*13)



        self.tree = ttk.Treeview(self, columns=('ID', 'lastName', 'Name', 'middleName', 'both', 'city', 'serialNumber', 'dateReg', 'placeIssue', 'divisionCode', 'agresReg', 'SNILS', 'tax', 'birthCertificat', 'issueCertificate', 'LNMFather', 'LNMMather'), height=15, show='headings')
        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('lastName', width=75, anchor=tk.CENTER)
        self.tree.column('Name', width=90, anchor=tk.CENTER)
        self.tree.column('middleName', width=140, anchor=tk.CENTER)
        self.tree.column('both', width=100, anchor=tk.CENTER)
        self.tree.column('city', width=100, anchor=tk.CENTER)
        self.tree.column('serialNumber', width=120, anchor=tk.CENTER)
        self.tree.column('dateReg', width=100, anchor=tk.CENTER)
        self.tree.column('placeIssue', width=100, anchor=tk.CENTER)
        self.tree.column('divisionCode', width=80, anchor=tk.CENTER)
        self.tree.column('agresReg', width=100, anchor=tk.CENTER)
        self.tree.column('SNILS', width=100, anchor=tk.CENTER)
        self.tree.column('tax', width=100, anchor=tk.CENTER)
        self.tree.column('birthCertificat', width=100, anchor=tk.CENTER)
        self.tree.column('issueCertificate', width=100, anchor=tk.CENTER)
        self.tree.column('LNMFather', width=100, anchor=tk.CENTER)
        self.tree.column('LNMMather', width=100, anchor=tk.CENTER)


        def selectItem(a):
            curItem = self.tree.focus()
            self.value_lastName.config(text = self.tree.item(curItem)['values'][1])
            self.value_name.config(text = self.tree.item(curItem)['values'][2])
            self.value_midleName.config(text = self.tree.item(curItem)['values'][3])
            self.value_birth.config(text = self.tree.item(curItem)['values'][4])
            self.value_placeBirth.config(text = self.tree.item(curItem)['values'][5])
            self.value_Namber.config(text = self.tree.item(curItem)['values'][6])
            self.value_dateGet.config(text = self.tree.item(curItem)['values'][7])
            self.value_whoGet.config(text = self.tree.item(curItem)['values'][8])
            self.value_codeWho.config(text = self.tree.item(curItem)['values'][9])
            self.value_adresReg.config(text = self.tree.item(curItem)['values'][10])
            self.value_snils.config(text = self.tree.item(curItem)['values'][11])
            self.value_tax.config(text = self.tree.item(curItem)['values'][12])
            self.value_certNum.config(text = self.tree.item(curItem)['values'][13])
            self.value_certPlace.config(text = self.tree.item(curItem)['values'][14])
            self.value_LNMFather.config(text = self.tree.item(curItem)['values'][15])
            self.value_LNMMather.config(text = self.tree.item(curItem)['values'][16])


            tempImg = Image.open(self.tree.item(curItem)['values'][17])
            tempImg = tempImg.resize((195,285), Image.ANTIALIAS)
            self.img1 = ImageTk.PhotoImage(tempImg)
            self.image_container = self.canvas.create_image(0,0, anchor="nw",image=self.img1)
            self.canvas.itemconfig(self.image_container,image=self.img1)

        self.tree.heading('ID', text='ID')
        self.tree.heading('lastName', text='Фамилия')
        self.tree.heading('Name', text='Имя')
        self.tree.heading('middleName', text='Отчество')
        self.tree.heading('both', text='Дата рождения')
        self.tree.heading('city', text='Место рождения')
        self.tree.heading('serialNumber', text='Серийный номер')
        self.tree.heading('dateReg', text='Дата выдачи')
        self.tree.heading('placeIssue', text='Паспорт выдан')
        self.tree.heading('divisionCode', text='Код подразделения')
        self.tree.heading('agresReg', text='Адрес регистрации')
        self.tree.heading('SNILS', text='СНИЛС')
        self.tree.heading('tax', text='ИНН')
        self.tree.heading('birthCertificat', text='Номер сведетельства о рождении')
        self.tree.heading('issueCertificate', text='Орган выдачи сведетельства')
        self.tree.heading('LNMFather', text='ФИО отца')
        self.tree.heading('LNMMather', text='ФИО матери')
        self.tree.bind('<ButtonRelease-1>', selectItem)


        self.tree.pack(side=tk.LEFT)
        curItem = self.tree.focus()
        print(self.tree.item(curItem))

        scroll = tk.Scrollbar(self, command=self.tree.yview)
        scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scroll.set)

    def records(self, lastName, Name, middleName, both, city, serialNumber, dateReg, placeIssue, divisionCode, agresReg, SNILS, tax, birthCertificat, issueCertificate, LNMFather, LNMMather, LinkPhoto ):
        self.db.insert_data( lastName, Name, middleName, both, city, serialNumber, dateReg, placeIssue, divisionCode, agresReg, SNILS, tax, birthCertificat, issueCertificate, LNMFather, LNMMather, LinkPhoto )
        self.view_records()

    def update_record(self, lastName, Name, middleName, both, city, serialNumber, dateReg, placeIssue, divisionCode, agresReg, SNILS, tax, birthCertificat, issueCertificate, LNMFather, LNMMather, LinkPhoto ):
        self.db.c.execute('''UPDATE DataBase SET lastName=?, Name=?, middleName=?, both=?, city=?, serialNumber=?, dateReg=?, placeIssue=?, divisionCode=?, agresReg=?, SNILS=?, tax=?, birthCertificat=?, issueCertificate=?, LNMFather=?, LNMMather=?, LinkPhoto=?  WHERE ID=?''',
                          (lastName, Name, middleName, both, city, serialNumber, dateReg, placeIssue, divisionCode, agresReg, SNILS, tax, birthCertificat, issueCertificate, LNMFather, LNMMather, LinkPhoto , self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_records()

    def view_records(self):
        self.db.c.execute('''SELECT * FROM DataBase''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('''DELETE FROM DataBase WHERE id=?''', [self.tree.set(selection_item, '#1')])
        self.db.conn.commit()
        self.view_records()

    def search_records(self, description):
        description = ('%' + description + '%',)
        self.db.c.execute('''SELECT * FROM DataBase WHERE description LIKE ?''', description)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def open_dialog(self):
        Child()

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()



class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить данные')
        self.geometry('1200x900')
        self.resizable(False, False)

        def autocrop(image, thresh):
            # load image
            img = cv2.imread(image) #load image by path

            rsz_img = cv2.resize(img, None, fx=1, fy=1) # resize since image is huge

            gray = cv2.cvtColor(rsz_img, cv2.COLOR_BGR2GRAY) # convert to grayscale

            # threshold
            retval, thresh_gray = cv2.threshold(gray, thresh=thresh, maxval=255, type=cv2.THRESH_BINARY)

            # find where the signature is and make a cropped region
            points = np.argwhere(thresh_gray==0) # find where the black pixels are
            points = np.fliplr(points) # store them in x,y coordinates instead of row,col indices

            x, y, w, h = cv2.boundingRect(points) # create a rectangle around those points
            #x, y, w, h = x-10, y-10, w+20, h+20 # make the box a little bigger

            crop = gray[y:y+h, x:x+w] # create a cropped region of the gray image

            # get the thresholded crop
            retval, thresh_crop = cv2.threshold(crop, thresh=220, maxval=255, type=cv2.THRESH_BINARY)

            # display
            #cv2.imshow("Cropped and thresholded image", thresh_crop)
            cv2.imwrite("cropped.jpg", thresh_crop)
            cv2.waitKey(0)

            print(x,y,w,h) #x,y = base offset;  w,h = width and height of crop ########################################################

            img = cv2.imread('cropped.jpg')
            mask = np.uint8(np.where(img == 0, 1, 0))

            col_counts = cv2.reduce(mask, 0, cv2.REDUCE_SUM, dtype=cv2.CV_32SC1).flatten().tolist()
            row_counts = cv2.reduce(mask, 1, cv2.REDUCE_SUM, dtype=cv2.CV_32SC1).flatten().tolist()

            xthresh=200
            ythresh=200
            xlow=-1
            xhigh=-1
            ylow=-1
            yhigh=-1

            for i in range (0,len(col_counts),3):
                a=col_counts[i]
                if a>xthresh:
                    if xlow==-1:
                        xlow=i/3
                    xhigh=i/3

            for i in range (0,len(row_counts),3):
                a=row_counts[i]
                if a>ythresh:
                    if ylow==-1:
                        ylow=i/3
                    yhigh=i/3

            xlow=int(xlow)
            xhigh=int(xhigh//1)
            ylow=int(ylow//1)
            yhigh=int(yhigh//1)

            print(xlow,xhigh) #no shadow offsets
            print(ylow,yhigh)

            crop_img = img[ylow:yhigh, xlow:xhigh]
            cv2.imwrite("noshadow.jpg", crop_img)

            #print ("Column counts: ", col_counts.flatten().tolist()) #200
            #print ("Row counts: ", row_counts.flatten().tolist()) #200

            img = cv2.imread(image)
            crop_img = img[y+ylow:y+yhigh, x+xlow:x+xhigh]
            cv2.imwrite("final.jpg", crop_img)
            return [x,xlow,xhigh,y,ylow,yhigh]

        def scan(pas, X11, Y11, X12, Y12, file, tresh):
            pas.crop((X11, Y11, X12, Y12)).save(file, quality=95)
            monochrome(file, tresh)
            return pytesseract.image_to_string(file, lang="rus")

        def monochrome(file, tresh):
            img_grey = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

            img_binary = cv2.threshold(img_grey, tresh, 600, cv2.THRESH_BINARY)[1]
            cv2.imwrite(file,img_binary)

        def updatePassReg():
            global img3

            path = filedialog.askopenfilename()

            pas = Image.open(path)
            #noshedow = Image.open(path)

            # file = "images/pas2124.png"
            # pas.crop((55, 13, 600, 730)).save(file, quality=95)
            # x,xlow,xhigh,y,ylow,yhigh = autocrop(file, 220)
            file = "images/pas2124.png"

            try:
                pas.crop((1079, 13, 2055, 629)).save(file, quality=95)
                x,xlow,xhigh,y,ylow,yhigh = autocrop(file, 100)

            except cv2.error:
                pas.crop((31, 13, 969, 629)).save(file, quality=95)
                x,xlow,xhigh,y,ylow,yhigh = autocrop(file, 90)

            final = Image.open('final.jpg')
            agresReg = scan(final, 120, 110, 820, 315, file, 160)

            # if agresReg == ' ' or agresReg == '':
            #     sdf

            # SNULS = scan(pas, 663, 19, 1229, 730, file, 180)
            # a = autocrop(file, 180)


            self.velue_agresReg.delete(0, 'end')
            self.velue_agresReg.insert(0, agresReg)

            img = Image.open(path)
            img = img.resize((800, 500)).save("test.png", quality=95)

            img3 = ImageTk.PhotoImage(file="test.png")
            canvas.itemconfig(image_container,image=img3)


        def updateCertificate():
            global img3

            path = filedialog.askopenfilename()

            file = "images/pas2124.png"

            pas = Image.open(path)

            LFather = scan(pas, 315, 1443, 1897, 1589, file, 160)
            self.velue_LNMFather.delete(0, 'end')
            self.velue_LNMFather.insert(0, LFather)

            LMather = scan(pas, 315, 1760, 1897, 1900, file, 150)
            self.velue_LNMMather.delete(0, 'end')
            self.velue_LNMMather.insert(0, LMather)

            Issue1 = scan(pas, 943, 2055, 1881, 2111, file, 180)
            Issue2 = scan(pas, 209, 2115, 1881, 2187, file, 180)
            self.velue_issueCertificate.delete(0, 'end')
            self.velue_issueCertificate.insert(0, Issue1 + " " + Issue2)

            Number = scan(pas, 1045, 2610, 1491, 2731, file, 180)
            self.velue_birthCertificat.delete(0, 'end')
            self.velue_birthCertificat.insert(0, Number)

            img = Image.open(path)
            img = img.resize((500, 800)).save("test.png", quality=95)

            img3 = ImageTk.PhotoImage(file="test.png")
            canvas.itemconfig(image_container,image=img3)

        def updateSNILS():
            global img3

            path = filedialog.askopenfilename()
            # a = autocrop(path)

            # path = 'final.jpg'

            file = "images/pas2124.png"

            pas = Image.open(path)

            SNULS = scan(pas, 315, 264, 1037, 350, file, 146)

            self.velue_SNILS.delete(0, 'end')
            self.velue_SNILS.insert(0, SNULS)

            img = Image.open(path)
            img = img.resize((800, 500)).save("test.png", quality=95)

            img3 = ImageTk.PhotoImage(file="test.png")
            canvas.itemconfig(image_container,image=img3)

        def updateTax():
            global img3

            path = filedialog.askopenfilename()
            # a = autocrop(path)

            # path = 'final.jpg'

            file = "images/pas2124.png"

            pas = Image.open(path)

            Tax = scan(pas, 985, 1189, 2033, 1503, file, 200)
            taxnorm = ''

            for i in Tax:
                if i == 'о' or i == 'О':
                    taxnorm += '0'
                elif i != '[' and i != ']' and i != '|' and i != '{' and i != '}' and i != ' ':
                    taxnorm += i


            self.velue_tax.delete(0, 'end')
            self.velue_tax.insert(0, taxnorm)

            img = Image.open(path)
            img = img.resize((800, 500)).save("test.png", quality=95)

            img3 = ImageTk.PhotoImage(file="test.png")
            canvas.itemconfig(image_container,image=img3)

        def updatePass():
            global linkPhoto, img3

            path = filedialog.askopenfilename()

            file = "images/pas2124.png"

            pas = Image.open(path)

            placeIssue = scan(pas, 113, 163, 1363, 391, file,130)
            self.velue_placeIssue.delete(0, 'end')
            self.velue_placeIssue.insert(0, placeIssue)

            dateReg = scan(pas, 116, 397, 754, 475, file, 130)
            self.velue_dateReg.delete(0, 'end')
            self.velue_dateReg.insert(0, dateReg)

            divisionCode = scan(pas, 760, 397, 1356, 475, file,130)
            self.velue_divisionCode.delete(0, 'end')
            self.velue_divisionCode.insert(0, divisionCode)

            pas.crop((1366, 120, 1470, 860)).save(file, quality=95)
            img = Image.open(file)
            img = img.resize((1360, 1361)).rotate(90).resize((700, 150)).save(file, quality=95)
            monochrome(file, 146)
            SerialNumber = pytesseract.image_to_string(file, lang="rus")
            self.velue_SerialNumber.delete(0, 'end')
            self.velue_SerialNumber.insert(0, SerialNumber)

            X11 = 600
            X12 = 1341
            Y12 = 1243

            LastName1 = scan(pas, X11, Y12-72, 1250, Y12, file, 146)
            LastName2 = scan(pas, X11, Y12, X12, Y12+72, file, 146)
            self.velue_LastName.delete(0, 'end')
            self.velue_LastName.insert(0, LastName1 + LastName2)

            Name = scan(pas, X11, Y12+72, X12, Y12+72*2, file, 150)
            self.velue_Name.delete(0, 'end')
            self.velue_Name.insert(0, Name)

            MidleName = scan(pas, X11, Y12+72*2 , X12, Y12+72*3, file, 146)
            self.velue_MiddleName.delete(0, 'end')
            self.velue_MiddleName.insert(0, MidleName)

            # Sex = scan(pas, X11-60,Y12+72*3, 721, Y12+72*4, file, 146)

            Both = scan(pas, X11+236,Y12+72*3, X12, Y12+72*4, file, 146)
            self.velue_Both.delete(0, 'end')
            self.velue_Both.insert(0, Both)

            City1 = scan(pas, X11,Y12+72*4, X12, Y12+72*5, file, 146)
            City2 = scan(pas, X11-50,Y12+72*5, X12, Y12+72*7, file, 146)
            self.velue_City.delete(0, 'end')
            self.velue_City.insert(0, City1 + " " + City2)

            SN = str(self.velue_SerialNumber.get()).strip()

            DC = str(self.velue_divisionCode.get()).strip()

            linkPhoto = ''
            for i in SN:
                if i != ' ':
                    linkPhoto += i
            for i in DC:
                if i != ' ' and i != '-':
                    linkPhoto += i
            linkPhoto = "images/"+linkPhoto+".png"
            pas.crop((103, 1284, 472, 1763)).resize((190,285)).save(linkPhoto, quality=95)

            img = Image.open(path)
            img = img.resize((500, 800)).save("test.png", quality=95)

            img3 = ImageTk.PhotoImage(file="test.png")
            canvas.itemconfig(image_container,image=img3)

        def loadPhoto():
            try:
                global img
                global image_container
                canvas.delete("all")
                img = tk.filedialog.askopenfilename()
                img = Image.open(img)
                img = resizeImage(img, 600)
                image = ImageTk.PhotoImage(img)
                image_container = canvas.create_image(0, 0, anchor='nw', image=image)
                canvas.place(x=400, y=0)
                canvas.config(width=img.width, height=img.height)
                root.mainloop()
            except:
                print("Что то сломалось")

        def reloadPhoto():
            try:
                global img
                global image_container
                canvas.delete("all")
                image = ImageTk.PhotoImage(img)
                image_container = canvas.create_image(0, 0, anchor='nw', image=image)
                canvas.place(x=400, y=0)
                root.mainloop()
            except:
                print("Что то сломалось")

        def resizeImage(image, fixed_w):
            fixed_width = fixed_w
            width_percent = (fixed_width / float(image.size[0]))
            height_size = int((float(image.size[0]) * float(width_percent)))
            new_image = image.resize((fixed_width, height_size))
            return new_image

        def firstPointCrop(event):
            print(event.x, event.y)
            global FirstX
            global FirstY
            FirstX = event.x
            FirstY = event.y
            reloadPhoto()


        def secondPointCrop(event):
            print(event.x, event.y)
            global SecondX
            global SecondY
            global img
            SecondX = event.x
            SecondY = event.y

            if(SecondX < 0):
                SecondX = 0
            if(SecondY < 0):
                SecondY = 0
            if(SecondX > img.width):
                SecondX = img.width
            if (SecondY > img.height):
                SecondY = img.height

            canvas.create_rectangle(FirstX,FirstY,SecondX,SecondY,outline="red")

        def cropImage(img):
            if FirstX == SecondX and FirstY == SecondY:
                return 0

            if img != None:
                if FirstX < SecondX and FirstY < SecondY:
                    croppedImg = img.crop((FirstX, FirstY, SecondX, SecondY))
                elif FirstX < SecondX and FirstY > SecondY:
                    croppedImg = img.crop((FirstX, SecondY, SecondX, FirstY))
                elif FirstX > SecondX and FirstY < SecondY:
                    croppedImg = img.crop((SecondX, FirstY, FirstX, SecondY))
                elif FirstX > SecondX and FirstY > SecondY:
                    croppedImg = img.crop((SecondX, SecondY, FirstX, FirstY))

            return croppedImg




        def scanPhoto(velue, arg = "none"):
            global img
            croppedImg = cropImage(img)

            if arg == "serial":
                croppedImg = croppedImg.rotate(90, expand=True)

            croppedImg.save('pas2124.png', quality=95)
            testPhoto = cv2.imread('pas2124.png')

            config = r'--oem 3 --psm 6'

            tempResult = pytesseract.image_to_string(testPhoto, lang="rus", config=config)

            result = ""

            for i in tempResult:
                if  i != '[' and i != ']' and i != '|' and i != '{' and i != '}':
                    result += i

            velue.delete(0, 'end')
            velue.insert(0, result)

            print(result)
            print("Success")


        def cutPhoto():
            global image_container
            global img
            img = cropImage(img)
            img = resizeImage(img, 600)
            canvas.delete("all")
            image = ImageTk.PhotoImage(img)
            image_container = canvas.create_image(0, 0, anchor='nw', image=image)
            canvas.place(x=400, y=0)
            root.mainloop()

        def loadPassPhoto(X2, Y):
            global image_container
            global img
            global linkPhoto
            photo = cropImage(img)
            photo = resizeImage(photo, 80)
            new_canvas.delete("all")
            image = ImageTk.PhotoImage(photo)
            image_container = new_canvas.create_image(0, 0, anchor='nw', image=image)
            new_canvas.place(x=X2, y=Y + 30*16)
            linkPhoto = "images/"+repr(time.time())+".png"
            photo.save(linkPhoto, quality = 95)
            root.mainloop()






        canvas= Canvas(self, width=800, height= 800)
        canvas.place(x=400, y=50)



        canvas.bind("<ButtonPress-1>", firstPointCrop)
        canvas.bind("<ButtonRelease-1>", secondPointCrop)

        global SecondX
        global SecondY
        global FirstX
        global FirstY
        global img
        global image_container

        SecondX = 0
        SecondY = 0
        FirstX = 0
        FirstY = 0

        img = None


        global linkPhoto
        linkPhoto = ''
        X1 = 50
        Y = 50
        X2 = 260

        new_canvas = Canvas(self, width=80, height=120)
        new_canvas.place(x=X2, y=Y + 30*16)

        self.velue_LastName = ttk.Entry(self)
        self.velue_LastName.place(x=X2, y=Y )
        label_description = tk.Button(self, text='Фамилия:', command=lambda: scanPhoto(self.velue_LastName))
        label_description.place(x=X1, y=Y )

        self.velue_Name = ttk.Entry(self)
        self.velue_Name.place(x=X2, y=Y + 30)
        label_description = tk.Button(self, text='Имя:', command=lambda: scanPhoto(self.velue_Name))
        label_description.place(x=X1, y=Y + 30)

        self.velue_MiddleName = ttk.Entry(self)
        self.velue_MiddleName.place(x=X2, y=Y + 30*2)
        label_description = tk.Button(self, text='Отчество:', command=lambda: scanPhoto(self.velue_MiddleName))
        label_description.place(x=X1, y=Y + 30*2)

        self.velue_Both = ttk.Entry(self)
        self.velue_Both.place(x=X2, y=Y + 30*3)
        label_description = tk.Button(self, text='Дата рождения:', command=lambda: scanPhoto(self.velue_Both))
        label_description.place(x=X1, y=Y + 30*3)

        self.velue_City = ttk.Entry(self)
        self.velue_City.place(x=X2, y=Y + 30*4)
        label_description = tk.Button(self, text='Место рождения:', command=lambda: scanPhoto(self.velue_City))
        label_description.place(x=X1, y=Y + 30*4)

        self.velue_SerialNumber = ttk.Entry(self)
        self.velue_SerialNumber.place(x=X2, y=Y + 30*5)
        serial_description = tk.Button(self, text='Серия и номер:', command=lambda: scanPhoto(self.velue_SerialNumber, "serial"))
        serial_description.place(x=X1, y=Y + 30*5)

        self.velue_dateReg = ttk.Entry(self)
        self.velue_dateReg.place(x=X2, y=Y + 30*6)
        label_description = tk.Button(self, text='Дата выдачи:', command=lambda: scanPhoto(self.velue_dateReg))
        label_description.place(x=X1, y=Y + 30*6)

        self.velue_placeIssue = ttk.Entry(self)
        self.velue_placeIssue.place(x=X2, y=Y + 30*7)
        label_description = tk.Button(self, text='Паспорт выдан:', command=lambda: scanPhoto(self.velue_placeIssue))
        label_description.place(x=X1, y=Y + 30*7)

        self.velue_divisionCode = ttk.Entry(self)
        self.velue_divisionCode.place(x=X2, y=Y + 30*8)
        label_description = tk.Button(self, text='Код подразделения:', command=lambda: scanPhoto(self.velue_divisionCode))
        label_description.place(x=X1, y=Y + 30*8)

        self.velue_agresReg = ttk.Entry(self)
        self.velue_agresReg.place(x=X2, y=Y + 30*9)
        label_description = tk.Button(self, text='Адрес регистрации:', command=lambda: scanPhoto(self.velue_agresReg))
        label_description.place(x=X1, y=Y + 30*9)

        self.velue_SNILS = ttk.Entry(self)
        self.velue_SNILS.place(x=X2, y=Y + 30*10)
        label_description = tk.Button(self, text='СНИЛС:', command=lambda: scanPhoto(self.velue_SNILS))
        label_description.place(x=X1, y=Y + 30*10)

        self.velue_tax = ttk.Entry(self)
        self.velue_tax.place(x=X2, y=Y + 30*11)
        label_description = tk.Button(self, text='ИНН:', command=lambda: scanPhoto(self.velue_tax))
        label_description.place(x=X1, y=Y + 30*11)

        self.velue_birthCertificat = ttk.Entry(self)
        self.velue_birthCertificat.place(x=X2, y=Y + 30*12)
        label_description = tk.Button(self, text='Номер сведетельства о рождении:', command=lambda: scanPhoto(self.velue_birthCertificat))
        label_description.place(x=X1, y=Y + 30*12)

        self.velue_issueCertificate = ttk.Entry(self)
        self.velue_issueCertificate.place(x=X2, y=Y + 30*13)
        label_description = tk.Button(self, text='Орган выдачи сведетельства:', command=lambda: scanPhoto(self.velue_issueCertificate))
        label_description.place(x=X1, y=Y + 30*13)

        self.velue_LNMFather = ttk.Entry(self)
        self.velue_LNMFather.place(x=X2, y=Y + 30*14)
        label_description = tk.Button(self, text='ФИО отца:', command=lambda: scanPhoto(self.velue_LNMFather))
        label_description.place(x=X1, y=Y + 30*14)

        self.velue_LNMMather = ttk.Entry(self)
        self.velue_LNMMather.place(x=X2, y=Y + 30*15)
        label_description = tk.Button(self, text='ФИО матери:', command=lambda: scanPhoto(self.velue_LNMMather))
        label_description.place(x=X1, y=Y + 30*15)

        label_description = tk.Button(self, text='Фото:', command=lambda: loadPassPhoto(X2, Y))
        label_description.place(x=X1, y=Y + 30*16)


        # label_description = tk.Label(self, text='Ссылка на фото:')
        # label_description.place(x=X1, y=Y + 30*16)
        # self.velue_LinkPhoto = ttk.Entry(self)
        # self.velue_LinkPhoto.place(x=X2, y=Y + 30*16)

        self.btn_ok= ttk.Button(self, text="Сканировать фото", command=lambda: loadPhoto())
        self.btn_ok.place(x=60, y=Y + 30*20)

        self.btn_cut= ttk.Button(self, text="Обрезать", command=lambda: cutPhoto())
        self.btn_cut.place(x=200, y=Y + 30*20)



        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(
            self.velue_LastName.get(),
            self.velue_Name.get(),
            self.velue_MiddleName.get(),
            self.velue_Both.get(),
            self.velue_City.get(),
            self.velue_SerialNumber.get(),
            self.velue_dateReg.get(),
            self.velue_placeIssue.get(),
            self.velue_divisionCode.get(),
            self.velue_agresReg.get(),
            self.velue_SNILS.get(),
            self.velue_tax.get(),
            self.velue_birthCertificat.get(),
            self.velue_issueCertificate.get(),
            self.velue_LNMFather.get(),
            self.velue_LNMMather.get(),
            linkPhoto
        ))

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y= Y + 30*21+50)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(
            self.velue_LastName.get(),
            self.velue_Name.get(),
            self.velue_MiddleName.get(),
            self.velue_Both.get(),
            self.velue_City.get(),
            self.velue_SerialNumber.get(),
            self.velue_dateReg.get(),
            self.velue_placeIssue.get(),
            self.velue_divisionCode.get(),
            self.velue_agresReg.get(),
            self.velue_SNILS.get(),
            self.velue_tax.get(),
            self.velue_birthCertificat.get(),
            self.velue_issueCertificate.get(),
            self.velue_LNMFather.get(),
            self.velue_LNMMather.get(),
            linkPhoto
        ))

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=Y + 30*21+50)

        self.grab_set()
        self.focus_set()






class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app
        self.db = db
        self.default_data()

    def init_edit(self):
        self.title('Редактировать позицию')
        btn_edit = ttk.Button(self, text='Редактировать')
        btn_edit.place(x=200, y=50 + 30*21+50)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(
            self.velue_LastName.get(),
            self.velue_Name.get(),
            self.velue_MiddleName.get(),
            self.velue_Both.get(),
            self.velue_City.get(),
            self.velue_SerialNumber.get(),
            self.velue_dateReg.get(),
            self.velue_placeIssue.get(),
            self.velue_divisionCode.get(),
            self.velue_agresReg.get(),
            self.velue_SNILS.get(),
            self.velue_tax.get(),
            self.velue_birthCertificat.get(),
            self.velue_issueCertificate.get(),
            self.velue_LNMFather.get(),
            self.velue_LNMMather.get(),
            self.velue_LinkPhoto.get()
        ))

        self.btn_ok.destroy()

    def default_data(self):
        self.db.c.execute('''SELECT * FROM DataBase WHERE id=?''',
                          (self.view.tree.set(self.view.tree.selection()[0], '#1'),))
        row = self.db.c.fetchone()
        self.velue_LastName.insert(0, row[1])
        self.velue_Name.insert(0, row[2])
        self.velue_MiddleName.insert(0, row[3])
        self.velue_Both.insert(0, row[4])
        self.velue_City.insert(0, row[5])
        self.velue_SerialNumber.insert(0, row[6]),
        self.velue_dateReg.insert(0, row[7])
        self.velue_placeIssue.insert(0, row[8])
        self.velue_divisionCode.insert(0, row[9])
        self.velue_agresReg.insert(0, row[10])
        self.velue_SNILS.insert(0, row[11])
        self.velue_tax.insert(0, row[12])
        self.velue_birthCertificat.insert(0, row[13])
        self.velue_issueCertificate.insert(0, row[14])
        self.velue_LNMFather.insert(0, row[15])
        self.velue_LNMMather.insert(0, row[16])
        self.velue_LinkPhoto.insert(0, row[17])


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title('Поиск')
        self.geometry('300x100+400+300')
        self.resizable(False, False)

        label_search = tk.Label(self, text='Поиск')
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text='Поиск')
        btn_search.place(x=105, y=50)

        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('DataBase.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS DataBase (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , lastName text, Name text, middleName text, both text, city text, serialNumber intager, dateReg text, placeIssue text, divisionCode intager, agresReg text, SNILS text, tax, birthCertificat text, issueCertificate text, LNMFather text, LNMMather text, LinkPhoto text )''')
        self.conn.commit()

    def insert_data(self, lastName, Name, middleName, both, city, serialNumber, dateReg, placeIssue, divisionCode, agresReg, SNILS, tax, birthCertificat, issueCertificate, LNMFather, LNMMather, LinkPhoto ):
        self.c.execute('''INSERT INTO DataBase( lastName, Name, middleName, both, city, serialNumber, dateReg, placeIssue, divisionCode, agresReg, SNILS, tax, birthCertificat, issueCertificate, LNMFather, LNMMather, LinkPhoto ) VALUES (?, ?, ?, ?, ?, ?,?,?,?,?,?,?,?,?,?,?,?)''',(
         lastName,
         Name,
         middleName,
         both,
         city,
         serialNumber,
         dateReg,
         placeIssue,
         divisionCode,
         agresReg,
         SNILS,
         tax,
         birthCertificat,
         issueCertificate,
         LNMFather,
         LNMMather,
         LinkPhoto ))
        self.conn.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("ReadPass")
    root.geometry("1280x720")
    root.resizable(True, True)
    root.mainloop()