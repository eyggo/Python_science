import math
import matplotlib.pyplot as plt
if __name__ == '__main__':
    a=0
    y=[]
    print('-'*50)
    print("물체의 낙하운동에서 물체의 반발 거리를 구한다")
    print('-'*50)
    print('중력가속도 = 10m/s^2')
    print('높이 단위 = m')
    print('질량 단위 = kg')
    print('-'*50)
    print('아래에 값을 입력하세요!')
    h = int(input("물체의 높이 = "))
    e = float(input("적용할 반발계수 = "))
    m = int(input("물체의 질량 = "))
    print('-'*50)
    print('중력가속도 = 10m/s^2')
    print('높이 단위 = m')
    print('질량 단위 = kg')
    print('물체의 높이 = '+str(h))
    print('지면과의 반발계수 = '+str(e))
    print('물체의 질량 = '+str(m))
    print('-'*50)

    
    while(1):
        a+=1
        t = math.sqrt((2 * h)/10 )
        E = m*10*h 
        E2=(e*e)*E
        E2=int(E2)
        H2=(e*e)*h
        H2=round(float(H2),2)

        print(str(a)+'번째'+'-'*50)
        print("물체가 0m에 도달하는데 걸리는 시간 = "+str(t))
        print("물체의 역학적 에너지의 총 합 = "+str(E)+'J')

       
        print("지면과 충돌 후 역학적 에너지 = "+str(E2)+"J")
        print("지면과 충돌 후 뛰어오르는 높이 = "+str(H2)+"m")
        print('-'*50)
        h=H2
        y.append(H2)
        if h<1:
            break
    
    plt.plot(a,y)
    plt.show()