import math
def period(r_,R_):
    A = {'수성': 0.387, '금성': 0.723, '지구': 1, '화성': 1.524, '목성': 5.2, '토성': 9.54, '천왕성': 19.19, '해왕성': 30.68}
    for i in A:
        if r_ == i: r_ = A[i]
        if R_ == i: R_ = A[i]
    R = max(r_, R_)
    r = min(r_, R_)
    Tr = r**1.5  # 안쪽 행성의 공전 주기
    TR = R**1.5  # 바같쪽 행성이 공전 주기
    Ts = Tr*TR/(TR-Tr)  # 회합 주기
    x = math.asin(Ts/r*((R**2-r**2)/(TR**2+TR*Ts*2))**0.5)  # 접선의 각
    xd = math.degrees(x)  # 육십분법으로
    b = math.asin(r/R*math.cos(x))  # 내행성 이각
    bd = math.degrees(b)  # 육십분법으로
    ad = 90-xd-bd  # 유 중심각
    t = ad/360*365*Ts  # 내합 또는 충에서 유까지 시간
    bm = math.asin(r / R)  # 최대 이각
    bmd = math.degrees(bm)  # 육십분법으로
    T = (90-bmd) / 360 * 365 * Ts  # 내합에서 최대이각까지의 시간
    return f' 최대이각(내행성): {bmd:6.3f}°, 유 이각(내행성): {bd:6.3f}°, 유 이각(외행성): {180-ad-bd:7.3f}°' \
           f', 회합주기:{Ts*365:7.3f}일, 최대이각-유(구-유): {T-t:6.3f}일, 역행 일수 :{2*t:7.3f}일'
