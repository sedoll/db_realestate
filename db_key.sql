-- 다중 기본키 설정
ALTER TABLE test2 ADD PRIMARY KEY(address, name);

-- 컬럼 타입 변경, text 타입으로는 기본키 설정 불가
ALTER TABLE test2 modify address varchar(10);

-- 외래키 삭제
alter table test2 drop foreign key test2_ibfk_1;

-- 설정된 외래키값 확인
SHOW CREATE TABLE test2;

-- 다중 외래키 설정
ALTER TABLE test2 ADD FOREIGN KEY (address, name) REFERENCES test1(address, name);