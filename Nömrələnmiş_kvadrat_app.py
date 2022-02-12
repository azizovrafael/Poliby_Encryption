from tkinter import *
from itertools import cycle

hard_dictionary = {
"a":"11", "b":"12", "c":"13", "d":"14", "e":"15",
"f":"21", "g":"22", "h":"23", "i":"24", "k":"25",
"l":"31", "m":"32", "n":"33", "o":"34", "p":"35",
"q":"41", "r":"42", "s":"43", "t":"44", "u":"45",
"v":"51", "w":"52", "x":"53", "y":"54", "z":"55",
}
root = Tk()

root.geometry('500x300')
root.resizable(0,0)
root.title("Rafael") # Atyən   \U0001F49C

Label(root, text ='Şifrələmə və Deşifrələmə', font = 'arial 20 bold').pack()

Label(root, text ='Vijner ', font = 'arial 20 bold').pack(side =BOTTOM)

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

def Encode(fraze : str):
    new_txt = ""
    list_fraze = list(fraze)
    for x in fraze.lower():
        if x in hard_dictionary:
            new_txt += hard_dictionary.get(x)
        else:
            new_txt += (x + x)
    return new_txt

def Decode(fraze):
    new_txt = ""
    list_fraze = []
    # str to list with letter length steep
    step = 2
    for i in range(0, len(fraze), 2):
        list_fraze.append(fraze[i:step])
        step += 2
    # list to decode fraze
    key_hard_dictionary_list = list(hard_dictionary.keys())
    val_hard_dictionary_list = list(hard_dictionary.values())

    for x in list_fraze:
        if x in val_hard_dictionary_list:
            i = val_hard_dictionary_list.index(x)
            new_txt += key_hard_dictionary_list[i]
        else:
            new_txt += x[0:1]
    return new_txt


def Mode():
    if(mode.get() == 's'):
        Result.set(Encode(Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(Text.get()))
    else:
        Result.set('Mod Təyin Edilməyib')

def Exit():
    root.destroy()

def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")

Label(root, font= 'arial 12 bold', text='Mətin').place(x= 60,y=60)
Entry(root, font = 'arial 10', textvariable = Text, bg = 'ghost white').place(x=290, y = 60)

#Label(root, font = 'arial 12 bold', text ='Açar').place(x=60, y = 90)
#Entry(root, font = 'arial 10', textvariable = private_key , bg ='ghost white').place(x=290, y = 90)

Label(root, font = 'arial 12 bold', text ='MOD(s-Şifrələmə, d-Deşifrələmə)').place(x=60, y = 120)
Entry(root, font = 'arial 10', textvariable = mode , bg= 'ghost white').place(x=290, y = 120)
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='ghost white').place(x=290, y = 150)

Button(root, font = 'arial 10 bold', text = 'Nəticə'  ,padx =2,bg ='LightGray' ,command = Mode).place(x=60, y = 150)

Button(root, font = 'arial 10 bold' ,text ='Təmizləmək' ,width =10, command = Reset,bg = 'LimeGreen', padx=2).place(x=80, y = 190)

Button(root, font = 'arial 10 bold',text= 'Çıxış' , width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=180, y = 190)

root.mainloop()
