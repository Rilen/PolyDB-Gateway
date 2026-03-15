```mermaid
sequenceDiagram
    participant Client
    participant API as PolyDB Gateway
    participant Auth as Auth Layer
    participant Manager as Connection Manager
    participant Engine as Query Engine
    participant DB as Database
    participant Format as JSON Formatter

    Client->>API: HTTP Request (Query JSON)

    API->>Auth: Validate API Key / Token
    Auth-->>API: Authorized

    API->>Manager: Request DB Connection
    Manager-->>API: Connection Granted

    API->>Engine: Execute Query

    Engine->>DB: SQL Query
    DB-->>Engine: Query Result

    Engine->>Format: Convert to JSON
    Format-->>API: Structured Response

    API-->>Client: JSON Response
