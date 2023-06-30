grammar rules;



INTEGER: [1-9][0-9]*;
DOUBLE: INTEGER DOT INTEGER;

TRUE: 'true';
FALSE: 'false';

INT_T: 'int';
DOUBLE_T: 'double';
VOID_T: 'void';
BOOLEAN_T: 'boolean';

RETURN: 'return';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
PLUSPLUS: '++';
MINUSMINUS: '--';
MINUS: '-';
EXCLEM: '!';
TIMES: '*';
DEVIDE: '/';
MOD: '%';
PLUS: '+';
LT: '<';
GT:'>';
LE: '<=';
GE: '>=';
EQ: '==';
NE: '!=';
LOG_AND: '&&';
LOG_OR: '||';
DOT: '.';
O_B: '{';
C_B: '}';
O_P: '(';
C_P: ')';
SC: ';';
DQ: '"';
ASSIGN: '=';
COMMA: ',';
ID: {return $text not in ["true", "false", "int", "double", "void", "boolean", "return", "if", "else", "while"]}? [a-zA-Z_] [a-zA-Z_0-9]* ;

STRING: DQ BASIC_SOURCE_CHAR* DQ;
BASIC_SOURCE_CHAR: ~["\\\n] | ESCAPE_SEQUENCE;
ESCAPE_SEQUENCE: '\\' ('"' | '\\');
COMMENT: '/*' .*? '*/'-> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;



program: functions;

functions: function functions
| function;

function: type ID O_P arguments C_P block
| type ID O_P C_P block;

arguments: argument COMMA arguments
| argument;

argument: type ID;

type: INT_T
| DOUBLE_T
| BOOLEAN_T
| VOID_T;

block: O_B statements C_B;

statements: statement statements
| empty;

empty: ;

statement : SC
| block
| type items
| ID ASSIGN expression
| ID PLUSPLUS
| ID MINUSMINUS
| RETURN SC
| RETURN expression SC
| IF O_P expression C_P statement
| IF O_P expression C_P statement ELSE statement
| WHILE O_P expression C_P statement
| expression SC;

items : items item | item;

item : ID | ID ASSIGN expression;

expression: INTEGER
| DOUBLE
| ID
| TRUE
| FALSE
| STRING
| ID O_P C_P
| ID O_P parameters C_P
| O_P expression C_P
| unaryoperator expression
| expression binaryoperator expression;

parameters: expression COMMA parameters | expression;

unaryoperator: MINUS | EXCLEM;

binaryoperator: TIMES | DEVIDE | MOD | PLUS | MINUS | LT | GT | LE | GE | EQ | NE | LOG_AND | LOG_OR;
