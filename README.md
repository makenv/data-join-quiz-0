## 介绍

相关数据都保存在`data`目录下的csv文件中, 要求不通过
数据库的其他方式, 处理数据获得任务列表中的结果.

## 数据文件介绍

  - `students.csv` 学生数据,学号和姓名
  - `courses.csv` 课程数据, 课程号和课程名字
  - `grades.csv` 成绩数据, 学号, 课程号对应的成绩

## 任务

### 语文成绩单
输出所有同学的语文课程成绩, 输出学生姓名, 对应的语文成绩, 要求按照成绩排序.

### 个人总成绩
输出两列数据, 学生姓名, 对应的总成绩, 要求按照学号排序.

### 课程及格率
输出两列数据, 课程名称, 对应课程的及格率 (及格学生人数/总学生人数)


## 要点/提示

  - 使用`list`/`map`构造内存表/索引
  - 尝试使用`jackson`反序列化csv数据
  - 尝试使用`josql`直接操作对象列表
  - 尝试使用`lambda`表达式(`jdk8`)操作对象列表