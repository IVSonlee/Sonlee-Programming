-- Act4_Lee : Weekly Class Schedule
-- Run in phpMyAdmin (XAMPP) > SQL tab, or: mysql -u root < schedule.sql

CREATE DATABASE IF NOT EXISTS class_schedule
    CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE class_schedule;

DROP TABLE IF EXISTS schedule;

CREATE TABLE schedule (
    id           INT AUTO_INCREMENT PRIMARY KEY,
    day_name     ENUM('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday') NOT NULL,
    start_time   TIME         NOT NULL,
    end_time     TIME         NOT NULL,
    subject_code VARCHAR(20)  NULL,
    activity     VARCHAR(150) NOT NULL,
    room         VARCHAR(50)  NULL,
    entry_type   ENUM('Class','Routine') NOT NULL,
    INDEX idx_day_time (day_name, start_time)
);

-- ===================== CLASSES (from regcard) =====================
INSERT INTO schedule (day_name, start_time, end_time, subject_code, activity, room, entry_type) VALUES
-- Tuesday
('Tuesday',  '10:20:00','13:20:00','ITCP312','IT Capstone Project 2',                          'MAC LAB', 'Class'),
('Tuesday',  '16:50:00','19:50:00','ARTA111','Art Appreciation',                               'VSB 505', 'Class'),
-- Thursday
('Thursday', '08:00:00','10:00:00','ITEL312','IT Elective Professional 2 w/ Lab (Lab)',        'CAS DTL', 'Class'),
('Thursday', '10:20:00','13:20:00','ITEL312','IT Elective Professional 2 w/ Lab (Lecture)',    'CNL',     'Class'),
('Thursday', '13:30:00','16:30:00','SADM411','System Admin and Maintenance w/ Lab',            'CNL',     'Class'),
('Thursday', '16:50:00','18:50:00','SADM411','System Admin and Maintenance w/ Lab',            'CAS 208', 'Class'),
-- Saturday
('Saturday', '10:20:00','13:20:00','RIZL211','Life and Works of Rizal',                        'VSB 505', 'Class'),
('Saturday', '13:30:00','16:30:00','CTIC411','Current Trends in Computing',                    'VSB 504', 'Class');

-- ===================== ROUTINES (vacant days: Mon, Wed, Fri, Sun) =====================
-- EDIT these so they match what you really do.
INSERT INTO schedule (day_name, start_time, end_time, subject_code, activity, room, entry_type) VALUES
-- Monday
('Monday',   '17:00:00','18:00:00',NULL,'Workout - push-ups, squats and plank (3 sets each)',            'Home', 'Routine'),
('Monday',   '18:30:00','19:30:00',NULL,'Cooking and eating dinner',                                      'Home', 'Routine'),
('Monday',   '19:30:00','21:30:00',NULL,'Programming - PHP and MySQL practice in VS Code with XAMPP',     'Home', 'Routine'),
('Monday',   '21:30:00','22:30:00',NULL,'Writing capstone documentation (Eco-Pulse Bot chapters)',       'Home', 'Routine'),
-- Wednesday
('Wednesday','17:00:00','18:00:00',NULL,'Reviewing SADM411 notes - Linux server commands',                'Home', 'Routine'),
('Wednesday','18:30:00','19:30:00',NULL,'Cooking and eating dinner',                                      'Home', 'Routine'),
('Wednesday','19:30:00','21:00:00',NULL,'Training and testing the YOLOv8-Nano model for Eco-Pulse Bot',   'Home', 'Routine'),
('Wednesday','21:00:00','22:00:00',NULL,'Cybersecurity reading - analyzing past data breach case studies','Home', 'Routine'),
-- Friday
('Friday',   '09:00:00','10:00:00',NULL,'Workout',                                                        'Home', 'Routine'),
('Friday',   '10:20:00','10:40:00',NULL,'Breakfast',                                                      'Home', 'Routine'),
('Friday',   '11:00:00','12:30:00',NULL,'Doing assignments',                                              'Home', 'Routine'),
('Friday',   '13:00:00','14:00:00',NULL,'Programming',                                                    'Home', 'Routine'),
('Friday',   '17:30:00','19:00:00',NULL,'Working on the Dimple Star bus reservation website (PHP)',       'Home', 'Routine'),
('Friday',   '19:30:00','20:30:00',NULL,'Cooking and eating dinner',                                      'Home', 'Routine'),
-- Sunday
('Sunday',   '09:00:00','10:00:00',NULL,'Church',                                                         'Church','Routine'),
('Sunday',   '10:30:00','12:30:00',NULL,'Programming',                                                    'Home', 'Routine'),
('Sunday',   '13:00:00','14:00:00',NULL,'Preparing meal',                                                 'Home', 'Routine'),
('Sunday',   '15:00:00','17:00:00',NULL,'Creating personal projects',                                     'Home', 'Routine'),
('Sunday',   '17:30:00','18:30:00',NULL,'Weekly review - listing deadlines and tasks for the coming week','Home', 'Routine'),
('Sunday',   '19:00:00','20:00:00',NULL,'Preparing bag and materials for Monday',                         'Home', 'Routine');
