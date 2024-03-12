@echo off
setlocal

:: specify database details
set "user=django"
set "host=localhost"
set "db=coordinacion"
set "password=django"

:: specify the order of tables
set "tables=auth_group auth_group_permissions auth_permission auth_user auth_user_groups auth_user_user_permissions django_admin_log django_content_type django_migrations django_session studentform_career studentform_school_cycle studentform_status studentform_syllabus studentform_subject studentform_semester studentform_student studentform_contact studenthistory_section studenthistory_gradeperiod studenthistory_course studenthistory_careersubject"

:: set the PGPASSWORD environment variable
set "PGPASSWORD=%password%"

:: dump each table in order
for %%a in (%tables%) do (
    pg_dump -U %user% -h %host% -d %db% -t %%a >> backup.sql
)