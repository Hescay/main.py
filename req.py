def phone_data():
    phone_data_win = displayframe

    search_model_label = tk.Label(phone_data_win, text="SEARCH MODEL")
    search_model_label.grid()

    search_model_entry = tk.Entry(phone_data_win)
    search_model_entry.grid()

    def phone_model():
        try:
            data = pd.read_csv('file.csv')
            data_file = data.drop(columns=data.columns[2:6])
            data_file = data_file.to_dict()

            data_file.get('PHONE NAME')

            input_model = search_model_entry.get()
            model_key = [x for x in data_file['PHONE MODEL'].keys() if data_file['PHONE MODEL']
            [x] == input_model.upper()][0]

            result = (data_file['PHONE NAME'][model_key])

            tk.messagebox.showinfo('SUCCESS', result)

        except IndexError as err:
            tk.messagebox.showerror('ERROR', 'WRONG MODEL NUMBER')

    search_button = tk.Button(phone_data_win, text='SEARCH', foreground='purple', command=phone_model)
    search_button.grid()

    phone_data_win.mainloop()
