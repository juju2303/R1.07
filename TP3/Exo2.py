import time

'''
def compte_rebours():
    n = int(input("Entrez le nombre pour le compe à rebours : "))
    for i in range(n, -1, -1):
        print(i)
        time.sleep(1)
print(compte_rebours())
'''
def compte_rebours():
    n = int(input("Entrez le nombre pour le compe à rebours : "))
    while n >= 0:
        print(n)
        n = n - 1
        time.sleep(1)
print(compte_rebours())