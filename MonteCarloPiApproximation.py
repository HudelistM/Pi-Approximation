from math import sqrt
import datetime
import sys
sys.setrecursionlimit(5000)
# varijable koje mijenjaju vrijednost: seed,n, out, s,
# Linearni kongruentni generator  nasumicnih brojeva
def linearniGenerator(seed, a, b, m, n,results):
        seed = (a * seed + b) % m
        results.append(seed)
        if n==0:
            return results
        return linearniGenerator(seed,a,b,m,n-1,results)
# Polje brojeva koji se koriste kao seed za LFG
s = [852375763782,26000,5200,25873259,4400000,24000,524646263,3100,196125,35342,483,4834,36326,620000]
# Varijable koje se koriste u LFG-u(x koji sluzi za prekid rekurzije,i za iteraciju kroz polja, 
# out za spremanje rezultata,li_results za spremanje polja generiranih brojeva)
x=len(s)
i=0
out=0
li_results = []
#Lagged Fibonacci generator nasumicnih brojeva
def laggedFibonaccigen(j,k,s,i,li_results,x,out):
    if i == 0:
        out = (s[j-1] + s[k-1]) % 100 # pseudonasumicno generiran broj
        li_results.append(out)
        i+=1
    elif 0 < i < 13:
        s[i] = s[i+1] # pomak polja
        i+=1
    else:
        s[i] = out
    if x == 0:
        return li_results
    return laggedFibonaccigen(j,k,s,i,li_results,x-1,out)

def laggedFibbonacirekurzija(j,k,s,li,n):
    laggedFibonaccigen(j,k,s,i,li_results,x,out)
    li=li_results
    if n==0:
        return li
    return laggedFibbonacirekurzija(j,k,s,li,n-1)
# Kolicina nasumicnih brojeva koji ce se generirati
INTERVAL = 3000
# Polja u koja spremamo rezultate generatora pseudonasumicnih brojeva
resultsLCG = []
resultsLFG = []

tocke_u_krugu = 0
tocke_izvan_kruga = 0
# Spremanje trenutnog datuma i vremena u varijablu dt
dt = datetime.datetime.now()
# Pretvaranje varijable dt u integer koji ce se koristiti kao seed za linearni kongruetni generator pseudonasumicnih brojeva
seq = int(dt.strftime("%Y%m%d%H%M%S"))
# Spremanje polja pseudonasumicnih brojeva generiranih pomoću LCG-a u varijable LCG_rand_x i LCG_rand_y
LCG_rand_x=linearniGenerator(seq,3362693726,2364386438,100,INTERVAL,resultsLCG)
LCG_rand_y=LCG_rand_x
# Spremanje polja pseudonasumicnih brojeva generiranih pomoću LFG-a u varijable LFG_rand_x i LFG_rand_y
LFG_rand_x=laggedFibbonacirekurzija(3,7,s,resultsLFG,INTERVAL)
LFG_rand_y=LFG_rand_x

# Funkcija provjera provjerava da li je tocka unutar ili izvan kruga
def provjera(x, y):
    r = 100
    #Udaljenost tocke od središta kruga
    udaljenost=sqrt(x**2 + y**2)
    if udaljenost < r:
        return True
    else:
        return False 
i=int(0)
li_test=[]
def pi(Interval,tocke_u_krugu,tocke_izvan_kruga,a,b,i):
    # Nasumicno generirane x i y vrijednosti za tocke
    rand_x = a[i]
    rand_y = b[Interval]
    if provjera(rand_x, rand_y):
        tocke_u_krugu += 1
    tocke_izvan_kruga += 1
    pi_rez = 4 * tocke_u_krugu / tocke_izvan_kruga
    if Interval == 0:
        return pi_rez
    return pi(Interval-1,tocke_u_krugu,tocke_izvan_kruga,a,b,i+1)

output=pi(INTERVAL,tocke_u_krugu,tocke_izvan_kruga,LCG_rand_x,LCG_rand_y,i)
print("Aproksimacija pi koristeci nasumicno generirane vrijednosti linearnog kongruetnog generatora:",output)
output=pi(INTERVAL,tocke_u_krugu,tocke_izvan_kruga,LFG_rand_x,LFG_rand_y,i)
print("Aproksimacija pi koristeci nasumicno generirane vrijednosti LFG-a:",output)
