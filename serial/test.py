import serial
import threading

ser = serial.Serial('COM3', timeout = 1,  ) 
alivethread = True
read = 0

print('Start')
print(ser.name)
print(ser.baudrate)
#ser.write(b'dasdfasdf475 ')

print('Reading')
read = ser.readline().decode('ascii')
print('Reading: ', read)


# 쓰레드
def readthread(ser):
    global line
    
    # 쓰레드 종료될때까지 계속 돌림
    while alivethread:
        # 데이터가 있있다면
        for c in ser.read():
            # line 변수에 차곡차곡 추가하여 넣는다.
            line += (chr(c))
            if line.startswith('[') and line.endswith(']'):  # 라인의 끝을 만나면..
                # 데이터 처리 함수로 호출
                print('receive data=' + line)
                # line 변수 초기화
                line = ''

    ser.close()


def main():

    # 시리얼 읽을 쓰레드 생성
    thread = threading.Thread(target=readthread, args=(ser,))
    thread.start()

    count = 10
    while count > 0:
        strcmd = '[test' + str(count) + ']'
        print('send data=' + strcmd)
        ser.write(strcmd.encode())
        time.sleep(1)
        count -= 1
        
    alivethread = False


#main()
#bcc = 0
#identifier = 0
#etc = 0
#
#
#data = bytearray(b'\xfa\x02\x02\x2a\xfe\x0c')
#
#bcc = identifier ^ data ^ etc
#
#No = ser.write(data)
#
#print(data)                    # data 출력
#dataIn = ser.readline()        
#print(dataIn)                  # 받은 data 출력
#
#ser.close()