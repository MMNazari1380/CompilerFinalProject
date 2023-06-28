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
X_P: ')';
SC: ';';
ASSIGN: '=';
COMMA: ',';
EMPTY: ' ';
ID: [a-zA-Z_] [a-zA-Z_0-9]* {
	if (getText().equals("true") ||
	    getText().equals("false") ||
	    getText().equals("int") ||
		getText().equals("double") ||
		getText().equals("void") ||
		getText().equals("boolean") ||
		getText().equals("if") ||
		getText().equals("else") ||
		getText().equals("while") ||
		getText().equals("return")){
			System.err.println("Error");
		}
};

STRING: BASIC_SOURCE_CHAR*;
BASIC_SOURCE_CHAR: ~["\\\n] | ESCAPE_SEQUENCE;
ESCAPE_SEQUENCE: '\\' ('"' | '\\');



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
| EMPTY;

statement : SC
| block
| type items
| ID ASSIGN expression ;
| ID PLUSPLUS ;
| ID MINUSMINUS ;
| RETURN SC
| RETRUN expression SC
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
| unary-operator expression
| expression binary-operator expression;

parameters: expression COMMA parameters | expression;

unary-operator: MINUS | EXCLEM;

binary-operator: TIMES | DEVIDE | MOD | PLUS | MINUS | LT | GT | LE | GE | EQ | NE | LOG_AND | LOG_OR;
