if __name__ == '__main__':

    with open('data.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()[0]
    print(data)