# VM Migration Attack Diagram

@startuml
rectangle Mobile
database SQL
rectangle WebServer
Mobile -> SQL
SQL -> Mobile
SQL -> WebServer
WebServer -- SQL
@enduml