# Pokemon Database Engine

<p>
A basic CRUD module written in Core Python using SQLAlchemy as the ORM-engine.
Contains a DATABASE package that handles the ORM-SQL aspect.
</p>

## .ENV File Format:

```
DB_TYPE = <PostgreSQL/SQLite/mySQL>
PGHOST = <IP Address of database host>
PGPORT = <Port on host where database can be accessed>
PGDATABASE = <Name of the database>
PGUSER = <Database login username>
PGPASSWORD = <Database login password>
```