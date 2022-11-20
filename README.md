# PLC_Test2

a.
Regex:

Addition +

Minus –

Times *

Division /

Module %

Less than <

Greater than >

Less than Equal To <=

Greater than Equal To >=

Equal To =

 Not Equal To !=
 
Assignment ===

Break precedence () \(.*\)

LEFTPAREN (

RIGHTPAREN )

WHOLE_NUM

IDENT

b.

E-> E+T|E-T|T 

T->T*F|T/F|T%F

F->ident|whole_num|(E)|total

c. 

Yes,the rule sets pass the disjoint test by not starting with the same nonterminals.

d.

Not ambiguous because you cannot create 2 different parse trees



Screenshot of the ouputs:

e.

<img width="523" alt="LexicalScreenshot" src="https://user-images.githubusercontent.com/86116604/202878708-62723391-100b-4f47-82e9-2e2578991d59.png">
f.

<img width="662" alt="SyntaxScreenshot" src="https://user-images.githubusercontent.com/86116604/202878710-868ee743-5f23-4b6a-9add-d365b166bde4.png">

g.

2 with no errors:

(sum+4*5)*num(6-)/total*(n)+(5)+(amount)/(x+4*5)*num(6-4)

(a*b*c)+(d+4*5)*e(6-)/f*(n)+(5)+(r)/(x+4*5)*g(6-4)+11

1 with  syntax error

int x = ((a*b**c)+(d+4*5)*e(6--)//f*(n)++(5)+(r)/(x+4*5)*g(6-4)++11;

int isn't define

; isn't define

** isn't deine

// isn't define

++ isn't define

1 with lexical error

@(sum+4*5)*num^?(6-)/total*(n)+(5)+(amount)/#(x+4*5)*num(6-4)&

@ symbol not define

# symbol not define

^ symbol not define

& symbol not define

? symbol not define




h.

<img width="1423" alt="Screen Shot 2022-11-19 at 11 36 44 PM" src="https://user-images.githubusercontent.com/86116604/202885832-3d25c8e7-6a04-4b01-9ce5-47aa2f912b6b.png">




