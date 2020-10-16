
# Diagrama de Casos de Uso do Módulo SIGA

@startuml
left to right direction
skinparam packageStyle rectangle
actor Student
rectangle SIGA {
  Student --> (Go to the Login Page)
  Student --> (Consult Academic Pathway)
  Student --> (Consult Course Plan)
  Student --> (Consult Course Units)
  Student --> (Consult Personal Data)
  Student --> (Enroll Curricular Units)
  Student --> (Consult Current Account)
  Student --> (Consult Debts)
  Student --> (Consult ATM References)
}

@enduml

@startuml
left to right direction
skinparam packageStyle rectangle
actor Teacher
rectangle SIGA {
    Teacher --> (Go to the Login Page)
    Teacher --> (Launch Notes)
    Teacher --> (See Notes Schedule)
    Teacher --> (Consult Courses)
    Teacher --> (Consult Course Plan)
    Teacher --> (Edit Course Units)
    Teacher --> (Create Study Plan)
}
@enduml

@startuml
left to right direction
skinparam packageStyle rectangle
actor Operator
rectangle SIGA {
    Operator --> (Go to the Login Page)
    Operator --> (Create Curse)
    Operator --> (Edit Curse)
    Operator --> (Consult Curses)
    Operator --> (Create Course Unit)
    Operator --> (Edit Course Units)
    Operator --> (Consult Curricular Units)
    Operator --> (Create Student Sheet)
    Operator --> (Edit Student Sheet)
    (Edit Student Sheet) -.-> (Find Student)
    Operator --> (Consult Student Sheet)
    (Consult Student Sheet) -.-> (Find Student)
    Operator --> (Consult Academic Pathway)
    (Consult Academic Pathway) -.-> (Find Student)
    Operator --> (Consult Student Study Plan)
    (Consult Student Study Plan) -.-> (Find Student)
    Operator --> (Enroll Curricular Units)
    (Enroll Curricular Units) -.-> (Find Student)
    Operator --> (Consult Student Schedule)
    (Consult Student Schedule) -.->(Find Teacher)
}
@enduml
