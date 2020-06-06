%sintomas 

sintomas(fiebre).
sintomas(fatiga).
sintomas(tosSeca).
sintomas(faltaDeApetito).
sintomas(doloresDeCuerpo).
sintomas(dificultadAlRespirar).
sintomas(mucosidad).

%relacion sintomas medicamento
%hermana(x,y): x tomar medicamento y

tomar_medicamento(acetaminofen,fiebre).
tomar_medicamento(ibuprofeno,fiebre).
tomar_medicamento(aspirina,fiebre).
tomar_medicamento(cafeina,fatiga).
tomar_medicamento(metifenidad,fatiga).
tomar_medicamento(dextroafetamina,fatiga).
tomar_medicamento(modafilino,fatiga).
tomar_medicamento(levodropropizina,tosSeca).
tomar_medicamento(dropropizina,tosSeca).
tomar_medicamento(dextrometorfano,tosSeca).
tomar_medicamento(cloval,tosSeca).
tomar_medicamento(aceiteDePescado,faltaDeApetito).
tomar_medicamento(iproheptadina,faltaDeApetito).
tomar_medicamento(pizotifeno,faltaDeApetito).
tomar_medicamento(ibuprofeno,doloresDeCuerpo).
tomar_medicamento(paracetamol,doloresDeCuerpo).
tomar_medicamento(dipirona,doloresDeCuerpo).
tomar_medicamento(albuterol,dificultadAlRespirar).
tomar_medicamento(levalbuterol,dificultadAlRespirar).
tomar_medicamento(combivent,dificultadAlRespirar).
tomar_medicamento(ambroxol,mucosidad).
tomar_medicamento(mucovital,mucosidad).

:-
write('Realizar Test ingrese si o no').

si :-
write('Favor ingresar el numero 1 si su respuesta es SI'),nl,nl,
write('Si su respuesta es NO ingresar el numero 0 a las siguientes preguntas'),nl,nl,
write('Tiene fiebre: '), read(A),nl,
write('Tiene fatiga: '), read(B),nl,
write('Tiene tos seca: '), read(C),nl,
write('Tiene falta de apetito: '), read(D),nl,
write('Tiene Dolores de cuerpo: '), read(E),nl,
write('Tiene dificultad al respirar: '), read(F),nl,
write('Tiene mucosidad: '), read(G),nl,


H is A * 20,
I is B * 20,
J is C * 20,
K is D * 10,
L is E * 10,
M is F * 10,
N is G * 3,
R is H + I + J + K + L + M + N,
COVID is 90,

%reglas
write('El resultado es: '),write(R),write('%'),tab(1),nl,nl,

(R > COVID -> write('USTED TIENE COVID19 '); (R < COVID ->write('USTED NO TIENE COVID19 ')) ),nl,nl,

write('MEDICINA RECOMENDADA '),nl,nl,

(A = 1 -> write('USTED TIENE FIEBRE PUEDE TOMAR ACETAMINOFEN, IBUPROFENO, ASPIRINA '); (A = 0 -> write(' ')) ),nl,
(B = 1 -> write('USTED TIENE FATIGA PUEDE TOMAR CAFEINA, METIFENIDATO,DEXTROAFETAMINA,MODAFILINO '); (B = 0 -> write(' ')) ),nl,
(C = 1 -> write('USTED TIENE TOS SECA PUEDE TOMAR LEVODROPROPIZINA,DROPROPIZINA,DEXTROMETORFANO,CLOVAL  '); (C = 0 -> write(' ')) ),nl,
(D = 1 -> write('USTED TIENE FALTA DE APETITO PUEDE TOMAR ACEITE DE PESCADO,IPROHEPTADINA,PIZOTIFENO '); (D = 0 -> write(' ')) ),nl,
(E = 1 -> write('USTED TIENE DOLORES DE CUERPO PUEDE TOMAR IBUPROFENO,PARACETAMOL,DIPIRONA '); (E = 0 -> write(' ')) ),nl,
(F = 1 -> write('USTED TIENE DIFICULTADPARA RESPIRAR PUEDE TOMAR ALBUTEROL,LEVALBUTEROL,COMBIVENT '); (F = 0 -> write(' ')) ),nl,
(G = 1 -> write('USTED TIENE MUCOSIDAD PUEDE TOMAR AMBROXOL,MUCOVITAL '); (G = 0 -> write(' ')) ),nl,nl,

FARMACIA is 1,
R1 is A+B+C+D+E+F+G,

write('FARMACIAS CERCANAS'),nl,nl,

(R1 >= FARMACIA -> write('Farmacia Galeno 24, 2 Av, Cdad. de Guatemala '),nl,
write('Farmacia galeno zona 6, Cdad. de Guatemala '),nl,
write('Farmacias Galeno 15 Av. Z. 6, 2-61, 15 Avenida 6, Cdad. de Guatemala '),nl,
write('Farmacias Galeno, 15 Calle C 15-72 '),nl,
write('Farmacia galeno zona 6 15 av 12 calle, Cdad. de Guatemala'),nl,
write('Farmacia galeno zona 6 1 calle santa luisa, Cdad. de Guatemala '),nl,
write('1A. Calle Y 2A. Av. Lote 13 "A", Jocotales Zona 6 Chinautla, Guatemala'); (FAR