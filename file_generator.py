import random
import datetime


def main():
    '''
    Генератор файла со случайными значениями
    '''
    name = str(datetime.datetime.now().strftime('%Y%m%d%H%M%S')) + '.test'
    f = open(name, 'w')
    count = random.randint(9000, 10000)
    for _ in range(count):
        x = random.randint(0, 10000)
        y = random.randint(0, 10000)
        z = random.randint(0, 10000)
        i = random.randint(1, 255)
        f.write(f'{x} {y} {z} {i}\n')
    f.close()


if __name__ == '__main__':
    main()
