from pprint import pprint
from indexes import ForwardIndex,InvertedIndex

FW_Index = None
IW_Index = None


def set_directory():
    global FW_Index, IW_Index
    dir_path = input('Enter directory path where text files will be indexed: ') or 'test'
    FW_Index = ForwardIndex(dir_path)
    IW_Index = InvertedIndex(dir_path)


def build_indexes():
    global FW_Index, IW_Index
    if FW_Index and IW_Index:
        FW_Index.build_index()
        IW_Index.build_index()
        print('\nIndexes built successfully\n')
    else:
        print('\nDirectory for indexes not set\n')


def search_with_indexes():
    global FW_Index, IW_Index
    if FW_Index and IW_Index:
        search_word = input('Enter search word: ')
        print('\nForward index search result:')
        pprint(FW_Index.search(search_word))
        print('\nInverted index search result:')
        pprint(IW_Index.search(search_word))
    else:
        print('\nDirectory for indexes not set\n')


def show_indexes_structure():
    global FW_Index, IW_Index
    if FW_Index and IW_Index:
        print('\nForward index:')
        pprint(FW_Index.index)
        print('\nInverted index:')
        pprint(IW_Index.index)
    else:
        print('\nDirectory for indexes not set\n')


def main_menu():
    while True:
        print('\nSelect option:')
        print('1. Set directory')
        print('2. Build indexes')
        print('3. Search with indexes')
        print('4. Show indexes structure')
        print('5. Exit\n')
        option = input()
        match option:
            case '1':
                set_directory()
            case '2':
                build_indexes()
            case '3':
                search_with_indexes()
            case '4':
             show_indexes_structure()
            case '5':
                break

    
if __name__ == '__main__':
    main_menu()
