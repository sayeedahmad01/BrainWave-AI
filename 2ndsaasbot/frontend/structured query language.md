structured query language

\-> it is a language use to communicate with db server (MySQL, oracle, sql server)

\-> a query is a command/instruction/question given to db server ti perform  some action on db

\-> sql originally introduced by IBM  and initial language of this language was 'seqential'and later it is renamed to sql

\-> SQL  is common to all relational database servers



OLTP                                               OLAP





\-> based on the operations over db SQL is categorized into following sub-languages



DDL= data definition language

DML= data manipulation language

DR/DQL = data retrieval language/data query language

TCL = transactional control language

DCL = data control language



which operation are going there in each command are listed below



DDL = create, alter , drop,  truncate

DML = insert, update, delete, merge

DQL = select

TCL = commit, rollback, save transaction

DCL = grant, revoke



open ssms (sql server management studio) and enter username  \& password



&#x20;     server name :-Desktop -G2DM7GI

&#x20;     authentication :- window/SQL sever

&#x20;     username :- SA (system admin)

&#x20;     password :- 1234





creating database in sql server:-

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\---------------------------------------

&#x20;in object explorer select database => new databse

enter database name:-DBMS



click Ok



command to create and execute the folling command

\--------------------------------------------------

\------------------------------------------------------

create new query and execute the following command



CREATE DATABASE NARESHIT















































1\) name should start with alphabet

2\) name should not contain spaces \& special character  but allows\_$ #

3\) name can be unto 128 chars

4\) a table can have max 1024 columns

5\) no of rows unlimited



&#x20;     123emp invalid

&#x20;     emp 123 invalid

&#x20;     emp\*123 invalid

&#x20;     emp\_123 valid





EX:

\-> create table with following structure?

&#x20;

CUST

CID    NAME    GENDER   AGE   CITY    DOR



CREATE TABLE CUST

(

&#x20; CID   TINYINT,

&#x20; NAME  VARCHAR(10),

&#x20; GENDER CHAR(1),

&#x20; AGE   TINYINT,

&#x20; CITY  VARCHAR(10),

&#x20; DOR   DATE

)



\-> above command is created table structure that includes columns, datatypes and



INSERTION DATA INTO TABLE :-

\---------------------------



\-> "INSERT" command is used to insert data into table

\-> INSERT command creates row

\-> we can insert



1\) single row

2\) multiple rows





inserting single rows:

\----------------------



INSERT INTO<tabname>VALUES(v1,v2,v3-----)



EX:-

INSERT INTO CUST VALUES(100,'sachine','m',40,'hyd','2026-06-26')

INSERT INTO CUST VALUES(101,'sayeed','m',23,'Lucknow','2003-12-25')



MULTIPLE ROWS:-

\---------------

INSERT INTO CUST VALUES(102,'arvind','m',44,'mun','2020-02-22'),

&#x20;                      (103,'mansha','f',25,'hyd','2018-10-15')







insetting the nulls:

\-------------------

\-> a null means blank or empty

\-> null inserted way into two way

\-> it is null equal to zero



method 1:

\--------



INSERT INTO  cuts VALUES(104,'david','m','NULL','hyd','NULL')





METHOD 2:

\-----------



INSERT INTO Cust VALUES(105,'sindhu','f','del')



\-> remaining two fields are filled with nulls



Operation operator:

\------------------



Arithmetic operation      ---> +,-,\*,%

Relational operators  ------> > ,= ,<, <= !=, <>

Logical operators ----> AND, OR , NOT

Special operators --> BETWWEN IN LIKE IS ANY ALL EXISTS PIVOT

Set Operators----> UNION ,UNION ALL INTERSECT EXCEPT

Concatenation Operators ====> +





Displaying Data:

================



"SELECT" command is used to display the data from table

=> we can display all rows or specific rows

=> we can display all columns or specific columns



&#x20;  SELECT col1, col2, col3---/ \* 	FROM table name



SQL   =   ENGLISH

QUERIES = SENTENCES

CLAUSES = WORDS



FROM clause ==> specify table name

SELECT clause ==> specify column names

&#x20;          \*    => all columns



EX:

&#x20;   ==> display customer names and gender ?



SELECT name, gender FROM cust



==> display customer







where clause:

============

=> use where clause to select specific row/rows from table

=> where clause is associated with condition



&#x20;SELECT columns

&#x20;FROM tablename

&#x20;WHERE condition





condition:

==========



&#x20;      cCOLNAME     OP     VALUE



&#x20;=>a condition is a relation expression that return TRUE/FALSE

==> OP must be any relational oprater  like => > >=,< <= !=

=> if condition = true then row will be selected

=> if condition = false then row is not selected



EX:

==> display customer details whose cid = 102 ?

SELECT \* FROM  cust  WHERE cid = 102



=> display customer details whose name = 'David'

&#x20; SELECT \*FROM 	cust WHERE name  = 'david'

=>display customer age>30?

=> display customers registration after 2020?

SELECT \*FROM cust WHERE dor > 2020 ==> ERROR

SELECT\* FROM cust WHERE dor > '2020-12-31'



compound condition\_

==================



multiple combination combined with AND/OR oprators is called compound conditions



WHERE     COND1    AND       COND2           RESULT

&#x20;            T                 T              T

&#x20;            F                 F              F

&#x20;            F                 T              F

&#x20;            F                 F              F

WHERE    COND1     OR        COND2          RESULT

&#x20;          T                  T              T

&#x20;          F                  F              F

&#x20;          T                  F              T

&#x20;          F                  T              T





&#x20;  => list of customer staying in hyd,bir?

SELECT \* FROM cust WHERE city = 'hyd' AND





















=> students who fail two subjects in 2 subjects?

SELECT \*

FROM students

WHERE (s1>=35AND s2<35AND s3<35)



&#x20;     OR

&#x20;     (s1<35AND s2>=25 AND s3<35)

&#x20;     OR

&#x20;     (s1<35 AND s2<35 AND s3>=35)



IN operator:

============

=> use IN operator for list comparison

=> use IN  operator for "=" comparison with multiple values



&#x20;   WHERE colname = v1, v2, v3 --  => INVALID

&#x20;   WHERE colname  IN (v1,v2,v3--) =>  VALID

=> list of customers whose id  = 100,101,103?

&#x20; SELECT \*

&#x20; FROM cust

WHERE cid IN (100,101,103)





=> LIST  of customer staying in hyd, bir, mum?

&#x20;SELECT  \*

&#x20;FROM cust

&#x20;WHERE city IN ('hyd',





BETWEEN operator:

===============



=> use between operator for range comparison

&#x20;     list => 10,20,30,40,50

&#x20;     range => 10 to 50

&#x20;WHERE colname BETWEEN v1 AND  v2

EX:

=> list of customer age between 20 \& 30?

SELECT \*

FROM cust

WHERE  age BETWEEN 20 AND 30(20 and 30 are included)

=> customer registered in 2020?

&#x20;SELECT \*

FROM  cust

WHERE dor BETWEEN '2020-01-01' AND '2020-12-31'



=>*display female customers*

*staying in hyd, bir*

*age between 20 and 30?*

*not registered in 2020 ?*



*SELECT \**

*FROM cust*

*WHERE gender ='f'*

&#x20;      *AND*

&#x20;     *city IN ('hyd','bir')*

&#x20;     *AND*

&#x20;     *age BETWEEN 20 to 30*

&#x20;     *ABD*

&#x20;     *dor NOT BETWEEN '2020-01-01' AND '2020-12-31'*



*=> list of Samsung , redmi,redmi, realmi price  between 10000 and 20000?*

*PRODUCTS*



*prodid   pname         price       category      brand*





*SELECT \**

*FROM products*

*WHERE brand IN('samsung', 'redmi', 'realme')*

&#x20;           *AND*

&#x20;          *price BETWEEN 10000 AND 20000*

&#x20;         *AND*

&#x20;         *category='mobiles'*







*=> customer*















*ORDER BY clause:*

*================*

*=> ORDER BY clause is used to sort table*

*=> ORDER BY is based on one or more fields*

*=> we can  sort  data either in ascending or descending order*



&#x20;                  *ASC                        DESC*

*NUMERUIC          0-9                         9-0*

*CHAR              A-Z                         Z-A*

*DATE             OLD-NEW                   NEW-OLD*



*syntax:*

*---------*

*SELECT columns*

*FROM tablename*

*\[WHERE cond]*

*ORDER BY colname ASC/DESC, colnameASC/DESC,-------*























*=> TRANSACTIONS:*

*================*

*TRID     TIYPE        TDATE          TAMT      ACCCNO*

*1         W           02-jul-26      2000*       100



SELECT \*

FROM TRANSACTIONS

WHERE ACCON0 = 100

&#x20;      AND

&#x20;      TDATE BERTWEEN '2026-01-01' AND '2026-07-01'

ORDER BY TDATE DES



sorting based on multiple :

\----------------------------



=> arrange employee list dept wise asc and with in dept sal wise desc?

SELECT  empno, enmae, sal, depatna

FROM emp'ORDER BY deptno ASC, sal DESC



1 A 30000 20                 6 F 60000 10

2 B 10000 30                 3 C 40000 10

3 C 40000 10 =========>      5 E 60000 20

4 D 50000 30                 1 A 30000 20

5 E 60000 20                 4 D 50000 30

6 F 60000 10                 2 B 10000 30





=>

STUDENT

sno       sname      m       p      c

1           A        80      90     70   240

2           B        60      70     70   240

3           C        90      70     80   240

4           D        90      80     70   180





SELECT\*

FROM STUDENT

ORDER BY(M+P+C)







==> DISPLAY employees joined in 1981 years

arrange  output name wise asc?



SELECT \*

FROM  EMP

WHERE hiredate LIKE '1981%'

ORDER  BY enmae ASC











TOP clause:

============



=> top class returns top n rows

&#x20;

&#x20;  SELECT \[DISTINCT] TOP <n> col1, col2, col3.-----

&#x20;  	FROM tablename

&#x20;       \[WHERE cond]

&#x20;       \[ORDER BY ---]

EX:--

SELECT TOP 5\*

FROM EMP

ORDER BY SAL DESC



Execution:-

=========



FROM

ORDER BY

SELECT

TOP



=> display top 3  max salaries?

SELECT SAL  ( WHEN we apply distinct duplicate will be remove)

FROM EMP

ORDER BY SAL DESC



OR



SELECT DISTINICT TOP 3 SAL

FROM EMP

ORDER BY SAL DESC



=> TOP 3 EMPLOYEES BASED ON EXPERIANCE

&#x20;

&#x20;    SELECT \*

&#x20;    FROM  EMP

&#x20;    ORDER BY HIREDATE ASC



=> latest 5 transactions of particular customer ?



&#x20;  TRANSACTIONS

trid        ttype         tdate           tamt          accno

1            w            2026-07-02       2000          100

2            D            2026-07-03       5000          101



SELECT  \*

FROM TRANSACTIONS

WHERE ACCNO = 100

&#x20;     AND

&#x20;     TTYPE = 'D'

ORDER BY TDATE DESC





WHERE=> TO filter data

ORDER=> TO SHORT THE DATA

DISTINCT => TO ELIMINATE DUBLICATES

TOP=>  to display top n rows





DML commands:-

==============



INSERT

UPDATE

DELETE

MERGE



=> ALL DML commands acts on table data

=> all DML commands are auto committed(saved)

=> top stop auto commit execute the following command



&#x20;    SET IMPLICIT\_TRANSACTIONS ON



=> TO SAVE the dml operation  execute COMMIT

=> TO save the dml operation execute ROLLBACK





TABLE =        ROW(DATA)   +           COLUMNS(STRUCTURE)

&#x20;                DML                       DDL

&#x20;

&#x20;                INSERT

&#x20;                UPDATE

&#x20;                DELETE

&#x20;                MERGE







UPDATE Command:

===============

=> command used to modify the table data

=> we can update column or multiple columns

=> we can update all rows or specific rows





&#x20;   UPDATE tabname

&#x20;   SET colname = value , colname =  value,--------

&#x20;   WHERE cond



EX:

=>  update all employees comm with 500?

&#x20;UPDATE emp comm = 500

=> update employee comm with 800 whose empno = 7369?

&#x20;UPDATE emp SET comm = 800 WHERE  empno = 7369



=> update sal with 2000 and col comm with 500

those working as salesman and  join in 1981 year



UPDATE emp

SET sal = 2000, comm = 500

WHERE job  = 'SALESMAN'

&#x20;     AND

&#x20;     hire   LIKE '1981%'





4-JUL-2026



=> INCREASE sal by 20% and comm by 10%

only those employees working as clerk, manager working for dept 20, 30















DELETE COMMAND:-

================

=> Command used to delete rows/rows from table

=> we can delete all rows or specific rows

&#x20;EX:=

=> delete all rows from emp?

DELETE FROM emp

=>delete employee whose empno = 7369?

DELETE FROM EMP WHERE job IN('CLERK','%MAN%')



above query

A   ERROR

B    delete clerk, manager, salesman

C    deletes only clerk

D     none

&#x20;

ans:- C => because %MAN% is not treated as pattern



DELETE FROM emp WHERE job = 'CLERK' OR job LIKE  '%MAN%'



ANS:- B



&#x20;



DDL commands:-(Data definition language)

=============

CREATE

ALTER

DROP

TRUNCATE



=> DDL commands acts on table structure(columns, datatype, size)



How to see the table structure:-

===============================



SP\_HELP  EMP     (SP => stored procedure)





ALTER command:-

==============

=> command used to modify the table structure

=> using ALTER command we can

1 add columns

2 drop columns

3 modify column

&#x20;        changing datatype

&#x20;        changing size



Adding columns:-

==============

ALTER TABLE  tablename

&#x20;     ADD colname  datatype(size),------------

EX:-

=> add colum gender to emp table ?

ALTER TABLE emp

&#x20;     ADD gender CHAR(1)

after adding by default the new column is filled with nulls

to insert data into the new column use update command



UPDATE emp SET gender  = 'M' WHERE  empno  = 7499

&#x20;=> drp the col gender

&#x20; => alter table emp drop col gender

&#x20;   select \* from emp

&#x20;    rollback

&#x20;=> added col, updare, derop col, rollback, we do it all but it not show the table then what?

&#x20;    => ALTER TABLE EMP









Modifying columns:=

==================

=> modify columns empno datatype to int?

EX:

AFTER









=> MODIFYING COlumn hiredate datatype to datetime?





ALTER TABLE emp

&#x20; ALTER COLUMN hiredate  DATETIME







TRUNCATE command:

=================

=> deletes all the data from table but keeps  structure

=> will empty the table

=> releases memory





EX: TRUNCATE TABLE customer



DROP VS DELETE VS TRUNCATE

=============================



DROP                                 DELETE/TRUNCATE

drop structure with data                   delete only data but not structure





&#x20;  DELETE                                 TRUNCATE





1  DML command                            DDL command

2  can delete all rows                    can delete only all rows

&#x20;   and specific rows                     but can not delete specific rows

3 where cond can be used with delete      where cond can not be used be used with truncate

4 deletes row by row                      deletes all rows at a time

5 slower                                  faster

6 will not release memory                 release memory



SP\_RENAME:

==========

=> command used to rename table OR COLUMN

&#x20;    SP\_RENAME 'old name','new name'











Built-in function in SQL:

===========================



=> A function  is a program that accepts some input performs some calculation and returns one value

=> function are used

&#x20; 1) Data processing

2\) data cleaning

3\) data transforming

4\) data analysis



Types of function:

==================



1. character functiuon
2. data function
3. numeric function
4. conversion function
5. special function
6. analytical function
7. aggregate function





Character function:

===================

UPPER() \& LOWER :

================



UPPER(arg) => converts string to uppercase

LOWER(arg):=> converts string to lowercase



EX:

SELECT UPPER('naresh') => NARESH

SELECT  LOWER('NARESH') => naresh









=> employee list name contains 5 chars ?

SELECT \* FROM emp WHERE ename  LIKE '\_\_\_\_\_\_'

SELECT  \* FROM emp WHERE LEN(ename)  = 5



LEFT() \& RIGHT():-

================

LEFT(string, no of characters) => returns chars starting from left side

RIGHT(string, no of chars) => returns chars starting from right side



EX:=

SELECT LEFT('HELLO WELCOME',5) => HELLO

SELECT RIGHT('HELLO WELCOME',7) => WELCOME



=> employees name starts and ends with same char?

WHERE enmae LIKE 's%s'

&#x20;       OR

&#x20;       enmae LIKE 'b%b'



SELECT \*FROM emp WHERE LEFT(ename,1) = RIGHT(ename,1)

=> generate email ids for employees as follows?



&#x20;   empno                  ename                      emailed

&#x20;   7499                   nitin                   nit786@tcs.com

&#x20;   7521                   ward                    war752@tcs.com



SELECT empno, ename,

LEFT(ename, 3)   +    LEFT(empno,3) + '@tcs.com' as emailed

FROM emp

=> store email ids in database?



&#x20; step1:- add emailed column to emp table

ALTER TABLE emp

&#x20;      ADD emailed VARCHAR(20)



&#x20;step 2: update the column with email ids

&#x20;  UPDATE emp

&#x20;  SET emailed = LEFT(ename, 3)   +    LEFT(empno,3) + '@tcs.com'





SUBSTRING():

=============

=> returns  chars starting from specific position



&#x20;      SUBSTRING(string, star,\[no of chars])

EX:-

SELECT SUBSTRIBG('Hello Welcome',1,5) => HELLO

SELECT SUBSTRING('HELLO WELCOME',7,5) => WELCOME

SELECT SUBSTRING('HELLO WELCOME', 10) => COME





CHARINDEX():

==============



=> RETURNS position of a character in a string



&#x20; CHARINDEX(char, string, \[start])



EX:-

SELECT CHARINDEX('O','HELLO WELCOME') => 5

SELECT CHARINDEX('K','HELLO WELCOME') => 0

SELECT CHARINDEX('O',;HELLO WELCOME', 6) => 13



EX:-



CUST

cid         cname

10          Sachine Tendulkar

11          Virat kohali





=> display CID  FNAME   LNAME

&#x20;

&#x20;  FNAME  =  substring(string, start, no of chars)

&#x20;

&#x20;            substring(cname,1,charindex('',cname)-1)



LNAME = substring(cnmae, charindex('', cname)+1)



SELECT cid,

&#x20;         substring(cname,1,charindex('', cname)-









RUPLICATE():-

===========



=> repeats given char  for given no of times

&#x20;       REPLICATE(char, length)

EX:- SELECT RUPLICATE('\*',5)

=> display ENAME SAL ?

&#x20;

SELECT ENAME,REPLICATE('\*', LEN(SAL)) AS SAL FROM EMP

&#x20;        allen          \*\*\*\*



=> your a/c no xxxxx8758 debited



ACCOUNTS

account             bal

123345677989         2000



&#x20;      REPLICATE('X',4)     +    RIT(ACCNO,4)



&#x20;



REPLACE():

===========



=> functions used to replace one string with another string

&#x20;         REPLACE(string1, string2, string3)

=> in string1, atring2 replace  with string 3

EX: SELECT REPLACE('HELLO','L','ABC')=> HABCO

&#x20;   SELECT REPLACE('HELLO','L','ABC') => HEABCABCO

&#x20;   SELECT REPLACE('HELO','ELO','ABC') => HELLO



&#x20;   SELECT REPLACE('@@HE@@L@@@','@',") => HELLO





=> IN heridate replace month April with October in table??



UPDATE  EMP SET HIREDATE = REPLACE(HIREDATE,'-04-','-10-')



TRANSLATE():

===========



=> USED TO TRANSLATE  one char to another charater

&#x20;    TRANSLATE(string1, string2, string3)



EX:

&#x20; SELECT TRANSLATE('HELLO','ELO','ALB')  => HABBC



E=> A

L=> B

O=> C

=> TRANSLAE FUNCTION CAN  be used to encrypt data i.e converting plain text  to cipher text

display ENAME    SAL   ?  encrypt  salaries?



SELECT ENAME,TRANSLATE(SAL,'0123456789','$bT\*#@^%!k) AS SAL FROM  EMP

jones 2975.00   T!^\&$$





= remove all special chars from !@HE#SLL%^O\&\*^

EX:

=> remove numeric part from 'abc123xyz456' ?

=> remove character part from 'abc123xyz456'





DATE function:

=============



DATEPART():

===========



=> USED TO extract part of the data

&#x20;        DATEPART(YY, GETDATE)



EX:-



SELECT DATAPART(YY, GETDATE()) =>  2026

&#x20;                MM             => 07

&#x20;                DD            =>  08

&#x20;                DW            => 4

&#x20;                DY            =>

&#x20;                HH            => HOURS

&#x20;                MI            => MINUTES

&#x20;                SS            => SECONDS

&#x20;                QQ            => 3(3 JUL-SEP)



=> Display ENAME YEAR\_OF\_JOIN ?

SELECT ENAME, DATEPARTY(YY, HIREDATE) AS YEAR\_OF\_JOIN FROM EMP



=> display employees joined in 1980,1983, 1985?

&#x20;

SELECT \*

FROM emp

WHERE DATEPART(YY, HIREDATE) IN (1980,1983,1985)



=> who are joined in leap year ?

SELECT \*

FROM emp

WHERE DATEPARTY(YY, HIREDATE)%4 = 0

=> who joined on sunday ?



SELECT \*

FROM emp

WHERE DATEPART(DW, HIREDATE) =1

=> who joined in 2nd quater of 1981 year ?

SELECT \*

FROM EMP

WHERE DATEPART(YY, HIREDATE)=1981

&#x20;        AND

&#x20;    DATEPART(QQ, HIREDATE) = 2



DATENAME():-

============



=> similar to datepart used to extract part of the date





&#x20;                       MM                   DW

DATEPART                 7                   4

ATENAME                 July                Wednesday







DATEADD:

=========



=> TO add/substract days/months/years to//from a date



&#x20;    DATEADD(INTERVAL, INT,DATE)

EX:

SELECT DATAADD(ADD,10,GETDATE())=> adds 10 days to generate =>

&#x20;







=> display ENAME DAY ?

SELECT ENAME











=> display employees joined today ?

INSERT INTO emp(empno, enmae,sal,hiredate) values(100,'ABC',2000,GETDATE())

SELECT\*FROM emp WHERE hiredate = CAST(GETDATE() AS DATE)



&#x20;                  2026-07-10 = 2026-07-10





=> GOLD RATES

&#x20;  DATED             RATE

&#x20;  2024-01-01         ?

&#x20;  2024 -01-02        ?



&#x20;  2026-07-10         ?







=> DISPLAY TODAYS gold rate?

SELECT \* FROM GOLD\_RATES WHERE DATED = CAST(GATDATE()AS DATE)

=> display yesterday's gold rate ?

SELECT\*

FROM GOLD RATES

WHERE DATEDID = CAST(DATEADD(DD,-1,GATEDATE()) AS DATE)

=> display last month same day gold rate ?

SELECT \*

FROM GOLD RATES

WHERE DATEID = CAST(DATEADD(MM,-1,GETDATE()) AS DATE)





=> display last year same day gold rate?

SELECT \*

FROM GOLD RATES

WHERE DATEID = CAST(DATEADD(YY,-1,GETDATE()) AS DATE)



=> display last 1 month gold rate ?

SELECT \*

FROM GOLD RATES

WHERE DATED BETWEEN CAST(DATEADD(MM,-1,GETDATE()) AS DATE)

&#x20;                             AND

&#x20;                           CAST(GETDATE()  AS DATE)



**DATEDIFF():**

**===========**



**=> used to find difference two dates**

**=> difference can be calculated in days/months/years**



&#x20;           **DATEDIFF(INTERVAL, START DATE,END DATE)**

**EX:**

&#x20;     **SELECT DATEDIFF(DD,'2025-07-10',GETDATE()) => '12'**

&#x20;     **SELECT DATEDIFF(MM,'2025-07-10',GETDATE()) => '365'**

&#x20;     **SELECT DATEDIFF(YY,'2025-07-10', GATEDATE()) => '1'**



=>display ENMAE EXPERIENCE in years ?

SELECT ename, DATEDIFF(YY,  hiredte()) as experience FROM emp



=> display ENAME EXPERIENCE in years?

&#x20;            M years N   months

experience = 40 months = 3 YEARS 4 months



YEARS = months/12 = 40/12 =  40//12



**MONTHS  = months%12 = 40%12 =4**



**SELECT ename, DATEDIFF(MM,hiredate, getdate())/12 as years,**

&#x20;                    **DATEDIFF(MM,hiredate())%12 as months**



**FROM emp**

**NITHIN             1981-02-20             2026-02-20          45**

&#x20;                                             **03**

&#x20;                                             **04**

&#x20;                                             **05**

&#x20;                                             **06**

&#x20;                                             **07**

&#x20;

**=> display ENAME EXPERIENCE ?**

&#x20;                **M YEARS  N  MONTHS D DAYS**

**ex:- 500 days**



**YEARS: 500/365 = 1(With a remainder of 135 days)**

**Months:135/**













**Numeric function:**

**===============**

**ROUND**

**CEILING**

**FLOOR**



**ROUND():**

**=========**

**=> rounds numbers to integer or to decimals places**

&#x20;  **ROUND(number, decimal place)**

**EX:-**

&#x20;  **SELECT ROUND(38,5678,0)    =>**



**38..........................38.5..................................39**

&#x20;

&#x20;                           **number>=avg=>rounded to highest**

&#x20;                           **number < avg => rounded to lowest**



**SELECT ROUND(38.678,0)   => 38**

**SELECT ROUND(38.5678,2)  => 38.57**

**SELECT ROUND(38.5678,1)  => 38.6**





**SELECT ROUND(386,-1)   => 390**



**380.......................385..............................390**





**SELECT ROUND(386,-2)                 =>                   400**



**300..........................350...........................400**





**SELECT ROUND(386,-3)          =>                      0**

&#x20;**0..........................500.......................10000**





**CEILING():**

**===========**

**=> rounds number always to highest**

&#x20;          **CEILING(number)**



**Ex:**

&#x20;**SELECT CEILING(3.1)            =>    4**





**FLOOR():**

**======**

**=>  round number  always to lowest**



&#x20;            **FLOOR(number)**

**EX:-**

&#x20;      **SELECT FLOOR(3.9)       =>          3**



**CONVERSION FUNCTION():**

**=======================**

**=> function used to convert one datatype to another datatype**





&#x20;   **1) CAST**

&#x20;   **2) CONVERT**



**CAST:-**

**=======**



&#x20; **CAST(EXPR AS TARGET-TYPE)**

**EX:-**

&#x20; **SELECT CAST(10.5 AS INT)        =>   10**

&#x20; **SELECT CAST(10 AS DECIMAL(4,2))  => 10.0**

&#x20; **SELECT CAST(GETDATE() AS DATE)    => 2026-07-10**















**ISNULL():**

**==========**



**=> function used to convert null values**



&#x20;     **ISNULL(arg1, arg2)**

&#x20;     **if arg1 = null returns arg2**

&#x20;     **if arg1 <> null returns arg1 only**

**EX:**



**SELECT ISNULL(100,200)  => 100**

**SELECT ISNULL(NULL,200)  => 200**



**=> display ENAME SAL COMM TOTSAL**

&#x20;  **TOTSAL = SAL + COMM**



**SELECT ENAME,SAL,COMM,SAL+COMM AS TOTSAL FROM EMP**



**ABC        2000.0     NULL     2000**

**nitin      1600.0     300.0    1900.0**

**ward       1250.00    500.00   1750.00**

**joins      2975.0     NULL     2975**





=> **Display ENAME SAL COMM?**

&#x20;  **IF comm = NULL display N/A ?**



**SELECT ENAME, SAL, ISNULL(COMM,'N/A') AS COMM FROM EMP => EMP**

**SELECT ENAME, SAL, ISNULL(CAST(COMM, AS VARCHAR),'N/A') AS COMM FROM EMP => EMP**



**ABC        2000.0     N/A**

**nitin      1600.0     300.0**

**ward       1250.00    500.00**

**joins      2975.0     N/A**





**=> display SNO SNAME M P C TOTAL ?**

&#x20;   **If subject marks = NULL display 'ABSENT'**



**STUDENT**

**sno       sname       m       p        c**

**1         A           70      60       50**

**2         B           NULL    50       60**

**3         C           40      NULL     NULL**





**COALESCE():-**

**===========**





**=> returns first not null expression**

&#x20;

&#x20;  **COALESCE(exp1,exp2,exp3,....................)**

**EX:**

**SELECT COALESCE(NULL,100,NULL,200)     =>    100**

**SELECT COALESCE(100, 200, 300,400)     =>    100**

**=> display    CNAME      CONTYACT ?**

**if phone is available   display    phone**

**if  phone not available   display   emailid**

**if emailid  not available display  addr**

**=>**

**CUST               cname             phone             emailid               add**

**100                A                  98               abc@gmail.com          hyd**

**101                B                  NULL             xyz@ gmail.com         hyd**

**102                C                  NULL             NULL                   hyd**





**SELECT cname,COALESCE(pbone,email,addr) as**







**EX:-**



**T1**

**D      VARCHAR(20)**

**13-07-2026**

**07/13/2026**

**13-07-2026**

**07-13-2026**



**=> Standardize**



**ANALYTICAL FUNCTION/WINDO FUNCTION**

**===================================**



**RANK**

**DENSE\_RANK**

**ROW\_NUMBER**

**LAG**

**LEAD**

**NTILE**



**RANK \& DENSE\_RANK:-**

**===================**

**=> used to find ranks**

**=> ranks are based on one or more columns(ex:-salary , hiredate,--)**

**=> for ranks function date must be sorted**



&#x20;          **RANKED()  OVER (ORDER BY colname ASC/DESC,...........)**

&#x20;          **DENSE\_RANK() OVER (ORDER BY colname ASC/DESC,.........)**



**EX:-**

**=> display ranks of the employees based on sal?**

**highest  paid employee should get 1st ranked?**



&#x20;**SELECT  emp, ename, sal**

&#x20;     **DENSE\_RANK()  OVER(ORDER BY sal DESC) as rnk**

**FROM emp**



**difference between are same then rank function will skip next rank**

**but dense\_rank will not skip next rank?**



**if two ranks same then rank function will skip next rank**

**but  dense\_rank  will not skip next rank**





**SAL                     RANK                       DENSE\_RANK**

**5000                    1                           1**

**4000                    2                           2**

**3000                    3                           3**

**3000                    3                           3**

**3000                    3                           3**

**2000                    6                           4**

**2000                    6                           4**

**2000                    6                           4**

**1000                    8                           5**





PARTITION CLAUSE:-

**==================**



**=> partition by clause is used to divide the table based on one or more fields**

**=> used to find ranks with in group , for ex to find ranks with in dept**

&#x20;  **first divide the table dept wise and apply  rank/dense\_rank function on each dept**



**EX:-**



=> **FIND the ranks of the employees with in dept based on sal?**



**SELECT ename, sal,**

&#x20;           **DENSE\_RANK() OVER(PARTITION BY deptno ORDER BY sal  DESC) as rank**

**FROM emp**





ROW\_NUMBER():-

=============



**=> row\_number returns record number**

**=> it is also based on one or more  columns** 

**=> for row\_number  also data must be sorted**





&#x20;  **ROW\_NUMBER() OVER (ORDER BY colname ASC/DESC,....)**

**EX 1:-**

**SELECT empno,ename,sal,**

&#x20;      **ROW\_NUMBER() OVER (ORDER BY DESC) as rno**

**FROM emp**





**SAL                     RANK                       DENSE\_RANK         RNO**

**5000                    1                           1                 1**

**4000                    2                           2                 2**

**3000                    3                           3                 3**

**3000                    3                           3                 4**

**3000                    3                           3                 5**

**2000                    6                           4                 6**

**2000                    6                           4                 7**

**2000                    6                           4                 8**

**1000                    8                           5                 9**



**EX:-2**



**row\_number  based on empno**

**=>  select empno, ename,sal , row\_number() over (order by empno asc) as rno**

**FROM emp**

**WHERE rno = 5 => ERROR**



**column alias can not be used in where clause because where clause is executed**

**before select.To overcome this use CTE(common table expression)**  



**WITH E**

**AS**

**(SELECT empno, ename, sal,**

&#x20;      **row\_number() over (order by empno asc) as rno**

**FROM emp**

**)**

**SELECT \* FROM WHERE rno = 5**



&#x20;            **WHERE rno IN(5,10,15)**

&#x20;            **WHERE rno BETWEEN 5 AND 10**

&#x20;            **WHERE rno%2 = 0**

&#x20;            **WHERE  rno%2 = 1**



**NOTE:-**

**=> operations (select, insert,update, delete) perform on E are actually performed on EMP**

**EX:-**



**EMP44**

**ENO         ENAME       SAL**

**1            A          5000**

**2            B          6000**

**3            C          7000**

**1            A          5000=> duplicate**

**2            B          6000=> duplicate**



**step 1:- generate row\_numbers with in the group of eno, ename,sal**





&#x20;   **SELECT eno, ename, sal,**

&#x20;         **ROW\_NUMBER() OVER(PARTITION BY eno, ename,sal\\**

&#x20;                          **ORDER BY eno ASC) as rno**

&#x20;

&#x20;    **FROM emp44**



**1        A           5000           1**

**1        B           5000           2**



**2        B           6000           1**

**2        B           6000           2**



**3        C           7000           1**



**step 2: to delete duplicates deletes the records with rno>1**



**WITH E**

&#x20; **AS**

&#x20; **(** 

&#x20; **SELECT eno, ename, sal,**

&#x20;      **ROW\_NUMBER() OVER(PARTITIONS BY eno, ename, sal**

&#x20;                       **ORDER BY eno ASC) as rno**

**FROM emp44)**

**DELETE FROM E WHERE  rno>1**























































































































































































**\[**

