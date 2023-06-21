import tkinter as tk
import pyperclip

# ==================================
# Applicationオブジェクトクラスの定義
# ==================================
#メインウィンドウ－－フレーム－－ウィジェット
#メインウィンドウ = tk.Tk()
# サブウィンドウ名 = tk.Toplevel(
# 背景色bg,ボーダーbd,カーソル指定cursor,ウィンドウの外観設定relief,高さheight,幅width)
#配置pack, grid, place
#pack : どこに寄せるかanchor(),親とサイズを合わせるexpand,スペースを埋めるfill,外隙間padx,pady
#       内隙間ipadx,ipady,つめる方向side
#grid : 配置する列column,何列にわたって配置するかcolumnspan,padx,pady,ipadx,ipady
#       配置する行row,何行にわたって配置するかrowspan,pack+anchor+fill=sticky
#place: 

class DesktopApp(tk.Frame):

    # ======================================
    # アプリケーションオブジェクト初期設定
    # ======================================
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        
        # ウィンドウの設定
        self.master.title("Copy&Paste App")    # タイトル
        self.master.geometry("600x400")     # サイズ

        # サイズ調整
        self.pack_propagate(0)

        
        # フレーム作成
        self.frame()
        # ウィジェット作成
        self.widgets()


        


    # ======================================
    # フレーム作成
    # ======================================

    #フレーム：Frame,Labelframe
    #フレーム名 = tk.Frame(親指定,幅width,高さheight,フレームの枠指定relief,背景色bg,ボーダーbd,
    #           マウスポインタの見た目cursor,枠とテキストとの間の縦の空白pady,横の空白padx
    #           Tabキーでのフォーカス移動の有無10)

    def frame(self):
        
        self.frame1 = tk.Frame(self.master,padx=10, pady=5, bg="#D8D8D8")
        self.frame1.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.1)

        self.frame2 = tk.Frame(self.master,padx=10, pady=5, bg="#E6E6E6")
        self.frame2.place(relx=0.0, rely=0.1, relwidth=1.0, relheight=0.1)

        self.frame3 = tk.Frame(self.master,padx=10, pady=5, bg="#D8D8D8")
        self.frame3.place(relx=0.0, rely=0.2, relwidth=1.0, relheight=0.1)

        self.frame4 = tk.Frame(self.master,padx=10, pady=5, bg="#E6E6E6")
        self.frame4.place(relx=0.0, rely=0.3, relwidth=1.0, relheight=0.1)

        self.frame5 = tk.Frame(self.master,padx=10, pady=5, bg="#D8D8D8")
        self.frame5.place(relx=0.0, rely=0.4, relwidth=1.0, relheight=0.1)

        self.frame6 = tk.Frame(self.master,padx=10, pady=5, bg="#E6E6E6")
        self.frame6.place(relx=0.0, rely=0.5, relwidth=1.0, relheight=0.1)

        self.frame7 = tk.Frame(self.master,padx=10, pady=5, bg="#D8D8D8")
        self.frame7.place(relx=0.0, rely=0.6, relwidth=1.0, relheight=0.1)

        self.frame8 = tk.Frame(self.master,padx=10, pady=5, bg="#E6E6E6")
        self.frame8.place(relx=0.0, rely=0.7, relwidth=1.0, relheight=0.1)

        self.frame9 = tk.Frame(self.master,padx=10, pady=5, bg="#D8D8D8")
        self.frame9.place(relx=0.0, rely=0.8, relwidth=1.0, relheight=0.1)

        self.frame10 = tk.Frame(self.master,padx=10, pady=5, bg="#E6E6E6")
        self.frame10.place(relx=0.0, rely=0.9, relwidth=1.0, relheight=0.1)

    # ======================================
    # ウィジェット作成
    # ======================================

    #ウィジェット:文字Label,ボタン,Button,文字入力Entry,データ一覧表示Listbox,クリックでon/off切替Checkbutton,
    #           クリックでon/off切替Radiobutton,スライド調整Scale,文字列表示Message,プルダウン選択Combobox,
    #           アイテムをツリー表示Treeview,進捗状況表示Progressbar,Tab切替Notebook,調整可能なテキストボックスSpinbox
    #ウィジェット名 = tk.ウィジェット名(親指定,オプション)
    #Label = text,bg,bd,3D表示relief(flat,raised,sunken,groove,ridge),文字の色fg,font
    #button = text,command
    #entry = bg,bd,relief,textvariable,Entryに値を.set(),.get(),.delete()


    def widgets(self):
        #1行目
        self.btn1_copy = tk.Button(self.frame1, text="", command=lambda:self.copy(self.entry1))
        self.btn1_edit = tk.Button(self.frame1, text="編集", command=lambda:self.edit(self.entry1,self.btn1_determine,self.btn1_copy,self.btn1_edit))
        self.btn1_determine = tk.Button(self.frame1, text="決定", command=lambda:self.determine(self.entry1,self.btn1_determine,self.btn1_copy,self.btn1_edit))
        self.entry1 = tk.Entry(self.frame1)
        self.btn1_edit.place(relx=0.9, rely=0, relwidth=0.1, relheight=1.0)
        self.btn1_copy.place(relx=0.0, rely=0, relwidth=0.85, relheight=1.0)
        #2行目
        self.btn2_copy = tk.Button(self.frame2, text="", command=lambda:self.copy(self.entry2))
        self.btn2_edit = tk.Button(self.frame2, text="編集", command=lambda:self.edit(self.entry2,self.btn2_determine,self.btn2_copy,self.btn2_edit))
        self.btn2_determine = tk.Button(self.frame2, text="決定", command=lambda:self.determine(self.entry2,self.btn2_determine,self.btn2_copy,self.btn2_edit))
        self.entry2 = tk.Entry(self.frame2)
        self.btn2_edit.place(relx=0.9, rely=0, relwidth=0.1, relheight=1.0)
        self.btn2_copy.place(relx=0.0, rely=0, relwidth=0.85, relheight=1.0)
        #3行目
        self.btn3_copy = tk.Button(self.frame3, text="", command=lambda:self.copy(self.entry3))
        self.btn3_edit = tk.Button(self.frame3, text="編集", command=lambda:self.edit(self.entry3,self.btn3_determine,self.btn3_copy,self.btn3_edit))
        self.btn3_determine = tk.Button(self.frame3, text="決定", command=lambda:self.determine(self.entry3,self.btn3_determine,self.btn3_copy,self.btn3_edit))
        self.entry3 = tk.Entry(self.frame3)
        self.btn3_edit.place(relx=0.9, rely=0, relwidth=0.1, relheight=1.0)
        self.btn3_copy.place(relx=0.0, rely=0, relwidth=0.85, relheight=1.0)
        #4行目
        self.btn4_copy = tk.Button(self.frame4, text="", command=lambda:self.copy(self.entry4))
        self.btn4_edit = tk.Button(self.frame4, text="編集", command=lambda:self.edit(self.entry4,self.btn4_determine,self.btn4_copy,self.btn4_edit))
        self.btn4_determine = tk.Button(self.frame4, text="決定", command=lambda:self.determine(self.entry4,self.btn4_determine,self.btn4_copy,self.btn4_edit))
        self.entry4 = tk.Entry(self.frame4)
        self.btn4_edit.place(relx=0.9, rely=0, relwidth=0.1, relheight=1.0)
        self.btn4_copy.place(relx=0.0, rely=0, relwidth=0.85, relheight=1.0)
        #2行目
        self.btn5_copy = tk.Button(self.frame5, text="", command=lambda:self.copy(self.entry5))
        self.btn5_edit = tk.Button(self.frame5, text="編集", command=lambda:self.edit(self.entry5,self.btn5_determine,self.btn5_copy,self.btn5_edit))
        self.btn5_determine = tk.Button(self.frame5, text="決定", command=lambda:self.determine(self.entry5,self.btn5_determine,self.btn5_copy,self.btn5_edit))
        self.entry5 = tk.Entry(self.frame5)
        self.btn5_edit.place(relx=0.9, rely=0, relwidth=0.1, relheight=1.0)
        self.btn5_copy.place(relx=0.0, rely=0, relwidth=0.85, relheight=1.0)
        #6行目
        self.btn6_copy = tk.Button(self.frame6, text="", command=lambda:self.copy(self.entry6))
        self.btn6_edit = tk.Button(self.frame6, text="編集", command=lambda:self.edit(self.entry6,self.btn6_determine,self.btn6_copy,self.btn6_edit))
        self.btn6_determine = tk.Button(self.frame6, text="決定", command=lambda:self.determine(self.entry6,self.btn6_determine,self.btn6_copy,self.btn6_edit))
        self.entry6 = tk.Entry(self.frame6)
        self.btn6_edit.place(relx=0.9, rely=0, relwidth=0.1, relheight=1.0)
        self.btn6_copy.place(relx=0.0, rely=0, relwidth=0.85, relheight=1.0)
        #7行目
        self.btn7_copy = tk.Button(self.frame7, text="", command=lambda:self.copy(self.entry7))
        self.btn7_edit = tk.Button(self.frame7, text="編集", command=lambda:self.edit(self.entry7,self.btn7_determine,self.btn7_copy,self.btn7_edit))
        self.btn7_determine = tk.Button(self.frame7, text="決定", command=lambda:self.determine(self.entry7,self.btn7_determine,self.btn7_copy,self.btn7_edit))
        self.entry7 = tk.Entry(self.frame7)
        self.btn7_edit.place(relx=0.9, rely=0, relwidth=0.1, relheight=1.0)
        self.btn7_copy.place(relx=0.0, rely=0, relwidth=0.85, relheight=1.0)
        #8行目
        self.btn8_copy = tk.Button(self.frame8, text="", command=lambda:self.copy(self.entry8))
        self.btn8_edit = tk.Button(self.frame8, text="編集", command=lambda:self.edit(self.entry8,self.btn8_determine,self.btn8_copy,self.btn8_edit))
        self.btn8_determine = tk.Button(self.frame8, text="決定", command=lambda:self.determine(self.entry8,self.btn8_determine,self.btn8_copy,self.btn8_edit))
        self.entry8 = tk.Entry(self.frame8)
        self.btn8_edit.place(relx=0.9, rely=0, relwidth=0.1, relheight=1.0)
        self.btn8_copy.place(relx=0.0, rely=0, relwidth=0.85, relheight=1.0)
        #9行目
        self.btn9_copy = tk.Button(self.frame9, text="", command=lambda:self.copy(self.entry9))
        self.btn9_edit = tk.Button(self.frame9, text="編集", command=lambda:self.edit(self.entry9,self.btn9_determine,self.btn9_copy,self.btn9_edit))
        self.btn9_determine = tk.Button(self.frame9, text="決定", command=lambda:self.determine(self.entry9,self.btn9_determine,self.btn9_copy,self.btn9_edit))
        self.entry9 = tk.Entry(self.frame9)
        self.btn9_edit.place(relx=0.9, rely=0, relwidth=0.1, relheight=1.0)
        self.btn9_copy.place(relx=0.0, rely=0, relwidth=0.85, relheight=1.0)
        #8行目
        self.btn10_copy = tk.Button(self.frame10, text="", command=lambda:self.copy(self.entry10))
        self.btn10_edit = tk.Button(self.frame10, text="編集", command=lambda:self.edit(self.entry10,self.btn10_determine,self.btn10_copy,self.btn10_edit))
        self.btn10_determine = tk.Button(self.frame10, text="決定", command=lambda:self.determine(self.entry10,self.btn10_determine,self.btn10_copy,self.btn10_edit))
        self.entry10 = tk.Entry(self.frame10)
        self.btn10_edit.place(relx=0.9, rely=0, relwidth=0.1, relheight=1.0)
        self.btn10_copy.place(relx=0.0, rely=0, relwidth=0.85, relheight=1.0)



    # ======================================
    # イベント処理
    # ======================================
    def edit(self, entry,determine,copy,edit):
        edit.place_forget()
        copy.place_forget()
        entry.place(relx=0.0, rely=0, relwidth=0.85, relheight=1.0)
        determine.place(relx=0.9, rely=0, relwidth=0.1, relheight=1.0)


    def copy(self, entry):
        pyperclip.copy(entry.get())
    
    def determine(self,entry,determine,copy,edit):
        entry.place_forget()
        determine.place_forget()
        copy["text"] = entry.get()
        edit.place(relx=0.9, rely=0, relwidth=0.1, relheight=1.0)
        copy.place(relx=0.0, rely=0, relwidth=0.85, relheight=1.0)




# ==================================
# アプリケーション起動
# ==================================
if __name__=="__main__":
    root = tk.Tk()
    app = DesktopApp(master=root)
    app.mainloop()