# Composition Relationship :자동차-엔진 처럼 밀접한 관계
# class diagram :채워진 다이아몬드
class Engine:
    def __init__(self):
        print('새로운 엔진입니다..')
    
    def start(self):
        print('엔진 동작하는 중')

class Car:
    def __init__(self):
        print('붕붕카')
        self.engine = Engine()
        print('엔진 장착')

    def run(self):
        self.engine.start()

c = Car()
c.run()
