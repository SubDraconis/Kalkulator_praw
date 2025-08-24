def omma(I,U,R):
    try:
        if I == 0:
            I = U / R
            return I
        elif U == 0:
            U = I * R
            return U
        elif R == 0:
            R = U / I
            return R
        else:
            return "Podaj 0 w miejscu niewiadomej"
    except :
        return "Nieprawidłowe dane wejściowe"
    
def Joule(I,U,R,t):
    try:
        if I == 0:
            I = (U * t) / R
            return I
        elif U == 0:
            U = (I * R) / t
            return U
        elif R == 0:
            R = (U * t) / I
            return R
        elif t == 0:
            t = (I * R) / U
            return t
        else:
            return "Podaj 0 w miejscu niewiadomej"
    except :
        return "Nieprawidłowe dane wejściowe"

def druga_zasada_dynamiki(F,m,a):
    try:
        if F == 0:
            F = m * a
            return F
        elif m == 0:
            m = F / a
            return m
        elif a == 0:
            a = F / m
            return a
        else:
            return "Podaj 0 w miejscu niewiadomej"
    except :
        return "Nieprawidłowe dane wejściowe"

def coulomb(F,k,q1,q2,r):
    try:
        if F == 0:
            F = k * (q1 * q2) / (r ** 2)
            return F
        elif k == 0:
            k = F * (r ** 2) / (q1 * q2)
            return k
        elif q1 == 0:
            q1 = (F * (r ** 2)) / (k * q2)
            return q1
        elif q2 == 0:
            q2 = (F * (r ** 2)) / (k * q1)
            return q2
        elif r == 0:
            r = ((k * (q1 * q2)) / F) ** 0.5
            return r
        else:
            return "Podaj 0 w miejscu niewiadomej"
    except :
        return "Nieprawidłowe dane wejściowe"

def powszechnego_ciazenia(F,G,m1,m2,r):
    try:
        if F == 0:
            F = G * (m1 * m2) / (r ** 2)
            return F
        elif G == 0:
            G = F * (r ** 2) / (m1 * m2)
            return G
        elif m1 == 0:
            m1 = (F * (r ** 2)) / (G * m2)
            return m1
        elif m2 == 0:
            m2 = (F * (r ** 2)) / (G * m1)
            return m2
        elif r == 0:
            r = ((G * (m1 * m2)) / F) ** 0.5
            return r
        else:
            return "Podaj 0 w miejscu niewiadomej"
    except :
        return "Nieprawidłowe dane wejściowe"

def hooke(F,k,x):
    try:
        if F == 0:
            F = k * x
            return F
        elif k == 0:
            k = F / x
            return k
        elif x == 0:
            x = F / k
            return x
        else:
            return "Podaj 0 w miejscu niewiadomej"
    except :
        return "Nieprawidłowe dane wejściowe"
    
def Indukcja_magnetyczna(ε,N,ΔΦʙ,Δt):
    try:
        if ε == 0:
            ε = N * (ΔΦʙ / Δt)
            return ε
        elif N == 0:
            N = ε / (ΔΦʙ / Δt)
            return N
        elif ΔΦʙ == 0:
            ΔΦʙ = (ε * Δt) / N
            return ΔΦʙ
        elif Δt == 0:
            Δt = (N * ΔΦʙ) / ε
            return Δt
        else:
            return "Podaj 0 w miejscu niewiadomej"
    except :
        return "Nieprawidłowe dane wejściowe"

def main():
    print("Witaj w kalkulatorze praw!")
    print("Dostępne prawa: omma, Joule'a, druga zasada dynamiki, Coulomba, powszechnego ciążenia, Hooke'a, Indukcja magnetyczna")
    prawo = input("Wybierz prawo do obliczenia: ").strip().lower()
    if prawo == "omma":
        try:
            I = float(input("Podaj natężenie prądu (I,A) w amperach (podaj 0 jeśli nieznane): "))
            U = float(input("Podaj napięcie (U,V) w woltach (podaj 0 jeśli nieznane): "))
            R = float(input("Podaj opór (R,Ω) w omach (podaj 0 jeśli nieznane): "))
            wynik = omma(I, U, R)
            print(f"Wynik: {wynik}")
        except ValueError:
            print("Nieprawidłowe dane wejściowe. Proszę podać liczby.")
    elif prawo == "joule'a":
        try:
            I = float(input("Podaj natężenie prądu (I,A) w amperach (podaj 0 jeśli nieznane): "))
            U = float(input("Podaj napięcie (U,V) w woltach (podaj 0 jeśli nieznane): "))
            R = float(input("Podaj opór (R,Ω) w omach (podaj 0 jeśli nieznane): "))
            t = float(input("Podaj czas (t,s) w sekundach (podaj 0 jeśli nieznane): "))
            wynik = Joule(I, U, R, t)
            print(f"Wynik: {wynik}")
        except ValueError:
            print("Nieprawidłowe dane wejściowe. Proszę podać liczby.")
    elif prawo == "druga zasada dynamiki":
        try:
            F = float(input("Podaj siłę (F,N) w niutonach (podaj 0 jeśli nieznane): "))
            m = float(input("Podaj masę (m,kg) w kilogramach (podaj 0 jeśli nieznane): "))
            a = float(input("Podaj przyspieszenie (a,m/s²) w metrach na sekundę kwadrat (podaj 0 jeśli nieznane): "))
            wynik = druga_zasada_dynamiki(F, m, a)
            print(f"Wynik: {wynik}")
        except ValueError:
            print("Nieprawidłowe dane wejściowe. Proszę podać liczby.")
    elif prawo == "coulomba":
        try:
            F = float(input("Podaj siłę (F,N) w niutonach (podaj 0 jeśli nieznane): "))
            k = float(input("Podaj stałą elektrostatyczną (k,N·m²/C²) w niutonach metrów kwadrat na kulomb kwadrat (podaj 0 jeśli nieznane): "))
            q1 = float(input("Podaj ładunek q1 (C) w kulombach (podaj 0 jeśli nieznane): "))
            q2 = float(input("Podaj ładunek q2 (C) w kulombach (podaj 0 jeśli nieznane): "))
            r = float(input("Podaj odległość (r,m) w metrach (podaj 0 jeśli nieznane): "))
            wynik = coulomb(F, k, q1, q2, r)
            print(f"Wynik: {wynik}")
        except ValueError:
            print("Nieprawidłowe dane wejściowe. Proszę podać liczby.")
    elif prawo == "powszechnego ciążenia":
        try:
            F = float(input("Podaj siłę (F,N) w niutonach (podaj 0 jeśli nieznane): "))
            G = float(input("Podaj stałą grawitacyjną (G,N·m²/kg²) w niutonach metrów kwadrat na kilogram kwadrat (podaj 0 jeśli nieznane): "))
            m1 = float(input("Podaj masę m1 (kg) w kilogramach (podaj 0 jeśli nieznane): "))
            m2 = float(input("Podaj masę m2 (kg) w kilogramach (podaj 0 jeśli nieznane): "))
            r = float(input("Podaj odległość (r,m) w metrach (podaj 0 jeśli nieznane): "))
            wynik = powszechnego_ciazenia(F, G, m1, m2, r)
            print(f"Wynik: {wynik}")
        except ValueError:
            print("Nieprawidłowe dane wejściowe. Proszę podać liczby.")
    elif prawo == "hooke'a":
        try:
            F = float(input("Podaj siłę (F,N) w niutonach (podaj 0 jeśli nieznane): "))
            k = float(input("Podaj stałą sprężystości (k,N/m) w niutonach na metr (podaj 0 jeśli nieznane): "))
            x = float(input("Podaj odkształcenie (x,m) w metrach (podaj 0 jeśli nieznane): "))
            wynik = hooke(F, k, x)
            print(f"Wynik: {wynik}")
        except ValueError:
            print("Nieprawidłowe dane wejściowe. Proszę podać liczby.")
    elif prawo == "indukcja magnetyczna":
        try:
            ε = float(input("Podaj siłę elektromotoryczną (ε,V) w woltach (podaj 0 jeśli nieznane): "))
            N = float(input("Podaj liczbę zwojów (N) (podaj 0 jeśli nieznane): "))
            ΔΦʙ = float(input("Podaj zmianę strumienia magnetycznego (ΔΦʙ,Wb) w weberach (podaj 0 jeśli nieznane): "))
            Δt = float(input("Podaj zmianę czasu (Δt,s) w sekundach (podaj 0 jeśli nieznane): "))
            wynik = Indukcja_magnetyczna(ε, N, ΔΦʙ, Δt)
            print(f"Wynik: {wynik}")
        except ValueError:
            print("Nieprawidłowe dane wejściowe. Proszę podać liczby.")
    else:
        print("Nieznane prawo. Dostępne prawa: omma")
    

if __name__ == "__main__":
    main()