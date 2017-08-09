DROP TABLE IF EXISTS ipmsg_log;
 
CREATE TABLE ipmsg_log (
    seq       INTEGER PRIMARY KEY AUTOINCREMENT,
    datetime  DATETIME NOT NULL,
    fromto    TEXT NOT NULL,
    name      TEXT NOT NULL,
    groupname TEXT NOT NULL,
    msg       TEXT NOT NULL
);

CREATE INDEX ipmsg_index on ipmsg_log (
    datetime,
    fromto,
    name,
    groupname,
    msg
);

