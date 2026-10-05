coeficenti= [(1, -3, 2), (1, 2, 1), (2, 1, 3),]

prima=coefficenti[0]
a=prima[0]
b=prima[1]
c=prima[2]
desriminante=[]
for a,b,c in coefficente:
    delta=b*b-4*a*c
if delta >0:
    tipo="due soluzioni reali distinta"
x1=(math.sqrt(delta)+(-b))/(2*a)
x2=(math.sqrt(delta)-(-b))/(2*a)
soluzioni={"a":a,"b":b,"c":c,"delta":delta,"tipo":tipo,"soluzioni":str(x1)+" "+str(X2)}
elif delta == 0:
    tipo="due soluzioni coincidenti"
x1=(math.sqrt(delta)+(-b))/(2*a)
x2=(math.sqrt(delta)+(-b))/(2*a)
soluzioni={"a":a,"b":b,"c":c,"delta":delta,"tipo":tipo,"soluzioni":str(x1)+" "+str(X2)}
else:
    tipo="nessuna soluzione reale"
soluzione=(x)
soluzioni={"a":a,"b":b,"c":c,"delta":delta,"tipo":tipo,"soluzioni":str(x}