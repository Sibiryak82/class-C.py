# Файл timerdecol.py
# Предостережение: область все же отличается - в Python 2.X,
# итерируемый объект в Python 3.X
# Предостережение: в таком виде timer не будет работать с методами
# ( см. ответ на контрольный вопрос)

# немогу разобраться в чем проблема, заменил time.clock() на time.process_time() работает частично

import time, sys

forse = list if sys.version_info[0] == 3 else (lambda X: X)

class timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0
    def __call__(self, *args, **kargs):
        start = time.process_time()
        result = self.func(*args, **kargs)
        elapsed = time.process_time() - start
        self.alltime += elapsed
        print('%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime))
        return result

@timer
def listcomp(N):
    return [x * 2 for x in range(N)]

@timer
def mapcall(N):
    return force(map((lambda x: x * 2), range(N)))

result = listcomp(5)

listcomp(50000)
listcomp(500000)
listcomp(1000000)
print(result)
print('allTime = %s' % listcomp.alltime)
print('')
result = mapcall(5)
mapcall(50000)
mapcall(500000)
mapcall(1000000)
print(result)
print('allTime = %s' % mapcall.alltime)

print('\n**map/comp = %s' % round(mapcall.alltime / listcomp.alltime, 3))
            
