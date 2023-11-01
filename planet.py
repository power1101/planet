import math
def period(r_,R_):
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
    return f'planet retrograde period :{2*t:7.3f}days'
