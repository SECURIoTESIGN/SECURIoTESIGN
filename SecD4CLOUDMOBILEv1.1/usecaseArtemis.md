# Use Case Diagram
@startuml
rectangle {
:Student: -left-> (Access to Login Page) 
:Student: -right-> (Enroll in a Course)
:Student: -right-> (Consult Notes) 
:Student: -up-> (Consult Study Plans)
:Student: -down-> (Access Current Account)
:Student: --> (Consult Curses)
:Student: --> (Update Password)
:Student: --> (Update Profile Photo)
}
@enduml