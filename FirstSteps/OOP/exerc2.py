class Editor():

    def view_document(self):
        print('View document')

    def edit_document(self):
        print('Edit document only for paid version')


class ProEditor(Editor):
    def edit_document(self):
        print('Edit document is enable')


def main():
    key = input('Input the key to unlock : ')
    if key == 'fuckthemillenium':
        print('program is full open')
        editor = ProEditor()
    else:
        print('The key is invalid, please input correct key')
        editor = Editor()




if __name__ == '__main__':
    main()
