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

Token Codes:

a.
Regex:

Addition + [Token Code:1]

Minus – [Token Code:2]

Times * [Token Code:3]

Division / [Token Code:4]

Module % [Token Code:5]

Less than < [Token Code:6]

Greater than > [Token Code:7]

Less than Equal To <= [Token Code:8]

Greater than Equal To >= [Token Code:9]

Equal To = [Token Code:10]

 Not Equal To != [Token Code:11]
 
Assignment === [Token Code:12]

Break precedence () \(.*\) [Token Code:13]

LEFTPAREN ( [Token Code:14]

RIGHTPAREN ) [Token Code:15]

WHOLE_NUM [Token Code:16]

IDENT [Token Code:17]


Integer Literals:
1 byte = 1_1111;
 2 bytes = 2_2222;
 4 bytes = 4_4444;
 8 bytes = 8_8888

![IMG_3F5947CF30EF-1](https://user-images.githubusercontent.com/86116604/205744962-def71fe1-c99c-4f3c-9b67-bd963a968100.jpeg)


Key Words:

Loop: for_loop

Data Type declaration: num|words|
Statement Selection: if_ 



b.

 PESAMD

 < A> --> <A - B>|<A + B>|< B >
 
  < B> --> < B > * < C > |< B > / < C >|< B > % < C>|< C >
 
   < C> --> id |int |float |(< A >)


Production Rule:
  
EBNF:
  
< Program > ::= BEGIN < stmt_list > END

< stmt_list > ::= {< stmt >}

< stmt >::=< dec >|< if >|<loop_>|< assign_ >

 < dec >::= ={< stm t>';'}
 
 
 < if_ >::= if_`(` < bool > `)` `{` < stmt_list > `}` [else `{` < stmt_list > `}` ]
 
 
< loop_ >::= {' < loop_ >' (< stmt >`={;}`)` }

<assign_>::= 'id' '='< expr >

c. 

Yes,the rule sets pass the disjoint test by not starting with the same nonterminals.

d.

Not ambiguous because you cannot create 2 different parse trees



Screenshot of the ouputs:

e.

<img width="523" alt="LexicalScreenshot" src="https://user-images.githubusercontent.com/86116604/202878708-62723391-100b-4f47-82e9-2e2578991d59.png">
f.

<img width="662" alt="SyntaxScreenshot" src="https://user-images.githubusercontent.com/86116604/202878710-868ee743-5f23-4b6a-9add-d365b166bde4.png">

<img width="655" alt="Screen Shot 2022-11-19 at 4 26 18 PM" src="https://user-images.githubusercontent.com/86116604/202886009-5a86d985-f1ea-48ce-81ff-4c7e1915a2d7.png">

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

<img width="1428" alt="Screen Shot 2022-12-05 at 5 34 05 PM" src="https://user-images.githubusercontent.com/86116604/205757504-f3963592-e609-4c37-91b2-6e6ee9f61736.png">
 
 <img width="654" alt="Screen Shot 2022-12-05 at 5 35 46 PM" src="https://user-images.githubusercontent.com/86116604/205757613-c885042d-ab71-408d-81f2-080ce4549f27.png">
 
 <img width="495" alt="Screen Shot 2022-12-06 at 7 21 07 PM" src="https://user-images.githubusercontent.com/86116604/206055832-0e2631db-7ec2-43be-b3fe-3308fad2bc12.png">
 
 <img width="473" alt="Screen Shot 2022-12-06 at 7 21 38 PM" src="https://user-images.githubusercontent.com/86116604/206055858-fcd2b5a4-49c4-408b-a858-c9b6957f035e.png">




