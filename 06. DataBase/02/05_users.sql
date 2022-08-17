-- SQLite
CREATE TABLE users(
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT  NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);

-- 데이터 추가 
/*******************************************************************************
users.csv:1000: expected 6 columns but found 1 - filling the rest with NULL
users.csv:1000: INSERT failed: NOT NULL constraint failed: users.last_name .mode csv 안할 경우 발생
********************************************************************************/
.mode csv
-- 같은 디렉토리에 있는 users.csv 파일을 users 테이블로 수입
.import users.csv

/* 쿼리 */

/* WHERE clause */
-- Q. age 30이상인 유저의 모든 컬럼 정보 조회
SELECT * from users where age >= 30; -- 소문자 써도 문제 없음
-- Q. 30세 이상의 이름만
SELECT first_name FROM users WHERE age >= 30 limit 3;
-- Q. users 테이블에서 나이가 30이상이고 성이 '김'인 사람의 나이와 성만 조회
SELECT rowid ID, age, last_name from users where age >= 30;


/* Aggregate functions */

-- 30세 이상인 사람들의 숫자
SELECT count(*) from users where age >= 30;
-- 전체 중에 가장 작은 나이
select min(age) from users;
-- 이씨중에 가장 작은 나이
select min(age), first_name, balance from users where last_name = '이';
-- 30세 이상인 사람들의 평균 나이
select avg(age) from users where age >= 30;
-- balance가 가장 높은 사람과 그 액수
select first_name, max(balance) from users;



/* Like */

-- Q. 지역 번호가 02인 사람만 조회한다면?
select * from users WHERE phone LIKE '02-%';
-- Q. 이름이 '준'으로 끝나는 사람만 조회한다면?
select * from users where first_name like '%준';
-- Q. 중간번호가 5114인 사람만 조회한다면?
select * from users where phone like '%-5114-%';



/* ORDER BY */

-- Q. 나이 순으로 오름차순 정렬하여 상위 10개 조회
select * from users order by age asc limit 10;
-- Q. 나이 순, 성 순으로 오름차순 정렬하여 상위 10개
select * from users order by age, last_name LIMIT 5;
-- Q. 계좌 잔액 순으로 내림차순 정렬하여 해당 유저의 성과 이름 조회
select last_name, first_name, balance from users order by balance DESC, last_name ASC limit 10;