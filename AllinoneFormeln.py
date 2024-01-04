import math


def rad_2_deg(rad):
    deg = rad * 180 / math.pi
    return deg


def deg_2_rad(deg):
    rad = deg * math.pi / 180
    return rad


def kmh_2_ms(km_pro_s):
    return km_pro_s * 1000 / (60 * 60)


g = 9.81
km_h_2_m_s = 5 / 18


def auto_beschleunigung(end_v, t):
    v = end_v * 1000 / (60 * 60)
    # v=a*t
    # a=v/t
    # v=a*t
    a = v / t
    print(a)
    x = 0 + 0 + a * 0.5 * t * t
    print(x)
    return a


def auto_beschleunigung2(end_v, t):
    v = end_v * 0.27778
    # v=a*t
    # a=v/t
    # v=a*t
    a = v / t
    print(a)
    x = 0 + 0 + a * 0.5 * t * t
    print(x)


kmh = kmh_2_ms(1)
print(kmh)
auto_beschleunigung(50, 8)
auto_beschleunigung2(50, 8)
print("kind")


def kind():
    # bremsen = -8 m/(s*s)
    # bremsvorgang start nach 1 s
    # v0 = 50 km/h
    # v = a*t
    # 50*0.27778 = 8 * t
    t = (50 * (5 / 18)) / 8
    s_reaktion = 1 * 50 * (5 / 18)
    print(f"sreaktion:{s_reaktion}")
    s_brems = 0.5 * 8 * t * t
    print(f"sbresm:{s_brems}")
    s_gesamt = s_reaktion + s_brems
    print(f"gesamt {s_gesamt}")


kind()

print("student")


def student():
    # 15 m/s up
    # v=g*t
    # t=v/g
    t = 15 / g
    peak = 0.5 * g * t * t
    print(f"peak time:{t}")
    print(f"peak:{peak}")
    round_trip = t * 2
    print(f"round trip:{round_trip}")
    pass


student()


def schwimmer():
    print("Schwimmer")
    v_x = 1.6
    y = 40
    # v_x*t=80
    t = 80 / v_x
    v_y = y / t
    print(f"v(wasser):{v_y}")
    v_abs = (v_y ** 2 + v_x ** 2) ** 0.5
    print(f"v(absulut):{v_abs}")
    # cos(alpha)=v_y/v_x
    alpha = math.acos(v_y / v_x)
    print(f"relativ zum x:{math.degrees(alpha)}")


schwimmer()


class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


def wurf_v_x(v_magnitude, alpha):
    return v_magnitude * math.cos(alpha)


def wurf_v_y(v_magnitude, alpha):
    return v_magnitude * math.sin(alpha)


def peak_height(v, alpha):
    v_y = math.sin(alpha) * v
    # v_y=g*t
    t = v_y / g
    return 0.5 * g * t * t


def peak_time(v, alpha):
    v_y = math.sin(alpha) * v
    t = v_y / g
    return t


def wurf_s_x(v, alpha):
    v_y = math.sin(alpha) * v
    t = v_y / g
    t = t * 2  # up and down
    v_x = math.cos(alpha)
    s_x = v_x * t
    return s_x


print(f"Kanone:")


def kanone():
    alpha = math.radians(55)
    v = 70
    height = 150
    peak = peak_height(v, alpha) + height
    print(f"peak:{peak}")
    # peak=0.5*g*t*t
    # t=(peak/g*2)**0.5
    down_t = (peak * 2 / g) ** 0.5
    peak_t = peak_time(v, alpha)
    total_t = down_t + peak_t
    v_x = math.cos(alpha) * v
    s_x = v_x * total_t
    print(s_x)
    v_end = (v_x ** 2 + (down_t * g) ** 2) ** 0.5
    print(v_end)


kanone()

print("rotation")

print("Helicopter")


def heli():
    r = 15 / 2
    d_t = 30
    v_w = (260 / 60) * 2 * math.pi
    a_w = v_w / d_t
    v_b = r * v_w
    a_z = r * v_w * v_w
    print(f"winkelgeschwidigkeit: {v_w} "
          f"Winkelbeschleunigung:{a_w}"
          f" Bahn_v:{v_b} zentripedal_a:{a_z}")


heli()

print("Bremsen")


def brems_weg_horizontal(v, reibungs_koeffizient):
    t = v / g / reibungs_koeffizient
    s = 0.5 * g * reibungs_koeffizient * t * t
    return s


bremsweg = brems_weg_horizontal(30, 0.5)
bremsweg2 = brems_weg_horizontal(30, 0.3)
print(f"abs:{bremsweg}  no_abs:{bremsweg2}")


def besch_massen():
    print("beschleunigte massen")
    m1 = 2
    m2 = 8
    f_g = m2 * g
    # F=a*m
    a = f_g / (m1 + m2)
    print(a)
    print("mit müh")
    gleitreibungs_koeffizient = 0.65
    f_h = gleitreibungs_koeffizient * 1 * g * 2
    f = f_g - f_h
    a = f / (m1 + m2)
    print(a)


besch_massen()


def schlitten():
    print("schlitten")

    # wenn f horizont = f
    alpha = math.radians(30)
    koeffizient = 0.1
    m = 65
    f_g = m * g
    f_down = f_g
    # f_r= (f_down-f_tot*sin(alpha))*koeffizient
    # f_r=f_tot*cos(alpha)
    # f_tot*cos(alpha)=(f_down-f_tot*sin(alpha))*koeffizient
    # cos(alpha)=f_down*koeffizient/f_tot-sin(alpha)*koeffizient
    # cos(alpha)+sin(alpha)*koeffizient=f_down*koeffizient/f_tot
    f = (f_down * koeffizient) / (math.cos(alpha) + math.sin(alpha) * koeffizient)
    print(f)
    print(f" arbeit:{f * 1000 * math.cos(alpha)}")
    print("schlitten ende")


schlitten()


def leistung_pkw():
    print("pkw")
    m = 1200
    v = 100 * 0.27778
    t = 5
    w = 0.5 * v * v * m
    p = w / t
    print(p)


leistung_pkw()


def flipper():
    print("flipper")
    d = 500
    s = 0.2
    m = 2
    e = 0.5 * d * s * s
    h = e / m / g
    # e=0.5 * m* v*v
    # e*2/m=v*v
    v = (e * 2 / m) ** 0.5
    print(f"v:{v}")
    print(f"h:{h}")


flipper()

print("balls")


class Ball:
    def __init__(self, x, y, masse):
        self.x = x
        self.y = y
        self.masse = masse


def calculate_elastic_impuls(v_1, m_1, v_2, m_2):
    v_1_neu = (m_1 - m_2) * v_1 / (m_1 + m_2) + 2 * m_2 * v_2 / (m_1 + m_2)
    v_2_neu = (m_2 - m_1) * v_2 / (m_1 + m_2) + 2 * m_1 * v_1 / (m_1 + m_2)
    return v_1_neu, v_2_neu


def calculate_inelastic(v_1, m_1, v_2, m_2):
    return (m_1 * v_1 + m_2 * v_2) / (m_1 + m_2)


def eis_stock():
    print("eis_stock")
    m_1 = 4.5
    v_0_start = 10
    koeff = 0.1
    p_start = m_1 * v_0_start
    f_n = f_g = m_1 * koeff * g
    s = 25
    e_abzug = s * f_n
    e_kin = 0.5 * v_0_start * v_0_start * m_1
    e_kin_neu = e_kin - e_abzug
    v_0_neu = (e_kin_neu * 2 / m_1) ** 0.5
    print(v_0_neu)
    v_2 = 0
    m_2 = 0.3
    v_eisstock, v_daube = calculate_elastic_impuls(v_0_neu, m_1, v_2, m_2)
    print(v_eisstock)
    print(v_daube)
    print("spieler")
    v_mixed = calculate_inelastic(v_eisstock, 4.5, -1, 80)
    print(v_mixed)


eis_stock()


def Schwungrad():
    print("Schwungrad Gyrobus")
    m = 10000
    j = 25
    v = 60 * 0.27778
    e_k = m * v * v * 0.5
    # e_k=0.5*j*v_w*v_w
    v_w = (e_k * 2 / j) ** 0.5
    rotationen = v_w / 2 / math.pi
    print(v_w)
    print(f"rpm:{rotationen * 60}")


Schwungrad()


def eislauf():
    print("eislauf")


eislauf()


def eisberg():
    print("Eisberg")

    dichte_eis = 920
    dichte_salzwasser = 1025
    # F_A = F_G
    # V_G = V_U+V_O
    # F_A = ß_wasser * V_U *g
    # F_G = ß_eis * V_G *g
    # ß_wasser * V_U  = ß_eis * (V_U+V_O)
    # V_U / (V_U+V_O) = ß_eis / ß_wasser
    vh = dichte_eis / dichte_salzwasser
    print(vh)
    print("ca. 10% über dem Wasser")


eisberg()


def federpendel():
    print("federpendel")
    m = 1
    deampfung = 0.03
    D = 900
    v_w_e = (D / m) ** 0.5
    Q = 2 * math.pi / deampfung
    print(f"Q:{Q}")
    # Q=v_w/(2*roh)
    # v_w*v_w=((D/m)-(c/(2*m))^2)


federpendel()


def gedeampft():
    print("gedeampft")
    m = 1
    D = 900
    E_pp = 0.03
    Q = 2 * math.pi / E_pp
    print(f"Q:{Q}")
    # Q=((D/m)**0.5)/(2*C/(2*m))
    # Q*2*C=((D/m)**0.5)*(2*m)
    C = ((D / m) ** 0.5) * m / Q
    # 0.1*A_Max =A_max*e^(-roh*t)
    # ln(0.1*A_max)=ln(A_max*e^(-roh*t))
    # ln(0.1*A_max)=ln(A_max)+(-roh*t)
    roh = C / (2 * m)
    t = -math.log(0.1) / roh
    print(t)
    print(f"C:{C}")


gedeampft()


def uebung_blatt_1():
    print(f"Uebungsblatt 1")
    t_0 = 5
    a_0 = g
    v_1 = a_0 * 5
    a_f = 25 - 9.81
    s = 700
    v_f = 5
    s_1 = a_0 * 0.5 * t_0 * t_0
    # v_1 -> v_f  v_1 muss zu v_f werden mit a_f = 25
    v_delta = v_1 - v_f
    # v_delta=a_f*t_f
    t_f = v_delta / a_f
    s_f = 0.5 * (t_f ** 2) * a_f + t_f * v_f
    s_rest = s - s_1 - s_f
    # v_f=s_rest/t_rest
    t_rest = s_rest / v_f
    t_total = t_rest + t_0 + t_f
    v_mittel = s / t_total
    print(f" v nach 5s:{v_1} hohe nach 5s:{s - s_1} gefaallen:{s_1}"
          f"\n zeit bis 5:{t_f} strecke bis 5: {s_f}"
          f"\ntotal time:{t_total}"
          f"\nMittel:{v_mittel}")


uebung_blatt_1()


def uebungsblatt_2():
    print("uebungsblatt 2")
    v_muendung = 240
    s_ziel = 40
    a_v = 9.81
    t = s_ziel / v_muendung
    s_hoehe = 0.5 * a_v * t ** 2
    print(s_hoehe)


uebungsblatt_2()


def schiefer_wurf_rettungsinsel():
    print("rettungsinsel")
    v_f = 350 * 5 / 18
    hoehe = 300
    a_v = 9.81
    # hohe=0.5*a*t²
    # t²=hohe*2/a
    # t=(hoehe*2/a)^0.5
    # v=s/t
    # s=v*t
    t = (hoehe * 2 / a_v) ** 0.5
    s = t * v_f
    print(f"bei :-{s}")
    v_h = v_f
    v_v = a_v * t
    magnitude = (v_h ** 2 + v_v ** 2) ** 0.5
    print(f"magnitude:{magnitude}")


schiefer_wurf_rettungsinsel()


def golf_ball():
    print("golf")
    s = 30
    v_total = 20
    a_down = 9.81
    # v_forward=v_total*cos(alpha)
    # v_up=v_total*sin(alpha)
    # v_up=9.81*(t/2)
    # v_up**2+v_forward**2=v_total**2
    # s=v_forward*t
    # t=v_up*2/9.81
    # s=v_forward*v_up*2/9.81
    # v_forward*v_up=s*9.81/2

    # v_up**2+v_forward**2=v_total**2
    # v_up=(v_total**2-v_forward**2)**0.5

    # v_forward*(v_total**2-v_forward**2)**0.5=s*9.81/2

    # v_forward**2*(votal**2-v_forward**2)=(s*9.81/2)**2
    # v_forward**2=x
    # x*(v_total**2-x)=
    # x*v_total**2-x**2
    # x**2-v_total**2*x+(s*9.81/2)**2=0
    p_halbe = v_total ** 2 / 2
    term_temp = (p_halbe ** 2 - (s * 9.81 / 2) ** 2) ** 0.5
    x_1 = (p_halbe - term_temp) ** 0.5
    x_2 = (p_halbe + term_temp) ** 0.5
    alpha_1 = math.degrees(math.acos(x_1 / v_total))
    alpha_2 = math.degrees(math.acos(x_2 / v_total))
    print(f"alpha1:{alpha_1}  alpha2:{alpha_2}")

    t = s / x_2
    v_x = math.cos(math.radians(50)) * 2
    v_y = math.sin(math.radians(50)) * 2
    x_x = t * v_x
    x_y = t * v_y
    print(f"x verschiebung:{x_x} y verschiebung:{x_y}")


golf_ball()


def winkelbeschleunigung_uebung():
    print("winkel")
    v_w = 4
    a_w = 2
    t = 5
    v_w_2 = v_w + a_w * t
    print(f"danach:{v_w_2}")
    rads = v_w * t + 0.5 * a_w * t ** 2
    umdrehungen = rads / math.pi / 2
    print(f"umdrehungen{umdrehungen}")


winkelbeschleunigung_uebung()


def zentrifuge():
    print("zentrifuge")
    rpm = 15000
    f = rpm / 60
    v_w = f * 2 * math.pi
    r = 0.15
    a_z = r * v_w ** 2
    print(f" az:{a_z}")
    # a_w*t=v_w
    t = 75
    a_w = v_w / t
    print(f"a:{a_w}")


zentrifuge()


def ice():
    print("ice")
    v_max = 330 * 5 / 18
    a_z_max = 0.08 * 9.81
    # a_z=v_b*v_b/r
    # r=v_b**2/a_z
    r = v_max ** 2 / a_z_max
    print(f"min kurvenradius:{r / 1000} km")
    r_2 = 1200
    v_b_2 = (a_z_max * r_2) ** 0.5
    print(f"vb:{v_b_2 / 5 * 18}")
    degree = 30
    r_3 = 2000
    radiants = degree / 180 * math.pi
    distance = radiants * r_3
    v_start = 100 * 5 / 18
    print(100 * 5 / 18)
    # v(t)=100*5/18 m/s+0,5 m/s²*t
    # a_z_p(t)=(100*5/18 m/s+0,5m/s²*t)²/r
    # s=100*5/18*t+0.5*0.5*t*t
    # 4*s=100*4*5/18*t+t*t
    # 0=t²+100*4*5/18*t-4*s
    minus_p_halbe = v_start * -2
    q = -4 * distance
    x1 = minus_p_halbe + (minus_p_halbe ** 2 - q) ** 0.5
    x2 = minus_p_halbe - (minus_p_halbe ** 2 - q) ** 0.5
    print(x1)
    t_kurve = x1
    v_max_kurve = 100 * 5 / 18 + 0.5 * t_kurve
    a_z_max_kurve = v_max_kurve ** 2 / 2000
    print(a_z_max_kurve / 9.81)


ice()


def lkw_fahrer():
    print("lkw")
    ko_h = 0.3
    v = 80 * 5 / 18
    g_down = 9.81
    f_haft = g_down * ko_h  # *m
    a_max = f_haft  # /m
    # v=a*t
    t = v / a_max
    s = a_max * 0.5 * t ** 2
    print(f"s:{s}")


lkw_fahrer()


def tuete():
    print("tuete")
    m = 9
    a_down = 9.81
    f_max = 100
    f_down = a_down * m
    f_delta = f_max - f_down
    a_delta = f_delta / m
    print(a_delta)


tuete()


def dreck():
    print("dreck")
    f = 600
    alpha = math.radians(3)
    f_y = f / 2
    # f_y/f_tot=sin(3)
    f_tot = f_y / math.sin(alpha)
    f_x = math.cos(alpha) * f_tot
    print(f" f_x:{f_x} f_tot:{f_tot}")


dreck()


def bungee():
    print("buntee")
    s_ungedehnt = 25
    plattform_hoehe = 50
    masse_springer = 80
    stopp_ueber_boden = 5
    # 5+s_gedehnt=50
    s_gedehnt = plattform_hoehe - stopp_ueber_boden
    s_delta = s_gedehnt - s_ungedehnt
    a_down = 9.81
    E_25 = a_down * masse_springer * s_gedehnt
    D = 2 * E_25 / (s_delta ** 2)
    print(f"Federkonstante D:{D}")
    F_springer = masse_springer * a_down
    s_baumeln = F_springer / D
    baumeln_hoehe = plattform_hoehe - (s_ungedehnt + s_baumeln)
    print(f"baumeln:{baumeln_hoehe}")
    dehn_delta_max = plattform_hoehe - s_ungedehnt
    # E=D*s**2/2
    E_max = D * dehn_delta_max ** 2 / 2
    # E=g*m*s
    # m=E/g/s
    m_max = E_max / a_down / (s_ungedehnt + dehn_delta_max)
    print(f"maximale Masse:{m_max}")
    m_springer_schwer = 130
    E_Total = a_down * m_springer_schwer * plattform_hoehe
    E_absorbiert = (dehn_delta_max ** 2) * D * 0.5
    E_delta = E_Total - E_absorbiert
    v_impact = (E_delta * 2 / m_springer_schwer) ** 0.5
    print(f"E_delta:{E_delta} impact:{v_impact}")


bungee()


def Pkw_leistung():
    print("pkw leistung 2")
    m_person = 80
    P_0 = 50000
    t = 10
    v_end = 100 * 5 / 18
    # v=a*t
    a = v_end / t
    s = 0.5 * a * t ** 2
    print(f"s:{s}")
    # P=a*m*s/t
    # m=P*t/a/s
    m_gesammt = P_0 * t / a / s
    m_auto = m_gesammt - m_person

    # P=e/t
    E_0 = P_0 * t
    # E=0.5*m*v*v
    m_auto_v2 = E_0 * 2 / (v_end ** 2)
    m_auto_v2 -= m_person
    print(f"ma1:{m_auto}  ma2:{m_auto_v2}")

    m_2 = m_auto + 400
    P_2 = P_0
    E_kin = v_end * v_end * 0.5 * m_2
    # P=e/t
    t_neu = E_kin / P_2
    print(f"neue Zeit:{t_neu}")


Pkw_leistung()


def Ladung_ungesichert():
    print("Ladung ungesichert")
    m = 100
    v_0 = 72 * 5 / 18
    s = 10 - 1
    ko = 0.5

    E_0 = 0.5 * m * v_0 ** 2
    E_aborbiert = m * g * s * ko
    E_delta = E_0 - E_aborbiert
    # E=0.5*m*v²
    v = (E_delta * 2 / m) ** 0.5
    print(f"v:{v}")


Ladung_ungesichert()


def Trampolin():
    print("trampolin")
    m = 25
    s = 12
    D = 40000
    v_contact = (s * g * 2) ** 0.5
    # 0.5*D*x²=m*g*(s+x)
    # x²=m*g*s*2/D+m*g*x*2/D
    # 0=x²-x*2*m*g/D-m*g*s*2/D
    p = -2 * m * g / D
    q = -2 * m * g * s / D
    t2 = ((p / 2) ** 2 - q) ** 0.5
    x1 = -p / 2 + t2
    x2 = -p / 2 - t2

    print(f"v_contact:{v_contact} x1:{x1} x2:{x2}")


Trampolin()


def pendel_invers():
    print("ip")
    m = 1
    s_feder = 0.5
    s_pendel = 2 * s_feder
    s_total = s_feder + s_pendel
    alpha_0 = math.radians(60)
    h_0 = s_pendel * math.sin(alpha_0)
    h_delta = s_pendel - h_0
    print(h_delta)
    x_horizontal = s_pendel * math.cos(alpha_0)
    y_vertikal_p_0 = s_total - math.sin(alpha_0) * s_pendel
    hypotehnuse = (x_horizontal ** 2 + y_vertikal_p_0 ** 2) ** 0.5
    print(hypotehnuse)
    dehnung = hypotehnuse - s_feder
    D = 50
    E_feder = 0.5 * dehnung ** 2 * D
    E_delta_hoehe = g * m * h_delta
    E = E_feder - E_delta_hoehe
    # E=v²*0.5*m
    # E/0.5/m=v²
    v = (E / 0.5 / m) ** 0.5
    print(v)


pendel_invers()


def rangierbahnhof():
    print("r_bahnhof")
    m_1 = 24000
    v_1 = 3
    m_2 = 20000
    v_2 = 1.8
    v_1_neu = (m_1 * v_1 + m_2 * v_2) / (m_1 + m_2)
    print(f"inelastisch gleich:{v_1_neu}")
    v_1_neu = (m_1 * v_1 - m_2 * v_2) / (m_1 + m_2)
    print(f"inelastisch gegen:{v_1_neu}")
    v_1_neu = (m_1 - m_2) * v_1 / (m_1 + m_2) + 2 * m_2 * v_2 / (m_1 + m_2)
    v_2_neu = (m_2 - m_1) * v_2 / (m_1 + m_2) + 2 * m_1 * v_1 / (m_1 + m_2)
    print(f" elastisch v_1:{v_1_neu} elastisch v_2:{v_2_neu}")
    v_1_neu = (m_1 - m_2) * v_1 / (m_1 + m_2) - 2 * m_2 * v_2 / (m_1 + m_2)
    v_2_neu = (m_2 - m_1) * v_2 / (m_1 + m_2) - 2 * m_1 * v_1 / (m_1 + m_2)
    print(f"gegen: elastisch v_1:{v_1_neu} gegen elastisch v_2:{v_2_neu}")


rangierbahnhof()


def Impulskanone():
    print("impulskanone")
    m1 = 0.1
    m2 = 0.01
    h = 1
    m_g = m1 + m2
    v_max = (2 * g * h) ** 0.5
    v_1 = v_max
    v_2 = -v_max
    print(f"v_max:{v_max}")
    v_2_neu = (m2 - m1) * v_2 / (m1 + m2) + 2 * m1 * v_1 / (m1 + m2)
    print(f"vneu:{v_2_neu}")
    E_kin = 0.5 * v_2_neu * v_2_neu * m2
    # E_lage=g*h*m
    h = E_kin / g / m2
    print(h)


Impulskanone()


def Einkaufen():
    print("einkaufen")
    m_m = 80
    m_e = 60
    v_e = 2.9 * 5 / 18
    v_m = 8 * 5 / 18
    v_neu = (m_m * v_m + m_e * v_e) / (m_e + m_m)
    print(f"v_neu m/s:{v_neu} v_neu kmh:{v_neu / 5 * 18}")
    m_neu = m_m + m_e
    v_f = 4.5 * 5 / 18
    m_f = 75
    i_f = v_f * m_f
    i_neu = v_neu * m_neu
    i_kom = (i_f ** 2 + i_neu ** 2) ** 0.5
    m_kom = m_neu + m_f
    v_kom = i_kom / m_kom
    print(v_kom / 5 * 18)
    alpha = math.atan(i_neu / i_f)
    print(f" alpha:{90 - alpha * 180 / math.pi}  v:{v_kom / 5 * 18}")
    # i_kom=i_me
    # i_me=m_me*v_me
    # i_kom=m_me*v_me
    m_me = 130
    v_me = i_kom / m_me
    print(v_me / 5 * 18)
    E_bauch = (0.5 * v_kom ** 2 * m_kom) + (0.5 * m_me * v_me ** 2)
    print(E_bauch)


Einkaufen()


def eisstock():
    print("eisstock")
    m_s = 4.5
    r_s = 0.15
    k_g = 0.1
    v_0 = 10
    m_d = 0.3
    r_d = 0.06
    s = 25
    E_s = v_0 ** 2 * 0.5 * m_s
    F_down = g * m_s * k_g
    E_down = F_down * s
    E_delta = E_s - E_down
    v_i = (E_delta * 2 / m_s) ** 0.5
    print(v_i)
    print("b)")
    v_neu_s = (m_s - m_d) * v_i / (m_s + m_d)
    v_neu_d = 2 * m_s * v_i / (m_s + m_d)
    print(f"v neu stock:{v_neu_s}  v neu daube:{v_neu_d}")
    v_spieler = 1
    m_spieler = 80
    v_neu = (m_spieler * v_spieler - m_s * v_neu_s) / (m_spieler + m_s)
    print(v_neu)
    alpha = math.acos(r_s / (r_s + r_d))
    v_para = math.sin(alpha) * v_i
    v_ortho = math.cos(alpha) * v_i
    v_neu_para = (m_s - m_d) * v_para / (m_s + m_d)
    v_neu_d_2 = 2 * m_s * v_para / (m_s + m_d)
    v_total = (v_neu_para ** 2 + v_ortho ** 2) ** 0.5
    print(f" Vektor stock x:{v_neu_para} y:{v_ortho}"
          f"\n Vektor daube x:{v_neu_d_2} y:0")
    print(f" v stock:{v_total}")
    alpha2 = math.atan(v_ortho / v_neu_para)
    print(f"Winkel:{math.degrees(alpha2)}")
    print(v_total)
    alpha3 = math.acos((v_neu_para * v_neu_d_2) / (v_total * v_neu_d_2))

    print(math.degrees(alpha3))


eisstock()

print("Satelliten")


def Satteliten():
    print("Sattelite")
    # Zentripedalkraft
    # G-Kraft
    m_s = 10
    m_e = 10
    r_e = 10
    h = 10
    r = r_e + h
    G = 10  # Gravitationskonstate
    F_g = -G * (m_s * m_e) / (r * r)  # Kraft
    T = 10  # Umlaufdauer in Sekunden
    Kreisumfang = r * 2 * math.pi
    v_b = Kreisumfang / T
    F_z = m_s * v_b ** 2 / r  # Gegenkraft
    # m_s * v_b ** 2 / r = -G * (m_s * m_e) / (r * r)
    #  v_b ** 2  = -G *  m_e / r


Satteliten()


def Erdumlaufbahn():
    print("Erdumlaufbahn")
    m_e = 5.97e24
    r_e = 6370000
    sec_day = 24 * 60 * 60
    T_e = sec_day
    f_e = 1 / sec_day
    v_w_e = f_e * 2 * math.pi
    G = 6.674e-11
    v_w_s = v_w_e

    # A_g=G*m_e/r**2
    # az=v_w_s**2*r
    # v_w_s**2*r=-G*m_e/r**2
    # auflosen nach r
    # v_w_s**2*r**3=-G*m_e
    # r**3=G*m_e/v_w_s**2
    r = (G * m_e / v_w_s ** 2) ** (1 / 3)
    s_h = r - r_e
    print(f" abstand zur Erdoberfläche:{s_h} m in km:{s_h / 1000} km")
    v_b = r * v_w_s
    print(f" Bahngeschwindigkeit:{v_w_s * r / 5 * 18}")
    # A_g=G*m_e/r**2
    # A_z=r*(v_w_e*6)**2
    # G*m_e/r**2=r*(v_w_e*6)**2
    # auflösen nach r
    # G*m_e=r**3*(v_w_e*6)**2
    r_2 = (G * m_e / ((v_w_e * 6) ** 2)) ** (1 / 3)
    print(f" Abstand zur Erdoberfläche:{r_2 - r_e}")
    v_b_2 = v_w_e * 6 * r_2
    print(f" speed={v_b_2 / 5 * 18}")


Erdumlaufbahn()


def rotor_volksfest():
    print("Oktoberfest")
    r = 9 / 2
    # F_z=m*r*v_w²
    # F_g=g*m
    # F_h=F_z*ko_h
    # F_h=F_g
    # m*r*v_w²*ko_h=g*m
    # nach v_w auflösen
    # v_w²=g/r/ko_h
    # v_w = (g/r/ko_h)^0.5
    ko_h = 1
    v_w = (g / r / ko_h) ** 0.5
    print(f"min v_w pro minute:{v_w * 60}")
    ko_h = 0.55
    v_w = (g / r / ko_h) ** 0.5
    f = v_w / (2 * math.pi)
    print(f" min rpm:{f * 60}")


rotor_volksfest()


def fliehkraftregler():
    print("fliehkraftregler")
    # F_z=m*r*v_w²

    # F_z=m*sin(alpha)*L*v_w²

    # r=sin(alpha)*L
    # h=cos(alpha)*L
    # tan(alpha)=F_z/F_g
    # 1/cos(alpha)=L*v_w²/g
    # g/(L*v_w²)=cos(alpha)
    # alpha=arccos(g/(L*v_w²))
    L = 0.2
    v_w = 150 * math.pi * 2 / 60
    alpha = math.acos(g / (L * v_w ** 2))
    print(f" winkel:{alpha / math.pi * 180}")


fliehkraftregler()


def rollende_koerper():
    print("koerper rollen")
    # Rotationsenergie E_r
    # E_r = 0.5 * J * v_w*v_w
    # -> je geringer rotationsenergie desto höher kinetische Energie
    # -> je geringer J desto höher kin-Energie
    r = 1
    m = 1
    J_k = 2 / 5 * m * r ** 2
    J_vz = 0.5 * m * r ** 2
    r_i = 0.5
    J_hz = 0.5 * m * (r ** 2 + r_i ** 2)
    # 2/5<0.5 Vollkugel weniger rotenergie also mehr kin
    # r²<r²+x²  x²>0 -> Vollzylinder rotenergie < hohlzylinder -> vollzylinder schneller


rollende_koerper()


def kanonen_kugel2():
    print("kan kug 3")
    s = 0.2
    m_k = 0.015
    m_b = 2
    # impulserhaltung

    # Energierhaltung
    # E=m*g*s
    # E=0.5*m*v²
    # v=(E*2/m)^0.5
    # Impulserhaltung
    # v=v_k*m_k/(m_b+m_k)
    # v_k=v*(m_b+m_k)/m_k
    m_g = m_k + m_b
    E = m_g * g * s
    v_k = (E * 2 / m_g) ** 0.5 * m_g / m_k
    print(v_k)


kanonen_kugel2()


def v_by_impuls(v1, m1, v2, m2):
    v_neu = (v1 * m1 + v2 * m2) / (m1 + m2)
    return v_neu


def v_by_energy(v1, m1, v2, m2):
    E1 = m1 * (v1 ** 2) * 0.5
    E2 = m2 * (v2 ** 2) * 0.5
    v_neu = (((E1 + E2) * 2) / (m1 + m2)) ** 0.5
    return v_neu


def entest(v1, m1, v2, m2):
    vbyi = v_by_impuls(v1, m1, v2, m2)
    vbye = v_by_energy(v1, m1, v2, m2)

    print(f"{v1} {m1} {v2} {m2}:   by impuls:{vbyi} by energy:{vbye}")


entest(1, 1, 1, 1)
entest(2, 2, 2, 2)
entest(2, 4, 5, 8)


def drehmaschine():
    print("Drehmaschine")
    P = 1000
    t_s = 3
    f = 500 / 60
    t_b = 5
    Arbeit = P * t_s
    # Rotarbeit=0.5*J*v_w²
    v_w = f * 2 * math.pi
    # J=rotarbeit*2/v_w²
    J = Arbeit * 2 / v_w ** 2
    print(J)
    # M=a_w*J
    # a_w=v_w/s
    a_w = v_w / t_b
    t_m = a_w * J
    print(t_m)
    Bremsleistung = Arbeit / t_b
    t_m_alternativ = Bremsleistung / ((0 - v_w) / 2)
    print(t_m_alternativ)


drehmaschine()


def drehmaschine2():
    print("drehmaschine2")
    P = 1000
    t_s = 3
    t_b = 5
    f = 500 / 60
    v_w = f * math.pi * 2
    E = P * t_s
    # E=J*v_w²*0.5
    J = E / (v_w ** 2 * 0.5)
    print(f"Trägheitsmoment:{J}")
    # Drehmoment=J*a_w
    drehmoment = J * v_w / t_b
    print(f"Drehmoment:{drehmoment}")
    v_b_max = 400 / 60
    # v_b=v_w*r
    r = v_b_max / v_w
    print(f"Max Radius:{r}")
    # J=0.5*r²*m
    # Volumen=pi*r²*h
    r_werkstueck = 0.1
    h_werkstueck = 0.2
    volumen = math.pi * r_werkstueck ** 2 * h_werkstueck
    dichte = 8500
    # p=m/v
    m_werkstueck = dichte * volumen
    J_Werkstück = 0.5 * r_werkstueck ** 2 * m_werkstueck
    J_total = J_Werkstück + J
    f2 = 500 / 60
    v_w2 = f2 * 2 * math.pi
    E2 = J_total * v_w2 ** 2 * 0.5
    # P=E/t
    t2 = E2 / P
    print(f" Dauer neu:{t2}")
    # J=0.5*m*r²
    radius1 = 0.1
    radius2 = 0.1
    radius2_innen = 0.09
    hoehe2 = 0.15
    hoehe1 = 0.2 - hoehe2
    dichte = 8500
    volumen1 = math.pi * radius1 ** 2 * hoehe1
    volumen2 = math.pi * (radius2 ** 2 - radius2_innen ** 2) * hoehe2  # - math.pi * radius2_innen ** 2 * hoehe2
    masse1 = volumen1 * dichte
    masse2 = volumen2 * dichte
    J1 = 0.5 * masse1 * radius1 ** 2
    J2 = 0.5 * masse2 * (radius2 ** 2 + radius2_innen ** 2)
    J_total2 = J1 + J2
    print(f"J1:{J1}  J2:{J2} total:{J_total2}")


drehmaschine2()


def ruderboot():
    print("Ruderboot")
    dichteStein = 1
    volumenStein = 1
    masseStein = volumenStein * dichteStein
    dichteWasser = 0.5
    dichteBoot = 0.1
    volumenBoot = 20
    masseBoot = dichteBoot * volumenBoot

    # Wenn Stein nicht im Boot:
    F_down_boot = g * masseBoot
    # F_down_boot=F_a
    # F_a=dichteWasser*VolumenWasser_verdreangt
    volumenWasserVerdreangt = F_down_boot / dichteWasser
    volumenWasserVerdreangt += volumenStein
    print(f" Wasser verdeangt, wenn Stein im Wasser:{volumenWasserVerdreangt}")
    volumenBackup = volumenWasserVerdreangt
    # Wenn Stein im Boot:
    masse_system = masseBoot + masseStein
    F_down_system = masse_system * g
    volumenWasserVerdreangt = F_down_system / dichteWasser
    print(f" Wasser verdrängt, wenn Stein im Boot:{volumenWasserVerdreangt}")
    print(f" Je mehr wasser verdrängt wird, desto höher der Wasserspiegel")
    print(f" Wenn Stein im boot, wird mehr wasser verdrängt:{volumenWasserVerdreangt > volumenBackup}")
    print(f" Begründung, wenn Stein nicht im boot, geht ein teil der Gewichtskraft des Steins verloren, da er zum Grund"
          f"sinkt, daher wird insgesamt weniger Wasser verdrängt")


ruderboot()


def unterwasser_bergung():
    print("lift it up")
    ß_k = 8800
    m_k = 2500
    ß_w = 1030
    F_k = m_k * g
    v_k = m_k / ß_k
    v_w = v_k
    m_w = v_w * ß_w
    F_w = m_w * g
    F_unterWasser = F_k - F_w
    # F_w=F_k
    # m_w=m_k
    # ß_w*v_ß=m_k
    v_required = m_k / ß_w
    v_required -= v_k
    # f=a*m
    a = 0.3
    f_required = (g + a) * m_k
    # f=m_wasser*g
    masse_wasser_required = f_required / g
    # ß=m/v
    v_required_for_ascend = masse_wasser_required / ß_w - v_k
    pressure_surface = 1013 * 100
    tiefe = 30
    pressure_required = pressure_surface + tiefe * g * ß_w
    print(f" Gewicht unter Wasser:{F_unterWasser}"
          f"\n benötigtes Volumen:{v_required}"
          f"\n benötigtes Volumen für aufstieg"
          f"{v_required_for_ascend}"
          f"\n Druck benötigt:{pressure_required} Pa"
          f"\n ={pressure_required / 100} hPa"
          f"\n ={pressure_required / 100000} bar")


unterwasser_bergung()


def zwei_waagen():
    print(" 2 waagen ")
    m_becher = 1
    m_h20 = 2
    m_al = 2
    ß_al = 2700
    ß_h2o = 1000
    vol_al = m_al / ß_al
    vol_h20 = m_h20 / ß_h2o

    F_down_al = m_al * g
    m_h2o_verdreangt = ß_h2o * vol_al
    F_up_al = g * m_h2o_verdreangt
    F_sum = F_down_al - F_up_al
    m_al_angezeigt = F_sum / g

    print(f" Federwaage Anzeige:{m_al_angezeigt}")

    m_delta = m_al - m_al_angezeigt  # das was zu wenig ist, muss bei der anderen Waage zu viel sein
    m_kuechenwage_angezeigt = m_becher + m_h20 + m_delta
    print(f" Küchenwage Angezeigt{m_kuechenwage_angezeigt}")

    F_additional = vol_al * ß_h2o * g
    F_sum = m_becher * g + F_additional + m_h20 * g
    masse = F_sum / g
    print(f" masse:{masse}")


zwei_waagen()


def youtube_feder_masse_system(t):
    print("ffm")
    m = 2
    s = 0.02
    F = 1
    D = F / s
    print(D)
    v_w_e = (D / m) ** 0.5
    print(v_w_e)
    A = 0.02
    # 1=sin(offset)
    # asin(1)=offset
    offset = math.asin(-1)
    print(offset)
    return A * math.sin(v_w_e * t + offset)


youtube_feder_masse_system(0)


def helium_ballon():
    print("helium ballon")
    m = 75
    m_ballon = 1.5
    ß_helium = 0.1786
    ß_luft = 1.293
    # F_down =(m_ballon + m+m_helium) * g
    # m_luft=v_ballon*ß_luft
    # F_down=m_luft*g
    # (v_ballon*ß_luft)*g=(m_ballon + m+m_helium) * g
    # (v_ballon*ß_luft)=(m_ballon + m+m_helium)
    # m_helium=v_ballon*ß_helium
    # v_ballon*ß_luft=m_ballon + m+v_ballon*ß_helium
    # v_ballon*(ß_luft-ß_helium)=m_ballon + m
    v_ballon = (m_ballon + m) / (ß_luft - ß_helium)
    print(v_ballon)
    v_neu = v_ballon * 2
    F_up = v_neu * ß_luft * g
    print(f" {v_neu}*{ß_luft}*{g} / ({90}+{1.5}+{v_neu}*{ß_helium})")
    m = (90 + v_neu * ß_helium + 1.5)

    up = (F_up / m) - g
    print(up)


helium_ballon()


def u_rohr():
    print("U rohr")
    h_oel = 0.110
    delta = 0.012
    h_wasser = h_oel - delta
    ß_wasser = 1000
    # m_wasser=ß_wasser*h_wasser*fläche
    # m_öl=h_oel*ß_öl*fläche
    # h_oel*ß_öl*fläche=ß_wasser*h_wasser*fläche
    # h_oel*ß_öl=ß_wasser*h_wasser
    ß_oel = ß_wasser * h_wasser / h_oel
    print(ß_oel)


u_rohr()


def schnorchel():
    print("Schnorchel")
    # F=druck*A
    # druck=ß*g*s
    # F=ß*g*s
    # dichte wasser= 1 kg/(0.1*0.1*0.1)
    h = 400 / g / 1000
    print(h)


schnorchel()


def SchwebungYT():
    print("Schwebung")
    # f_s=f1-f2
    f1 = 400
    T_s = 0.1
    # T=1/F
    f_s = 1 / T_s
    f2 = f1 - f_s
    print(f2)


SchwebungYT()


def BMI_Nasa():
    print("Nasa bmi")
    m_s = 4
    m_a = 75
    m = m_s + m_a
    T = 2
    f = 1 / 2
    # T_e=2*pi*(m/D)**0.5
    # (T_e/2/pi)**2=m/D
    D = m / ((T / 2 / math.pi)) ** 2
    T_m = 2 * math.pi * ((m_s + 60) / D) ** 0.5
    print(T_m)


BMI_Nasa()


def kran():
    print("kran")
    r = 20
    m = 1000
    alpha = 5 * math.pi / 180
    v_w_e = (g / r) ** 0.5
    T_e = 2 * math.pi / v_w_e
    f = 1 / T_e
    # logisiche Lösung:
    x = math.sin(alpha) * r

    print(f"Schwingungsdauer:{T_e} Frequenz:{f}")
    print(f" Mindestens springen:{x}")
    # x=alpha=max_alpha*sin(v_w_e*t)
    # abgeleitet nach t = geschwindigkeit:
    # v_w=max_alpha*cos(v_w_e*t)*v_w_e
    # v_b=v_w*r
    # v_b=r*alpha*math.cos(v_w_e*t)*v_w_e
    # 1=math.cos(v_w_e*t)
    # acos(1)=v_w_e*t
    t = math.cos(1) / v_w_e
    v_b = r * alpha * v_w_e
    print(f"max vb:{v_b}")

    y = math.cos(alpha) * r
    delta = r - y
    print(delta)
    E = m * delta * g
    v = (E * 2 / m) ** 0.5
    print(f"Probe:{v}")
    # f=f_down+f_zentrifugal
    f_down = g * m
    f_z = m * v_b ** 2 / r
    tot = f_down + f_z
    print(f"max f:{tot}")


kran()


def ringpendel():
    print(f"Ringpendel")
    print("Phsikalisches Pendel")
    f = 5 / 7
    v_w_e = f * 2 * math.pi
    r = 0.20
    # J_0= 0.5*m*(r_a²+r²)
    # J_0=0.5*m*r_a²+0.5*m*r²
    # J_0=(m*g*r-v_w_e²*m*r²)/v_w_e²
    # (m*g*r-v_w_e²*m*r²)/v_w_e²=0.5*m*r_a²+0.5*m*r²
    # Masse rauskürzen
    # (g*r-v_w_e²*r²)/v_w_e²=0.5*r_a²+0.5*r²
    # (g*r-v_w_e²*r²)/v_w_e²-0.5*r²=0.5*r_a²
    # r_a=(((g*r-v_w_e²*r²)/v_w_e²-0.5*r²)*2)**0.5
    r_a = (((g * r - v_w_e ** 2 * r ** 2) / v_w_e ** 2 - 0.5 * r ** 2) * 2) ** 0.5
    print(r_a)


ringpendel()


def lautsprecher():
    print("Lautsprecher")
    A = 0.001
    m = 0.005
    # f
    # w=f*pi*2
    # x(t)=A*sin(w*t)
    # x'(t)=A*cos(w*t)*w
    # x''(t)=A*-sin(w*t)*w²
    # sin(w*t)=1
    # sin(w*t)=-1
    # asin(1)/w=t
    # asin(-1)/w=t
    # a=g
    # g=A*-sin(w*t)*w²
    # g=A*w²
    w = (g / A) ** 0.5
    f = w / 2 / math.pi
    print(f)


lautsprecher()


def angeln():
    print("Angeln")
    r = 0.005
    boden = math.pi * r ** 2
    ß = 1000
    # wasserkonstante=ß*boden
    wasserkonstante = ß * boden
    # F_up(y)=wasserkonstante*y*g
    # 0=wasserkonstante*y*g+y''*m
    # 0=wasserkonstante*g/m*y+y''
    # ist harmonisch weil
    # 0=a*y+y''
    t = 5
    schwingungen = 10
    f = schwingungen / t
    w_e = f * math.pi * 2
    # w_e=(wasserkonstante*g/m)**0.5
    # w_e²=wasserkonstante*g/m
    m = wasserkonstante * g / w_e ** 2
    print(f"{m} kg  {m * 1000}g")


angeln()


def kinderwagen():
    print("Kinderwagen")
    m_leer = 13
    m_kind = 10
    m = m_leer + m_kind
    D = (m_kind) * g / 0.05
    print(D)
    v_w_e = (D / m) ** 0.5
    f = v_w_e / 2 / math.pi
    T = 1 / f
    print(v_w_e)
    t = 3
    roh = math.log(10, math.e) / t
    print(roh)


kinderwagen()
