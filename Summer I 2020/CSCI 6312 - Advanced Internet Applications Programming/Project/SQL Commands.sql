CREATE TABLE IF NOT EXISTS SensorsAndActuators(
    DevID VARCHAR(10),
    DevType ENUM('SENSOR', 'ACTUATOR'),
    FunctionDescription VARCHAR(255),
    Control ENUM('RPI', 'ANDROID'),
    DeviceStatus INT NOT NULL,
    PRIMARY KEY(DevID)
);

CREATE TABLE IF NOT EXISTS Alarms(
    AlarmID VARCHAR(10),
    Alarm ENUM('ALARM'),
    MessageID VARCHAR(255),
    PRIMARY KEY(AlarmID)
);

CREATE TABLE IF NOT EXISTS ActiveAlarms(
    AlarmID VARCHAR(10),
    SinceTS VARCHAR(255),
    AcknowledgementStatus INT NOT NULL,
    PRIMARY KEY(AlarmID)
);


CREATE TABLE IF NOT EXISTS CannedMessages(
    MessageID VARCHAR(10),
    MessageType VARCHAR(255),
    MessageDescription VARCHAR(255),
    PRIMARY KEY(MessageID)
);

CREATE TABLE IF NOT EXISTS TransactionalLogs
(
    logID VARCHAR(10),
    TimestampInfo VARCHAR(255),
    MessageID VARCHAR(255),
	DataInformation VARCHAR(255),
    PRIMARY KEY(logID)
);


CREATE TABLE IF NOT EXISTS Users(
    pname VARCHAR(30) NOT NULL,
    password VARCHAR(255) NOT NULL,
    PRIMARY KEY(pname)
);

/* Inserting */

INSERT INTO SensorsAndActuators VALUES ('SW1', 'SENSOR', 'sense systolic BP > 140 mm Hg', 'RPI', 0);
INSERT INTO SensorsAndActuators VALUES ('SW2', 'SENSOR', 'sense diastolic BP < 30 mm Hg', 'RPI', 0);
INSERT INTO SensorsAndActuators VALUES ('SW3', 'SENSOR', 'sense blood sugar > 120 mg/dL', 'RPI', 0);
INSERT INTO SensorsAndActuators VALUES ('SW4', 'SENSOR', 'sense blood sugar < 50 mg/dL', 'RPI', 0);
INSERT INTO SensorsAndActuators VALUES ('LED1', 'ACTUATOR', 'IV infusion of pressor to increase BP', 'ANDROID', 0);
INSERT INTO SensorsAndActuators VALUES ('LED2', 'ACTUATOR', 'IV infusion of Y to decrease BP', 'ANDROID', 0);
INSERT INTO SensorsAndActuators VALUES ('LED3', 'ACTUATOR', 'IV infusion of W to decrease blood sugar', 'ANDROID', 0);
INSERT INTO SensorsAndActuators VALUES ('LED4', 'ACTUATOR', 'IV infusion of Z to increase blood sugar', 'ANDROID', 0);


INSERT INTO Alarms VALUES ('1', 'ALARM', '1');
INSERT INTO Alarms VALUES ('2', 'ALARM', '2');
INSERT INTO Alarms VALUES ('3', 'ALARM', '3');
INSERT INTO Alarms VALUES ('4', 'ALARM', '4');


INSERT INTO ActiveAlarms VALUES ('3', '2020-03-11 14:25:21', '0');
INSERT INTO ActiveAlarms VALUES ('1', '2020-03-11 13:17:23', '1');

INSERT INTO CannedMessages VALUES ('1', 'ALARM', 'Systolic BP HIGH');
INSERT INTO CannedMessages VALUES ('2', 'ALARM', 'Diastolic BP LOW');
INSERT INTO CannedMessages VALUES ('3', 'ALARM', 'BLOOD SUGAR HIGH');
INSERT INTO CannedMessages VALUES ('4', 'ALARM', 'BLOOD SUGAR LOW');
INSERT INTO CannedMessages VALUES ('5', 'CNST', 'Diastolic & Systolic BP simultaneously out of range');
INSERT INTO CannedMessages VALUES ('6', 'CNST', '?');
INSERT INTO CannedMessages VALUES ('7', 'SYSTEM', 'System up');
INSERT INTO CannedMessages VALUES ('8', 'SYSTEM', 'System shutting down');
INSERT INTO CannedMessages VALUES ('9', 'SYSTEM', 'User login - success');
INSERT INTO CannedMessages VALUES ('10', 'SYSTEM', 'User login - failure');
INSERT INTO CannedMessages VALUES ('11', 'SYSTEM', 'User logout');
INSERT INTO CannedMessages VALUES ('12', 'ADVISE', 'Reboot system');
INSERT INTO CannedMessages VALUES ('13', 'OPER', 'IV infusion of pressor');
INSERT INTO CannedMessages VALUES ('14', 'OPER', 'IV infusion of X');
INSERT INTO CannedMessages VALUES ('15', 'OPER', 'IV infusion of W');

INSERT INTO TransactionalLogs VALUES ('1', '2020-03-11 12:23:16', '7', "");
INSERT INTO TransactionalLogs VALUES ('2', '2020-03-12 10:8:37', '9',  "ben");
INSERT INTO TransactionalLogs VALUES ('3', '2020-03-12 10:8:37', '11',  "ben");